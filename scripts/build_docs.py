#!/usr/bin/env python3
"""Build Context7-friendly markdown docs for the RO App Public API v2.

Every page of https://roapp.readme.io/reference is published as markdown with an
embedded OpenAPI fragment. This script merges the fragments into one spec
(spec/openapi.json) and renders one markdown file per API resource (docs/api/).

Usage: scripts/build_docs.py [cache_dir]   (cache_dir is filled by fetch_docs.sh)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE_URL = "https://api.roapp.io/v2"
REF_URL = "https://roapp.readme.io/reference"

# (file, title, intro, path prefixes). The first group whose prefix matches wins.
GROUPS = [
    ("work-schedule-and-timesheets", "Work Schedule & Timesheets",
     "Plan employee work schedules and record actual worked time (timesheets) per day and location.",
     ["/company/work-schedule", "/company/timesheets"]),
    ("company", "Company",
     "Company account, license, locations (branches) and their resources, employees, employee groups, "
     "legal entities, taxes and custom directories. Most IDs used elsewhere (`branch_id`, `manager_id`, "
     "`assignee_id`, `legal_entity_id`, `tax_id`) come from these endpoints.",
     ["/company"]),
    ("catalog-services", "Catalog: Services",
     "Services catalog: categories, units of measure, services, prices and default price settings.",
     ["/catalog/services"]),
    ("catalog-products", "Catalog: Products",
     "Products (inventory items) catalog: categories, units of measure, product types, custom fields, "
     "products, prices and default price settings.",
     ["/catalog/products"]),
    ("catalog-bundles", "Catalog: Bundles",
     "Bundles are predefined sets of products and/or services that can be added to documents at once.",
     ["/catalog/bundles"]),
    ("bookings", "Bookings",
     "Bookings (appointments) and their items (products/services).",
     ["/bookings"]),
    ("inquiries", "Inquiries (Leads)",
     "Inquiries (called *leads* in webhooks, e.g. `Lead.Created`): requests from potential clients, "
     "with types, statuses, custom fields and comments.",
     ["/inquiries"]),
    ("estimates", "Estimates",
     "Estimates (quotes) with types, statuses, custom fields, items, comments and a public URL for the client.",
     ["/estimates"]),
    ("orders", "Orders",
     "Orders (tickets, jobs, work orders) with types, statuses, custom fields, items (products/services), "
     "comments and a public URL for the client.",
     ["/orders"]),
    ("sales", "Sales",
     "Point-of-sale (retail) sales. Read-only.",
     ["/sales"]),
    ("invoices", "Invoices",
     "Invoices with items, statuses and comments.",
     ["/invoices"]),
    ("finance", "Finance",
     "Cash & bank accounts, account transactions and transfers, cashflow categories, exchange rates, "
     "refunds and finance tags.",
     ["/finance"]),
    ("contacts-people", "Contacts: People",
     "People (individual clients and suppliers): CRUD, comments, merge, custom fields and organization links.",
     ["/contacts/people"]),
    ("contacts-organizations", "Contacts: Organizations",
     "Organizations (company clients and suppliers): CRUD, people membership, comments, merge and custom fields.",
     ["/contacts/organizations"]),
    ("contacts-tags", "Contacts: Tags",
     "Tags that can be assigned to people and organizations.",
     ["/contacts/tags"]),
    ("telephony", "Telephony",
     "Telephony integrations: providers, extensions, call log, call recordings and AI transcripts.",
     ["/telephony"]),
]

METHOD_ORDER = {"get": 0, "post": 1, "put": 2, "patch": 3, "delete": 4}
MAX_RESPONSE_LINES = 80


def load_pages(cache: Path):
    """Return [(slug, page_title, page_description, fragment)] in llms.txt order."""
    urls = re.findall(r"https://roapp\.readme\.io/reference/([^)\s]+)\.md", (cache / "llms.txt").read_text())
    seen, pages = set(), []
    for slug in urls:
        if slug in seen:
            continue
        seen.add(slug)
        text = (cache / "pages" / f"{slug}.md").read_text()
        m = re.search(r"# OpenAPI definition\s*```json\s*(.*?)```\s*$", text, re.S)
        if m:
            pages.append((slug, json.loads(m.group(1))))
    return pages


def merge_spec(pages):
    spec = None
    for slug, frag in pages:
        if spec is None:
            spec = {k: frag[k] for k in ("openapi", "info", "servers", "components", "security")}
            spec["info"] = {
                "title": "RO App Public API",
                "version": frag["info"]["version"],
                "description": "Merged from the per-page OpenAPI fragments published at " + REF_URL,
            }
            spec["paths"] = {}
        for path, item in frag["paths"].items():
            for method, op in item.items():
                op = dict(op)
                op["externalDocs"] = {"url": f"{REF_URL}/{slug}"}
                spec["paths"].setdefault(path, {})[method] = op
    return spec


# ---------- schema helpers ----------

def type_label(schema):
    if not schema:
        return "any"
    t = schema.get("type", "object" if "properties" in schema else "any")
    if t == "array":
        return f"array<{type_label(schema.get('items', {}))}>"
    fmt = schema.get("format")
    if fmt and fmt not in ("int32", "int64"):
        return f"{t} ({fmt})"
    return t


def cell(text):
    return " ".join(str(text).split()).replace("|", "\\|")


RANGE_HINT = "Accepts an array with one or two ISO 8601 date-time values"


def sentence(text):
    text = text.strip()
    return text if text[-1:] in ".?!" else text + "."


def describe(schema, desc="", defaults=True):
    desc = desc or schema.get("description", "")
    if RANGE_HINT in desc:
        # Collapse the long boilerplate repeated on every date filter.
        desc = desc.split(". ")[0] + ". Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started"
    parts = [desc]
    if schema.get("enum"):
        parts.append("One of: " + ", ".join(f"`{e}`" for e in schema["enum"]))
    items = schema.get("items") or {}
    if items.get("enum"):
        parts.append("Items one of: " + ", ".join(f"`{e}`" for e in items["enum"]))
    if defaults and "default" in schema and schema["default"] not in ("", None):
        parts.append(f"Default: `{json.dumps(schema['default'], ensure_ascii=False)}`")
    return cell(" ".join(sentence(p) for p in parts if p and p.strip()))


def flatten(schema, prefix="", required=(), depth=0):
    """Yield (dotted name, schema, required) rows for an object schema."""
    req = set(schema.get("required", [])) | set(required)
    for name, prop in (schema.get("properties") or {}).items():
        full = f"{prefix}{name}"
        yield full, prop, name in req
        if depth >= 4:
            continue
        if prop.get("type") == "object" or "properties" in prop:
            yield from flatten(prop, full + ".", depth=depth + 1)
        elif prop.get("type") == "array" and isinstance(prop.get("items"), dict) and prop["items"].get("properties"):
            yield from flatten(prop["items"], full + "[].", depth=depth + 1)


def field_table(schema, defaults=True):
    rows = list(flatten(schema))
    if not rows:
        return ""
    out = ["| Field | Type | Required | Description |", "|---|---|---|---|"]
    for name, prop, req in rows:
        out.append(f"| `{name}` | {type_label(prop)} | {'yes' if req else 'no'} | {describe(prop, defaults=defaults)} |")
    return "\n".join(out)


SAMPLE_STRINGS = {
    "first_name": "John", "last_name": "Doe", "name": "Example", "names": "John Doe", "title": "Example",
    "client_names": "John Doe", "address": "1 Main St, Springfield", "notes": "Note text",
    "comment": "Comment text", "text": "Comment text", "description": "Description text",
    "q": "screen", "sku": "SKU-001", "barcode": "4006381333931", "mpn": "MPN-001", "tags": "vip",
    "tag": "vip", "numbers": "A0001", "asset_uid": "356938035643809", "malfunction": "Broken screen",
    "color": "#3b82f6", "discount_code": "SUMMER10",
}


def sample_scalar(name, schema):
    if "example" in schema:
        return schema["example"]
    if schema.get("enum"):
        return schema["enum"][0]
    t, fmt, n = schema.get("type"), schema.get("format"), name.lower()
    desc = schema.get("description", "")
    if fmt == "json":
        return '{"f123": "value"}'
    if t in ("integer", "number"):
        if n.endswith("price") or n in ("amount", "value", "cost", "rate", "discount", "quantity"):
            return 1 if n == "quantity" else 100
        return 1 if n in ("day", "month", "page") else (2000 if n == "year" else 123)
    if t == "boolean":
        d = schema.get("default")
        return d in (True, "true") if d is not None else False
    if fmt == "date-time" or n.endswith("_at") or n in ("scheduled_for", "scheduled_to", "due_date"):
        return "2026-10-01T10:00:00Z"
    if fmt == "date" or n in ("day", "date", "date_from", "date_to") or 'for example "2026' in desc:
        return "2026-10-01"
    if n in SAMPLE_STRINGS:
        return SAMPLE_STRINGS[n]
    if "email" in n:
        return "client@example.com"
    if "phone" in n:
        return "+15555550123"
    if n in ("rate", "price", "amount", "cost", "value") or n.endswith("_price") or "price" in n:
        return "100.00"
    if n in ("code", "currency") or n.endswith("currency"):
        return "USD"
    if t == "array":
        return []
    return "string"


def sample(name, schema, depth=0):
    t = schema.get("type")
    if t == "object" or "properties" in schema:
        if depth > 4:
            return {}
        return {k: sample(k, v, depth + 1) for k, v in (schema.get("properties") or {}).items()}
    if t == "array":
        items = schema.get("items") or {"type": "string"}
        return [sample(name.rstrip("s"), items, depth + 1)]
    return sample_scalar(name, schema)


def shrink(value):
    """Keep only the first element of every list so examples stay short."""
    if isinstance(value, list):
        return [shrink(value[0])] if value else []
    if isinstance(value, dict):
        return {k: shrink(v) for k, v in value.items()}
    return value


def response_example(op):
    for code in ("200", "201"):
        content = ((op.get("responses") or {}).get(code) or {}).get("content") or {}
        for media in content.values():
            for ex in (media.get("examples") or {}).values():
                raw = ex.get("value")
                try:
                    data = json.loads(raw) if isinstance(raw, str) else raw
                except (TypeError, ValueError):
                    continue
                if data in ({}, [], None, ""):
                    continue
                text = json.dumps(shrink(data), indent=2, ensure_ascii=False)
                lines = text.splitlines()
                if len(lines) > MAX_RESPONSE_LINES:
                    text = "\n".join(lines[:MAX_RESPONSE_LINES]) + "\n  ..."
                return code, text, media.get("schema") or {}
    return None


# ---------- rendering ----------

def render_curl(method, path, params, body):
    url = BASE_URL + path
    for p in params:
        if p["in"] == "path":
            url = url.replace("{" + p["name"] + "}", str(sample_scalar(p["name"], p.get("schema", {}))))
    query = []
    query_params = [p for p in params if p["in"] == "query"]
    picked = [p for p in query_params if p.get("required")] or query_params[:2]
    for p in picked:
        s = p.get("schema", {})
        if s.get("type") == "array":
            v = sample_scalar(p["name"], s.get("items", {}))
            # OpenAPI default (style=form, explode=true): repeat the key per value
            query.append(f"{p['name']}={v}")
        else:
            query.append(f"{p['name']}={sample_scalar(p['name'], s)}")
    if query:
        url += "?" + "&".join(query)
    lines = [f"curl -X {method.upper()} \"{url}\" \\", '  -H "Authorization: Bearer $ROAPP_API_KEY"']
    if body is not None:
        lines[-1] += " \\"
        lines.append('  -H "Content-Type: application/json" \\')
        payload = json.dumps(body, indent=2, ensure_ascii=False).replace("'", "'\\''")
        lines.append(f"  -d '{payload}'")
    return "\n".join(lines)


def param_table(params):
    out = ["| Name | In | Type | Required | Description |", "|---|---|---|---|---|"]
    for p in params:
        s = p.get("schema", {})
        out.append(f"| `{p['name']}` | {p['in']} | {type_label(s)} | {'yes' if p.get('required') else 'no'} "
                   f"| {describe(s, p.get('description', ''))} |")
    return "\n".join(out)


def render_op(method, path, op, slug):
    title = op.get("summary") or slug
    desc = (op.get("description") or "").strip()
    params = op.get("parameters") or []
    body_schema = (((op.get("requestBody") or {}).get("content") or {}).get("application/json") or {}).get("schema")
    has_body = bool(body_schema and body_schema.get("properties"))
    resource = path.split("/")[1]

    out = [f"## {title}", ""]
    out.append(f"`{method.upper()} {path}`")
    out.append("")
    if desc:
        out += [sentence(desc), ""]
    if params:
        out += ["### Parameters", "", param_table(params), ""]
        if any(p["in"] == "query" and p["name"] == "page" for p in params):
            out += ["Paginated: up to 50 entries per page, `count` in the response is the total number of records.", ""]
    if has_body:
        out += ["### Request body (`application/json`)", "", field_table(body_schema), ""]

    body = sample("body", body_schema) if has_body else None
    out += [f"### Example: {title} with cURL", "", "```bash", render_curl(method, path, params, body), "```", ""]

    example = response_example(op)
    if example:
        code, text, schema = example
        out += [f"### Example response ({code})", "", "```json", text, "```", ""]
        if schema.get("properties") and resource not in ("sales",):
            table = field_table(schema, defaults=False)
            if table and table.count("\n") < 120:
                out += ["### Response fields", "", table, ""]

    codes = list((op.get("responses") or {}).keys())
    if codes:
        out += ["**Response codes:** " + ", ".join(f"`{c}`" for c in codes), ""]
    out += [f"Source: {REF_URL}/{slug}", ""]
    return "\n".join(out)


def group_for(path):
    for g in GROUPS:
        if any(path == p or path.startswith(p + "/") or path.startswith(p + ":") for p in g[3]):
            return g[0]
    raise KeyError(path)


def main():
    cache = Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / ".cache" / "roapp")
    pages = load_pages(cache)
    spec = merge_spec(pages)

    (ROOT / "spec").mkdir(exist_ok=True)
    (ROOT / "spec" / "openapi.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n")

    ops = {g[0]: [] for g in GROUPS}
    for slug, frag in pages:  # llms.txt order = documentation sidebar order
        for path, item in frag["paths"].items():
            for method, op in sorted(item.items(), key=lambda kv: METHOD_ORDER.get(kv[0], 9)):
                ops[group_for(path)].append((method, path, op, slug))

    api_dir = ROOT / "docs" / "api"
    api_dir.mkdir(parents=True, exist_ok=True)
    index = ["# RO App API v2 — Endpoint Index", "",
             f"Base URL: `{BASE_URL}`. All endpoints require `Authorization: Bearer <API_KEY>`.", ""]
    total = 0
    for file, title, intro, _ in GROUPS:
        items = ops[file]
        if not items:
            continue
        total += len(items)
        doc = [f"# RO App API: {title}", "", intro, "",
               f"Base URL: `{BASE_URL}`. Authenticate every request with `Authorization: Bearer <API_KEY>` "
               "(see [Getting Started](../getting-started.md)).", "",
               "| Method | Path | Summary |", "|---|---|---|"]
        doc += [f"| `{m.upper()}` | `{p}` | {cell(o.get('summary', ''))} |" for m, p, o, _ in items]
        doc.append("")
        doc += [render_op(*it) for it in items]
        (api_dir / f"{file}.md").write_text("\n".join(doc).rstrip() + "\n")

        index += [f"## [{title}](api/{file}.md)", "", "| Method | Path | Summary |", "|---|---|---|"]
        index += [f"| `{m.upper()}` | `{p}` | {cell(o.get('summary', ''))} |" for m, p, o, _ in items]
        index.append("")
    (ROOT / "docs" / "endpoints.md").write_text("\n".join(index).rstrip() + "\n")
    print(f"Rendered {total} operations into {len(GROUPS)} files")


if __name__ == "__main__":
    main()

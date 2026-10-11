# RO App Public API v2 — Documentation for Context7

LLM-friendly documentation of the [RO App Public API v2](https://roapp.readme.io/reference/getting-started-with-api),
structured for indexing by [Context7](https://context7.com). RO App is a business management platform for repair and
service businesses; the API covers orders, estimates, bookings, inquiries (leads), contacts, catalog, invoices, sales,
finance, work schedules, telephony and webhooks.

- **Base URL:** `https://api.roapp.io/v2`
- **Auth:** `Authorization: Bearer <API_KEY>` (key from [Settings > API](https://web.roapp.io/settings/api))
- **Rate limit:** 3 requests/second (`429` when exceeded)
- **Pagination:** `page` parameter, 50 entries per page, `count` = total records

## Quick start

```bash
curl "https://api.roapp.io/v2/orders?page=1" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

```python
import os, requests

resp = requests.get(
    "https://api.roapp.io/v2/orders",
    headers={"Authorization": f"Bearer {os.environ['ROAPP_API_KEY']}"},
    params={"page": 1, "sort": "-modified_at"},
)
resp.raise_for_status()
body = resp.json()
print(body["count"], [o["id"] for o in body["data"]])
```

## Contents

Guides:

- [Getting Started](docs/getting-started.md) — authentication, response format, errors, rate limits, pagination, filtering, custom fields
- [Recipes](docs/recipes.md) — end-to-end examples (create client + order, items, statuses, sync, payments, reports)
- [Webhooks](docs/webhooks.md) — events, payload, signature verification, retries
- [MCP server](docs/mcp.md) — connect Cursor, Claude, Codex to RO App
- [Endpoint index](docs/endpoints.md) — all 175 endpoints

API reference (`docs/api/`):

| Resource | File |
|---|---|
| Company, locations, employees, legal entities, taxes, directories | [company.md](docs/api/company.md) |
| Work schedule & timesheets | [work-schedule-and-timesheets.md](docs/api/work-schedule-and-timesheets.md) |
| Catalog: services | [catalog-services.md](docs/api/catalog-services.md) |
| Catalog: products | [catalog-products.md](docs/api/catalog-products.md) |
| Catalog: bundles | [catalog-bundles.md](docs/api/catalog-bundles.md) |
| Bookings | [bookings.md](docs/api/bookings.md) |
| Inquiries (leads) | [inquiries.md](docs/api/inquiries.md) |
| Estimates | [estimates.md](docs/api/estimates.md) |
| Orders | [orders.md](docs/api/orders.md) |
| Sales | [sales.md](docs/api/sales.md) |
| Invoices | [invoices.md](docs/api/invoices.md) |
| Finance: accounts, transactions, cashflow categories, exchange rates, refunds, tags | [finance.md](docs/api/finance.md) |
| Contacts: people | [contacts-people.md](docs/api/contacts-people.md) |
| Contacts: organizations | [contacts-organizations.md](docs/api/contacts-organizations.md) |
| Contacts: tags | [contacts-tags.md](docs/api/contacts-tags.md) |
| Telephony: providers, extensions, calls, recordings, transcripts | [telephony.md](docs/api/telephony.md) |

The merged OpenAPI 3.1 specification is in [`spec/openapi.json`](spec/openapi.json).

## Regenerating

`docs/api/`, `docs/endpoints.md` and `spec/openapi.json` are generated from the official reference; the guides in
`docs/*.md` are written by hand.

```bash
scripts/fetch_docs.sh .cache/roapp     # download llms.txt + every reference page as markdown
python3 scripts/build_docs.py .cache/roapp
```

## Adding to Context7

Push this repository to GitHub and submit it at https://context7.com/add-library. Indexing is configured in
[`context7.json`](context7.json) (only `docs/` is indexed; rules for coding agents are included).

This is an unofficial mirror; the source of truth is https://roapp.readme.io/reference.

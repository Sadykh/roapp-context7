# RO App API: Getting Started

The RO App Public API v2 is a REST/JSON API for RO App, a business management platform (CRM, orders, inventory, POS, finance) for repair and service
businesses. Use it to integrate RO App with your own systems, automate workflows, and sync orders, estimates, bookings,
inquiries (leads), contacts, catalog (products, services, bundles), invoices, sales, finance and telephony data.

- **Base URL:** `https://api.roapp.io/v2`
- **Format:** JSON request and response bodies (`Content-Type: application/json`)
- **Auth:** Bearer token (API key) in the `Authorization` header
- **Rate limit:** 3 requests per second, exceeding it returns `429 Too Many Requests`
- **Pagination:** `page` query parameter, up to 50 entries per page, `count` = total number of records
- **Official reference:** https://roapp.readme.io/reference/getting-started-with-api

## Authentication

All requests must be authenticated with a **Bearer token**. The API key is linked to a user profile and is created in the
RO App web app under [Settings > API](https://web.roapp.io/settings/api). A compromised key can be regenerated on the same page.

```http
GET /v2/orders HTTP/1.1
Host: api.roapp.io
Authorization: Bearer YOUR_API_KEY
```

- Requests without a valid token return `401 Unauthorized`.
- Keep keys out of source control and client-side code; read them from an environment variable such as `ROAPP_API_KEY`.

### Authenticate with cURL

```bash
export ROAPP_API_KEY="your-api-key"

curl "https://api.roapp.io/v2/orders" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

### Authenticate with Python (requests)

```python
import os
import requests

API_KEY = os.environ["ROAPP_API_KEY"]
BASE_URL = "https://api.roapp.io/v2"

session = requests.Session()
session.headers.update({"Authorization": f"Bearer {API_KEY}"})

response = session.get(f"{BASE_URL}/orders")
response.raise_for_status()
print(response.json())
```

### Authenticate with JavaScript / TypeScript (fetch)

```typescript
const BASE_URL = "https://api.roapp.io/v2";
const API_KEY = process.env.ROAPP_API_KEY!;

const res = await fetch(`${BASE_URL}/orders`, {
  headers: { Authorization: `Bearer ${API_KEY}` },
});
if (!res.ok) throw new Error(`RO App API error ${res.status}: ${await res.text()}`);
const body = await res.json();
console.log(body.data, body.count);
```

### Authenticate with PHP (cURL)

```php
<?php
$apiKey = getenv('ROAPP_API_KEY');

$curl = curl_init();
curl_setopt_array($curl, [
    CURLOPT_URL => "https://api.roapp.io/v2/orders",
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER => ["Authorization: Bearer $apiKey"],
]);
$response = curl_exec($curl);
$httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
curl_close($curl);

echo "HTTP Status: $httpCode\n";
$data = json_decode($response, true);
```

### Authenticate with Kotlin (OkHttp)

```kotlin
import okhttp3.OkHttpClient
import okhttp3.Request

fun main() {
    val apiKey = System.getenv("ROAPP_API_KEY")
    val client = OkHttpClient()
    val request = Request.Builder()
        .url("https://api.roapp.io/v2/orders")
        .addHeader("Authorization", "Bearer $apiKey")
        .build()
    client.newCall(request).execute().use { response ->
        println("HTTP Status: ${response.code}")
        println(response.body?.string())
    }
}
```

## Response format

List and object responses are wrapped in a JSON envelope:

```json
{
  "data": [
    { "id": 3319495, "name": "Draft", "color": "#1E79C7", "group": 8 }
  ],
  "page": 1,
  "count": 5,
  "success": true
}
```

- `data` — an array (list endpoints) or an object (single-entity endpoints)
- `count` — total number of records matching the filters (not just the current page)
- `page` — current page number (paginated endpoints)
- `success` — `true` when the request succeeded

Some timestamps in responses (e.g. `created_at` in sales) are Unix timestamps in **milliseconds**; request
parameters and bodies use ISO 8601 strings.

## Errors and status codes

| Code | Meaning |
|---|---|
| `200` | Success |
| `204` | Success, no content (e.g. invoice comments and status updates) |
| `400` | Bad request — invalid parameters or body |
| `401` | Missing or invalid API key |
| `404` | Entity not found |
| `429` | Rate limit exceeded (more than 3 requests per second) |

## Rate limits

You can make up to **3 requests per second**. Throttle client-side and retry `429` responses with backoff.

### Rate-limited client with retries (Python)

```python
import os
import time
import requests

BASE_URL = "https://api.roapp.io/v2"


class RoAppClient:
    """Minimal RO App API client: auth, 3 req/s throttle, retry on 429."""

    def __init__(self, api_key=None, max_rps=3):
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key or os.environ['ROAPP_API_KEY']}",
            "Content-Type": "application/json",
        })
        self.min_interval = 1.0 / max_rps
        self._last = 0.0

    def request(self, method, path, retries=5, **kwargs):
        for attempt in range(retries):
            wait = self.min_interval - (time.monotonic() - self._last)
            if wait > 0:
                time.sleep(wait)
            self._last = time.monotonic()
            resp = self.session.request(method, BASE_URL + path, timeout=30, **kwargs)
            if resp.status_code == 429:
                time.sleep(2 ** attempt)
                continue
            resp.raise_for_status()
            return resp.json() if resp.content else None
        raise RuntimeError(f"Rate limited after {retries} retries: {method} {path}")

    def get(self, path, **params):
        return self.request("GET", path, params=params)

    def post(self, path, json):
        return self.request("POST", path, json=json)

    def patch(self, path, json):
        return self.request("PATCH", path, json=json)

    def delete(self, path):
        return self.request("DELETE", path)


client = RoAppClient()
print(client.get("/company"))
```

### Rate-limited client with retries (TypeScript)

```typescript
const BASE_URL = "https://api.roapp.io/v2";
const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

export class RoAppClient {
  private last = 0;
  constructor(private apiKey = process.env.ROAPP_API_KEY!, private minIntervalMs = 334) {}

  async request<T = any>(method: string, path: string, body?: unknown, retries = 5): Promise<T> {
    for (let attempt = 0; attempt < retries; attempt++) {
      const wait = this.minIntervalMs - (Date.now() - this.last);
      if (wait > 0) await sleep(wait);
      this.last = Date.now();
      const res = await fetch(BASE_URL + path, {
        method,
        headers: { Authorization: `Bearer ${this.apiKey}`, "Content-Type": "application/json" },
        body: body === undefined ? undefined : JSON.stringify(body),
      });
      if (res.status === 429) { await sleep(1000 * 2 ** attempt); continue; }
      if (!res.ok) throw new Error(`${method} ${path} -> ${res.status}: ${await res.text()}`);
      const text = await res.text();
      return (text ? JSON.parse(text) : undefined) as T;
    }
    throw new Error(`Rate limited after ${retries} retries: ${method} ${path}`);
  }
}
```

## Pagination

Every list endpoint that accepts a `page` parameter is paginated: each page returns up to **50 entries**, and `count`
is the total number of records. Iterate by appending `page=N` until you have collected `count` records (or a page
returns fewer than 50 entries).

### Iterate over all pages (Python)

```python
def iter_all(client, path, **params):
    """Yield every record of a paginated RO App list endpoint."""
    page, seen = 1, 0
    while True:
        body = client.get(path, page=page, **params)
        items = body.get("data") or []
        yield from items
        seen += len(items)
        if not items or len(items) < 50 or seen >= body.get("count", 0):
            break
        page += 1


all_people = list(iter_all(client, "/contacts/people"))
```

### Iterate over all pages (TypeScript)

```typescript
async function* iterAll(client: RoAppClient, path: string, params: Record<string, string> = {}) {
  for (let page = 1, seen = 0; ; page++) {
    const qs = new URLSearchParams({ ...params, page: String(page) });
    const body = await client.request("GET", `${path}?${qs}`);
    const items = body.data ?? [];
    yield* items;
    seen += items.length;
    if (items.length < 50 || seen >= body.count) break;
  }
}

for await (const order of iterAll(new RoAppClient(), "/orders")) console.log(order.id);
```

## Filtering, sorting and date ranges

List endpoints accept filters as query parameters.

- **Array filters** (`ids`, `branch_ids`, `statuses`, `types`, `managers`, `client_ids`, `tags`, ...) — the OpenAPI spec
  declares them as arrays without an explicit serialization style, so the OpenAPI default applies: repeat the key for
  each value, e.g. `?statuses=1&statuses=2`. (`requests` and `URLSearchParams` do this automatically for lists.)
- **Date-time range filters** (`created_at`, `modified_at`, `closed_at`, `scheduled_for`, `due_date`, `issue_date`)
  accept one or two ISO 8601 date-time values. One value is the start (left) boundary; two values define a range:
  - `created_at=2025-05-01T00:00:00Z` — from May 1, 2025 onward
  - `created_at=2025-05-01T00:00:00Z&created_at=2025-05-02T00:00:00Z` — between May 1 and May 2, 2025
- **Sorting** — `sort` takes a field name for ascending order or `-field` for descending, e.g. `sort=-modified_at`.
  Allowed fields are listed per endpoint (typically `id`, `modified_at`, `created_at`, ...).

### Filter orders by status and date range (cURL)

```bash
curl -G "https://api.roapp.io/v2/orders" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  --data-urlencode "statuses=101" \
  --data-urlencode "statuses=102" \
  --data-urlencode "created_at=2025-05-01T00:00:00Z" \
  --data-urlencode "created_at=2025-05-31T23:59:59Z" \
  --data-urlencode "sort=-modified_at" \
  --data-urlencode "page=1"
```

### Filter orders by status and date range (Python)

```python
orders = client.get(
    "/orders",
    statuses=[101, 102],                       # sent as statuses=101&statuses=102
    created_at=["2025-05-01T00:00:00Z", "2025-05-31T23:59:59Z"],
    sort="-modified_at",
    page=1,
)
```

## Custom fields

Orders, estimates, inquiries, people, organizations and products support custom fields. Discover field IDs with the
`GET /<resource>/custom-fields` endpoints (e.g. `GET /orders/custom-fields`, `GET /contacts/people/custom-fields`) and
send values as a **JSON-encoded string** keyed by `f<field_id>`:

```json
{
  "custom_fields": "{\"f123\": \"value\", \"f234\": \"value\"}"
}
```

```python
import json

client.patch("/orders/50699833", json={
    "custom_fields": json.dumps({"f123": "IMEI checked", "f234": "Yes"}),
})
```

## Reference IDs

Many request fields reference entities you look up first:

| Field | Where to get it |
|---|---|
| `branch_id`, `branch_ids` | `GET /company/locations` (locations are called *branches* in the API) |
| `manager_id`, `assignee_id`, `employee_id` | `GET /company/employees` |
| `resource_id` | `GET /company/locations/{id}/resources` |
| `legal_entity_id` | `GET /company/legal-entities` |
| `tax_ids` | `GET /company/taxes` |
| `order_type_id` / `status_id` | `GET /orders/types`, `GET /orders/statuses` (same for estimates, inquiries, invoices) |
| `client_id`, `payer_id` | `GET /contacts/people`, `GET /contacts/organizations` |
| `entity_id` (document items) | `GET /catalog/products`, `GET /catalog/services` |
| `category_id` (finance) | `GET /finance/cashflow-categories` |

## Next steps

- [Endpoint index](endpoints.md) — every endpoint grouped by resource
- [Recipes](recipes.md) — end-to-end integration examples
- [Webhooks](webhooks.md) — real-time event notifications
- [MCP server](mcp.md) — connect AI assistants to RO App

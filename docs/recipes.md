# RO App API: Recipes

End-to-end examples for common RO App integrations. They use the `RoAppClient` and `iter_all` helpers from
[Getting Started](getting-started.md) (auth, 3 req/s throttling, retries on `429`, pagination).
Base URL: `https://api.roapp.io/v2`.

> The published spec has no response examples for most write endpoints. The recipes assume the standard envelope
> (`{"data": {...}, "success": true}`) with the created entity in `data` — check field names against a real response
> before relying on them. Type, status, location and employee IDs are company-specific: always look them up first.

## Create a client and a repair order

Look up the location and order type, create (or reuse) a person, then create an order for them.

```python
locations = client.get("/company/locations")["data"]
order_types = client.get("/orders/types")["data"]
branch_id = locations[0]["id"]
order_type_id = order_types[0]["id"]

# Reuse an existing client by phone, or create one
found = client.get("/contacts/people", phones=["+15555550123"])["data"]
if found:
    client_id = found[0]["id"]
else:
    person = client.post("/contacts/people", json={
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phones": [{
            "title": "Mobile",
            "phone": "+15555550123",
            "notify": True,
            "has_viber": False,
            "has_whatsapp": True,
        }],
    })
    client_id = person["data"]["id"]

order = client.post("/orders", json={
    "branch_id": branch_id,
    "order_type_id": order_type_id,
    "client_id": client_id,
    "malfunction": "Cracked screen",
    "manager_notes": "Created via API",
    "due_date": "2026-10-15T18:00:00Z",
    "urgent": False,
})
order_id = order["data"]["id"]
```

## Add a service or product to an order

Order items reference a catalog product or service through `entity_id`. `discount` and `warranty` objects are required.

```python
service = client.get("/catalog/services", q="screen replacement")["data"][0]
employees = client.get("/company/employees")["data"]

client.post(f"/orders/{order_id}/items", json={
    "entity_id": service["id"],
    "assignee_id": employees[0]["id"],
    "quantity": 1,
    "price": 120.0,
    "cost": 40.0,
    "discount": {"type": "percentage", "percentage": 10, "amount": 0, "sponsor": "company"},
    "warranty": {"period": "90", "periodUnits": "days"},
    "comment": "OEM part",
    "comment_visibility": "public",
})
```

```bash
curl -X POST "https://api.roapp.io/v2/orders/50699833/items" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "entity_id": 4512,
    "assignee_id": 200206,
    "quantity": 1,
    "price": 120.0,
    "cost": 40.0,
    "discount": {"type": "percentage", "percentage": 10, "amount": 0, "sponsor": "company"},
    "warranty": {"period": "90", "periodUnits": "days"}
  }'
```

## Change order status and add a comment

Status IDs are company-specific: fetch them from `GET /orders/statuses`.

```python
statuses = {s["name"]: s["id"] for s in client.get("/orders/statuses")["data"]}

client.post(f"/orders/{order_id}/status", json={
    "status_id": statuses["In progress"],
    "comment": "Technician started the repair",
})
client.post(f"/orders/{order_id}/comments", json={
    "comment": "Waiting for the part from the supplier",
    "is_private": True,
})

# Share the order with the client
public_url = client.get(f"/orders/{order_id}/public-url")
```

The same pattern works for estimates (`/estimates/{estimate_id}/status`), inquiries (`/inquiries/{inquiry_id}/status`)
and invoices (`/invoices/{invoice_id}/status`).

## Incremental sync of orders modified since the last run

Use `modified_at` with one value (lower boundary) and sort by modification time.

```python
from datetime import datetime, timezone

last_sync = "2026-10-01T00:00:00Z"   # persist this between runs
started = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

for order in iter_all(client, "/orders", modified_at=[last_sync], sort="modified_at"):
    upsert_order(order)                # your storage logic

last_sync = started
```

Combine with [webhooks](webhooks.md) (`Order.Created`, `Order.Status.Changed`, ...) for near-real-time updates and keep
the periodic sync as a safety net.

## Create a booking (appointment)

```python
resources = client.get(f"/company/locations/{branch_id}/resources")["data"]

booking = client.post("/bookings", json={
    "branch_id": branch_id,
    "assignee_id": employees[0]["id"],
    "client_id": client_id,
    "scheduled_for": "2026-10-20T09:00:00Z",
    "scheduled_to": "2026-10-20T10:00:00Z",
    "resource_id": resources[0]["id"] if resources else None,
    "comment": "Diagnostics",
})
```

## Capture a lead (inquiry) from a website form

`type_id` is required; get it from `GET /inquiries/types`. A client can be passed by `client_id` or by contact data.

```python
inquiry_type = client.get("/inquiries/types")["data"][0]

client.post("/inquiries", json={
    "type_id": inquiry_type["id"],
    "branch_id": branch_id,
    "client_name": "Jane Smith",
    "client_phone": "+15555550199",
    "email": "jane@example.com",
    "comment": "Laptop does not turn on",
    "urgent": True,
})
```

## Record a payment for an order

Create an income transaction on a finance account and link it to the order via `related_document`.

```python
account = client.get("/finance/accounts")["data"][0]

client.post(f"/finance/accounts/{account['id']}/transactions", json={
    "amount": "108.00",
    "direction": "income",
    "description": "Payment for order",
    "client_id": client_id,
    "related_document": {"id": order_id, "type": "order"},
})
```

## Sales report for the last 30 days

```python
from datetime import datetime, timedelta, timezone

since = (datetime.now(timezone.utc) - timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
sales = list(iter_all(client, "/sales", created_at=[since]))

totals = [
    sum(p["price"] * p["amount"] - p.get("discount_value", 0) for p in s.get("products", []))
    for s in sales
]
average = sum(totals) / len(totals) if totals else 0
print(f"{len(sales)} sales, average {average:.2f}")
```

## Update work schedule for an employee

```python
client.request("PUT", "/company/work-schedule/days/2026-10-20/employees/200206", json={
    "type": "working",
    "intervals": [
        {"branch_id": branch_id, "starts_at": "2026-10-20T09:00:00Z", "ends_at": "2026-10-20T18:00:00Z"},
    ],
})

# Mark a vacation day
client.request("PUT", "/company/work-schedule/days/2026-10-21/employees/200206", json={
    "type": "non_working",
    "non_working": {"type": "vacation", "is_unpaid": False},
})
```

## Fetch missed calls with transcripts

```python
missed = client.get("/telephony/calls", status="missed", sort="-id")["data"]
for call in missed:
    transcript = client.get(f"/telephony/calls/{call['id']}/transcript")
    print(call["id"], transcript)
```

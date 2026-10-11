# RO App Webhooks

Webhooks deliver real-time updates when events occur in RO App. Each event is sent as an HTTP `POST` request with a
JSON payload to your endpoint. Use them to automate workflows, integrate third-party applications and react to changes
without polling the API.

## How it works

1. **Event occurs** — a predefined event is triggered in RO App (e.g. order created, status changed).
2. **Payload sent** — RO App sends an HTTP `POST` request with event details in JSON to your endpoint.
3. **Process the payload** — your system handles the data; fetch the full entity through the API if needed.

## Registering a webhook

Webhooks are configured in the RO App web app, not through the API.

1. Log in and open [Settings > API](https://web.roapp.io/settings/api).
2. Click **+ Webhook** and enter:
   - **Endpoint URL** — where event data will be sent (must be publicly reachable, use HTTPS)
   - **Description**
   - **Events to subscribe** — the events you want to receive
3. Click **Save**.

Each account can create a maximum of **5 webhooks**.

## Supported events

### Tasks

| Event | Triggered when |
|---|---|
| `Task.Created` | A new task is created |
| `Task.Completed` | A task is marked as completed |
| `Task.Reopened` | A task is reopened |
| `Task.Deadline.Changed` | A task's deadline date is changed |
| `Task.Assignee.Changed` | A task's assignee is changed |
| `Task.Deleted` | A task is deleted |

### Inquiries (leads)

| Event | Triggered when |
|---|---|
| `Lead.Created` | A new lead (inquiry) is created |
| `Lead.Status.Changed` | A lead's status is changed |
| `Lead.Client.Changed` | A lead's client is changed |
| `Lead.Type.Changed` | A lead's type is changed |
| `Lead.Deadline.Changed` | A lead's deadline date is changed |
| `Lead.Location.Changed` | A lead's location is changed |
| `Lead.Manager.Changed` | A lead's manager is changed |
| `Lead.Deleted` | A lead is deleted |

### Bookings

| Event | Triggered when |
|---|---|
| `Booking.Created` | A new booking is created |
| `Booking.Status.Changed` | A booking's status is changed |
| `Booking.Time.Changed` | A booking's appointment time is updated |
| `Booking.Assignee.Changed` | A booking's assignee is updated |
| `Booking.Deleted` | A booking is deleted |

### Estimates and orders (tickets, jobs, ...)

| Event | Triggered when |
|---|---|
| `Order.Created` | A new order is created |
| `Order.Type.Changed` | An order's type is updated |
| `Order.Status.Changed` | An order's status is changed |
| `Order.Client.Changed` | The client associated with an order is updated |
| `Order.Manager.Changed` | An order's manager is updated |
| `Order.Assignee.Changed` | An order's engineer (assignee) is updated |
| `Order.Deadline.Changed` | An order's deadline is updated |
| `Order.Amount.Changed` | An order's total amount is changed |
| `Order.Location.Changed` | An order is moved to another location |
| `Order.Approval.Accepted` | An estimate or order is accepted by the client |
| `Order.Approval.Declined` | An estimate or order is declined by the client |
| `Order.Deleted` | An order is deleted |

### Sales

| Event | Triggered when |
|---|---|
| `Sale.Created` | A new sale is created |
| `Sale.Deleted` | A sale is deleted |

### Clients

| Event | Triggered when |
|---|---|
| `Client.Created` | A new client is created |
| `Client.Deleted` | A client is deleted |
| `CustomerFeedback.Created` | A new feedback review from a client is created |

### Invoices

| Event | Triggered when |
|---|---|
| `Invoice.Created` | A new invoice is created |
| `Invoice.Status.Changed` | An invoice's status is changed |
| `Invoice.Deleted` | An invoice is deleted |

### Other events

| Event | Triggered when |
|---|---|
| `Comment.Created` | A new comment is created |
| `Attachment.Created` | A file or image is attached to an object (task, lead, order, etc.) |
| `Auth.Login` | An employee logs into their account |

## Webhook payload

```json
{
  "id": "9cba80cc-93b5-459b-bfd3-445e724dafc5",
  "created_at": "2024-12-05T11:31:39.440424Z",
  "created_at_ts": 1733398299.440424,
  "event_name": "Order.Status.Changed",
  "context": {
    "object_id": 50699833,
    "object_type": "order"
  },
  "metadata": {
    "new": { "id": 267312 },
    "old": { "id": 393648 },
    "order": { "id": 50699833, "name": "AB0300" }
  },
  "employee": {
    "id": 200206,
    "full_name": "John Doe",
    "email": "j.doe@corp.com"
  }
}
```

| Field | Description |
|---|---|
| `id` | Unique webhook delivery ID (UUID) |
| `created_at` | Event time, ISO 8601 |
| `created_at_ts` | Event time as a Unix timestamp (seconds, fractional) |
| `event_name` | Event name, e.g. `Order.Status.Changed` |
| `context` | Where the event occurred: `object_id` and `object_type` (e.g. `order`) |
| `metadata` | Event-specific data, e.g. `old` / `new` values for `*.Changed` events (for `Order.Status.Changed` these are status IDs) |
| `employee` | Employee who initiated the event (`id`, `full_name`, `email`) |

## Securing webhooks (X-Signature)

Each request includes an `X-Signature` header with an **HMAC-SHA256** hash generated from the webhook `id` and your
secret key. Recompute it on your side and compare in constant time to make sure the payload comes from RO App.

> The official guide does not specify the exact encoding of the signature. The examples below compute
> `hex(HMAC_SHA256(key=secret, message=payload.id))`; confirm against a real delivery before enforcing verification.

### Verify the signature and handle events (Python, Flask)

```python
import hashlib
import hmac
import os

from flask import Flask, abort, request

app = Flask(__name__)
WEBHOOK_SECRET = os.environ["ROAPP_WEBHOOK_SECRET"].encode()


def is_valid(payload: dict, signature: str) -> bool:
    expected = hmac.new(WEBHOOK_SECRET, payload["id"].encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature or "")


@app.post("/roapp/webhook")
def roapp_webhook():
    event = request.get_json(force=True)
    if not is_valid(event, request.headers.get("X-Signature")):
        abort(401)

    name, ctx = event["event_name"], event["context"]
    if name == "Order.Status.Changed":
        print(f"Order {ctx['object_id']}: status {event['metadata']['old']['id']} -> {event['metadata']['new']['id']}")
    elif name == "Order.Created":
        print(f"New order {ctx['object_id']}")

    # Respond 2XX quickly; do slow work in a background job.
    return "", 200
```

### Verify the signature and handle events (Node.js, Express)

```typescript
import crypto from "node:crypto";
import express from "express";

const app = express();
app.use(express.json());
const SECRET = process.env.ROAPP_WEBHOOK_SECRET!;

function isValid(payload: { id: string }, signature: string | undefined): boolean {
  const expected = crypto.createHmac("sha256", SECRET).update(payload.id).digest("hex");
  const a = Buffer.from(expected);
  const b = Buffer.from(signature ?? "");
  return a.length === b.length && crypto.timingSafeEqual(a, b);
}

app.post("/roapp/webhook", (req, res) => {
  if (!isValid(req.body, req.header("X-Signature"))) return res.sendStatus(401);

  const { event_name, context, metadata } = req.body;
  switch (event_name) {
    case "Order.Created":
      console.log("New order", context.object_id);
      break;
    case "Invoice.Status.Changed":
      console.log("Invoice", context.object_id, metadata);
      break;
  }
  res.sendStatus(200);
});

app.listen(3000);
```

### Deduplicate deliveries

Retries can deliver the same event more than once. Use the payload `id` as an idempotency key:

```python
def handle_once(event, store):
    if store.exists(event["id"]):
        return
    store.add(event["id"])
    process(event)
```

## Error handling and retries

If your endpoint does not respond with a `2XX` status code, RO App retries the delivery:

1. 1st retry — after 5 seconds
2. 2nd retry — after 10 seconds
3. 3rd retry — after 15 seconds

If no `200 OK` is received after multiple retries over the course of **1 hour**, the webhook is **disabled
automatically**. Fix the endpoint and re-enable the webhook manually on the [Settings > API](https://web.roapp.io/settings/api) page.

Best practices:

- Return `200` as fast as possible and process events asynchronously.
- Treat the payload as a notification: fetch the current entity via the API (e.g. `GET /orders/{order_id}`) when you
  need full data.
- Run a periodic incremental sync (`modified_at` filter) as a safety net for missed events — see [Recipes](recipes.md).

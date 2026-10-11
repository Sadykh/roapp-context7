# RO App API: Orders

Orders (tickets, jobs, work orders) with types, statuses, custom fields, items (products/services), comments and a public URL for the client.

Base URL: `https://api.roapp.io/v2`. Authenticate every request with `Authorization: Bearer <API_KEY>` (see [Getting Started](../getting-started.md)).

| Method | Path | Summary |
|---|---|---|
| `GET` | `/orders` | Get Orders |
| `GET` | `/orders/{order_id}` | Get Order by ID |
| `POST` | `/orders` | Create Order |
| `PATCH` | `/orders/{order_id}` | Update Order |
| `GET` | `/orders/{order_id}/items` | Get Order Items |
| `POST` | `/orders/{order_id}/items` | Add Order Item |
| `PATCH` | `/orders/{order_id}/items/{item_id}` | Update Order Item |
| `POST` | `/orders/{order_id}/status` | Update Order Status |
| `POST` | `/orders/{order_id}/comments` | Create Order Comment |
| `GET` | `/orders/{order_id}/public-url` | Get Order Public Page Url |
| `GET` | `/orders/statuses` | Get Order Statuses |
| `GET` | `/orders/types` | Get Order Types |
| `GET` | `/orders/custom-fields` | Get Order Custom Fields |

## Get Orders

`GET /orders`

Retrieve a list of orders.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | number | no | Page number. Default: `1`. |
| `types` | query | array<number> | no | List of Order Type IDs (same as order types). |
| `branch_ids` | query | array<number> | no | List of Location IDs. |
| `ids` | query | array<number> | no | List of Order IDs. |
| `numbers` | query | array<string> | no | List of Order document numbers. |
| `statuses` | query | array<number> | no | List of Order Status IDs. |
| `managers` | query | array<number> | no | List of Employee IDs. |
| `client_ids` | query | array<number> | no | List of Client (Person / Organization) IDs. |
| `client_names` | query | array<string> | no | List of Client (Person / Organization) names. |
| `client_phones` | query | array<string> | no | List of phone numbers. |
| `asset_uid` | query | array<string> | no | List of asset serial numbers (vin, imei). |
| `created_at` | query | array<string (date-time)> | no | Filter by creation date. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `modified_at` | query | array<string (date-time)> | no | Filter by modification date. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `closed_at` | query | array<string (date-time)> | no | Filter by close date. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `scheduled_for` | query | array<string (date-time)> | no | Filter by "Scheduled from" date and time. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `due_date` | query | array<string (date-time)> | no | Filter by due date. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `id`, `-id`, `modified_at`, `-modified_at`, `scheduled_for`, `-scheduled_for`, `due_date`, `-due_date`, `closed_at`, `-closed_at`. |

Paginated: up to 50 entries per page, `count` in the response is the total number of records.

### Example: Get Orders with cURL

```bash
curl -X GET "https://api.roapp.io/v2/orders?page=1&types=123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-orders

## Get Order by ID

`GET /orders/{order_id}`

Retrieve detailed information about a specific order.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `order_id` | path | integer | yes | Order ID. |

### Example: Get Order by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/orders/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-order-by-id

## Create Order

`POST /orders`

Create a new order.

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `branch_id` | integer | yes | Location ID. |
| `order_type_id` | integer | yes | Estimate/Order Type ID. |
| `manager_id` | integer | no | Manager ID. |
| `assignee_id` | integer | no | Assigned Employee ID. |
| `asset_id` | integer | no | Asset ID. |
| `client_id` | integer | yes | Client (Person / Organization) ID. |
| `payer_id` | integer | no | Payer (Person / Organization) ID. |
| `ad_campaign_id` | integer | no | Ad Campaign ID. |
| `scheduled_for` | string (date-time) | no | "Scheduled From" date and time (ISO 8601). |
| `scheduled_to` | string (date-time) | no | "Scheduled to" date and time (ISO 8601). |
| `resource_id` | integer | no | Resource ID. |
| `malfunction` | string | no | Malfunction text. |
| `manager_notes` | string | no | Manager notes. |
| `engineer_notes` | string | no | Technician notes. |
| `resume` | string | no | Conclusion / client recommendations. |
| `estimated_price` | string | no | Estimates price or price range. |
| `due_date` | string (date-time) | no | Order Due Date (ISO 8601). |
| `urgent` | boolean | no | Is Order urgent? |
| `custom_fields` | string (json) | no | Custom fields values in format {"f123": "value", "f234": "value"}, where "f123" and "f234" is a custom field id. |

### Example: Create Order with cURL

```bash
curl -X POST "https://api.roapp.io/v2/orders" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "branch_id": 123,
  "order_type_id": 123,
  "manager_id": 123,
  "assignee_id": 123,
  "asset_id": 123,
  "client_id": 123,
  "payer_id": 123,
  "ad_campaign_id": 123,
  "scheduled_for": "2026-10-01T10:00:00Z",
  "scheduled_to": "2026-10-01T10:00:00Z",
  "resource_id": 123,
  "malfunction": "Broken screen",
  "manager_notes": "string",
  "engineer_notes": "string",
  "resume": "string",
  "estimated_price": "100.00",
  "due_date": "2026-10-01T10:00:00Z",
  "urgent": false,
  "custom_fields": "{\"f123\": \"value\"}"
}'
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/create-order

## Update Order

`PATCH /orders/{order_id}`

Update an existing order.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `order_id` | path | integer | yes | Order ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `branch_id` | integer | no | Location ID. |
| `order_type_id` | integer | no | Estimate/Order Type ID. |
| `manager_id` | integer | no | Manager ID. |
| `assignee_id` | integer | no | Assigned Employee ID. |
| `asset_id` | integer | no | Asset ID. |
| `client_id` | integer | no | Client (Person / Organization) ID. |
| `payer_id` | integer | no | Payer (Person / Organization) ID. |
| `ad_campaign_id` | integer | no | Ad Campaign ID. |
| `scheduled_for` | string (date-time) | no | "Scheduled From" date and time (ISO 8601). |
| `scheduled_to` | string (date-time) | no | "Scheduled To" date and time (ISO 8601). |
| `resource_id` | integer | no | Resource ID. |
| `malfunction` | string | no | Malfunction text. |
| `manager_notes` | string | no | Manager notes. |
| `engineer_notes` | string | no | Technician notes. |
| `resume` | string | no | Conclusion / client recommendations. |
| `estimated_price` | string | no | Estimates price or price range. |
| `due_date` | string (date-time) | no | Order Due Date (ISO 8601). |
| `urgent` | string | no | Is Order urgent? |
| `custom_fields` | string (json) | no | Custom fields values in format {"f123": "value", "f234": "value"}, where "f123" and "f234" is a custom field id. |

### Example: Update Order with cURL

```bash
curl -X PATCH "https://api.roapp.io/v2/orders/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "branch_id": 123,
  "order_type_id": 123,
  "manager_id": 123,
  "assignee_id": 123,
  "asset_id": 123,
  "client_id": 123,
  "payer_id": 123,
  "ad_campaign_id": 123,
  "scheduled_for": "2026-10-01T10:00:00Z",
  "scheduled_to": "2026-10-01T10:00:00Z",
  "resource_id": 123,
  "malfunction": "Broken screen",
  "manager_notes": "string",
  "engineer_notes": "string",
  "resume": "string",
  "estimated_price": "100.00",
  "due_date": "2026-10-01T10:00:00Z",
  "urgent": "string",
  "custom_fields": "{\"f123\": \"value\"}"
}'
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/update-order

## Get Order Items

`GET /orders/{order_id}/items`

Retrieve all items (products or services) for a specific order.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `order_id` | path | integer | yes | Order ID. |

### Example: Get Order Items with cURL

```bash
curl -X GET "https://api.roapp.io/v2/orders/123/items" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

### Example response (200)

```json
[
  {
    "id": 78870627,
    "created_at": "2025-05-09T12:52:32Z",
    "assignee_id": 206039,
    "quantity": "1.000",
    "price": "20.00",
    "cost": "100.00000",
    "margin_id": null,
    "is_deduction_required": false,
    "entity": {
      "id": 38527538,
      "type": "service",
      "code": "",
      "sku": "",
      "sn_accounting": false,
      "title": "Diagnostics",
      "image": "",
      "thumbnail": "",
      "uom": {
        "id": 1,
        "title": "pcs",
        "description": "Pieces"
      },
      "is_hidden": false
    },
    "comment": "",
    "write_offs": null,
    "is_refunded": false,
    "discount": {
      "type": "value",
      "percentage": 0,
      "amount": "0.00",
      "sponsor": "staff"
    },
    "warranty": {
      "period": 2,
      "period_units": "days"
    },
    "taxes": [
      {
        "id": 5628,
        "name": "State taxes",
        "rate": 10
      }
    ],
    "expiration_date": null
  }
]
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-order-items

## Add Order Item

`POST /orders/{order_id}/items`

Add a new item to the order.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `order_id` | path | integer | yes | Order ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `entity_id` | integer | yes | Product or Service ID. |
| `assignee_id` | integer | yes | Assigned Employee ID. |
| `quantity` | number (float) | yes | Quantity. |
| `price` | number (float) | yes | Price per unit. |
| `cost` | number (float) | yes | Unit cost. |
| `discount` | object | yes | Item discount object. |
| `discount.type` | string | yes | Discount type. "percentage" — percent, "value" — absolute value. One of: `percentage`, `value`. Default: `"percentage"`. |
| `discount.percentage` | number (float) | yes | Percentage value. Default: `0`. |
| `discount.amount` | number (float) | yes | Default: `0`. |
| `discount.sponsor` | string | yes | "staff" — Employee wages calculation is based on the amount after discount. This way the company discount decreases the piecework employee wages. "company" — Employee commissions will be calculated from amount before discount. This way the company discount won't affect the employee commissions. One of: `staff`, `company`. Default: `"staff"`. |
| `warranty` | object | yes | Item warranty object. |
| `warranty.period` | string | yes | Warranty period. Default: `"0"`. |
| `warranty.periodUnits` | string | yes | Warranty unit of measure. One of: `days`, `months`. Default: `"days"`. |
| `tax_ids` | array<integer> | no | Array of Tax ID. |
| `comment` | string | no | Comment text. |
| `comment_visibility` | string | no | Comment visibility. One of: `private`, `public`. |

### Example: Add Order Item with cURL

```bash
curl -X POST "https://api.roapp.io/v2/orders/123/items" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "entity_id": 123,
  "assignee_id": 123,
  "quantity": 1,
  "price": 100,
  "cost": 100,
  "discount": {
    "type": "percentage",
    "percentage": 123,
    "amount": 100,
    "sponsor": "staff"
  },
  "warranty": {
    "period": "string",
    "periodUnits": "days"
  },
  "tax_ids": [
    123
  ],
  "comment": "Comment text",
  "comment_visibility": "private"
}'
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/create-order-item

## Update Order Item

`PATCH /orders/{order_id}/items/{item_id}`

Update an existing item in the order.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `order_id` | path | integer | yes | Order ID. |
| `item_id` | path | integer | yes | Order Item ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `assignee_id` | integer | no | Assigned Employee ID. |
| `quantity` | number (float) | no | Quantity. |
| `price` | number (float) | no | Price per unit. |
| `cost` | number (float) | no | Unit cost. |
| `discount` | object | no | Item discount object. |
| `discount.type` | string | yes | Discount type. "percentage" — percent, "value" — absolute value. One of: `percentage`, `value`. Default: `"percentage"`. |
| `discount.percentage` | number (float) | yes | Percentage value. Default: `0`. |
| `discount.amount` | number (float) | yes | Amount value. Default: `0`. |
| `discount.sponsor` | string | yes | "staff" — Employee wages calculation is based on the amount after discount. This way the company discount decreases the piecework employee wages. "company" — Employee commissions will be calculated from amount before discount. This way the company discount won't affect the employee commissions. One of: `staff`, `company`. Default: `"staff"`. |
| `warranty` | object | no | Item warranty object. |
| `warranty.period` | string | yes | Warranty period. Default: `"0"`. |
| `warranty.periodUnits` | string | yes | Warranty unit of measure. One of: `days`, `months`. Default: `"days"`. |
| `tax_ids` | array<integer> | no | Array of Tax ID. |
| `comment` | string | no | Comment text. |
| `comment_visibility` | string | no | Comment visibility. One of: `public`, `private`. |

### Example: Update Order Item with cURL

```bash
curl -X PATCH "https://api.roapp.io/v2/orders/123/items/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "assignee_id": 123,
  "quantity": 1,
  "price": 100,
  "cost": 100,
  "discount": {
    "type": "percentage",
    "percentage": 123,
    "amount": 100,
    "sponsor": "staff"
  },
  "warranty": {
    "period": "string",
    "periodUnits": "days"
  },
  "tax_ids": [
    123
  ],
  "comment": "Comment text",
  "comment_visibility": "public"
}'
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/update-order-item

## Update Order Status

`POST /orders/{order_id}/status`

Update the status of a specific order.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `order_id` | path | integer | yes | Order ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `status_id` | integer | yes | Status ID. |
| `comment` | string | no | Status comment. |

### Example: Update Order Status with cURL

```bash
curl -X POST "https://api.roapp.io/v2/orders/123/status" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "status_id": 123,
  "comment": "Comment text"
}'
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/update-order-status

## Create Order Comment

`POST /orders/{order_id}/comments`

Add a comment to a specific order.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `order_id` | path | integer | yes | Order ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `comment` | string | yes | Comment text. |
| `is_private` | boolean | no | Is this comment private? |

### Example: Create Order Comment with cURL

```bash
curl -X POST "https://api.roapp.io/v2/orders/123/comments" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "comment": "Comment text",
  "is_private": false
}'
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/create-order-comment

## Get Order Public Page Url

`GET /orders/{order_id}/public-url`

Retrieve a shareable public link to view the order.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `order_id` | path | integer | yes | Order ID. |

### Example: Get Order Public Page Url with cURL

```bash
curl -X GET "https://api.roapp.io/v2/orders/123/public-url" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-order-public-page-url

## Get Order Statuses

`GET /orders/statuses`

Retrieve a list of all possible statuses that can be assigned to an order.

### Example: Get Order Statuses with cURL

```bash
curl -X GET "https://api.roapp.io/v2/orders/statuses" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-order-statuses

## Get Order Types

`GET /orders/types`

### Example: Get Order Types with cURL

```bash
curl -X GET "https://api.roapp.io/v2/orders/types" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-order-types

## Get Order Custom Fields

`GET /orders/custom-fields`

### Example: Get Order Custom Fields with cURL

```bash
curl -X GET "https://api.roapp.io/v2/orders/custom-fields" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-order-custom-fields

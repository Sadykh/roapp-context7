# RO App API: Estimates

Estimates (quotes) with types, statuses, custom fields, items, comments and a public URL for the client.

Base URL: `https://api.roapp.io/v2`. Authenticate every request with `Authorization: Bearer <API_KEY>` (see [Getting Started](../getting-started.md)).

| Method | Path | Summary |
|---|---|---|
| `GET` | `/estimates` | Get Estimates |
| `GET` | `/estimates/{estimate_id}` | Get Estimate by ID |
| `POST` | `/estimates` | Create Estimate |
| `PATCH` | `/estimates/{estimate_id}` | Update Estimate |
| `GET` | `/estimates/{estimate_id}/items` | Get Estimate Items |
| `POST` | `/estimates/{estimate_id}/items` | Add Estimate Item |
| `PATCH` | `/estimates/{estimate_id}/items/{item_id}` | Update Estimate Item |
| `POST` | `/estimates/{estimate_id}/status` | Change Estimate Status |
| `POST` | `/estimates/{estimate_id}/comments` | Create Estimate Comment |
| `GET` | `/estimates/{estimate_id}/public-url` | Get Estimate Public Page Url |
| `GET` | `/estimates/statuses` | Get Estimate Statuses |
| `GET` | `/estimates/types` | Get Estimate Types |
| `GET` | `/estimates/custom-fields` | Get Estimate Custom Fields |

## Get Estimates

`GET /estimates`

Retrieve a list of estimates.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | number | no | Page number. Default: `1`. |
| `types` | query | array<number> | no | List of estimate type IDs. |
| `branch_ids` | query | array<number> | no | List of location IDs. |
| `ids` | query | array<number> | no | List of estimate IDs. |
| `numbers` | query | array<string> | no | List of estimate document numbers. |
| `statuses` | query | array<number> | no | List of estimate status IDs. |
| `managers` | query | array<number> | no | List of Employee IDs. |
| `client_ids` | query | array<number> | no | List of client IDs. |
| `client_names` | query | array<string> | no | List of client names. |
| `client_phones` | query | array<string> | no | List of Client phone numbers. |
| `created_at` | query | array<string (date-time)> | no | Filter by creation date. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `modified_at` | query | array<string (date-time)> | no | Filter by modification date. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `closed_at` | query | array<string (date-time)> | no | Filter by close date. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `scheduled_for` | query | array<string (date-time)> | no | Filter by "Scheduled from" date and time. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `due_date` | query | array<string (date-time)> | no | Filter by Due date" date and time. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `id`, `-id`, `modified_at`, `-modified_at`, `scheduled_for`, `-scheduled_for`, `due_date`, `-due_date`, `closed_at`, `-closed_at`. |

Paginated: up to 50 entries per page, `count` in the response is the total number of records.

### Example: Get Estimates with cURL

```bash
curl -X GET "https://api.roapp.io/v2/estimates?page=1&types=123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-estimates

## Get Estimate by ID

`GET /estimates/{estimate_id}`

Retrieve detailed information about a specific estimate.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `estimate_id` | path | integer | yes | Estimate ID. |

### Example: Get Estimate by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/estimates/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-estimate-by-id

## Create Estimate

`POST /estimates`

Create a new estimate.

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
| `scheduled_to` | string (date-time) | no | "Scheduled To" date and time (ISO 8601). |
| `resource_id` | integer | no | Resource ID. |
| `malfunction` | string | no | Malfunction text. |
| `manager_notes` | string | no | Manager notes. |
| `engineer_notes` | string | no | Technician notes. |
| `resume` | string | no | Conclusion / client recommendations. |
| `estimated_price` | string | no | Estimates price or price range. |
| `due_date` | string (date-time) | no | Estimate Due Date (ISO 8601). |
| `urgent` | boolean | no | Is Estimate urgent? |
| `custom_fields` | string (json) | no | Custom fields values in format {"f123": "value", "f234": "value"}, where "f123" and "f234" is a custom field id. |

### Example: Create Estimate with cURL

```bash
curl -X POST "https://api.roapp.io/v2/estimates" \
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

Source: https://roapp.readme.io/reference/create-estimate

## Update Estimate

`PATCH /estimates/{estimate_id}`

Update an existing estimate.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `estimate_id` | path | integer | yes | Estimate ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `branch_id` | string | no | Location ID. |
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
| `due_date` | string (date-time) | no | Estimate Due Date (ISO 8601). |
| `urgent` | boolean | no | Is Estimate urgent? |
| `custom_fields` | string (json) | no | Custom fields values in format {"f123": "value", "f234": "value"}, where "f123" and "f234" is a custom field id. |

### Example: Update Estimate with cURL

```bash
curl -X PATCH "https://api.roapp.io/v2/estimates/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "branch_id": "string",
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

Source: https://roapp.readme.io/reference/update-estimate

## Get Estimate Items

`GET /estimates/{estimate_id}/items`

Retrieve all items (products or services) listed in a specific estimate.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `estimate_id` | path | integer | yes | Estimate ID. |

### Example: Get Estimate Items with cURL

```bash
curl -X GET "https://api.roapp.io/v2/estimates/123/items" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-estimate-items

## Add Estimate Item

`POST /estimates/{estimate_id}/items`

Add a new item to the estimate.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `estimate_id` | path | integer | yes | Estimate ID. |

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

### Example: Add Estimate Item with cURL

```bash
curl -X POST "https://api.roapp.io/v2/estimates/123/items" \
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

Source: https://roapp.readme.io/reference/create-estimate-item

## Update Estimate Item

`PATCH /estimates/{estimate_id}/items/{item_id}`

Update an existing item in the estimate.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `estimate_id` | path | string | yes | Estimate ID. |
| `item_id` | path | string | yes | Estimate Item ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `assignee_id` | integer | no | Assigned Employee ID. |
| `quantity` | number (float) | no | Quantity. |
| `price` | number (float) | no | Price per unit. |
| `cost` | number (float) | no | Unit cost. |
| `discount` | object | no |  |
| `discount.type` | string | yes | Discount type. "percentage" — percent, "value" — absolute value. One of: `percentage`, `value`. Default: `"percentage"`. |
| `discount.percentage` | number (float) | yes | Percentage value. Default: `0`. |
| `discount.amount` | number (float) | yes | Default: `0`. |
| `discount.sponsor` | string | yes | "staff" — Employee wages calculation is based on the amount after discount. This way the company discount decreases the piecework employee wages. "company" — Employee commissions will be calculated from amount before discount. This way the company discount won't affect the employee commissions. One of: `staff`, `company`. Default: `"staff"`. |
| `warranty` | object | no |  |
| `warranty.period` | string | yes | Warranty period. Default: `"0"`. |
| `warranty.periodUnits` | string | yes | Warranty unit of measure. One of: `days`, `months`. Default: `"days"`. |
| `tax_ids` | array<integer> | no | Array of Tax ID. |
| `comment` | string | no | Comment text. |
| `comment_visibility` | string | no | Comment visibility. One of: `private`, `public`. |

### Example: Update Estimate Item with cURL

```bash
curl -X PATCH "https://api.roapp.io/v2/estimates/string/items/string" \
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
  "comment_visibility": "private"
}'
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/update-estimate-item

## Change Estimate Status

`POST /estimates/{estimate_id}/status`

Update the status of a specific estimate.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `estimate_id` | path | integer | yes | Estimate ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `status_id` | integer | yes | Status Id. |
| `comment` | string | no | Status comment. |

### Example: Change Estimate Status with cURL

```bash
curl -X POST "https://api.roapp.io/v2/estimates/123/status" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "status_id": 123,
  "comment": "Comment text"
}'
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/change-estimate-status

## Create Estimate Comment

`POST /estimates/{estimate_id}/comments`

Add a comment to a specific estimate.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `estimate_id` | path | integer | yes | Estimate ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `comment` | string | yes | Comment. |
| `is_private` | boolean | no | Is this comment private? Default: `false`. |

### Example: Create Estimate Comment with cURL

```bash
curl -X POST "https://api.roapp.io/v2/estimates/123/comments" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "comment": "Comment text",
  "is_private": false
}'
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/create-estimate-comment

## Get Estimate Public Page Url

`GET /estimates/{estimate_id}/public-url`

Retrieve a shareable public link to view the estimate.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `estimate_id` | path | integer | yes | Estimate ID. |

### Example: Get Estimate Public Page Url with cURL

```bash
curl -X GET "https://api.roapp.io/v2/estimates/123/public-url" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-estimate-public-page-url

## Get Estimate Statuses

`GET /estimates/statuses`

Retrieve a list of all possible statuses that can be assigned to an estimate.

### Example: Get Estimate Statuses with cURL

```bash
curl -X GET "https://api.roapp.io/v2/estimates/statuses" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-estimate-statuses

## Get Estimate Types

`GET /estimates/types`

### Example: Get Estimate Types with cURL

```bash
curl -X GET "https://api.roapp.io/v2/estimates/types" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-estimates-types

## Get Estimate Custom Fields

`GET /estimates/custom-fields`

### Example: Get Estimate Custom Fields with cURL

```bash
curl -X GET "https://api.roapp.io/v2/estimates/custom-fields" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-estimates-custom-fields

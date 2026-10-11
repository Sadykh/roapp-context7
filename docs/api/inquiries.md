# RO App API: Inquiries (Leads)

Inquiries (called *leads* in webhooks, e.g. `Lead.Created`): requests from potential clients, with types, statuses, custom fields and comments.

Base URL: `https://api.roapp.io/v2`. Authenticate every request with `Authorization: Bearer <API_KEY>` (see [Getting Started](../getting-started.md)).

| Method | Path | Summary |
|---|---|---|
| `GET` | `/inquiries` | Get Inquiries |
| `GET` | `/inquiries/{inquiry_id}` | Get Inquiry by ID |
| `POST` | `/inquiries` | Create Inquiry |
| `PATCH` | `/inquiries/{inquiry_id}` | Update Inquiry |
| `POST` | `/inquiries/{inquiry_id}/status` | Update Inquiry Status |
| `POST` | `/inquiries/{inquiry_id}/comments` | Create Inquiry Comment |
| `DELETE` | `/inquiries/{inquiry_id}` | Delete Inquiry |
| `GET` | `/inquiries/statuses` | Get Inquiry Statuses |
| `GET` | `/inquiries/types` | Get Inquiry Types |
| `GET` | `/inquiries/custom-fields` | Get Inquiry Custom Fields |

## Get Inquiries

`GET /inquiries`

Retrieve a list of inquiries.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | number | no | Page number. |
| `types` | query | array<number> | no | List of Inquiry Type IDs (same as order types). |
| `ids` | query | array<number> | no | List of Inquiry IDs. |
| `numbers` | query | array<string> | no | List of Inquiry document numbers. |
| `branch_ids` | query | array<number> | no | List of Location IDs. |
| `statuses` | query | array<number> | no | List of Inquiry Status IDs. |
| `managers` | query | array<number> | no | List of Employee IDs. |
| `clients_ids` | query | array<number> | no | List of Client (Person / Organization) IDs. |
| `client_names` | query | array<string> | no | List of Client (Person / Organization) names. |
| `client_phones` | query | array<string> | no | List of phone numbers. |
| `asset_uid` | query | string | no | List of asset serial numbers (vin, imei). |
| `created_at` | query | array<string (date-time)> | no | Filter by creation date. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `due_date` | query | array<string (date-time)> | no | Filter by due date. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `id`, `-id`, `due_date`, `-due_date`. |

Paginated: up to 50 entries per page, `count` in the response is the total number of records.

### Example: Get Inquiries with cURL

```bash
curl -X GET "https://api.roapp.io/v2/inquiries?page=1&types=123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-inquiries

## Get Inquiry by ID

`GET /inquiries/{inquiry_id}`

Retrieve detailed information about a specific inquiry.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `inquiry_id` | path | number | yes | Inquiry ID. |

### Example: Get Inquiry by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/inquiries/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-inquiry-by-id

## Create Inquiry

`POST /inquiries`

Create a new inquiry.

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `type_id` | number | yes | Inquiry type ID. |
| `branch_id` | number | no | Location ID. |
| `manager_id` | number | no | Manager ID. |
| `asset_id` | number | no | Asset ID. |
| `client_id` | number | no | Client (Person / Organization) ID. |
| `client_name` | string | no | Contact name. |
| `client_phone` | string | no | Contact phone. |
| `email` | string | no | Contact email. |
| `urgent` | boolean | no | Is Inquiry urgent? |
| `due_date` | string (date-time) | no | Inquiry due date. |
| `ad_campaign_id` | number | no | Ad Campaign ID. |
| `comment` | string | no | Inquiry comment. |
| `manager_notes` | string | no | Manager notes. |
| `address` | object | no | Address object. |
| `address.country` | string | yes |  |
| `address.state` | string | no |  |
| `address.city` | string | no |  |
| `address.address_line_1` | string | yes |  |
| `address.address_line_2` | string | no |  |
| `address.postal_code` | string | no |  |
| `address.comment` | string | no |  |
| `custom_fields` | string (json) | no | Custom fields values in format {"f123": "value", "f234": "value"}, where "f123" and "f234" is a custom field id. |

### Example: Create Inquiry with cURL

```bash
curl -X POST "https://api.roapp.io/v2/inquiries" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "type_id": 123,
  "branch_id": 123,
  "manager_id": 123,
  "asset_id": 123,
  "client_id": 123,
  "client_name": "string",
  "client_phone": "+15555550123",
  "email": "client@example.com",
  "urgent": false,
  "due_date": "2026-10-01T10:00:00Z",
  "ad_campaign_id": 123,
  "comment": "Comment text",
  "manager_notes": "string",
  "address": {
    "country": "string",
    "state": "string",
    "city": "string",
    "address_line_1": "string",
    "address_line_2": "string",
    "postal_code": "string",
    "comment": "Comment text"
  },
  "custom_fields": "{\"f123\": \"value\"}"
}'
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/create-inquiry

## Update Inquiry

`PATCH /inquiries/{inquiry_id}`

Update an existed inquiry.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `inquiry_id` | path | number | yes | Inquiry ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `branch_id` | number | yes | Location ID. |
| `manager_id` | number | no | Manager ID. |
| `asset_id` | number | no | Asset ID. |
| `client_id` | number | no | Client (Person / Organization) ID. |
| `client_name` | string | no | Contact name. |
| `client_phone` | string | no | Contact phone. |
| `email` | string | no | Contact email. |
| `urgent` | boolean | no | Is Inquiry urgent? |
| `due_date` | string (date-time) | no | Inquiry due date. |
| `ad_campaign_id` | number | no | Ad Campaign ID. |
| `comment` | string | no | Inquiry comment. |
| `manager_notes` | string | no | Manager notes. |
| `address` | object | no | Address object. |
| `address.country` | string | yes |  |
| `address.state` | string | no |  |
| `address.city` | string | no |  |
| `address.address_line_1` | string | yes |  |
| `address.address_line_2` | string | no |  |
| `address.postal_code` | string | no |  |
| `address.comment` | string | no |  |
| `custom_fields` | string (json) | no | Custom fields values in format {"f123": "value", "f234": "value"}, where "f123" and "f234" is a custom field id. |

### Example: Update Inquiry with cURL

```bash
curl -X PATCH "https://api.roapp.io/v2/inquiries/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "branch_id": 123,
  "manager_id": 123,
  "asset_id": 123,
  "client_id": 123,
  "client_name": "string",
  "client_phone": "+15555550123",
  "email": "client@example.com",
  "urgent": false,
  "due_date": "2026-10-01T10:00:00Z",
  "ad_campaign_id": 123,
  "comment": "Comment text",
  "manager_notes": "string",
  "address": {
    "country": "string",
    "state": "string",
    "city": "string",
    "address_line_1": "string",
    "address_line_2": "string",
    "postal_code": "string",
    "comment": "Comment text"
  },
  "custom_fields": "{\"f123\": \"value\"}"
}'
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/update-inquiry

## Update Inquiry Status

`POST /inquiries/{inquiry_id}/status`

Update the status of a specific inquiry.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `inquiry_id` | path | number | yes | Inquiry ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `status_id` | number | yes | Inquiry Status ID. |
| `comment` | string | no |  |

### Example: Update Inquiry Status with cURL

```bash
curl -X POST "https://api.roapp.io/v2/inquiries/123/status" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "status_id": 123,
  "comment": "Comment text"
}'
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/update-inquiry-status

## Create Inquiry Comment

`POST /inquiries/{inquiry_id}/comments`

Add a comment to a specific inquiry.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `inquiry_id` | path | string | yes | Inquiry ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `comment` | string | yes |  |
| `is_private` | boolean | no | Default: `"true"`. |

### Example: Create Inquiry Comment with cURL

```bash
curl -X POST "https://api.roapp.io/v2/inquiries/string/comments" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "comment": "Comment text",
  "is_private": true
}'
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/create-inquiry-comment

## Delete Inquiry

`DELETE /inquiries/{inquiry_id}`

Delete an existing inquiry.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `inquiry_id` | path | number | yes | Inquiry ID. |

### Example: Delete Inquiry with cURL

```bash
curl -X DELETE "https://api.roapp.io/v2/inquiries/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/delete-inquiry

## Get Inquiry Statuses

`GET /inquiries/statuses`

Retrieve a list of all possible statuses that can be assigned to an inquiry.

### Example: Get Inquiry Statuses with cURL

```bash
curl -X GET "https://api.roapp.io/v2/inquiries/statuses" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-lead-statuses

## Get Inquiry Types

`GET /inquiries/types`

### Example: Get Inquiry Types with cURL

```bash
curl -X GET "https://api.roapp.io/v2/inquiries/types" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-inquiry-types

## Get Inquiry Custom Fields

`GET /inquiries/custom-fields`

### Example: Get Inquiry Custom Fields with cURL

```bash
curl -X GET "https://api.roapp.io/v2/inquiries/custom-fields" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-inquiry-custom-fields

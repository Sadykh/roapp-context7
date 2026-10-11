# RO App API: Bookings

Bookings (appointments) and their items (products/services).

Base URL: `https://api.roapp.io/v2`. Authenticate every request with `Authorization: Bearer <API_KEY>` (see [Getting Started](../getting-started.md)).

| Method | Path | Summary |
|---|---|---|
| `GET` | `/bookings` | Get Bookings |
| `GET` | `/bookings/{booking_id}` | Get Booking by ID |
| `POST` | `/bookings` | Create Booking |
| `PATCH` | `/bookings/{booking_id}` | Update Booking |
| `DELETE` | `/bookings/{booking_id}` | Delete Booking |
| `GET` | `/bookings/{booking_id}/items` | Get Bookings Items |
| `POST` | `/bookings/{booking_id}/items` | Add Booking Item |
| `PATCH` | `/bookings/{booking_id}/items/{item_id}` | Update Booking Item |
| `DELETE` | `/bookings/{booking_id}/items/{item_id}` | Delete Booking Item |

## Get Bookings

`GET /bookings`

Retrieve a list of bookings.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer | no | Page number. Default: `1`. |
| `branches` | query | array<integer> | no | List of Location IDs. |
| `ids` | query | array<integer> | no | List of Booking IDs. |
| `statuses` | query | array<integer> | no | Array of Booking status IDs. |
| `assignees` | query | array<integer> | no | Array of employee IDs. |
| `clients_ids` | query | array<integer> | no | List of client (person / organization) IDs. |
| `client_names` | query | array<string> | no | List of client (person / organization) names. |
| `client_phones` | query | array<string> | no | List of phone numbers. |
| `created_at` | query | array<string (date-time)> | no | Filter by creation date. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `modified_at` | query | array<string (date-time)> | no | Filter by modification date. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `scheduled_for` | query | array<string (date-time)> | no | Filter by "Scheduled from" date and time. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `id`, `-id`, `modified_at`, `-modified_at`, `scheduled_for`, `-scheduled_for`. |

Paginated: up to 50 entries per page, `count` in the response is the total number of records.

### Example: Get Bookings with cURL

```bash
curl -X GET "https://api.roapp.io/v2/bookings?page=1&branches=123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-bookigs

## Get Booking by ID

`GET /bookings/{booking_id}`

Retrieve detailed information about a specific booking.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `booking_id` | path | integer | yes | Booking ID. |

### Example: Get Booking by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/bookings/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-booking-by-id

## Create Booking

`POST /bookings`

Create a new booking.

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `branch_id` | integer | yes | Location ID. |
| `assignee_id` | integer | yes | Assigned Employee ID. |
| `client_id` | integer | yes | Client (Person / Organization) ID. |
| `scheduled_for` | string (date-time) | yes | "Scheduled From" date and time (ISO 8601). |
| `scheduled_to` | string (date-time) | yes | "Scheduled To" date and time (ISO 8601). |
| `resource_id` | integer | no | Resource ID. |
| `comment` | string | no | Comment text. |

### Example: Create Booking with cURL

```bash
curl -X POST "https://api.roapp.io/v2/bookings" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "branch_id": 123,
  "assignee_id": 123,
  "client_id": 123,
  "scheduled_for": "2026-10-01T10:00:00Z",
  "scheduled_to": "2026-10-01T10:00:00Z",
  "resource_id": 123,
  "comment": "Comment text"
}'
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/create-booking

## Update Booking

`PATCH /bookings/{booking_id}`

Update an existing booking.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `booking_id` | path | integer | yes | Booking ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `branch_id` | integer | no | Location ID. |
| `status_id` | integer | no | Booking status ID (1: New, 2: Confirmed, 3: Pending, 4; In progress, 5: Completed 6 - Canceled, 7: No-show). |
| `assignee_id` | integer | no | Assigned employee ID. |
| `client_id` | integer | no | Client (Person / Organization) ID. |
| `scheduled_for` | string (date-time) | no | "Scheduled From" date and time (ISO 8601). |
| `scheduled_to` | string (date-time) | no | "Scheduled To" date and time (ISO 8601). |
| `resource_id` | integer | no | Resource ID. |
| `comment` | string | no | Comment text. |

### Example: Update Booking with cURL

```bash
curl -X PATCH "https://api.roapp.io/v2/bookings/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "branch_id": 123,
  "status_id": 123,
  "assignee_id": 123,
  "client_id": 123,
  "scheduled_for": "2026-10-01T10:00:00Z",
  "scheduled_to": "2026-10-01T10:00:00Z",
  "resource_id": 123,
  "comment": "Comment text"
}'
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/update-booking

## Delete Booking

`DELETE /bookings/{booking_id}`

Delete an existing booking.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `booking_id` | path | integer | yes | Booking ID. |

### Example: Delete Booking with cURL

```bash
curl -X DELETE "https://api.roapp.io/v2/bookings/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/delete-booking

## Get Bookings Items

`GET /bookings/{booking_id}/items`

Retrieve all services for a specific booking.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `booking_id` | path | string | yes | Booking ID. |

### Example: Get Bookings Items with cURL

```bash
curl -X GET "https://api.roapp.io/v2/bookings/string/items" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-bookings-items

## Add Booking Item

`POST /bookings/{booking_id}/items`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `booking_id` | path | integer | yes | Booking ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `entity_id` | integer | yes | Product or Service ID. |
| `quantity` | number (float) | yes | Quantity. |
| `price` | number (float) | no | Price per unit. |
| `cost` | number (float) | no | Unit cost. |
| `discount` | object | no | Item discount object. |
| `discount.type` | string | yes | Discount type. "percentage" — percent, "value" — absolute value. One of: `percentage`, `value`. Default: `"percentage"`. |
| `discount.percentage` | number (float) | yes | Percentage value. Default: `0`. |
| `discount.amount` | number (float) | yes | Default: `0`. |
| `discount.sponsor` | string | yes | "staff" — Employee wages calculation is based on the amount after discount. This way the company discount decreases the piecework employee wages. "company" — Employee commissions will be calculated from amount before discount. This way the company discount won't affect the employee commissions. One of: `staff`, `company`. Default: `"staff"`. |
| `warranty` | object | no | Item warranty object. |
| `warranty.period` | string | yes | Warranty period. Default: `"0"`. |
| `warranty.periodUnits` | string | yes | Warranty unit of measure. One of: `days`, `months`. Default: `"days"`. |
| `tax_ids` | array<integer> | no | Array of Tax IDs. |
| `comment` | string | no | Comment text. |
| `comment_visibility` | string | no | Comment visibility. One of: `public`, `private`. |

### Example: Add Booking Item with cURL

```bash
curl -X POST "https://api.roapp.io/v2/bookings/123/items" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "entity_id": 123,
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

Source: https://roapp.readme.io/reference/add-booking-item

## Update Booking Item

`PATCH /bookings/{booking_id}/items/{item_id}`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `booking_id` | path | integer | yes | Booking ID. |
| `item_id` | path | integer | yes | Booking Item ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `quantity` | integer | no | Quantity. |
| `price` | number (float) | no | Price per unit. |
| `cost` | number (float) | no | Unit cost. |
| `discount` | object | no | Item discount object. |
| `discount.type` | string | yes | Discount type. "percentage" — percent, "value" — absolute value. One of: `percentage`, `value`. Default: `"percentage"`. |
| `discount.percentage` | number (float) | yes | Percentage value. Default: `0`. |
| `discount.amount` | number (float) | yes | Default: `0`. |
| `discount.sponsor` | string | yes | "staff" — Employee wages calculation is based on the amount after discount. This way the company discount decreases the piecework employee wages. "company" — Employee commissions will be calculated from amount before discount. This way the company discount won't affect the employee commissions. One of: `staff`, `company`. Default: `"staff"`. |
| `warranty` | object | no | Item warranty object. |
| `warranty.period` | string | yes | Warranty period. Default: `"0"`. |
| `warranty.periodUnits` | string | yes | Warranty unit of measure. One of: `days`, `months`. Default: `"days"`. |
| `tax_ids` | array<integer> | no | Array of Tax ID. |
| `comment` | string | no | Comment text. One of: `private`, `public`. |

### Example: Update Booking Item with cURL

```bash
curl -X PATCH "https://api.roapp.io/v2/bookings/123/items/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
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
  "comment": "private"
}'
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/update-booking-item

## Delete Booking Item

`DELETE /bookings/{booking_id}/items/{item_id}`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `booking_id` | path | integer | yes | Booking ID. |
| `item_id` | path | integer | yes | Booking Item ID. |

### Example: Delete Booking Item with cURL

```bash
curl -X DELETE "https://api.roapp.io/v2/bookings/123/items/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/delete-booking-item

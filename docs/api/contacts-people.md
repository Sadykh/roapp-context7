# RO App API: Contacts: People

People (individual clients and suppliers): CRUD, comments, merge, custom fields and organization links.

Base URL: `https://api.roapp.io/v2`. Authenticate every request with `Authorization: Bearer <API_KEY>` (see [Getting Started](../getting-started.md)).

| Method | Path | Summary |
|---|---|---|
| `GET` | `/contacts/people` | Get People |
| `GET` | `/contacts/people/{person_id}` | Get Person by ID |
| `GET` | `/contacts/people/{person_id}/organizations` | Get Person's Organization |
| `POST` | `/contacts/people` | Create Person |
| `PATCH` | `/contacts/people/{person_id}` | Update Person |
| `DELETE` | `/contacts/people/{person_id}` | Delete Person |
| `POST` | `/contacts/people/{person_id}/comments` | Create Person Comment |
| `POST` | `/contacts/people/{person_id}/merge` | Merge People |
| `GET` | `/contacts/people/custom-fields` | Get People Custom Fields |

## Get People

`GET /contacts/people`

Retrieve a list of people.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer | no | Page number. Default: `1`. |
| `names` | query | array<string> | no | List of names. |
| `phones` | query | array<string> | no | List of phones. |
| `emails` | query | array<string> | no | List of emails. |
| `managers` | query | array<integer> | no | List of Employee IDs. |
| `tags` | query | array<string> | no | List of tags. |
| `created_at` | query | array<string (date-time)> | no | Filter by creation date. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `modified_at` | query | array<string (date-time)> | no | Filter by modification date. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `id`, `-id`, `modified_at`, `-modified_at`, `name`, `-name`. |

Paginated: up to 50 entries per page, `count` in the response is the total number of records.

### Example: Get People with cURL

```bash
curl -X GET "https://api.roapp.io/v2/contacts/people?page=1&names=John Doe" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-list-of-people

## Get Person by ID

`GET /contacts/people/{person_id}`

Retrieve detailed information about a specific person.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `person_id` | path | integer | yes | Person ID. |

### Example: Get Person by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/contacts/people/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`, `404`

Source: https://roapp.readme.io/reference/get-person-by-id

## Get Person's Organization

`GET /contacts/people/{person_id}/organizations`

Retrieve the organization to which this person belongs.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `person_id` | path | integer | yes | Person ID. |

### Example: Get Person's Organization with cURL

```bash
curl -X GET "https://api.roapp.io/v2/contacts/people/123/organizations" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`, `404`

Source: https://roapp.readme.io/reference/get-person-organizations

## Create Person

`POST /contacts/people`

Create a new person.

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `first_name` | string | yes | Person first name. |
| `last_name` | string | no | Person last name. |
| `birthday` | object | no | Person birthday. |
| `birthday.day` | integer | yes |  |
| `birthday.month` | integer | yes |  |
| `birthday.year` | integer | no |  |
| `email` | string | no | Valid email. |
| `phones` | array<object> | no | List of phone numbers. |
| `phones[].title` | string | yes | Phone's name. |
| `phones[].phone` | string | yes | Phone number in international format. |
| `phones[].notify` | boolean | yes | Is sending SMS allowed to this number? |
| `phones[].has_viber` | boolean | yes | Is sending Viber messaged allowed to this number? |
| `phones[].has_whatsapp` | boolean | yes | Is sending WhatsApp messages allowed to this number? |
| `notes` | string | no | Notes text. |
| `address` | string | no | Person address. |
| `supplier` | boolean | no | Is this person your supplier? Default: `false`. |
| `manager_id` | integer | no | Employee ID. |
| `ad_campaign_id` | integer | no | Ad Campaign ID. |
| `discount_code` | string | no | Discount code. |
| `custom_fields` | string (json) | no | Custom fields values in format {"f123": "value", "f234": "value"}, where "f123" and "f234" is a custom field id. |
| `tags` | array<string> | no | Array of tags. |
| `tax_identification_number` | string | no | Tax identification number. |

### Example: Create Person with cURL

```bash
curl -X POST "https://api.roapp.io/v2/contacts/people" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "first_name": "John",
  "last_name": "Doe",
  "birthday": {
    "day": 1,
    "month": 1,
    "year": 2000
  },
  "email": "client@example.com",
  "phones": [
    {
      "title": "Example",
      "phone": "+15555550123",
      "notify": false,
      "has_viber": false,
      "has_whatsapp": false
    }
  ],
  "notes": "Note text",
  "address": "1 Main St, Springfield",
  "supplier": false,
  "manager_id": 123,
  "ad_campaign_id": 123,
  "discount_code": "SUMMER10",
  "custom_fields": "{\"f123\": \"value\"}",
  "tags": [
    "vip"
  ],
  "tax_identification_number": "string"
}'
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/create-person

## Update Person

`PATCH /contacts/people/{person_id}`

Update an existing person.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `person_id` | path | integer | yes | Person ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `first_name` | string | no | Person first name. |
| `last_name` | string | no | Person last name. |
| `birthday` | object | no | Person birthday. |
| `birthday.day` | integer | yes |  |
| `birthday.month` | integer | yes |  |
| `birthday.year` | integer | no |  |
| `email` | string | no | Valid email. |
| `phones` | array<object> | no | List of phone numbers. |
| `phones[].title` | string | yes | Phone's name. |
| `phones[].phone` | string | yes | Phone number in international format. |
| `phones[].notify` | boolean | yes | Is sending SMS allowed to this number? |
| `phones[].has_viber` | boolean | yes | Is sending Viber messaged allowed to this number? |
| `phones[].has_whatsapp` | boolean | yes | Is sending WhatsApp messages allowed to this number? |
| `notes` | string | no | Notes text. |
| `address` | string | no | Person address. |
| `supplier` | boolean | no | Is this person your supplier? Default: `false`. |
| `manager_id` | integer | no | Employee ID. |
| `ad_campaign_id` | integer | no | Ad Campaign ID. |
| `discount_code` | string | no | Discount code. |
| `custom_fields` | string (json) | no | Custom fields values in format {"f123": "value", "f234": "value"}, where "f123" and "f234" is a custom field id. |
| `tags` | array<string> | no | Array of tags. |
| `tax_identification_number` | string | no | Tax identification number. |

### Example: Update Person with cURL

```bash
curl -X PATCH "https://api.roapp.io/v2/contacts/people/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "first_name": "John",
  "last_name": "Doe",
  "birthday": {
    "day": 1,
    "month": 1,
    "year": 2000
  },
  "email": "client@example.com",
  "phones": [
    {
      "title": "Example",
      "phone": "+15555550123",
      "notify": false,
      "has_viber": false,
      "has_whatsapp": false
    }
  ],
  "notes": "Note text",
  "address": "1 Main St, Springfield",
  "supplier": false,
  "manager_id": 123,
  "ad_campaign_id": 123,
  "discount_code": "SUMMER10",
  "custom_fields": "{\"f123\": \"value\"}",
  "tags": [
    "vip"
  ],
  "tax_identification_number": "string"
}'
```

**Response codes:** `200`, `400`, `404`

Source: https://roapp.readme.io/reference/update-person

## Delete Person

`DELETE /contacts/people/{person_id}`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `person_id` | path | integer | yes | Person ID. |

### Example: Delete Person with cURL

```bash
curl -X DELETE "https://api.roapp.io/v2/contacts/people/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`, `404`

Source: https://roapp.readme.io/reference/delete-person

## Create Person Comment

`POST /contacts/people/{person_id}/comments`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `person_id` | path | integer | yes | Person ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `comment` | string | yes | Comment text. |

### Example: Create Person Comment with cURL

```bash
curl -X POST "https://api.roapp.io/v2/contacts/people/123/comments" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "comment": "Comment text"
}'
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/create-person-comment

## Merge People

`POST /contacts/people/{person_id}/merge`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `person_id` | path | integer | yes | Person ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `ids` | array<integer> | no | Array of person IDs. |

### Example: Merge People with cURL

```bash
curl -X POST "https://api.roapp.io/v2/contacts/people/123/merge" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "ids": [
    123
  ]
}'
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/merge-people

## Get People Custom Fields

`GET /contacts/people/custom-fields`

### Example: Get People Custom Fields with cURL

```bash
curl -X GET "https://api.roapp.io/v2/contacts/people/custom-fields" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-people-custom-fields

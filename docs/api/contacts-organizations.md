# RO App API: Contacts: Organizations

Organizations (company clients and suppliers): CRUD, people membership, comments, merge and custom fields.

Base URL: `https://api.roapp.io/v2`. Authenticate every request with `Authorization: Bearer <API_KEY>` (see [Getting Started](../getting-started.md)).

| Method | Path | Summary |
|---|---|---|
| `GET` | `/contacts/organizations` | Get Organizations |
| `GET` | `/contacts/organizations/{organization_id}` | Get Organization by ID |
| `GET` | `/contacts/organizations/{organization_id}/people` | Get Organization People |
| `POST` | `/contacts/organizations/{organization_id}/people` | Add People to Organization |
| `DELETE` | `/contacts/organizations/{organization_id}/people/{person_id}` | Delete People from Organization |
| `POST` | `/contacts/organizations` | Create Organization |
| `PATCH` | `/contacts/organizations/{organization_id}` | Update Organization |
| `DELETE` | `/contacts/organizations/{organization_id}` | Delete Organization |
| `POST` | `/contacts/organizations/{organization_id}/comments` | Create Organization Comment |
| `POST` | `/contacts/organizations/{organization_id}/merge` | Merge Organizations |
| `GET` | `/contacts/organizations/custom-fields` | Get Organizations Custom Fields |

## Get Organizations

`GET /contacts/organizations`

Retrieve a list of organizations.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer | no | Default: `"1"`. |
| `names` | query | array<string> | no |  |
| `phones` | query | array<string> | no |  |
| `emails` | query | array<string> | no |  |
| `managers` | query | array<integer> | no |  |
| `tags` | query | array<string> | no |  |
| `created_at` | query | array<string (date-time)> | no | Filter by creation date. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `modified_at` | query | array<string (date-time)> | no | Filter by modification date. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `sort` | query | string | no | One of: `id`, `-id`, `name`, `-name`, `-modified_at`, `modified_at`. |

Paginated: up to 50 entries per page, `count` in the response is the total number of records.

### Example: Get Organizations with cURL

```bash
curl -X GET "https://api.roapp.io/v2/contacts/organizations?page=1&names=John Doe" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-organizations

## Get Organization by ID

`GET /contacts/organizations/{organization_id}`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `organization_id` | path | integer | yes | Organization ID. |

### Example: Get Organization by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/contacts/organizations/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-organization-by-id

## Get Organization People

`GET /contacts/organizations/{organization_id}/people`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `organization_id` | path | integer | yes | Organization ID. |

### Example: Get Organization People with cURL

```bash
curl -X GET "https://api.roapp.io/v2/contacts/organizations/123/people" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-organization-people

## Add People to Organization

`POST /contacts/organizations/{organization_id}/people`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `organization_id` | path | integer | yes | Organization ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `contact_id` | integer | yes | Person ID. |

### Example: Add People to Organization with cURL

```bash
curl -X POST "https://api.roapp.io/v2/contacts/organizations/123/people" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "contact_id": 123
}'
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/add-people-to-organization

## Delete People from Organization

`DELETE /contacts/organizations/{organization_id}/people/{person_id}`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `organization_id` | path | integer | yes | Organization ID. |
| `person_id` | path | integer | yes | Person ID. |

### Example: Delete People from Organization with cURL

```bash
curl -X DELETE "https://api.roapp.io/v2/contacts/organizations/123/people/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`, `404`

Source: https://roapp.readme.io/reference/delete-people-from-organization

## Create Organization

`POST /contacts/organizations`

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | yes | Organization name. |
| `email` | string | no | Organization email. |
| `phones` | array<object> | no | List of phone numbers. |
| `phones[].title` | string | yes | Phone's name. |
| `phones[].phone` | string | yes | Phone number in international format. |
| `phones[].notify` | boolean | yes | Is sending SMS allowed to this number? |
| `phones[].has_viber` | boolean | yes | Is sending Viber messaged allowed to this number? |
| `phones[].has_whatsapp` | boolean | yes | Is sending WhatsApp messages allowed to this number? |
| `notes` | string | no | Notes text. |
| `address` | string | no | Organization address. |
| `supplier` | boolean | no | Is this organization your supplier? Default: `false`. |
| `manager_id` | integer | no | Employee ID. |
| `ad_campaign_id` | integer | no | Ad Campaign ID. |
| `discount_code` | string | no | Discount code. |
| `custom_fields` | string (json) | no | Custom fields values in format {"f123": "value", "f234": "value"}, where "f123" and "f234" is a custom field id. |
| `tags` | array<string> | no | Array of tags. |
| `tax_identification_number` | string | no | Tax identification number. |
| `business_registration_number` | string | no | Business registration number. |

### Example: Create Organization with cURL

```bash
curl -X POST "https://api.roapp.io/v2/contacts/organizations" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "Example",
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
  "tax_identification_number": "string",
  "business_registration_number": "string"
}'
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/create-organization

## Update Organization

`PATCH /contacts/organizations/{organization_id}`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `organization_id` | path | integer | yes | Organization ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | no | Organization name. |
| `email` | string | no | Organization email. |
| `phones` | array<object> | no | List of phone numbers. |
| `phones[].title` | string | yes | Phone's name. |
| `phones[].phone` | string | yes | Phone number in international format. |
| `phones[].notify` | boolean | yes | Is sending SMS allowed to this number? |
| `phones[].has_viber` | boolean | yes | Is sending Viber messaged allowed to this number? |
| `phones[].has_whatsapp` | boolean | yes | Is sending WhatsApp messages allowed to this number? |
| `notes` | string | no | Notes text. |
| `address` | string | no | Organization address. |
| `supplier` | boolean | no | Is this organization your supplier? |
| `manager_id` | integer | no | Employee ID. |
| `ad_campaign_id` | integer | no | Ad Campaign ID. |
| `discount_code` | string | no | Discount code. |
| `custom_fields` | string (json) | no | Custom fields values in format {"f123": "value", "f234": "value"}, where "f123" and "f234" is a custom field id. |
| `tags` | array<string> | no | Array of tags. |
| `tax_identification_number` | string | no | Tax identification number. |
| `business_registration_number` | string | no | Business registration number. |

### Example: Update Organization with cURL

```bash
curl -X PATCH "https://api.roapp.io/v2/contacts/organizations/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "Example",
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
  "tax_identification_number": "string",
  "business_registration_number": "string"
}'
```

**Response codes:** `200`, `400`, `404`

Source: https://roapp.readme.io/reference/update-organization

## Delete Organization

`DELETE /contacts/organizations/{organization_id}`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `organization_id` | path | integer | yes | Organization ID. |

### Example: Delete Organization with cURL

```bash
curl -X DELETE "https://api.roapp.io/v2/contacts/organizations/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`, `404`

Source: https://roapp.readme.io/reference/delete-organization

## Create Organization Comment

`POST /contacts/organizations/{organization_id}/comments`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `organization_id` | path | integer | yes | Organization ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `comment` | string | yes | Comment text. |

### Example: Create Organization Comment with cURL

```bash
curl -X POST "https://api.roapp.io/v2/contacts/organizations/123/comments" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "comment": "Comment text"
}'
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/create-organization-comment

## Merge Organizations

`POST /contacts/organizations/{organization_id}/merge`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `organization_id` | path | integer | yes | Organization ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `ids` | array<integer> | yes | Array of organization IDs. |

### Example: Merge Organizations with cURL

```bash
curl -X POST "https://api.roapp.io/v2/contacts/organizations/123/merge" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "ids": [
    123
  ]
}'
```

**Response codes:** `200`, `400`, `404`

Source: https://roapp.readme.io/reference/merge-organizations

## Get Organizations Custom Fields

`GET /contacts/organizations/custom-fields`

### Example: Get Organizations Custom Fields with cURL

```bash
curl -X GET "https://api.roapp.io/v2/contacts/organizations/custom-fields" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-organizations-custom-fields

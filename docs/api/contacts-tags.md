# RO App API: Contacts: Tags

Tags that can be assigned to people and organizations.

Base URL: `https://api.roapp.io/v2`. Authenticate every request with `Authorization: Bearer <API_KEY>` (see [Getting Started](../getting-started.md)).

| Method | Path | Summary |
|---|---|---|
| `GET` | `/contacts/tags` | Get Contact Tags |
| `GET` | `/contacts/tags/{tag_id}` | Get Tag by Id |
| `POST` | `/contacts/tags` | Create Tag |
| `PATCH` | `/contacts/tags/{tag_id}` | Update Tag |
| `DELETE` | `/contacts/tags/{tag_id}` | Delete Tag |

## Get Contact Tags

`GET /contacts/tags`

Retrieve a list of contact tags.

### Example: Get Contact Tags with cURL

```bash
curl -X GET "https://api.roapp.io/v2/contacts/tags" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-contact-tags

## Get Tag by Id

`GET /contacts/tags/{tag_id}`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `tag_id` | path | integer | yes | Tag ID. |

### Example: Get Tag by Id with cURL

```bash
curl -X GET "https://api.roapp.io/v2/contacts/tags/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-tag-by-id

## Create Tag

`POST /contacts/tags`

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | yes | Tag name. |
| `color_name` | string | no | Tag color name. One of: `red`, `green`, `blue`, `navy`, `pink`, `yellow`, `orange`, `grey`. |

### Example: Create Tag with cURL

```bash
curl -X POST "https://api.roapp.io/v2/contacts/tags" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "Example",
  "color_name": "red"
}'
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/create-tag

## Update Tag

`PATCH /contacts/tags/{tag_id}`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `tag_id` | path | integer | yes | Tag ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | no | Tag name. |
| `color_name` | string | no | Tag color name. One of: `red`, `green`, `blue`, `navy`, `pink`, `yellow`, `orange`, `grey`. |

### Example: Update Tag with cURL

```bash
curl -X PATCH "https://api.roapp.io/v2/contacts/tags/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "Example",
  "color_name": "red"
}'
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/update-tag

## Delete Tag

`DELETE /contacts/tags/{tag_id}`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `tag_id` | path | integer | yes | Tag ID. |

### Example: Delete Tag with cURL

```bash
curl -X DELETE "https://api.roapp.io/v2/contacts/tags/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/delete-tag

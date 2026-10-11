# RO App API: Sales

Point-of-sale (retail) sales. Read-only.

Base URL: `https://api.roapp.io/v2`. Authenticate every request with `Authorization: Bearer <API_KEY>` (see [Getting Started](../getting-started.md)).

| Method | Path | Summary |
|---|---|---|
| `GET` | `/sales` | Get Sales |
| `GET` | `/sales/{id}` | Get Sale by ID |

## Get Sales

`GET /sales`

Returns the list of company sales.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | integer | no | Page number. |
| `branch_ids` | query | array<number> | no | List of Location IDs. |
| `created_at` | query | array<string (date-time)> | no | Filter by creation date. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `created_by_ids` | query | array<integer> | no | List of Employee IDs. |
| `client_ids` | query | array<integer> | no | List of Client (Person / Organization) IDs. |
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `id`, `-id`. |

Paginated: up to 50 entries per page, `count` in the response is the total number of records.

### Example: Get Sales with cURL

```bash
curl -X GET "https://api.roapp.io/v2/sales?page=1&branch_ids=123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

### Example response (200)

```json
{
  "data": [
    {
      "id": 23097650,
      "id_label": "A026",
      "created_at": 1747750438000,
      "created_by_id": 206037,
      "client_id": 33775229,
      "warehouse_id": 3649247,
      "products": [
        {
          "title": "Ailun Glass Screen Protector for iPhone 11",
          "uom": {
            "id": 1,
            "description": "Pieces",
            "title": "pcs"
          },
          "code": "",
          "article": "",
          "amount": 1,
          "price": 10,
          "cost": 100,
          "discount_value": 0,
          "service": false,
          "type": 0
        }
      ],
      "description": "",
      "ad_campaign": {}
    }
  ],
  "page": 1,
  "count": 30,
  "success": true
}
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-sales

## Get Sale by ID

`GET /sales/{id}`

Retrieve detailed information about a specific sale.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | number | yes | Sale ID. |

### Example: Get Sale by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/sales/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

### Example response (200)

```json
{
  "data": [
    {
      "id": 23097650,
      "id_label": "A026",
      "created_at": 1747750438000,
      "created_by_id": 206037,
      "client_id": 33775229,
      "warehouse_id": 3649247,
      "products": [
        {
          "title": "Ailun Glass Screen Protector for iPhone 11",
          "uom": {
            "id": 1,
            "description": "Pieces",
            "title": "pcs"
          },
          "code": "",
          "article": "",
          "amount": 1,
          "price": 10,
          "cost": 100,
          "discount_value": 0,
          "service": false,
          "type": 0
        }
      ],
      "description": "",
      "ad_campaign": {}
    }
  ],
  "page": 1,
  "count": 30,
  "success": true
}
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-sale-by-id

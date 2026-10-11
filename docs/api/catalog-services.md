# RO App API: Catalog: Services

Services catalog: categories, units of measure, services, prices and default price settings.

Base URL: `https://api.roapp.io/v2`. Authenticate every request with `Authorization: Bearer <API_KEY>` (see [Getting Started](../getting-started.md)).

| Method | Path | Summary |
|---|---|---|
| `GET` | `/catalog/services/categories` | Get Service Categories |
| `GET` | `/catalog/services/categories/{id}` | Get Service Category by ID |
| `GET` | `/catalog/services/uoms` | Get Service Unit Of Measure |
| `GET` | `/catalog/services/uoms/{id}` | Get Service Unit Of Measure by ID |
| `GET` | `/catalog/services` | Get Services |
| `GET` | `/catalog/services/{id}` | Get Service by ID |
| `POST` | `/catalog/services` | Create Service |
| `PATCH` | `/catalog/services/{service_id}` | Update Service |
| `DELETE` | `/catalog/services/{service_id}` | Delete Service |
| `GET` | `/catalog/services/prices` | Get Service Prices |
| `GET` | `/catalog/services/prices/{id}` | Get Service Price by ID |
| `GET` | `/catalog/services/settings` | Get Service Settings |

## Get Service Categories

`GET /catalog/services/categories`

Retrieve a list of service categories.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `parent_id` | query | number | no | Parent Category ID. |
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `id`, `-id`, `title`, `-title`. |

### Example: Get Service Categories with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/services/categories?parent_id=123&sort=id" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-service-categories-1

## Get Service Category by ID

`GET /catalog/services/categories/{id}`

Retrieve detailed information about a specific service category.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | number | yes | Service Category ID. |

### Example: Get Service Category by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/services/categories/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-service-category-by-id

## Get Service Unit Of Measure

`GET /catalog/services/uoms`

Retrieve a list of service UOMs.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `title`, `-title`. |

### Example: Get Service Unit Of Measure with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/services/uoms?sort=title" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-service-unit-of-meature

## Get Service Unit Of Measure by ID

`GET /catalog/services/uoms/{id}`

Retrieve detailed information about a specific service UOM.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | number | yes | Service Unit Of Measure ID. |

### Example: Get Service Unit Of Measure by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/services/uoms/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-service-unit-of-measure-by-id

## Get Services

`GET /catalog/services`

Retrieve a list of services.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `q` | query | string | no | Search query used to filter services by name. |
| `barcode` | query | string | no | Service barcode. |
| `category_ids` | query | array<number> | no | List of Service Category IDs. |
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `title`, `-title`. |

### Example: Get Services with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/services?q=screen&barcode=4006381333931" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-services

## Get Service by ID

`GET /catalog/services/{id}`

Retrieve detailed information about a specific service.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | number | yes | Service ID. |

### Example: Get Service by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/services/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-service-by-id-1

## Create Service

`POST /catalog/services`

Create a new service.

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `category_id` | number | yes | Service Category ID. |
| `title` | string | yes | Service title. |
| `description` | string | no | Service description. |
| `type` | string | no | One of: `labor`, `service`. |
| `uom_id` | number | yes | Unit of Measure ID. Default: `"1"`. |
| `cost` | string | no | Service cost. |
| `prices` | array<object> | no | List of prices. |
| `prices[].id` | number | yes | Price ID. |
| `prices[].price` | string | yes | Price value. |
| `duration` | number | no | Service duration in minutes. |
| `warranty` | object | no | Service warranty object. |
| `warranty.period` | number | yes | Warranty period. |
| `warranty.unit` | string | no | Warranty unit of measure. One of: `days`, `months`. |
| `barcodes` | array<object> | no | List of barcodes. |
| `barcodes[].type` | string | yes | Barcode type. One of: `ean8`, `ean13`, `qrcode`, `code128`. |
| `barcodes[].code` | string | yes | Barcode value. |

### Example: Create Service with cURL

```bash
curl -X POST "https://api.roapp.io/v2/catalog/services" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "category_id": 123,
  "title": "Example",
  "description": "Description text",
  "type": "labor",
  "uom_id": 123,
  "cost": "100.00",
  "prices": [
    {
      "id": 123,
      "price": "100.00"
    }
  ],
  "duration": 123,
  "warranty": {
    "period": 123,
    "unit": "days"
  },
  "barcodes": [
    {
      "type": "ean8",
      "code": "USD"
    }
  ]
}'
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/create-service

## Update Service

`PATCH /catalog/services/{service_id}`

Update an existing service.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `service_id` | path | string | yes | Service ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `category_id` | number | no | Service Category ID. |
| `title` | string | no | Service title. |
| `description` | string | no | Service description. |
| `type` | string | no | One of: `labor`, `service`. |
| `uom_id` | number | no | Unit of Measure ID. |
| `cost` | string | no | Service cost. |
| `prices` | array<object> | no | Service prices. |
| `prices[].id` | number | yes | Service Price ID. |
| `prices[].price` | string | yes | Price value. |
| `duration` | number | no | Service duration in minutes. |
| `warranty` | object | no | Service warranty object. |
| `warranty.period` | number | yes | Warranty period. |
| `warranty.unit` | string | yes | Warranty unit of measure. One of: `days`, `months`. |
| `barcodes` | array<object> | no | List of barcodes. |
| `barcodes[].type` | string | yes | Barcode type. One of: `ean8`, `ean13`, `qrcode`, `code128`. |
| `barcodes[].code` | string | yes | Barcode value. |

### Example: Update Service with cURL

```bash
curl -X PATCH "https://api.roapp.io/v2/catalog/services/string" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "category_id": 123,
  "title": "Example",
  "description": "Description text",
  "type": "labor",
  "uom_id": 123,
  "cost": "100.00",
  "prices": [
    {
      "id": 123,
      "price": "100.00"
    }
  ],
  "duration": 123,
  "warranty": {
    "period": 123,
    "unit": "days"
  },
  "barcodes": [
    {
      "type": "ean8",
      "code": "USD"
    }
  ]
}'
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/update-service

## Delete Service

`DELETE /catalog/services/{service_id}`

Delete an existing service.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `service_id` | path | number | yes | Service ID. |

### Example: Delete Service with cURL

```bash
curl -X DELETE "https://api.roapp.io/v2/catalog/services/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/delete-service

## Get Service Prices

`GET /catalog/services/prices`

Retrieve a list of service prices.

### Example: Get Service Prices with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/services/prices" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-service-prices

## Get Service Price by ID

`GET /catalog/services/prices/{id}`

Retrieve detailed information about a specific service price.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | number | yes | Service Price ID. |

### Example: Get Service Price by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/services/prices/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-service-price-by-id

## Get Service Settings

`GET /catalog/services/settings`

Retrieve settings for default service prices.

### Example: Get Service Settings with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/services/settings" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-service-settings

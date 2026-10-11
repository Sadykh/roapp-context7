# RO App API: Catalog: Bundles

Bundles are predefined sets of products and/or services that can be added to documents at once.

Base URL: `https://api.roapp.io/v2`. Authenticate every request with `Authorization: Bearer <API_KEY>` (see [Getting Started](../getting-started.md)).

| Method | Path | Summary |
|---|---|---|
| `GET` | `/catalog/bundles/categories` | Get Bundle Categories |
| `GET` | `/catalog/bundles/categories/{id}` | Get Bundle Category by ID |
| `GET` | `/catalog/bundles` | Get Bundles |
| `GET` | `/catalog/bundles/{id}` | Get Bundle by ID |
| `POST` | `/catalog/bundles` | Create Bundle |
| `PATCH` | `/catalog/bundles/{bundle_id}` | Update Bundle |
| `DELETE` | `/catalog/bundles/{bundle_id}` | Delete Bundle |
| `GET` | `/catalog/bundles/{id}/items` | Get Bundle Items |
| `POST` | `/catalog/bundles/{bundle_id}/items` | Add Bundle Item |
| `PATCH` | `/catalog/bundles/{bundle_id}/items/{item_id}` | Update Bundle Item |
| `DELETE` | `/catalog/bundles/{bundle_id}/items/{item_id}` | Delete Bundle Item |

## Get Bundle Categories

`GET /catalog/bundles/categories`

Retrieve a list of bundle categories.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `parent_id` | query | number | no | Parent Category ID. |
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `id`, `-id`, `title`, `-title`. |

### Example: Get Bundle Categories with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/bundles/categories?parent_id=123&sort=id" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-bundle-categories

## Get Bundle Category by ID

`GET /catalog/bundles/categories/{id}`

Retrieve detailed information about a specific bundle category.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | number | yes | Bundle Category ID. |

### Example: Get Bundle Category by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/bundles/categories/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-bundle-category-by-id

## Get Bundles

`GET /catalog/bundles`

Retrieve a list of bundles.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `q` | query | string | no | Search query used to filter bundles by name. |
| `barcode` | query | string | no | Bundle barcode. |
| `category_ids` | query | array<number> | no | List of Service Category IDs. |
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `title`, `-title`. |

### Example: Get Bundles with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/bundles?q=screen&barcode=4006381333931" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-bundles-1

## Get Bundle by ID

`GET /catalog/bundles/{id}`

Retrieve detailed information about a specific bundle.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | number | yes | Bundle ID. |

### Example: Get Bundle by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/bundles/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-bundle-by-id

## Create Bundle

`POST /catalog/bundles`

Create a new bundle.

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `title` | string | yes |  |
| `description` | string | no |  |
| `category_id` | number | yes | Bundle Category ID. |
| `barcode` | object | no | Bundle Barcode. |
| `barcode.type` | string | yes | Barcode type. One of: `ean8`, `ean13`, `qrcode`, `code128`, `upc`. |
| `barcode.code` | string | yes | Barcode value. |

### Example: Create Bundle with cURL

```bash
curl -X POST "https://api.roapp.io/v2/catalog/bundles" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "title": "Example",
  "description": "Description text",
  "category_id": 123,
  "barcode": {
    "type": "ean8",
    "code": "USD"
  }
}'
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/create-bundle

## Update Bundle

`PATCH /catalog/bundles/{bundle_id}`

Update an existed bundle.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bundle_id` | path | number | yes | Bundle ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `title` | string | no |  |
| `description` | string | no |  |
| `category_id` | number | no |  |
| `barcode` | object | no |  |
| `barcode.type` | string | yes | Barcode type. One of: `ean8`, `ean13`, `qrcode`, `code128`, `upc`. |
| `barcode.code` | string | yes | Barcode value. |

### Example: Update Bundle with cURL

```bash
curl -X PATCH "https://api.roapp.io/v2/catalog/bundles/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "title": "Example",
  "description": "Description text",
  "category_id": 123,
  "barcode": {
    "type": "ean8",
    "code": "USD"
  }
}'
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/update-bundle

## Delete Bundle

`DELETE /catalog/bundles/{bundle_id}`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bundle_id` | path | string | yes | Bundle ID. |

### Example: Delete Bundle with cURL

```bash
curl -X DELETE "https://api.roapp.io/v2/catalog/bundles/string" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/delete-bundle

## Get Bundle Items

`GET /catalog/bundles/{id}/items`

Retrieve all items (products or services) for a specific bundle.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | number | yes | Bundle ID. |

### Example: Get Bundle Items with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/bundles/123/items" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-bundle-items

## Add Bundle Item

`POST /catalog/bundles/{bundle_id}/items`

Add a new item to the bundle.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bundle_id` | path | number | yes | Bundle ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `entity_id` | number | yes | Product ID. |
| `quantity` | string | yes |  |
| `price` | string | yes |  |
| `warranty` | object | no |  |
| `warranty.period` | string | yes |  |
| `warranty.unit` | string | yes | One of: `days`, `months`. |
| `discount` | object | no |  |
| `discount.type` | string | yes | One of: `percentage`, `value`. |
| `discount.percentage` | number | yes |  |
| `discount.amount` | string | yes |  |
| `discount.sponsor` | string | yes | One of: `staff`, `company`. |

### Example: Add Bundle Item with cURL

```bash
curl -X POST "https://api.roapp.io/v2/catalog/bundles/123/items" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "entity_id": 123,
  "quantity": "string",
  "price": "100.00",
  "warranty": {
    "period": "string",
    "unit": "days"
  },
  "discount": {
    "type": "percentage",
    "percentage": 123,
    "amount": "100.00",
    "sponsor": "staff"
  }
}'
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/add-bundle-item

## Update Bundle Item

`PATCH /catalog/bundles/{bundle_id}/items/{item_id}`

Update an existed item in the bundle.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bundle_id` | path | number | yes | Bundle ID. |
| `item_id` | path | string | yes | Bundle Item ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `entity_id` | number | no | Product ID. |
| `quantity` | string | no |  |
| `price` | string | no |  |
| `warranty` | object | no |  |
| `warranty.period` | string | yes |  |
| `warranty.unit` | string | yes | One of: `days`, `months`. |
| `discount` | object | no |  |
| `discount.type` | string | yes | One of: `percentage`, `value`. |
| `discount.percentage` | number | yes |  |
| `discount.amount` | string | yes |  |
| `discount.sponsor` | string | yes | One of: `staff`, `company`. |

### Example: Update Bundle Item with cURL

```bash
curl -X PATCH "https://api.roapp.io/v2/catalog/bundles/123/items/string" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "entity_id": 123,
  "quantity": "string",
  "price": "100.00",
  "warranty": {
    "period": "string",
    "unit": "days"
  },
  "discount": {
    "type": "percentage",
    "percentage": 123,
    "amount": "100.00",
    "sponsor": "staff"
  }
}'
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/update-bundle-item

## Delete Bundle Item

`DELETE /catalog/bundles/{bundle_id}/items/{item_id}`

Delete an existing bundle item.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `bundle_id` | path | string | yes | Bundle ID. |
| `item_id` | path | string | yes | Bundle Item ID. |

### Example: Delete Bundle Item with cURL

```bash
curl -X DELETE "https://api.roapp.io/v2/catalog/bundles/string/items/string" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/delete-bundle-item

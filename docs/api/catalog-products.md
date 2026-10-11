# RO App API: Catalog: Products

Products (inventory items) catalog: categories, units of measure, product types, custom fields, products, prices and default price settings.

Base URL: `https://api.roapp.io/v2`. Authenticate every request with `Authorization: Bearer <API_KEY>` (see [Getting Started](../getting-started.md)).

| Method | Path | Summary |
|---|---|---|
| `GET` | `/catalog/products/categories` | Get Product Categories |
| `GET` | `/catalog/products/categories/{id}` | Get Product Category by ID |
| `GET` | `/catalog/products/uoms` | Get Product Unit Of Measures |
| `GET` | `/catalog/products/uoms/{id}` | Get Product Unit Of Measure by ID |
| `GET` | `/catalog/products/types` | Get Product Types |
| `GET` | `/catalog/products/custom-fields` | Get Product Custom Fields |
| `GET` | `/catalog/products` | Get Products |
| `GET` | `/catalog/products/{id}` | Get Product by ID |
| `POST` | `/catalog/products` | Create Product |
| `PATCH` | `/catalog/products/{product_id}` | Update Product |
| `DELETE` | `/catalog/products/{product_id}` | Delete Product |
| `GET` | `/catalog/products/prices` | Get Product Prices |
| `GET` | `/catalog/products/prices/{id}` | Get Product Price by ID |
| `GET` | `/catalog/products/settings` | Get Product Settings |

## Get Product Categories

`GET /catalog/products/categories`

Retrieve a list of product categories.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `parent_id` | query | number | no | Parent Category ID. |

### Example: Get Product Categories with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/products/categories?parent_id=123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-product-categories-1

## Get Product Category by ID

`GET /catalog/products/categories/{id}`

Retrieve detailed information about a specific product category.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | number | yes | Product Category ID. |

### Example: Get Product Category by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/products/categories/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-product-category-by-id

## Get Product Unit Of Measures

`GET /catalog/products/uoms`

Retrieve a list of product UOMs.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `title`, `-title`. |

### Example: Get Product Unit Of Measures with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/products/uoms?sort=title" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-product-unit-of-measures

## Get Product Unit Of Measure by ID

`GET /catalog/products/uoms/{id}`

Retrieve detailed information about a specific product UOM.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | number | yes | Product Unit Of Measure ID. |

### Example: Get Product Unit Of Measure by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/products/uoms/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-product-unit-of-measure-by-id

## Get Product Types

`GET /catalog/products/types`

Retrieve a list of product types.

### Example: Get Product Types with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/products/types" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-product-types

## Get Product Custom Fields

`GET /catalog/products/custom-fields`

### Example: Get Product Custom Fields with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/products/custom-fields" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-product-custom-fields

## Get Products

`GET /catalog/products`

Retrieve a list of products.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `q` | query | string | no | Search query used to filter products by name. |
| `barcode` | query | string | no | Product barcode. |
| `category_ids` | query | array<number> | no | List of Service Category IDs. |
| `sku` | query | string | no | Product SKU. |
| `code` | query | string | no | Product inner code. |
| `mpn` | query | string | no | Manufacturer Part Number. |
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `title`, `-title`. |

### Example: Get Products with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/products?q=screen&barcode=4006381333931" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-products-1

## Get Product by ID

`GET /catalog/products/{id}`

Retrieve detailed information about a specific product.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | number | yes | Product ID. |

### Example: Get Product by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/products/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-product-by-id-1

## Create Product

`POST /catalog/products`

Create a new product.

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `product_type_id` | number | yes | Product Type ID. |
| `category_id` | number | yes | Product Category ID. |
| `title` | string | yes | Product title. |
| `description` | string | no | Product description. |
| `sku` | string | no | Product SKU. |
| `code` | string | no | Product Code. |
| `mpn` | string | no | Manufacturer Part Number. |
| `uom_id` | number | yes | Unit of Measure ID. Default: `"1"`. |
| `barcodes` | array<object> | no | List of barcodes. |
| `barcodes[].type` | string | yes | Barcode type. One of: `ean8`, `ean13`, `qrcode`, `code128`, `upc`. |
| `barcodes[].code` | string | yes | Barcode value. |
| `prices` | array<object> | no | Product prices. |
| `prices[].id` | number | yes | Product Price ID. |
| `prices[].price` | string | yes | Price value. |
| `dimensions_and_weight` | object | no | Dimensions and weight parameters. |
| `dimensions_and_weight.is_enabled` | boolean | yes | Default: `"false"`. |
| `dimensions_and_weight.dimensions` | object | yes |  |
| `dimensions_and_weight.dimensions.length` | string | yes |  |
| `dimensions_and_weight.dimensions.width` | string | yes |  |
| `dimensions_and_weight.dimensions.height` | string | yes |  |
| `dimensions_and_weight.dimensions.unit` | string | yes | Dimensions unit of measure. One of: `mm`, `cm`, `in`. |
| `dimensions_and_weight.weight` | object | yes |  |
| `dimensions_and_weight.weight.value` | string | yes | Weight value. |
| `dimensions_and_weight.weight.unit` | string | yes | Weight unit of measure. One of: `g`, `kg`, `lb`. |
| `expiration_tracking` | object | no |  |
| `expiration_tracking.is_enabled` | boolean | yes | Default: `"false"`. |
| `expiration_tracking.expiration_soon_alert` | object | yes |  |
| `expiration_tracking.expiration_soon_alert.is_enabled` | boolean | yes | Default: `"false"`. |
| `expiration_tracking.expiration_soon_alert.value` | string | yes |  |
| `expiration_tracking.expiration_soon_alert.unit` | string | yes | One of: `days`, `months`. |
| `expiration_tracking.critical_alert` | object | yes |  |
| `expiration_tracking.critical_alert.is_enabled` | boolean | yes | Default: `"false"`. |
| `expiration_tracking.critical_alert.value` | string | yes |  |
| `expiration_tracking.critical_alert.unit` | string | yes | One of: `days`, `months`. |
| `default_supplier_id` | number | no | Default supplier for this product. |
| `warranty` | object | no | Product warranty. |
| `warranty.period` | number | yes |  |
| `warranty.unit` | string | yes | One of: `days`, `months`. |
| `is_serial` | boolean | no | Whether serial number tracking is enabled for this product. |

### Example: Create Product with cURL

```bash
curl -X POST "https://api.roapp.io/v2/catalog/products" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "product_type_id": 123,
  "category_id": 123,
  "title": "Example",
  "description": "Description text",
  "sku": "SKU-001",
  "code": "USD",
  "mpn": "MPN-001",
  "uom_id": 123,
  "barcodes": [
    {
      "type": "ean8",
      "code": "USD"
    }
  ],
  "prices": [
    {
      "id": 123,
      "price": "100.00"
    }
  ],
  "dimensions_and_weight": {
    "is_enabled": false,
    "dimensions": {
      "length": "string",
      "width": "string",
      "height": "string",
      "unit": "mm"
    },
    "weight": {
      "value": "100.00",
      "unit": "g"
    }
  },
  "expiration_tracking": {
    "is_enabled": false,
    "expiration_soon_alert": {
      "is_enabled": false,
      "value": "100.00",
      "unit": "days"
    },
    "critical_alert": {
      "is_enabled": false,
      "value": "100.00",
      "unit": "days"
    }
  },
  "default_supplier_id": 123,
  "warranty": {
    "period": 123,
    "unit": "days"
  },
  "is_serial": false
}'
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/create-product

## Update Product

`PATCH /catalog/products/{product_id}`

Update an existing product.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `product_id` | path | number | yes | Product ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `product_type_id` | number | no | Product Type ID. |
| `category_id` | number | no | Product Category ID. |
| `title` | string | no | Product title. |
| `description` | string | no | Product description. |
| `sku` | string | no | Product SKU. |
| `code` | string | no | Product Code. |
| `mpn` | string | no | Manufacturer Part Number. |
| `uom_id` | string | no | Unit of Measure ID. |
| `barcodes` | array<object> | no | List of barcodes. |
| `barcodes[].type` | string | yes | Barcode type. One of: `ean8`, `ean13`, `qrcode`, `code128`, `upc`. |
| `barcodes[].code` | string | yes | Barcode value. |
| `prices` | array<object> | no | Product prices. |
| `prices[].id` | number | yes | Product Price ID. |
| `prices[].price` | string | yes | Price value. |
| `dimensions_and_weight` | object | no | Dimensions and weight parameters. |
| `dimensions_and_weight.is_enabled` | boolean | yes |  |
| `dimensions_and_weight.dimensions` | object | yes |  |
| `dimensions_and_weight.dimensions.length` | string | yes |  |
| `dimensions_and_weight.dimensions.width` | string | yes |  |
| `dimensions_and_weight.dimensions.height` | string | yes |  |
| `dimensions_and_weight.dimensions.unit` | string | yes | Dimensions unit of measure. One of: `mm`, `cm`, `in`. |
| `dimensions_and_weight.weight` | object | yes |  |
| `dimensions_and_weight.weight.value` | string | yes | Weight value. |
| `dimensions_and_weight.weight.unit` | string | yes | Weight unit of measure. One of: `g`, `kg`, `lb`. |
| `expiration_tracking` | object | no |  |
| `expiration_tracking.is_enabled` | boolean | yes |  |
| `expiration_tracking.expiration_soon_alert` | object | yes |  |
| `expiration_tracking.expiration_soon_alert.is_enabled` | boolean | yes | Default: `"false"`. |
| `expiration_tracking.expiration_soon_alert.value` | string | yes |  |
| `expiration_tracking.expiration_soon_alert.unit` | string | yes | One of: `days`, `months`. |
| `expiration_tracking.critical_alert` | object | yes |  |
| `expiration_tracking.critical_alert.is_enabled` | boolean | yes | Default: `"false"`. |
| `expiration_tracking.critical_alert.value` | string | yes |  |
| `expiration_tracking.critical_alert.unit` | string | yes | One of: `days`, `months`. |
| `default_supplier_id` | number | no | Default supplier for this product. |
| `warranty` | object | no | Product warranty. |
| `warranty.period` | number | yes |  |
| `warranty.unit` | string | yes | One of: `days`, `months`. |
| `is_serial` | boolean | no | Whether serial number tracking is enabled for this product. |

### Example: Update Product with cURL

```bash
curl -X PATCH "https://api.roapp.io/v2/catalog/products/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "product_type_id": 123,
  "category_id": 123,
  "title": "Example",
  "description": "Description text",
  "sku": "SKU-001",
  "code": "USD",
  "mpn": "MPN-001",
  "uom_id": "string",
  "barcodes": [
    {
      "type": "ean8",
      "code": "USD"
    }
  ],
  "prices": [
    {
      "id": 123,
      "price": "100.00"
    }
  ],
  "dimensions_and_weight": {
    "is_enabled": false,
    "dimensions": {
      "length": "string",
      "width": "string",
      "height": "string",
      "unit": "mm"
    },
    "weight": {
      "value": "100.00",
      "unit": "g"
    }
  },
  "expiration_tracking": {
    "is_enabled": false,
    "expiration_soon_alert": {
      "is_enabled": false,
      "value": "100.00",
      "unit": "days"
    },
    "critical_alert": {
      "is_enabled": false,
      "value": "100.00",
      "unit": "days"
    }
  },
  "default_supplier_id": 123,
  "warranty": {
    "period": 123,
    "unit": "days"
  },
  "is_serial": false
}'
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/update-product

## Delete Product

`DELETE /catalog/products/{product_id}`

Delete an existing product.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `product_id` | path | number | yes | Product ID. |

### Example: Delete Product with cURL

```bash
curl -X DELETE "https://api.roapp.io/v2/catalog/products/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/delete-product

## Get Product Prices

`GET /catalog/products/prices`

Retrieve a list of product prices.

### Example: Get Product Prices with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/products/prices" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-product-prices

## Get Product Price by ID

`GET /catalog/products/prices/{id}`

Retrieve detailed information about a specific product price.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | number | yes | Product Price ID. |

### Example: Get Product Price by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/products/prices/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-product-price-by-id

## Get Product Settings

`GET /catalog/products/settings`

Retrieve settings for default product prices.

### Example: Get Product Settings with cURL

```bash
curl -X GET "https://api.roapp.io/v2/catalog/products/settings" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-product-settings

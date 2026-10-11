# RO App API: Invoices

Invoices with items, statuses and comments.

Base URL: `https://api.roapp.io/v2`. Authenticate every request with `Authorization: Bearer <API_KEY>` (see [Getting Started](../getting-started.md)).

| Method | Path | Summary |
|---|---|---|
| `GET` | `/invoices` | Get Invoices |
| `GET` | `/invoices/{invoice_id}` | Get Invoice by ID |
| `POST` | `/invoices` | Create Invoice |
| `PATCH` | `/invoices/{id}` | Update Invoice |
| `DELETE` | `/invoices/{id}` | Delete Invoice |
| `GET` | `/invoices/{invoice_id}/items` | Get Invoice Items |
| `GET` | `/invoices/{invoice_id}/items/{item_id}` | Get Invoice Item by ID |
| `POST` | `/invoices/{invoice_id}/items` | Add Invoice Item |
| `PATCH` | `/invoices/{invoice_id}/items/{item_id}` | Update Invoice Item |
| `DELETE` | `/invoices/{invoice_id}/items/{item_id}` | Delete Invoice Item |
| `POST` | `/invoices/{invoice_id}/status` | Update Invoice Status |
| `POST` | `/invoices/{invoice_id}/comments` | Create Invoice Comment |
| `GET` | `/invoices/statuses` | Get Invoice Statuses |

## Get Invoices

`GET /invoices`

Retrieve a list of invoices.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | number | no | Page number. Default: `1`. |
| `legal_entity_id` | query | number | no | Legal entity ID. |
| `ids` | query | array<number> | no | List of Invoice IDs. |
| `numbers` | query | array<string> | no | List of Invoice document numbers. |
| `payment_method` | query | string | no | Invoice payment method. One of: `cash`, `cashless`, `credit_card`. |
| `statuses` | query | array<number> | no | List of Invoice status IDs. |
| `client_ids` | query | array<number> | no | List of Client (Person / Organization) IDs. |
| `payer_ids` | query | array<number> | no | List of Payer IDs. |
| `managers` | query | array<number> | no | List of Manager IDs. |
| `created_at` | query | array<string (date-time)> | no | Filter by creation date. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `modified_at` | query | array<string (date-time)> | no | Filter by modification date. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `issue_date` | query | array<string (date-time)> | no | Filter by date of issue. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `due_date` | query | array<string (date-time)> | no | Filter by due date. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `id`, `-id`. |

Paginated: up to 50 entries per page, `count` in the response is the total number of records.

### Example: Get Invoices with cURL

```bash
curl -X GET "https://api.roapp.io/v2/invoices?page=1&legal_entity_id=123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

### Example response (200)

```json
{
  "data": [
    {
      "id": 309859,
      "id_label": "023",
      "client": {
        "id": 31152179,
        "name": "Chris Jules",
        "first_name": "Chris",
        "last_name": "Jules",
        "email": "chrissy_jules14@gmail.com",
        "phone": [
          "4487645389"
        ],
        "notes": "",
        "address": "",
        "supplier": false,
        "juridical": false,
        "conflicted": false,
        "modified_at": 1734549792000,
        "created_at": 1714652929000,
        "discount_code": "",
        "discount_goods": 0,
        "order_discount_services": 5,
        "sale_discount_services": 5,
        "discount_materials": 0,
        "custom_fields": {
          "f7757287": 968112000000
        },
        "ad_campaign": {
          "id": 349683,
          "name": "Friend"
        }
      },
      "payer": {
        "id": 31152179,
        "name": "Chris Jules",
        "first_name": "Chris",
        "last_name": "Jules",
        "email": "chrissy_jules14@gmail.com",
        "phone": [
          "4487645389"
        ],
        "notes": "",
        "address": "",
        "supplier": false,
        "juridical": false,
        "conflicted": false,
        "modified_at": 1734549792000,
        "created_at": 1714652929000,
        "discount_code": "",
        "discount_goods": 0,
        "order_discount_services": 5,
        "sale_discount_services": 5,
        "discount_materials": 0,
        "custom_fields": {
          "f7757287": 968112000000
        },
        "ad_campaign": {
          "id": 349683,
          "name": "Friend"
        }
      },
      "status": 0,
      "status_full": {
        "id": 3319497,
        "name": "Paid",
        "color": "#5CB85C",
        "group": 10
      },
      "created_at": 1740480923000,
      "issue_date": 1740480920000,
      "due_date": 1743072920000,
      "payment_type": 0,
      "products": [
        {
          "amount": 1,
          "id": 2847134,
          "order_id": 52100568,
          "price": 47.5,
  ...
```

### Response fields

| Field | Type | Required | Description |
|---|---|---|---|
| `data` | array<object> | no |  |
| `data[].id` | integer | no |  |
| `data[].id_label` | string | no |  |
| `data[].client` | object | no |  |
| `data[].client.id` | integer | no |  |
| `data[].client.name` | string | no |  |
| `data[].client.first_name` | string | no |  |
| `data[].client.last_name` | string | no |  |
| `data[].client.email` | string | no |  |
| `data[].client.phone` | array<string> | no |  |
| `data[].client.notes` | string | no |  |
| `data[].client.address` | string | no |  |
| `data[].client.supplier` | boolean | no |  |
| `data[].client.juridical` | boolean | no |  |
| `data[].client.conflicted` | boolean | no |  |
| `data[].client.modified_at` | integer | no |  |
| `data[].client.created_at` | integer | no |  |
| `data[].client.discount_code` | string | no |  |
| `data[].client.discount_goods` | integer | no |  |
| `data[].client.order_discount_services` | integer | no |  |
| `data[].client.sale_discount_services` | integer | no |  |
| `data[].client.discount_materials` | integer | no |  |
| `data[].client.custom_fields` | object | no |  |
| `data[].client.custom_fields.f7757287` | integer | no |  |
| `data[].client.ad_campaign` | object | no |  |
| `data[].client.ad_campaign.id` | integer | no |  |
| `data[].client.ad_campaign.name` | string | no |  |
| `data[].payer` | object | no |  |
| `data[].payer.id` | integer | no |  |
| `data[].payer.name` | string | no |  |
| `data[].payer.first_name` | string | no |  |
| `data[].payer.last_name` | string | no |  |
| `data[].payer.email` | string | no |  |
| `data[].payer.phone` | array<string> | no |  |
| `data[].payer.notes` | string | no |  |
| `data[].payer.address` | string | no |  |
| `data[].payer.supplier` | boolean | no |  |
| `data[].payer.juridical` | boolean | no |  |
| `data[].payer.conflicted` | boolean | no |  |
| `data[].payer.modified_at` | integer | no |  |
| `data[].payer.created_at` | integer | no |  |
| `data[].payer.discount_code` | string | no |  |
| `data[].payer.discount_goods` | integer | no |  |
| `data[].payer.order_discount_services` | integer | no |  |
| `data[].payer.sale_discount_services` | integer | no |  |
| `data[].payer.discount_materials` | integer | no |  |
| `data[].payer.custom_fields` | object | no |  |
| `data[].payer.custom_fields.f7757287` | integer | no |  |
| `data[].payer.ad_campaign` | object | no |  |
| `data[].payer.ad_campaign.id` | integer | no |  |
| `data[].payer.ad_campaign.name` | string | no |  |
| `data[].status` | integer | no |  |
| `data[].status_full` | object | no |  |
| `data[].status_full.id` | integer | no |  |
| `data[].status_full.name` | string | no |  |
| `data[].status_full.color` | string | no |  |
| `data[].status_full.group` | integer | no |  |
| `data[].created_at` | integer | no |  |
| `data[].issue_date` | integer | no |  |
| `data[].due_date` | integer | no |  |
| `data[].payment_type` | integer | no |  |
| `data[].products` | array<object> | no |  |
| `data[].products[].amount` | integer | no |  |
| `data[].products[].id` | integer | no |  |
| `data[].products[].order_id` | integer | no |  |
| `data[].products[].price` | number | no |  |
| `data[].products[].title` | string | no |  |
| `data[].products[].uom_id` | integer | no |  |
| `data[].products[].type` | integer | no |  |
| `data[].products[].service` | boolean | no |  |
| `data[].products[].warranty` | integer | no |  |
| `data[].products[].warranty_period` | integer | no |  |
| `data[].manager_id` | integer | no |  |
| `page` | integer | no |  |
| `count` | integer | no |  |
| `success` | boolean | no |  |

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-invoices

## Get Invoice by ID

`GET /invoices/{invoice_id}`

Retrieve detailed information about a specific invoice.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `invoice_id` | path | number | yes | Invoice ID. |

### Example: Get Invoice by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/invoices/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

### Example response (200)

```json
{
  "data": {
    "id": 309859,
    "id_label": "023",
    "client": {
      "id": 31152179,
      "name": "Chris Jules",
      "first_name": "Chris",
      "last_name": "Jules",
      "email": "chrissy_jules14@gmail.com",
      "phone": [
        "4487645389"
      ],
      "notes": "",
      "address": "",
      "supplier": false,
      "juridical": false,
      "conflicted": false,
      "modified_at": 1734549792000,
      "created_at": 1714652929000,
      "discount_code": "",
      "discount_goods": 0,
      "order_discount_services": 5,
      "sale_discount_services": 5,
      "discount_materials": 0,
      "custom_fields": {
        "f7757287": 968112000000
      },
      "ad_campaign": {
        "id": 349683,
        "name": "Friend"
      }
    },
    "payer": {
      "id": 31152179,
      "name": "Chris Jules",
      "first_name": "Chris",
      "last_name": "Jules",
      "email": "chrissy_jules14@gmail.com",
      "phone": [
        "4487645389"
      ],
      "notes": "",
      "address": "",
      "supplier": false,
      "juridical": false,
      "conflicted": false,
      "modified_at": 1734549792000,
      "created_at": 1714652929000,
      "discount_code": "",
      "discount_goods": 0,
      "order_discount_services": 5,
      "sale_discount_services": 5,
      "discount_materials": 0,
      "custom_fields": {
        "f7757287": 968112000000
      },
      "ad_campaign": {
        "id": 349683,
        "name": "Friend"
      }
    },
    "status": 0,
    "status_full": {
      "id": 3319497,
      "name": "Paid",
      "color": "#5CB85C",
      "group": 10
    },
    "created_at": 1740480923000,
    "issue_date": 1740480920000,
    "due_date": 1743072920000,
    "payment_type": 0,
    "products": [
      {
        "amount": 1,
        "id": 2847134,
        "order_id": 52100568,
        "price": 47.5,
        "title": "Delivery",
  ...
```

### Response fields

| Field | Type | Required | Description |
|---|---|---|---|
| `data` | object | no |  |
| `data.id` | integer | no |  |
| `data.id_label` | string | no |  |
| `data.client` | object | no |  |
| `data.client.id` | integer | no |  |
| `data.client.name` | string | no |  |
| `data.client.first_name` | string | no |  |
| `data.client.last_name` | string | no |  |
| `data.client.email` | string | no |  |
| `data.client.phone` | array<string> | no |  |
| `data.client.notes` | string | no |  |
| `data.client.address` | string | no |  |
| `data.client.supplier` | boolean | no |  |
| `data.client.juridical` | boolean | no |  |
| `data.client.conflicted` | boolean | no |  |
| `data.client.modified_at` | integer | no |  |
| `data.client.created_at` | integer | no |  |
| `data.client.discount_code` | string | no |  |
| `data.client.discount_goods` | integer | no |  |
| `data.client.order_discount_services` | integer | no |  |
| `data.client.sale_discount_services` | integer | no |  |
| `data.client.discount_materials` | integer | no |  |
| `data.client.custom_fields` | object | no |  |
| `data.client.custom_fields.f7757287` | integer | no |  |
| `data.client.ad_campaign` | object | no |  |
| `data.client.ad_campaign.id` | integer | no |  |
| `data.client.ad_campaign.name` | string | no |  |
| `data.payer` | object | no |  |
| `data.payer.id` | integer | no |  |
| `data.payer.name` | string | no |  |
| `data.payer.first_name` | string | no |  |
| `data.payer.last_name` | string | no |  |
| `data.payer.email` | string | no |  |
| `data.payer.phone` | array<string> | no |  |
| `data.payer.notes` | string | no |  |
| `data.payer.address` | string | no |  |
| `data.payer.supplier` | boolean | no |  |
| `data.payer.juridical` | boolean | no |  |
| `data.payer.conflicted` | boolean | no |  |
| `data.payer.modified_at` | integer | no |  |
| `data.payer.created_at` | integer | no |  |
| `data.payer.discount_code` | string | no |  |
| `data.payer.discount_goods` | integer | no |  |
| `data.payer.order_discount_services` | integer | no |  |
| `data.payer.sale_discount_services` | integer | no |  |
| `data.payer.discount_materials` | integer | no |  |
| `data.payer.custom_fields` | object | no |  |
| `data.payer.custom_fields.f7757287` | integer | no |  |
| `data.payer.ad_campaign` | object | no |  |
| `data.payer.ad_campaign.id` | integer | no |  |
| `data.payer.ad_campaign.name` | string | no |  |
| `data.status` | integer | no |  |
| `data.status_full` | object | no |  |
| `data.status_full.id` | integer | no |  |
| `data.status_full.name` | string | no |  |
| `data.status_full.color` | string | no |  |
| `data.status_full.group` | integer | no |  |
| `data.created_at` | integer | no |  |
| `data.issue_date` | integer | no |  |
| `data.due_date` | integer | no |  |
| `data.payment_type` | integer | no |  |
| `data.products` | array<object> | no |  |
| `data.products[].amount` | integer | no |  |
| `data.products[].id` | integer | no |  |
| `data.products[].order_id` | integer | no |  |
| `data.products[].price` | number | no |  |
| `data.products[].title` | string | no |  |
| `data.products[].uom_id` | integer | no |  |
| `data.products[].type` | integer | no |  |
| `data.products[].service` | boolean | no |  |
| `data.products[].warranty` | integer | no |  |
| `data.products[].warranty_period` | integer | no |  |
| `data.manager_id` | integer | no |  |
| `success` | boolean | no |  |

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-invoice-by-id

## Create Invoice

`POST /invoices`

Create a new invoice.

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `issue_date` | string | no | Invoice issue date (example: "2025-10-29"). |
| `due_date` | string | no | Invoice due date (example: "2025-10-29"). |
| `client_id` | number | yes | Client (Person / Organization) ID. |
| `payer_id` | number | no | Payer (Person / Organization) ID. |
| `payment_method` | string | yes | One of: `cash`, `cashless`, `credit_card`. Default: `"cashless"`. |
| `legal_entity_id` | number | no | Legal Entity ID. |
| `manager_id` | number | no | Employee ID. |
| `comment` | string | no | Comment text. |
| `items` | array<object> | no | List of invoice items (associated with Catalog listings). |
| `items[].entity_id` | number | yes | Product or Service ID. |
| `items[].quantity` | number | yes | Quantity. |
| `items[].price` | number | yes | Price per unit. |
| `items[].discount` | object | no | Discount object. |
| `items[].discount.type` | string | yes | Discount type. "percentage" — percent, "value" — absolute value. One of: `percentage`, `value`. |
| `items[].discount.percentage` | number | yes | Percentage value. |
| `items[].discount.amount` | number | yes | Amount value. |
| `items[].discount.sponsor` | string | yes | "staff" — Employee wages calculation is based on the amount after discount. This way the company discount decreases the piecework employee wages. "company" — Employee commissions will be calculated from amount before discount. This way the company discount won't affect the employee commissions. One of: `staff`, `company`. |
| `items[].warranty` | object | no | Warranty object. |
| `items[].warranty.period` | number | yes | Warranty period. |
| `items[].warranty.unit` | string | yes | Warranty unit of measure. One of: `days`, `months`. |
| `items[].tax_ids` | array<number> | no | List of tax IDs. |
| `items[].comment` | string | no | Comment text. |
| `items[].comment_visibility` | string | no | Comment visibility. One of: `public`, `private`. |
| `items_custom` | array<object> | no | List of invoice items (one-time products and services). |
| `items_custom[].entity` | object | yes | Custom product or service object. |
| `items_custom[].entity.type` | string | yes | Product or service. One of: `product`, `service`. |
| `items_custom[].entity.title` | string | yes |  |
| `items_custom[].entity.description` | string | no |  |
| `items_custom[].entity.uom_id` | number | yes | Unit of measure ID. |
| `items_custom[].quantity` | number | yes | Quantity. |
| `items_custom[].price` | number | yes | Price per unit. |
| `items_custom[].comment` | string | no | Comment text. |
| `items_custom[].comment_visibility` | string | no | Comment visibility. One of: `private`, `public`. |
| `items_custom[].discount` | object | no | Discount object. |
| `items_custom[].discount.type` | string | yes | Discount type. "percentage" — percent, "value" — absolute value. One of: `percentage`, `value`. |
| `items_custom[].discount.percentage` | number | yes | Percentage value. |
| `items_custom[].discount.amount` | number | yes | Amount value. |
| `items_custom[].discount.sponsor` | string | yes | "staff" — Employee wages calculation is based on the amount after discount. This way the company discount decreases the piecework employee wages. "company" — Employee commissions will be calculated from amount before discount. This way the company discount won't affect the employee commissions. One of: `staff`, `company`. |
| `items_custom[].warranty` | object | no | Warranty object. |
| `items_custom[].warranty.period` | number | yes | Warranty period. |
| `items_custom[].warranty.unit` | string | yes | Warranty unit of measure. One of: `days`, `months`. |
| `items_custom[].tax_ids` | array<number> | no | List of tax IDs. |

### Example: Create Invoice with cURL

```bash
curl -X POST "https://api.roapp.io/v2/invoices" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "issue_date": "string",
  "due_date": "2026-10-01T10:00:00Z",
  "client_id": 123,
  "payer_id": 123,
  "payment_method": "cash",
  "legal_entity_id": 123,
  "manager_id": 123,
  "comment": "Comment text",
  "items": [
    {
      "entity_id": 123,
      "quantity": 1,
      "price": 100,
      "discount": {
        "type": "percentage",
        "percentage": 123,
        "amount": 100,
        "sponsor": "staff"
      },
      "warranty": {
        "period": 123,
        "unit": "days"
      },
      "tax_ids": [
        123
      ],
      "comment": "Comment text",
      "comment_visibility": "public"
    }
  ],
  "items_custom": [
    {
      "entity": {
        "type": "product",
        "title": "Example",
        "description": "Description text",
        "uom_id": 123
      },
      "quantity": 1,
      "price": 100,
      "comment": "Comment text",
      "comment_visibility": "private",
      "discount": {
        "type": "percentage",
        "percentage": 123,
        "amount": 100,
        "sponsor": "staff"
      },
      "warranty": {
        "period": 123,
        "unit": "days"
      },
      "tax_ids": [
        123
      ]
    }
  ]
}'
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/create-invoice

## Update Invoice

`PATCH /invoices/{id}`

Update an existing invoice.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | number | yes | Invoice ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `issue_date` | string | no | Invoice issue date (example: "2025-10-29"). |
| `due_date` | string | no | Invoice due date (example: "2025-10-29"). |
| `client_id` | number | no | Client (Person / Organization) ID. |
| `payer_id` | number | no | Client (Person / Organization) ID. |
| `payment_type` | string | no | One of: `cash`, `cashless`, `credit_card`. |
| `manager_id` | number | no | Employee ID. |
| `comment` | string | no | Comment text. |

### Example: Update Invoice with cURL

```bash
curl -X PATCH "https://api.roapp.io/v2/invoices/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "issue_date": "string",
  "due_date": "2026-10-01T10:00:00Z",
  "client_id": 123,
  "payer_id": 123,
  "payment_type": "cash",
  "manager_id": 123,
  "comment": "Comment text"
}'
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/update-invoice

## Delete Invoice

`DELETE /invoices/{id}`

Delete an existing invoice.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | number | yes | Invoice ID. |

### Example: Delete Invoice with cURL

```bash
curl -X DELETE "https://api.roapp.io/v2/invoices/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/delete-invoice

## Get Invoice Items

`GET /invoices/{invoice_id}/items`

Retrieve all items (products or services) for a specific invoice.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `invoice_id` | path | number | yes | Invoice ID. |

### Example: Get Invoice Items with cURL

```bash
curl -X GET "https://api.roapp.io/v2/invoices/123/items" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

### Example response (200)

```json
{
  "data": {
    "id": 309859,
    "id_label": "023",
    "client": {
      "id": 31152179,
      "name": "Chris Jules",
      "first_name": "Chris",
      "last_name": "Jules",
      "email": "chrissy_jules14@gmail.com",
      "phone": [
        "4487645389"
      ],
      "notes": "",
      "address": "",
      "supplier": false,
      "juridical": false,
      "conflicted": false,
      "modified_at": 1734549792000,
      "created_at": 1714652929000,
      "discount_code": "",
      "discount_goods": 0,
      "order_discount_services": 5,
      "sale_discount_services": 5,
      "discount_materials": 0,
      "custom_fields": {
        "f7757287": 968112000000
      },
      "ad_campaign": {
        "id": 349683,
        "name": "Friend"
      }
    },
    "payer": {
      "id": 31152179,
      "name": "Chris Jules",
      "first_name": "Chris",
      "last_name": "Jules",
      "email": "chrissy_jules14@gmail.com",
      "phone": [
        "4487645389"
      ],
      "notes": "",
      "address": "",
      "supplier": false,
      "juridical": false,
      "conflicted": false,
      "modified_at": 1734549792000,
      "created_at": 1714652929000,
      "discount_code": "",
      "discount_goods": 0,
      "order_discount_services": 5,
      "sale_discount_services": 5,
      "discount_materials": 0,
      "custom_fields": {
        "f7757287": 968112000000
      },
      "ad_campaign": {
        "id": 349683,
        "name": "Friend"
      }
    },
    "status": 0,
    "status_full": {
      "id": 3319497,
      "name": "Paid",
      "color": "#5CB85C",
      "group": 10
    },
    "created_at": 1740480923000,
    "issue_date": 1740480920000,
    "due_date": 1743072920000,
    "payment_type": 0,
    "products": [
      {
        "amount": 1,
        "id": 2847134,
        "order_id": 52100568,
        "price": 47.5,
        "title": "Delivery",
  ...
```

### Response fields

| Field | Type | Required | Description |
|---|---|---|---|
| `data` | object | no |  |
| `data.id` | integer | no |  |
| `data.id_label` | string | no |  |
| `data.client` | object | no |  |
| `data.client.id` | integer | no |  |
| `data.client.name` | string | no |  |
| `data.client.first_name` | string | no |  |
| `data.client.last_name` | string | no |  |
| `data.client.email` | string | no |  |
| `data.client.phone` | array<string> | no |  |
| `data.client.notes` | string | no |  |
| `data.client.address` | string | no |  |
| `data.client.supplier` | boolean | no |  |
| `data.client.juridical` | boolean | no |  |
| `data.client.conflicted` | boolean | no |  |
| `data.client.modified_at` | integer | no |  |
| `data.client.created_at` | integer | no |  |
| `data.client.discount_code` | string | no |  |
| `data.client.discount_goods` | integer | no |  |
| `data.client.order_discount_services` | integer | no |  |
| `data.client.sale_discount_services` | integer | no |  |
| `data.client.discount_materials` | integer | no |  |
| `data.client.custom_fields` | object | no |  |
| `data.client.custom_fields.f7757287` | integer | no |  |
| `data.client.ad_campaign` | object | no |  |
| `data.client.ad_campaign.id` | integer | no |  |
| `data.client.ad_campaign.name` | string | no |  |
| `data.payer` | object | no |  |
| `data.payer.id` | integer | no |  |
| `data.payer.name` | string | no |  |
| `data.payer.first_name` | string | no |  |
| `data.payer.last_name` | string | no |  |
| `data.payer.email` | string | no |  |
| `data.payer.phone` | array<string> | no |  |
| `data.payer.notes` | string | no |  |
| `data.payer.address` | string | no |  |
| `data.payer.supplier` | boolean | no |  |
| `data.payer.juridical` | boolean | no |  |
| `data.payer.conflicted` | boolean | no |  |
| `data.payer.modified_at` | integer | no |  |
| `data.payer.created_at` | integer | no |  |
| `data.payer.discount_code` | string | no |  |
| `data.payer.discount_goods` | integer | no |  |
| `data.payer.order_discount_services` | integer | no |  |
| `data.payer.sale_discount_services` | integer | no |  |
| `data.payer.discount_materials` | integer | no |  |
| `data.payer.custom_fields` | object | no |  |
| `data.payer.custom_fields.f7757287` | integer | no |  |
| `data.payer.ad_campaign` | object | no |  |
| `data.payer.ad_campaign.id` | integer | no |  |
| `data.payer.ad_campaign.name` | string | no |  |
| `data.status` | integer | no |  |
| `data.status_full` | object | no |  |
| `data.status_full.id` | integer | no |  |
| `data.status_full.name` | string | no |  |
| `data.status_full.color` | string | no |  |
| `data.status_full.group` | integer | no |  |
| `data.created_at` | integer | no |  |
| `data.issue_date` | integer | no |  |
| `data.due_date` | integer | no |  |
| `data.payment_type` | integer | no |  |
| `data.products` | array<object> | no |  |
| `data.products[].amount` | integer | no |  |
| `data.products[].id` | integer | no |  |
| `data.products[].order_id` | integer | no |  |
| `data.products[].price` | number | no |  |
| `data.products[].title` | string | no |  |
| `data.products[].uom_id` | integer | no |  |
| `data.products[].type` | integer | no |  |
| `data.products[].service` | boolean | no |  |
| `data.products[].warranty` | integer | no |  |
| `data.products[].warranty_period` | integer | no |  |
| `data.manager_id` | integer | no |  |
| `success` | boolean | no |  |

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-invoice-items

## Get Invoice Item by ID

`GET /invoices/{invoice_id}/items/{item_id}`

Retrieve a specific invoice item by ID.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `invoice_id` | path | number | yes | Invoice ID. |
| `item_id` | path | number | yes | Item ID. |

### Example: Get Invoice Item by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/invoices/123/items/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

### Example response (200)

```json
{
  "data": {
    "id": 309859,
    "id_label": "023",
    "client": {
      "id": 31152179,
      "name": "Chris Jules",
      "first_name": "Chris",
      "last_name": "Jules",
      "email": "chrissy_jules14@gmail.com",
      "phone": [
        "4487645389"
      ],
      "notes": "",
      "address": "",
      "supplier": false,
      "juridical": false,
      "conflicted": false,
      "modified_at": 1734549792000,
      "created_at": 1714652929000,
      "discount_code": "",
      "discount_goods": 0,
      "order_discount_services": 5,
      "sale_discount_services": 5,
      "discount_materials": 0,
      "custom_fields": {
        "f7757287": 968112000000
      },
      "ad_campaign": {
        "id": 349683,
        "name": "Friend"
      }
    },
    "payer": {
      "id": 31152179,
      "name": "Chris Jules",
      "first_name": "Chris",
      "last_name": "Jules",
      "email": "chrissy_jules14@gmail.com",
      "phone": [
        "4487645389"
      ],
      "notes": "",
      "address": "",
      "supplier": false,
      "juridical": false,
      "conflicted": false,
      "modified_at": 1734549792000,
      "created_at": 1714652929000,
      "discount_code": "",
      "discount_goods": 0,
      "order_discount_services": 5,
      "sale_discount_services": 5,
      "discount_materials": 0,
      "custom_fields": {
        "f7757287": 968112000000
      },
      "ad_campaign": {
        "id": 349683,
        "name": "Friend"
      }
    },
    "status": 0,
    "status_full": {
      "id": 3319497,
      "name": "Paid",
      "color": "#5CB85C",
      "group": 10
    },
    "created_at": 1740480923000,
    "issue_date": 1740480920000,
    "due_date": 1743072920000,
    "payment_type": 0,
    "products": [
      {
        "amount": 1,
        "id": 2847134,
        "order_id": 52100568,
        "price": 47.5,
        "title": "Delivery",
  ...
```

### Response fields

| Field | Type | Required | Description |
|---|---|---|---|
| `data` | object | no |  |
| `data.id` | integer | no |  |
| `data.id_label` | string | no |  |
| `data.client` | object | no |  |
| `data.client.id` | integer | no |  |
| `data.client.name` | string | no |  |
| `data.client.first_name` | string | no |  |
| `data.client.last_name` | string | no |  |
| `data.client.email` | string | no |  |
| `data.client.phone` | array<string> | no |  |
| `data.client.notes` | string | no |  |
| `data.client.address` | string | no |  |
| `data.client.supplier` | boolean | no |  |
| `data.client.juridical` | boolean | no |  |
| `data.client.conflicted` | boolean | no |  |
| `data.client.modified_at` | integer | no |  |
| `data.client.created_at` | integer | no |  |
| `data.client.discount_code` | string | no |  |
| `data.client.discount_goods` | integer | no |  |
| `data.client.order_discount_services` | integer | no |  |
| `data.client.sale_discount_services` | integer | no |  |
| `data.client.discount_materials` | integer | no |  |
| `data.client.custom_fields` | object | no |  |
| `data.client.custom_fields.f7757287` | integer | no |  |
| `data.client.ad_campaign` | object | no |  |
| `data.client.ad_campaign.id` | integer | no |  |
| `data.client.ad_campaign.name` | string | no |  |
| `data.payer` | object | no |  |
| `data.payer.id` | integer | no |  |
| `data.payer.name` | string | no |  |
| `data.payer.first_name` | string | no |  |
| `data.payer.last_name` | string | no |  |
| `data.payer.email` | string | no |  |
| `data.payer.phone` | array<string> | no |  |
| `data.payer.notes` | string | no |  |
| `data.payer.address` | string | no |  |
| `data.payer.supplier` | boolean | no |  |
| `data.payer.juridical` | boolean | no |  |
| `data.payer.conflicted` | boolean | no |  |
| `data.payer.modified_at` | integer | no |  |
| `data.payer.created_at` | integer | no |  |
| `data.payer.discount_code` | string | no |  |
| `data.payer.discount_goods` | integer | no |  |
| `data.payer.order_discount_services` | integer | no |  |
| `data.payer.sale_discount_services` | integer | no |  |
| `data.payer.discount_materials` | integer | no |  |
| `data.payer.custom_fields` | object | no |  |
| `data.payer.custom_fields.f7757287` | integer | no |  |
| `data.payer.ad_campaign` | object | no |  |
| `data.payer.ad_campaign.id` | integer | no |  |
| `data.payer.ad_campaign.name` | string | no |  |
| `data.status` | integer | no |  |
| `data.status_full` | object | no |  |
| `data.status_full.id` | integer | no |  |
| `data.status_full.name` | string | no |  |
| `data.status_full.color` | string | no |  |
| `data.status_full.group` | integer | no |  |
| `data.created_at` | integer | no |  |
| `data.issue_date` | integer | no |  |
| `data.due_date` | integer | no |  |
| `data.payment_type` | integer | no |  |
| `data.products` | array<object> | no |  |
| `data.products[].amount` | integer | no |  |
| `data.products[].id` | integer | no |  |
| `data.products[].order_id` | integer | no |  |
| `data.products[].price` | number | no |  |
| `data.products[].title` | string | no |  |
| `data.products[].uom_id` | integer | no |  |
| `data.products[].type` | integer | no |  |
| `data.products[].service` | boolean | no |  |
| `data.products[].warranty` | integer | no |  |
| `data.products[].warranty_period` | integer | no |  |
| `data.manager_id` | integer | no |  |
| `success` | boolean | no |  |

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-invoice-item-by-id

## Add Invoice Item

`POST /invoices/{invoice_id}/items`

Add a new item to the invoice.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `invoice_id` | path | number | yes | Invoice ID. Default: `"477110"`. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `entity_id` | number | yes | Product or Service ID. |
| `quantity` | number | yes | Quantity. |
| `price` | number | yes | Price per unit. |
| `discount` | object | no |  |
| `discount.type` | string | yes | Discount type. "percentage" — percent, "value" — absolute value. One of: `percentage`, `value`. Default: `"percentage"`. |
| `discount.percentage` | number | yes | Percentage value. |
| `discount.amount` | number | yes | Amount value. |
| `discount.sponsor` | string | yes | "staff" — Employee wages calculation is based on the amount after discount. This way the company discount decreases the piecework employee wages. "company" — Employee commissions will be calculated from amount before discount. This way the company discount won't affect the employee commissions. One of: `staff`, `company`. |
| `warranty` | object | no |  |
| `warranty.period` | number | yes | Warranty period. Default: `"0"`. |
| `warranty.unit` | string | yes | Warranty unit of measure. One of: `days`, `months`. Default: `"days"`. |
| `comment` | string | no | Comment text. |
| `comment_visibility` | string | no | Comment visibility. One of: `private`, `public`. |

### Example: Add Invoice Item with cURL

```bash
curl -X POST "https://api.roapp.io/v2/invoices/123/items" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "entity_id": 123,
  "quantity": 1,
  "price": 100,
  "discount": {
    "type": "percentage",
    "percentage": 123,
    "amount": 100,
    "sponsor": "staff"
  },
  "warranty": {
    "period": 123,
    "unit": "days"
  },
  "comment": "Comment text",
  "comment_visibility": "private"
}'
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/create-invoice-item

## Update Invoice Item

`PATCH /invoices/{invoice_id}/items/{item_id}`

Update an existing item in the invoice.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `invoice_id` | path | number | yes | Invoice ID. |
| `item_id` | path | number | yes | Invoice Item ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `quantity` | number | no | Quantity. |
| `price` | number | no | Price per unit. |
| `discount` | object | no | Discount object. |
| `discount.type` | string | yes | Discount type. "percentage" — percent, "value" — absolute value. One of: `percentage`, `value`. |
| `discount.percentage` | number | yes | Percentage value. |
| `discount.amount` | number | yes | Amount value. |
| `discount.sponsor` | string | yes | "staff" — Employee wages calculation is based on the amount after discount. This way the company discount decreases the piecework employee wages. "company" — Employee commissions will be calculated from amount before discount. This way the company discount won't affect the employee commissions. One of: `staff`, `company`. Default: `"company"`. |
| `warranty` | object | no | Warranty object. |
| `warranty.period` | number | yes | Warranty period. |
| `warranty.unit` | string | yes | Warranty unit of measure. One of: `days`, `months`. Default: `"days"`. |
| `tax_ids` | array<number> | no | List of tax IDs. |
| `comment` | string | no | Comment text. |
| `comment_visibility` | string | no | Comment visibility. One of: `private`, `public`. |

### Example: Update Invoice Item with cURL

```bash
curl -X PATCH "https://api.roapp.io/v2/invoices/123/items/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "quantity": 1,
  "price": 100,
  "discount": {
    "type": "percentage",
    "percentage": 123,
    "amount": 100,
    "sponsor": "staff"
  },
  "warranty": {
    "period": 123,
    "unit": "days"
  },
  "tax_ids": [
    123
  ],
  "comment": "Comment text",
  "comment_visibility": "private"
}'
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/update-invoice-item

## Delete Invoice Item

`DELETE /invoices/{invoice_id}/items/{item_id}`

Delete item from the invoice.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `invoice_id` | path | number | yes | Invoice ID. |
| `item_id` | path | number | yes | Invoice Item ID. |

### Example: Delete Invoice Item with cURL

```bash
curl -X DELETE "https://api.roapp.io/v2/invoices/123/items/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/delete-invoice-item

## Update Invoice Status

`POST /invoices/{invoice_id}/status`

Update the status of a specific invoice.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `invoice_id` | path | number | yes | Invoice ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `status_id` | number | yes | Status ID. |
| `comment` | string | no | Status comment. |

### Example: Update Invoice Status with cURL

```bash
curl -X POST "https://api.roapp.io/v2/invoices/123/status" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "status_id": 123,
  "comment": "Comment text"
}'
```

**Response codes:** `204`, `400`

Source: https://roapp.readme.io/reference/update-invoice-status

## Create Invoice Comment

`POST /invoices/{invoice_id}/comments`

Add a comment to a specific invoice.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `invoice_id` | path | number | yes | Invoice ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `comment` | string | yes | Comment text. |
| `is_private` | boolean | no | Is comment private? |

### Example: Create Invoice Comment with cURL

```bash
curl -X POST "https://api.roapp.io/v2/invoices/123/comments" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "comment": "Comment text",
  "is_private": false
}'
```

**Response codes:** `204`, `400`

Source: https://roapp.readme.io/reference/create-invoice-comment

## Get Invoice Statuses

`GET /invoices/statuses`

Retrieve a list of all possible statuses that can be assigned to an invoice.

### Example: Get Invoice Statuses with cURL

```bash
curl -X GET "https://api.roapp.io/v2/invoices/statuses" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

### Example response (200)

```json
{
  "data": [
    {
      "id": 3319495,
      "name": "Draft",
      "color": "#1E79C7",
      "group": 8
    }
  ],
  "count": 5,
  "success": true
}
```

### Response fields

| Field | Type | Required | Description |
|---|---|---|---|
| `data` | array<object> | no |  |
| `data[].id` | integer | no |  |
| `data[].name` | string | no |  |
| `data[].color` | string | no |  |
| `data[].group` | integer | no |  |
| `count` | integer | no |  |
| `success` | boolean | no |  |

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-invoice-statuses

# RO App API: Finance

Cash & bank accounts, account transactions and transfers, cashflow categories, exchange rates, refunds and finance tags.

Base URL: `https://api.roapp.io/v2`. Authenticate every request with `Authorization: Bearer <API_KEY>` (see [Getting Started](../getting-started.md)).

| Method | Path | Summary |
|---|---|---|
| `GET` | `/finance/cashflow-categories` | Get Cashflow Categories |
| `GET` | `/finance/cashflow-categories/{id}` | Get Cashflow Category by ID |
| `GET` | `/finance/accounts` | Get Finance Accounts |
| `GET` | `/finance/accounts/{account_id}` | Get Finance Account by ID |
| `GET` | `/finance/accounts/{id}/transactions` | Get Account Transactions |
| `GET` | `/finance/accounts/{account_id}/transactions/{transaction_id}` | Get Account Transaction by ID |
| `POST` | `/finance/accounts/{account_id}/transactions` | Create Transaction |
| `DELETE` | `/finance/accounts/{account_id}/transactions/{transaction_id}` | Delete Transaction |
| `POST` | `/finance/accounts:transfer` | Create Transfer |
| `GET` | `/finance/refunds` | Get Refunds |
| `GET` | `/finance/refunds/{refund_id}` | Get Refund by ID |
| `GET` | `/finance/refunds/{refund_id}/items` | Get Refund Items |
| `GET` | `/finance/tags` | Get Finance Transaction Tags |
| `GET` | `/finance/tags/{tag_id}` | Get Tag by ID |
| `POST` | `/finance/tags` | Create Tag |
| `PATCH` | `/finance/tags/{tag_id}` | Update Tag |
| `DELETE` | `/finance/tags/{tag_id}` | Delete Tag |
| `GET` | `/finance/exchange-rates` | Get Exchange Rates |
| `GET` | `/finance/exchange-rates/{code}` | Get Exchange Rate by ID |
| `GET` | `/finance/exchange-rates/{code}/history` | Get Exchange Rate History |
| `POST` | `/finance/exchange-rates` | Create Exchange Rate |
| `PATCH` | `/finance/exchange-rates/{code}` | Update Exchange Rate |
| `DELETE` | `/finance/exchange-rates/{code}` | Delete Exchange Rate |

## Get Cashflow Categories

`GET /finance/cashflow-categories`

Returns a list of cash flow categories.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `direction` | query | string | no | Type of financial transaction. One of: `income`, `expense`. |
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `id`, `-id`, `title`, `-title`. |

### Example: Get Cashflow Categories with cURL

```bash
curl -X GET "https://api.roapp.io/v2/finance/cashflow-categories?direction=income&sort=id" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-cashflow-categories

## Get Cashflow Category by ID

`GET /finance/cashflow-categories/{id}`

Retrieve detailed information about a specific cashflow category.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | number | yes | Cashflow Category ID. |

### Example: Get Cashflow Category by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/finance/cashflow-categories/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-cashflow-category-by-id

## Get Finance Accounts

`GET /finance/accounts`

Returns the list of company finance accounts.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `payment_method` | query | string | no | Account's payment method type. One of: `cash`, `cashless`, `credit_card`. |
| `branch_id` | query | number | no | Location ID. |
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `id`, `-id`, `title`, `-title`. |

### Example: Get Finance Accounts with cURL

```bash
curl -X GET "https://api.roapp.io/v2/finance/accounts?payment_method=cash&branch_id=123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-accounts

## Get Finance Account by ID

`GET /finance/accounts/{account_id}`

Get detailed information about a specific finance account.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `account_id` | path | number | yes | Finance Account ID. |

### Example: Get Finance Account by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/finance/accounts/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-account-by-id

## Get Account Transactions

`GET /finance/accounts/{id}/transactions`

Returns the list of finance account transactions.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | number | yes | Finance Account ID. |
| `page` | query | number | no | Page number. |
| `direction` | query | string | no | Transaction direction. One of: `income`, `expense`. |
| `category_id` | query | number | no | Cashflow Category ID. |
| `created_by_id` | query | number | no | Employee ID. |
| `created_at` | query | array<string (date-time)> | no | Filter by creation date. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `created_at`, `-created_at`. |

Paginated: up to 50 entries per page, `count` in the response is the total number of records.

### Example: Get Account Transactions with cURL

```bash
curl -X GET "https://api.roapp.io/v2/finance/accounts/123/transactions?page=1&direction=income" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-transactions

## Get Account Transaction by ID

`GET /finance/accounts/{account_id}/transactions/{transaction_id}`

Get detailed information about a specific finance account transaction.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `account_id` | path | number | yes | Finance Account ID. |
| `transaction_id` | path | number | yes | Transaction ID. |

### Example: Get Account Transaction by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/finance/accounts/123/transactions/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-transaction-by-id

## Create Transaction

`POST /finance/accounts/{account_id}/transactions`

Create finance account transaction.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `account_id` | path | number | yes | Finance Account ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | string | yes | Transaction amount. |
| `direction` | string | yes | Transaction direction. One of: `income`, `expense`. |
| `description` | string | no | Transaction description. |
| `category_id` | number | no | Cashflow Category ID. |
| `client_id` | number | no | People/Organization ID. |
| `tags` | array<string> | no | Array of tags. |
| `related_document` | object | no |  |
| `related_document.id` | number | yes | Object ID. |
| `related_document.type` | string | yes | Object type. One of: `order`, `sale`. |
| `custom_created_at` | string (date-time) | no | Transaction backdate (ISO 8601). |

### Example: Create Transaction with cURL

```bash
curl -X POST "https://api.roapp.io/v2/finance/accounts/123/transactions" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "amount": "100.00",
  "direction": "income",
  "description": "Description text",
  "category_id": 123,
  "client_id": 123,
  "tags": [
    "vip"
  ],
  "related_document": {
    "id": 123,
    "type": "order"
  },
  "custom_created_at": "2026-10-01T10:00:00Z"
}'
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/create-transaction

## Delete Transaction

`DELETE /finance/accounts/{account_id}/transactions/{transaction_id}`

Delete finance account transaction.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `account_id` | path | number | yes | Finance Account ID. |
| `transaction_id` | path | number | yes | Transaction ID. |

### Example: Delete Transaction with cURL

```bash
curl -X DELETE "https://api.roapp.io/v2/finance/accounts/123/transactions/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/delete-transaction

## Create Transfer

`POST /finance/accounts:transfer`

Transfer fund between two financial accounts.

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `from_account_id` | number | yes | Account ID from which the funds will be transferred. |
| `to_account_id` | number | yes | Account ID to which the funds will be transferred. |
| `amount` | string | yes | Transfer amount. |
| `description` | string | no | Transfer description. |
| `custom_created_at` | string (date-time) | no | Transaction backdate (ISO 8601). |

### Example: Create Transfer with cURL

```bash
curl -X POST "https://api.roapp.io/v2/finance/accounts:transfer" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "from_account_id": 123,
  "to_account_id": 123,
  "amount": "100.00",
  "description": "Description text",
  "custom_created_at": "2026-10-01T10:00:00Z"
}'
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/create-transfer-2

## Get Refunds

`GET /finance/refunds`

Retrieve a list of refunds.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | number | no | Page number. |
| `branch_ids` | query | array<number> | no | List of location IDs. |
| `client_ids` | query | array<number> | no | List of Client (Person / Organization) IDs. |
| `related_document_type` | query | string | no | Type of related document. One of: `order`, `sale`. |
| `created_at` | query | array<string (date-time)> | no | Filter by creation date. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `id`, `-id`. |

Paginated: up to 50 entries per page, `count` in the response is the total number of records.

### Example: Get Refunds with cURL

```bash
curl -X GET "https://api.roapp.io/v2/finance/refunds?page=1&branch_ids=123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-refunds

## Get Refund by ID

`GET /finance/refunds/{refund_id}`

Retrieve detailed information about a specific refund.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `refund_id` | path | number | yes | Refund ID. |

### Example: Get Refund by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/finance/refunds/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-refund-by-id

## Get Refund Items

`GET /finance/refunds/{refund_id}/items`

Retrieve all items (products or services) for a specific refund.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `refund_id` | path | number | yes | Refund ID. |

### Example: Get Refund Items with cURL

```bash
curl -X GET "https://api.roapp.io/v2/finance/refunds/123/items" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-refund-items

## Get Finance Transaction Tags

`GET /finance/tags`

Retrieve a list of finance transaction tags.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `id`, `-id`, `name`, `-name`. |

### Example: Get Finance Transaction Tags with cURL

```bash
curl -X GET "https://api.roapp.io/v2/finance/tags?sort=id" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-finance-transaction-tags

## Get Tag by ID

`GET /finance/tags/{tag_id}`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `tag_id` | path | number | yes | Finance Transaction Tag ID. |

### Example: Get Tag by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/finance/tags/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-tag-by-id-1

## Create Tag

`POST /finance/tags`

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | yes | Tag name. |
| `color_name` | string | no | Tag color name. One of: `red`, `green`, `blue`, `navy`, `pink`, `yellow`, `orange`, `grey`. |

### Example: Create Tag with cURL

```bash
curl -X POST "https://api.roapp.io/v2/finance/tags" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "Example",
  "color_name": "red"
}'
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/create-tag-1

## Update Tag

`PATCH /finance/tags/{tag_id}`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `tag_id` | path | number | yes | Tag ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | no | Tag name. |
| `color_name` | string | no | Tag color name. One of: `red`, `green`, `blue`, `navy`, `pink`, `yellow`, `orange`, `grey`. |

### Example: Update Tag with cURL

```bash
curl -X PATCH "https://api.roapp.io/v2/finance/tags/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "Example",
  "color_name": "red"
}'
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/update-tag-1

## Delete Tag

`DELETE /finance/tags/{tag_id}`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `tag_id` | path | number | yes | Tag ID. |

### Example: Delete Tag with cURL

```bash
curl -X DELETE "https://api.roapp.io/v2/finance/tags/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/delete-tag-1

## Get Exchange Rates

`GET /finance/exchange-rates`

Returns the list of company's currency exchange rates.

### Example: Get Exchange Rates with cURL

```bash
curl -X GET "https://api.roapp.io/v2/finance/exchange-rates" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-exchange-rates

## Get Exchange Rate by ID

`GET /finance/exchange-rates/{code}`

Get detailed information about a specific currency exchange rate.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `code` | path | string | yes | Currency ISO code. |

### Example: Get Exchange Rate by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/finance/exchange-rates/USD" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-exchange-rate-by-id

## Get Exchange Rate History

`GET /finance/exchange-rates/{code}/history`

Returns the exchange rate change history.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `code` | path | string | yes | Currency ISO code. |

### Example: Get Exchange Rate History with cURL

```bash
curl -X GET "https://api.roapp.io/v2/finance/exchange-rates/USD/history" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-exchange-rate-history

## Create Exchange Rate

`POST /finance/exchange-rates`

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `currency` | string | yes | Currency ISO code. |
| `rate` | string | no | Exchange rate relative to the company’s base currency. |

### Example: Create Exchange Rate with cURL

```bash
curl -X POST "https://api.roapp.io/v2/finance/exchange-rates" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "currency": "USD",
  "rate": "100.00"
}'
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/create-exchange-rate

## Update Exchange Rate

`PATCH /finance/exchange-rates/{code}`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `code` | path | string | yes | Currency ISO code. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `rate` | string | yes | Exchange rate relative to the company’s base currency. |

### Example: Update Exchange Rate with cURL

```bash
curl -X PATCH "https://api.roapp.io/v2/finance/exchange-rates/USD" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "rate": "100.00"
}'
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/update-exchange-rate

## Delete Exchange Rate

`DELETE /finance/exchange-rates/{code}`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `code` | path | string | yes | Currency ISO code. |

### Example: Delete Exchange Rate with cURL

```bash
curl -X DELETE "https://api.roapp.io/v2/finance/exchange-rates/USD" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/delete-exchange-rate

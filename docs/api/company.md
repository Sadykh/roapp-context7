# RO App API: Company

Company account, license, locations (branches) and their resources, employees, employee groups, legal entities, taxes and custom directories. Most IDs used elsewhere (`branch_id`, `manager_id`, `assignee_id`, `legal_entity_id`, `tax_id`) come from these endpoints.

Base URL: `https://api.roapp.io/v2`. Authenticate every request with `Authorization: Bearer <API_KEY>` (see [Getting Started](../getting-started.md)).

| Method | Path | Summary |
|---|---|---|
| `GET` | `/company` | Get Company Information |
| `GET` | `/company/license` | Get License |
| `GET` | `/company/locations` | Get Locations |
| `GET` | `/company/locations/{id}` | Get Location by ID |
| `GET` | `/company/locations/{id}/resources` | Get Location Resources |
| `GET` | `/company/employees` | Get Employees |
| `GET` | `/company/employees/{id}` | Get Employee by ID |
| `GET` | `/company/employees/groups` | Get Employee Groups |
| `GET` | `/company/legal-entities` | Get Legal Entities |
| `GET` | `/company/legal-entities/{id}` | Get Legal Entity by ID |
| `GET` | `/company/taxes` | Get Taxes |
| `GET` | `/company/directories` | Get Directories |
| `GET` | `/company/directories/{id}/items` | Get Directory Items |

## Get Company Information

`GET /company`

Retrieves basic information about the company account.

### Example: Get Company Information with cURL

```bash
curl -X GET "https://api.roapp.io/v2/company" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-company

## Get License

`GET /company/license`

Retrieves information about the company’s license.

### Example: Get License with cURL

```bash
curl -X GET "https://api.roapp.io/v2/company/license" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-company-license

## Get Locations

`GET /company/locations`

Retrieve list of company locations.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `is_archived` | query | boolean | no | Filters locations by archived status. |
| `legal_entity_id` | query | integer | no | Legal entity ID. |
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `id`, `-id`, `name`, `-name`. |

### Example: Get Locations with cURL

```bash
curl -X GET "https://api.roapp.io/v2/company/locations?is_archived=False&legal_entity_id=123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-company-locations

## Get Location by ID

`GET /company/locations/{id}`

Retrieve detailed information about a specific location.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | yes | Location ID. |

### Example: Get Location by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/company/locations/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-location-by-id

## Get Location Resources

`GET /company/locations/{id}/resources`

Retrieve list of location resources.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | yes | Location ID. |
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `id`, `-id`, `name`, `-name`. |

### Example: Get Location Resources with cURL

```bash
curl -X GET "https://api.roapp.io/v2/company/locations/123/resources?sort=id" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-resources

## Get Employees

`GET /company/employees`

Retrieve list of company employees.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `groups` | query | array<number> | no | List of Employee Group IDs. |
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `id`, `-id`, `name`, `-name`. |

### Example: Get Employees with cURL

```bash
curl -X GET "https://api.roapp.io/v2/company/employees?groups=123&sort=id" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-company-employees

## Get Employee by ID

`GET /company/employees/{id}`

Retrieve detailed information about a specific employee.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | yes | Employee ID. |

### Example: Get Employee by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/company/employees/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-employee-by-id

## Get Employee Groups

`GET /company/employees/groups`

Get list of employee groups.

### Example: Get Employee Groups with cURL

```bash
curl -X GET "https://api.roapp.io/v2/company/employees/groups" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-employee-groups

## Get Legal Entities

`GET /company/legal-entities`

Retrieve list of company legal entities.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `id`, `-id`, `name`, `-name`. |

### Example: Get Legal Entities with cURL

```bash
curl -X GET "https://api.roapp.io/v2/company/legal-entities?sort=id" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-legal-entities

## Get Legal Entity by ID

`GET /company/legal-entities/{id}`

Retrieve detailed information about a specific legal entity.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | yes | Legal entity ID. |

### Example: Get Legal Entity by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/company/legal-entities/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-legal-entity-by-id

## Get Taxes

`GET /company/taxes`

Retrieve list of company tax rates.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `id`, `-id`, `name`, `-name`. |

### Example: Get Taxes with cURL

```bash
curl -X GET "https://api.roapp.io/v2/company/taxes?sort=id" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-taxes

## Get Directories

`GET /company/directories`

Retrieve list of custom directories.

### Example: Get Directories with cURL

```bash
curl -X GET "https://api.roapp.io/v2/company/directories" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-custom-directories

## Get Directory Items

`GET /company/directories/{id}/items`

Retrieve list item for specific directory.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | integer | yes | Custom Directory ID. |
| `branch_id` | query | integer | no | Location ID. |

### Example: Get Directory Items with cURL

```bash
curl -X GET "https://api.roapp.io/v2/company/directories/123/items?branch_id=123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`, `400`

Source: https://roapp.readme.io/reference/get-custom-directory-items

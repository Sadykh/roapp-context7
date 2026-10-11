# RO App API: Work Schedule & Timesheets

Plan employee work schedules and record actual worked time (timesheets) per day and location.

Base URL: `https://api.roapp.io/v2`. Authenticate every request with `Authorization: Bearer <API_KEY>` (see [Getting Started](../getting-started.md)).

| Method | Path | Summary |
|---|---|---|
| `GET` | `/company/work-schedule/days` | Get Work Schedule for a Date Range |
| `GET` | `/company/work-schedule/days/{day}` | Get Work Schedule for the Day |
| `GET` | `/company/work-schedule/days/{day}/employees/{employee_id}` | Get Work Schedule for the Employee |
| `PUT` | `/company/work-schedule/days/{day}/employees/{employee_id}` | Set Work Schedule Day for the Employee |
| `DELETE` | `/company/work-schedule/days/{day}/employees/{employee_id}` | Delete Work Schedule Day for the Employee |
| `GET` | `/company/timesheets/days` | Get Timesheet for a Date Range |
| `GET` | `/company/timesheets/days/{day}` | Get Timesheet for the Day |
| `GET` | `/company/timesheets/days/{day}/employees/{employee_id}` | Get Timesheet for the Employee |
| `PUT` | `/company/timesheets/days/{day}/employees/{employee_id}` | Set Timesheet for the Employee |
| `DELETE` | `/company/timesheets/days/{day}/employees/{employee_id}` | Delete Timesheet for the Employee |

## Get Work Schedule for a Date Range

`GET /company/work-schedule/days`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | number | no | Page number. Default: `"1"`. |
| `date_from` | query | string | yes | Date From (in ISO 8601 format, for example "2026-10-01"). |
| `date_to` | query | string | yes | Date To (in ISO 8601 format, for example "2026-10-31"). |
| `employees` | query | array<number> | no | List of Employee IDs. |
| `branches` | query | array<number> | no | List of Location IDs. |
| `types` | query | string | no | Type of the day. One of: `working`, `non_working`. |

Paginated: up to 50 entries per page, `count` in the response is the total number of records.

### Example: Get Work Schedule for a Date Range with cURL

```bash
curl -X GET "https://api.roapp.io/v2/company/work-schedule/days?date_from=2026-10-01&date_to=2026-10-01" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-work-schedule-for-interval

## Get Work Schedule for the Day

`GET /company/work-schedule/days/{day}`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `day` | path | string | yes | Day (in ISO 8601 format, for example "2026-10-01"). |
| `page` | query | number | no | Page number. Default: `"1"`. |
| `employees` | query | array<number> | no | List of Employee IDs. |
| `branches` | query | array<number> | no | List of Location IDs. |
| `types` | query | string | no | Type of the day. One of: `working`, `non_working`. |

Paginated: up to 50 entries per page, `count` in the response is the total number of records.

### Example: Get Work Schedule for the Day with cURL

```bash
curl -X GET "https://api.roapp.io/v2/company/work-schedule/days/2026-10-01?page=1&employees=123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-work-schedule-for-the-day

## Get Work Schedule for the Employee

`GET /company/work-schedule/days/{day}/employees/{employee_id}`

Retrieve an employee’s work schedule for a specific day.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `day` | path | string | yes | Day (in ISO 8601 format, for example "2026-10-01"). |
| `employee_id` | path | number | yes | Employee ID. |

### Example: Get Work Schedule for the Employee with cURL

```bash
curl -X GET "https://api.roapp.io/v2/company/work-schedule/days/2026-10-01/employees/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-work-schedule-for-the-employee

## Set Work Schedule Day for the Employee

`PUT /company/work-schedule/days/{day}/employees/{employee_id}`

Set an employee’s work schedule for a specific day.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `day` | path | string | yes | Day (in ISO 8601 format, for example "2026-10-01"). |
| `employee_id` | path | number | yes | Employee ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | string | yes | One of: `working`, `non_working`. |
| `intervals` | array<object> | no | Declaration of working intervals. |
| `intervals[].branch_id` | number | yes | Location ID. |
| `intervals[].starts_at` | string | yes | Interval start (ISO 8601 datetime in UTC, for example: "2026-09-25T11:00:00Z". |
| `intervals[].ends_at` | string | yes | Interval end (ISO 8601 datetime in UTC, for example: "2026-09-25T17:00:00Z". |
| `non_working` | object | no | Declaration for non working day. |
| `non_working.type` | string | yes | One of: `sick_day`, `vacation`, `day_off`. |
| `non_working.is_unpaid` | boolean | yes | Default: `"false"`. |

### Example: Set Work Schedule Day for the Employee with cURL

```bash
curl -X PUT "https://api.roapp.io/v2/company/work-schedule/days/2026-10-01/employees/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "type": "working",
  "intervals": [
    {
      "branch_id": 123,
      "starts_at": "2026-10-01T10:00:00Z",
      "ends_at": "2026-10-01T10:00:00Z"
    }
  ],
  "non_working": {
    "type": "sick_day",
    "is_unpaid": false
  }
}'
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/set-work-schedule-day-for-the-employee

## Delete Work Schedule Day for the Employee

`DELETE /company/work-schedule/days/{day}/employees/{employee_id}`

Delete an employee’s work schedule for a specific day.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `day` | path | string | yes | Day (in ISO 8601 format, for example "2026-10-01"). |
| `employee_id` | path | number | yes | Employee ID. |

### Example: Delete Work Schedule Day for the Employee with cURL

```bash
curl -X DELETE "https://api.roapp.io/v2/company/work-schedule/days/2026-10-01/employees/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/delete-work-schedule-day-for-the-employee

## Get Timesheet for a Date Range

`GET /company/timesheets/days`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | number | no | Page number. Default: `"1"`. |
| `date_from` | query | string | yes | Date From (in ISO 8601 format, for example "2026-10-01"). |
| `date_to` | query | string | yes | Date To (in ISO 8601 format, for example "2026-10-31"). |
| `employees` | query | array<number> | no | List of Employee IDs. |
| `branches` | query | array<number> | no | List of Location IDs. |
| `types` | query | string | no | Type of the day. One of: `working`, `non_working`. |

Paginated: up to 50 entries per page, `count` in the response is the total number of records.

### Example: Get Timesheet for a Date Range with cURL

```bash
curl -X GET "https://api.roapp.io/v2/company/timesheets/days?date_from=2026-10-01&date_to=2026-10-01" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-timesheet-for-a-date-range

## Get Timesheet for the Day

`GET /company/timesheets/days/{day}`

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `day` | path | string | yes | Day (in ISO 8601 format, for example "2026-10-01"). |
| `page` | query | number | no | Page number. Default: `"1"`. |
| `employees` | query | array<number> | no | List of Employee IDs. |
| `branches` | query | array<number> | no | List of Location IDs. |
| `types` | query | string | no | Type of the day. One of: `working`, `non_working`. |

Paginated: up to 50 entries per page, `count` in the response is the total number of records.

### Example: Get Timesheet for the Day with cURL

```bash
curl -X GET "https://api.roapp.io/v2/company/timesheets/days/2026-10-01?page=1&employees=123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-timesheet-for-the-day

## Get Timesheet for the Employee

`GET /company/timesheets/days/{day}/employees/{employee_id}`

Retrieve an employee’s timesheet for a specific day.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `day` | path | string | yes | Day (in ISO 8601 format, for example "2026-10-01"). |
| `employee_id` | path | number | yes | Employee ID. |

### Example: Get Timesheet for the Employee with cURL

```bash
curl -X GET "https://api.roapp.io/v2/company/timesheets/days/2026-10-01/employees/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-timesheet-for-the-employee

## Set Timesheet for the Employee

`PUT /company/timesheets/days/{day}/employees/{employee_id}`

Set an employee’s timesheet for a specific day.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `day` | path | string | yes | Day (in ISO 8601 format, for example "2026-10-01"). |
| `employee_id` | path | number | yes | Employee ID. |

### Request body (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | string | yes | One of: `working`, `non_working`. |
| `intervals` | array<object> | no | Declaration of working intervals. |
| `intervals[].branch_id` | number | yes | Location ID. |
| `intervals[].starts_at` | string | yes | Interval start (ISO 8601 datetime in UTC, for example: "2026-09-25T11:00:00Z". |
| `intervals[].ends_at` | string | yes | Interval end (ISO 8601 datetime in UTC, for example: "2026-09-25T17:00:00Z". |
| `non_working` | object | no | Declaration for non working day. |
| `non_working.type` | string | yes | One of: `sick_day`, `vacation`, `day_off`. |
| `non_working.is_unpaid` | boolean | yes | Default: `"false"`. |

### Example: Set Timesheet for the Employee with cURL

```bash
curl -X PUT "https://api.roapp.io/v2/company/timesheets/days/2026-10-01/employees/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "type": "working",
  "intervals": [
    {
      "branch_id": 123,
      "starts_at": "2026-10-01T10:00:00Z",
      "ends_at": "2026-10-01T10:00:00Z"
    }
  ],
  "non_working": {
    "type": "sick_day",
    "is_unpaid": false
  }
}'
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/set-timesheet-day-for-the-employee

## Delete Timesheet for the Employee

`DELETE /company/timesheets/days/{day}/employees/{employee_id}`

Delete an employee’s timesheet for a specific day.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `day` | path | string | yes | Day (in ISO 8601 format, for example "2026-10-01"). |
| `employee_id` | path | number | yes | Employee ID. |

### Example: Delete Timesheet for the Employee with cURL

```bash
curl -X DELETE "https://api.roapp.io/v2/company/timesheets/days/2026-10-01/employees/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/delete-timesheet-for-the-employee

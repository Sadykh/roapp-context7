# RO App API: Telephony

Telephony integrations: providers, extensions, call log, call recordings and AI transcripts.

Base URL: `https://api.roapp.io/v2`. Authenticate every request with `Authorization: Bearer <API_KEY>` (see [Getting Started](../getting-started.md)).

| Method | Path | Summary |
|---|---|---|
| `GET` | `/telephony/providers` | Get Telephony Providers |
| `GET` | `/telephony/providers/{provider_id}/extensions` | Get Provider Extensions |
| `GET` | `/telephony/providers/{provider_id}/extensions/{ext_id}` | Get Extension by ID |
| `GET` | `/telephony/calls` | Get Calls |
| `GET` | `/telephony/calls/{call_id}` | Get Call by ID |
| `GET` | `/telephony/calls/{call_id}/recording-url` | Get Call Recording Url |
| `GET` | `/telephony/calls/{call_id}/transcript` | Get Call Transcript |

## Get Telephony Providers

`GET /telephony/providers`

Returns a list of active telephony integrations connected to the company.

### Example: Get Telephony Providers with cURL

```bash
curl -X GET "https://api.roapp.io/v2/telephony/providers" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-telephony-providers

## Get Provider Extensions

`GET /telephony/providers/{provider_id}/extensions`

Returns a list of extension numbers configured for the provider.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `provider_id` | path | number | yes | Telephony Provider ID. |

### Example: Get Provider Extensions with cURL

```bash
curl -X GET "https://api.roapp.io/v2/telephony/providers/123/extensions" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-provider-extensions

## Get Extension by ID

`GET /telephony/providers/{provider_id}/extensions/{ext_id}`

Returns a single extension object.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `provider_id` | path | number | yes | Telephony Provider ID. |
| `ext_id` | path | number | yes | Extension ID. |

### Example: Get Extension by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/telephony/providers/123/extensions/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-extension-by-id

## Get Calls

`GET /telephony/calls`

Get a list of calls.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `page` | query | number | no | Page number. |
| `direction` | query | string | no | Filter by call direction. One of: `incoming`, `outgoing`. |
| `extension_ids` | query | array<number> | no | Filter by extension IDs. |
| `status` | query | string | no | Filter by call status. One of: `completed`, `noanswer`, `missed`. |
| `sentiment` | query | string | no | Filter by call sentiment. One of: `positive`, `neutral`, `negative`. |
| `insight` | query | string | no | Filter by call insights. One of: `booking_not_confirmed`, `follow_up_required`, `friendly_service`, `good_value`, `information_only`, `long_wait_time`, `loyalty_acknowledged`, `miscommunication`, `needs_quote_or_estimate`, `not_in_stock`, `policy_disagreement`, `poor_service`, `potential_sale`, `pricing_disagreement`, `quality_issue`, `quality_satisfaction`, `quick_resolution`, `repeat_problem`, `unresolved_issue`, `went_above_and_beyond`. |
| `contact_id` | query | number | no | Filter by contact ID. |
| `phone_number` | query | number | no | Filter by contact phone number. |
| `created_at` | query | array<string (date-time)> | no | Filter by creation date. Date-time range: `[from]` or `[from, to]` (ISO 8601), see Getting Started. |
| `sort` | query | string | no | Defines the sorting order of returned results. Use a field name to sort ascending or prefix it with a minus sign (-) to sort descending. One of: `id`, `-id`. |

Paginated: up to 50 entries per page, `count` in the response is the total number of records.

### Example: Get Calls with cURL

```bash
curl -X GET "https://api.roapp.io/v2/telephony/calls?page=1&direction=incoming" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-calls-list

## Get Call by ID

`GET /telephony/calls/{call_id}`

Returns detailed information about a single call.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `call_id` | path | number | yes | Call ID. |

### Example: Get Call by ID with cURL

```bash
curl -X GET "https://api.roapp.io/v2/telephony/calls/123" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-call-by-id

## Get Call Recording Url

`GET /telephony/calls/{call_id}/recording-url`

Get a call recording URL.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `call_id` | path | number | yes | Call ID. |

### Example: Get Call Recording Url with cURL

```bash
curl -X GET "https://api.roapp.io/v2/telephony/calls/123/recording-url" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-call-recording-url

## Get Call Transcript

`GET /telephony/calls/{call_id}/transcript`

Get a call transcript.

### Parameters

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `call_id` | path | number | yes | Call ID. |

### Example: Get Call Transcript with cURL

```bash
curl -X GET "https://api.roapp.io/v2/telephony/calls/123/transcript" \
  -H "Authorization: Bearer $ROAPP_API_KEY"
```

**Response codes:** `200`

Source: https://roapp.readme.io/reference/get-call-transcript

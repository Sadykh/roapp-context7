# RO App API v2 — Endpoint Index

Base URL: `https://api.roapp.io/v2`. All endpoints require `Authorization: Bearer <API_KEY>`.

## [Work Schedule & Timesheets](api/work-schedule-and-timesheets.md)

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

## [Company](api/company.md)

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

## [Catalog: Services](api/catalog-services.md)

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

## [Catalog: Products](api/catalog-products.md)

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

## [Catalog: Bundles](api/catalog-bundles.md)

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

## [Bookings](api/bookings.md)

| Method | Path | Summary |
|---|---|---|
| `GET` | `/bookings` | Get Bookings |
| `GET` | `/bookings/{booking_id}` | Get Booking by ID |
| `POST` | `/bookings` | Create Booking |
| `PATCH` | `/bookings/{booking_id}` | Update Booking |
| `DELETE` | `/bookings/{booking_id}` | Delete Booking |
| `GET` | `/bookings/{booking_id}/items` | Get Bookings Items |
| `POST` | `/bookings/{booking_id}/items` | Add Booking Item |
| `PATCH` | `/bookings/{booking_id}/items/{item_id}` | Update Booking Item |
| `DELETE` | `/bookings/{booking_id}/items/{item_id}` | Delete Booking Item |

## [Inquiries (Leads)](api/inquiries.md)

| Method | Path | Summary |
|---|---|---|
| `GET` | `/inquiries` | Get Inquiries |
| `GET` | `/inquiries/{inquiry_id}` | Get Inquiry by ID |
| `POST` | `/inquiries` | Create Inquiry |
| `PATCH` | `/inquiries/{inquiry_id}` | Update Inquiry |
| `POST` | `/inquiries/{inquiry_id}/status` | Update Inquiry Status |
| `POST` | `/inquiries/{inquiry_id}/comments` | Create Inquiry Comment |
| `DELETE` | `/inquiries/{inquiry_id}` | Delete Inquiry |
| `GET` | `/inquiries/statuses` | Get Inquiry Statuses |
| `GET` | `/inquiries/types` | Get Inquiry Types |
| `GET` | `/inquiries/custom-fields` | Get Inquiry Custom Fields |

## [Estimates](api/estimates.md)

| Method | Path | Summary |
|---|---|---|
| `GET` | `/estimates` | Get Estimates |
| `GET` | `/estimates/{estimate_id}` | Get Estimate by ID |
| `POST` | `/estimates` | Create Estimate |
| `PATCH` | `/estimates/{estimate_id}` | Update Estimate |
| `GET` | `/estimates/{estimate_id}/items` | Get Estimate Items |
| `POST` | `/estimates/{estimate_id}/items` | Add Estimate Item |
| `PATCH` | `/estimates/{estimate_id}/items/{item_id}` | Update Estimate Item |
| `POST` | `/estimates/{estimate_id}/status` | Change Estimate Status |
| `POST` | `/estimates/{estimate_id}/comments` | Create Estimate Comment |
| `GET` | `/estimates/{estimate_id}/public-url` | Get Estimate Public Page Url |
| `GET` | `/estimates/statuses` | Get Estimate Statuses |
| `GET` | `/estimates/types` | Get Estimate Types |
| `GET` | `/estimates/custom-fields` | Get Estimate Custom Fields |

## [Orders](api/orders.md)

| Method | Path | Summary |
|---|---|---|
| `GET` | `/orders` | Get Orders |
| `GET` | `/orders/{order_id}` | Get Order by ID |
| `POST` | `/orders` | Create Order |
| `PATCH` | `/orders/{order_id}` | Update Order |
| `GET` | `/orders/{order_id}/items` | Get Order Items |
| `POST` | `/orders/{order_id}/items` | Add Order Item |
| `PATCH` | `/orders/{order_id}/items/{item_id}` | Update Order Item |
| `POST` | `/orders/{order_id}/status` | Update Order Status |
| `POST` | `/orders/{order_id}/comments` | Create Order Comment |
| `GET` | `/orders/{order_id}/public-url` | Get Order Public Page Url |
| `GET` | `/orders/statuses` | Get Order Statuses |
| `GET` | `/orders/types` | Get Order Types |
| `GET` | `/orders/custom-fields` | Get Order Custom Fields |

## [Sales](api/sales.md)

| Method | Path | Summary |
|---|---|---|
| `GET` | `/sales` | Get Sales |
| `GET` | `/sales/{id}` | Get Sale by ID |

## [Invoices](api/invoices.md)

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

## [Finance](api/finance.md)

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

## [Contacts: People](api/contacts-people.md)

| Method | Path | Summary |
|---|---|---|
| `GET` | `/contacts/people` | Get People |
| `GET` | `/contacts/people/{person_id}` | Get Person by ID |
| `GET` | `/contacts/people/{person_id}/organizations` | Get Person's Organization |
| `POST` | `/contacts/people` | Create Person |
| `PATCH` | `/contacts/people/{person_id}` | Update Person |
| `DELETE` | `/contacts/people/{person_id}` | Delete Person |
| `POST` | `/contacts/people/{person_id}/comments` | Create Person Comment |
| `POST` | `/contacts/people/{person_id}/merge` | Merge People |
| `GET` | `/contacts/people/custom-fields` | Get People Custom Fields |

## [Contacts: Organizations](api/contacts-organizations.md)

| Method | Path | Summary |
|---|---|---|
| `GET` | `/contacts/organizations` | Get Organizations |
| `GET` | `/contacts/organizations/{organization_id}` | Get Organization by ID |
| `GET` | `/contacts/organizations/{organization_id}/people` | Get Organization People |
| `POST` | `/contacts/organizations/{organization_id}/people` | Add People to Organization |
| `DELETE` | `/contacts/organizations/{organization_id}/people/{person_id}` | Delete People from Organization |
| `POST` | `/contacts/organizations` | Create Organization |
| `PATCH` | `/contacts/organizations/{organization_id}` | Update Organization |
| `DELETE` | `/contacts/organizations/{organization_id}` | Delete Organization |
| `POST` | `/contacts/organizations/{organization_id}/comments` | Create Organization Comment |
| `POST` | `/contacts/organizations/{organization_id}/merge` | Merge Organizations |
| `GET` | `/contacts/organizations/custom-fields` | Get Organizations Custom Fields |

## [Contacts: Tags](api/contacts-tags.md)

| Method | Path | Summary |
|---|---|---|
| `GET` | `/contacts/tags` | Get Contact Tags |
| `GET` | `/contacts/tags/{tag_id}` | Get Tag by Id |
| `POST` | `/contacts/tags` | Create Tag |
| `PATCH` | `/contacts/tags/{tag_id}` | Update Tag |
| `DELETE` | `/contacts/tags/{tag_id}` | Delete Tag |

## [Telephony](api/telephony.md)

| Method | Path | Summary |
|---|---|---|
| `GET` | `/telephony/providers` | Get Telephony Providers |
| `GET` | `/telephony/providers/{provider_id}/extensions` | Get Provider Extensions |
| `GET` | `/telephony/providers/{provider_id}/extensions/{ext_id}` | Get Extension by ID |
| `GET` | `/telephony/calls` | Get Calls |
| `GET` | `/telephony/calls/{call_id}` | Get Call by ID |
| `GET` | `/telephony/calls/{call_id}/recording-url` | Get Call Recording Url |
| `GET` | `/telephony/calls/{call_id}/transcript` | Get Call Transcript |

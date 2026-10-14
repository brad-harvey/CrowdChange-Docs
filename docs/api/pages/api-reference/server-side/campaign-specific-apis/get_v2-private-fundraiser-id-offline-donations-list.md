---
title: Get offline transactions
slug: api-reference/server-side/campaign-specific-apis/get_v2-private-fundraiser-id-offline-donations-list
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/campaign-specific-apis/get_v2-private-fundraiser-id-offline-donations-list
nav_path:
- API Reference
- Server Side APIs
- Campaign-Specific APIs
- Get offline transactions
nav_order: 19
page_type: endpoint
endpoint: GET /v2/private/fundraiser/{id}/offline-donations/list
http_method: GET
endpoint_path: /v2/private/fundraiser/{id}/offline-donations/list
api_surface: server-side
auth: API key
tags:
- donations
- offline-donations
- reporting-and-data
- transactions
crm_relevant: true
description: Retrieve a paginated list of offline donation transactions recorded against a CrowdChange campaign, including amount, donor, and entry metadata.
retrieved: '2026-10-14'
word_count: 531
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/campaign-specific-apis/get_v2-private-fundraiser-id-offline-donations-list | Nav: API Reference > Server Side APIs > Campaign-Specific APIs > Get offline transactions | Mirrored 2026-10-14 -->

# Get offline transactions

> Retrieve a paginated list of offline donation transactions recorded against a CrowdChange campaign, including amount, donor, and entry metadata.

**Endpoint:** `GET /v2/private/fundraiser/{id}/offline-donations/list`  
**Surface:** Server Side API (server-to-server only; never call from a browser) · **Auth:** API key — `Authorization: Bearer {api-key}` header  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Path parameters

- `id` (integer, path, **required**) — Campaign ID.

## Query parameters

- `status` (string, query) — Transaction status. Allowed values: `received`, `pending`
- `fundraiser_team_id` (integer, query) — Campaign's Team.
- `fundraiser_page_id` (integer, query) — Campaign's Personal Page.
- `page` (integer, query) — Page number. Default: `1`
- `limit` (integer, query) — Number of results to return. Default: `10`
- `text` (string, query) — Search term.

## Response

Returns an array of objects with the following fields.

- `id` (integer) — Transaction ID.
- `amount` (number) — Amount.
- `amount_total` (number) — Amount Total.
- `currency` (string) — Currency code. Allowed values: `CAD`, `USD`, `AUD`, `EUR`
- `is_pending` (boolean) — True if transaction is pending.
- `pledge_code` (string) — Pledge code.
- `tax_eligible_amount` (number) — Tax Eligible Amount.
- `has_tax_receipt` (boolean) — True if transaction has tax receipt.
- `created_at` (string) — Transaction creation date.
- `billing` (object) — User's billing information.
  - `business_name` (string) — Business name.
  - `is_foundation` (boolean) — Is this transaction made by foundation?
  - `title` (string) — Honorific (i.e. Mr / Miss / etc).
  - `name` (string) — Full user name including honorific.
  - `first_name` (string) — User's first name.
  - `last_name` (string) — User's last name.
  - `street_address` (string) — Street name and number.
  - `city` (string) — City name.
  - `country` (string) — Country code.
  - `state` (string) — State or province..
  - `postal` (string) — ZIP or Postal Code.
  - `email` (string) — User's email address.
- `fundraiser_page` (object) — Personal Page.
  - `id` (integer) — Personal Page ID.
  - `name` (string) — Personal Page name.
- `fundraiser_team` (object) — Team.
  - `id` (integer) — Team ID.
  - `name` (string) — Team name.
- `tax_receipt` (object) — Tax receipt information.
  - `id` (integer) — Unique id.
  - `amount_donation` (number) — Total donation amount.
  - `amount_benefit` (number) — Benefit amount.
  - `amount_eligible` (number) — Eligible amount.
  - `name_on_receipt` (string) — Name on receipt.
  - `issued_on` (string) — Date when the tax receipt was issued.
  - `receipt_number` (string) — Tax receipt number
  - `title` (string) — Honorific (i.e. Mr / Miss / etc).
  - `first_name` (string) — First name.
  - `last_name` (string) — Last name.
  - `street_address` (string) — Street name and number.
  - `city` (string) — City name.
  - `country` (string) — Country code.
  - `state` (string) — State or province..
  - `postal` (string) — ZIP or Postal Code.
  - `email` (string) — Email address.
- `transaction_meta` (object) — Meta information.
  - `is_lump_sum` (boolean) — True if it is a lump sum.
  - `is_foundation` (boolean) — Is this transaction made by foundation?

**Other responses**

| Status | Description |
| - | - |
| `400` | Bad Request |
| `403` | Forbidden |

**Response example:**

```json
[
  {
    "id": 1,
    "amount": 100,
    "amount_total": 100,
    "currency": "USD",
    "is_pending": false,
    "pledge_code": "PLEDGE_CODE",
    "tax_eligible_amount": 100,
    "has_tax_receipt": false,
    "created_at": "2024-01-01 16:00:03",
    "billing": {
      "business_name": "Company Inc",
      "is_foundation": false,
      "title": "Mr.",
      "name": "Mr. John Snow",
      "first_name": "John",
      "last_name": "Snow",
      "street_address": "100 Main Street",
      "city": "Toronto",
      "country": "CA",
      "state": "ON",
      "postal": "A1A 1A1",
      "email": "john@example.com"
    },
    "fundraiser_page": {
      "id": 1001,
      "name": "Personal Page name"
    },
    "fundraiser_team": {
      "id": 1001,
      "name": "Team name"
    },
    "tax_receipt": {
      "id": 1001,
      "amount_donation": 100.99,
      "amount_benefit": 10.49,
      "amount_eligible": 90.5,
      "name_on_receipt": "John Smith",
      "issued_on": "2021-01-01 19:00:00",
      "receipt_number": "TAX-0012345",
      "title": "Mr.",
      "first_name": "John",
      "last_name": "Snow",
      "street_address": "100 Main Street",
      "city": "Toronto",
      "country": "CA",
      "state": "ON",
      "postal": "A1A 1A1",
      "email": "john@example.com"
    },
    "transaction_meta": {
      "is_lump_sum": false,
      "is_foundation": false
    }
  }
]
```

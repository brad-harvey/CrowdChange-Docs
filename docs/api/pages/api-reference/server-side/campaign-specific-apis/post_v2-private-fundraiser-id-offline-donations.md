---
title: Create Offline Transaction
slug: api-reference/server-side/campaign-specific-apis/post_v2-private-fundraiser-id-offline-donations
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/campaign-specific-apis/post_v2-private-fundraiser-id-offline-donations
nav_path:
- API Reference
- Server Side APIs
- Campaign-Specific APIs
- Create Offline Transaction
nav_order: 18
page_type: endpoint
endpoint: POST /v2/private/fundraiser/{id}/offline-donations
http_method: POST
endpoint_path: /v2/private/fundraiser/{id}/offline-donations
api_surface: server-side
auth: API key
tags:
- donations
- offline-donations
- payments-and-receipts
- transactions
crm_relevant: true
description: Record an offline donation transaction against a CrowdChange campaign on behalf of a donor, including amount, payment method, and donor details.
retrieved: '2026-10-14'
word_count: 302
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/campaign-specific-apis/post_v2-private-fundraiser-id-offline-donations | Nav: API Reference > Server Side APIs > Campaign-Specific APIs > Create Offline Transaction | Mirrored 2026-10-14 -->

# Create Offline Transaction

> Record an offline donation transaction against a CrowdChange campaign on behalf of a donor, including amount, payment method, and donor details.

**Endpoint:** `POST /v2/private/fundraiser/{id}/offline-donations`  
**Surface:** Server Side API (server-to-server only; never call from a browser) · **Auth:** API key — `Authorization: Bearer {api-key}` header  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Path parameters

- `id` (integer, path, **required**) — Campaign ID.

## Body

- `amount` (number, body) — Full amount of offline transaction in xxx.xx format.
- `name` (string, body) — Donor's full name.
- `fundraiser_team_id` (integer, body) — Team ID.
- `fundraiser_page_id` (integer, body) — Page ID.
- `email` (string, body) — Donor's email.
- `is_lump_sum` (boolean, body) — Whether the transaction is recorded as a lump sum.
- `is_pending` (boolean, body) — Whether the transaction is pending.
- `pay_method` (string, body) — Payment method used for the offline transaction.
- `comment` (string, body) — Comment associated with the transaction.
- `billing` (object, body) — Billing information.
  - `first_name` (string, body) — Donor's First Name.
  - `last_name` (string, body) — Donor's Last Name.
  - `business_name` (string, body) — Business Name
  - `is_foundation` (boolean, body) — Whether the donation is made by a foundation.
  - `address` (string, body) — Street Address.
  - `city` (string, body) — City.
  - `state` (string, body) — State or province.
  - `zip` (string, body) — Zip or Postal code.
  - `country` (string, body) — ISO 3166-1 alpha-2 country code.
  - `phone` (string, body) — Donor's phone number.

## Response

- `id` (integer) — Transaction ID.
- `user_id` (integer) — Donor ID.
- `email` (string) — Donor email.
- `amount` (number) — Full amount.
- `currency` (string) — Currency code. Allowed values: `CAD`, `USD`, `AUD`, `EUR`
- `fundraiser_id` (integer) — Campaign ID.
- `fundraiser_team_id` (integer) — Team ID.
- `fundraiser_page_id` (integer) — Page ID.

**Other responses**

| Status | Description |
| - | - |
| `400` | Bad Request |
| `403` | Forbidden |

**Response example:**

```json
{
  "id": 123123,
  "user_id": 120120,
  "email": "john@example.com",
  "amount": 49.95,
  "currency": "USD",
  "fundraiser_id": 1,
  "fundraiser_team_id": 1,
  "fundraiser_page_id": 1
}
```

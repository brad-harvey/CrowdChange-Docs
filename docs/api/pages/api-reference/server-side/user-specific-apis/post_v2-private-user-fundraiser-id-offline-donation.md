---
title: Create Offline Transaction
slug: api-reference/server-side/user-specific-apis/post_v2-private-user-fundraiser-id-offline-donation
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/user-specific-apis/post_v2-private-user-fundraiser-id-offline-donation
nav_path:
- API Reference
- Server Side APIs
- User-Specific APIs
- Create Offline Transaction
nav_order: 31
page_type: endpoint
endpoint: POST /v2/private/user/fundraiser/{id}/offline-donation
http_method: POST
endpoint_path: /v2/private/user/fundraiser/{id}/offline-donation
api_surface: server-side
auth: API key + user token
tags:
- donations
- offline-donations
- transactions
crm_relevant: true
description: Record an offline donation transaction on behalf of the authenticated user against a CrowdChange campaign, with amount and donor details.
retrieved: '2026-10-14'
word_count: 273
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/user-specific-apis/post_v2-private-user-fundraiser-id-offline-donation | Nav: API Reference > Server Side APIs > User-Specific APIs > Create Offline Transaction | Mirrored 2026-10-14 -->

# Create Offline Transaction

> Record an offline donation transaction on behalf of the authenticated user against a CrowdChange campaign, with amount and donor details.

**Endpoint:** `POST /v2/private/user/fundraiser/{id}/offline-donation`  
**Surface:** Server Side API (server-to-server only; never call from a browser) · **Auth:** API key + user token — `Authorization: Bearer {api-key}` header, plus the user token in the `auth-token` header or `token` param  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Path parameters

- `id` (integer, path, **required**) — Campaign ID.

## Body

- `token` (string, body, **required**) — User's access token.
- `amount` (number, body, **required**) — Full amount of offline transaction in xxx.xx format.
- `fundraiser_id` (integer, body, **required**) — Campaign ID.
- `fundraiser_team_id` (integer, body) — Team ID.
- `fundraiser_page_id` (integer, body) — Page ID.
- `email` (string, body) — Donor's email.
- `business_name` (string, body) — Business Name
- `billing` (object, body) — Billing information.
  - `first_name` (string, body) — Donor's First Name.
  - `last_name` (string, body) — Donor's Last Name.
  - `address` (string, body, **required**) — Street Address.
  - `city` (string, body, **required**) — City.
  - `state` (string, body, **required**) — State or province.
  - `zip` (string, body, **required**) — Zip or Postal code.
  - `country` (string, body, **required**) — ISO 3166-1 alpha-2 country code.

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

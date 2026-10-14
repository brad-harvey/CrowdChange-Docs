---
title: Page Donors List
slug: api-reference/client-side/campaign-specific-apis/get_v2-client-fundraiser-id-personal-page-pageid-donors
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/client-side/campaign-specific-apis/get_v2-client-fundraiser-id-personal-page-pageid-donors
nav_path:
- API Reference
- Client Side APIs
- Campaign-Specific APIs
- Page Donors List
nav_order: 47
page_type: endpoint
endpoint: GET /v2/client/fundraiser/{id}/personal-page/{pageId}/donors
http_method: GET
endpoint_path: /v2/client/fundraiser/{id}/personal-page/{pageId}/donors
api_surface: client-side
auth: API key
tags:
- donations
- peer-to-peer
crm_relevant: false
description: Retrieve a paginated list of donors for a personal fundraising page within a CrowdChange campaign, returning 10 donors per page with amount details.
retrieved: '2026-10-14'
word_count: 263
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/client-side/campaign-specific-apis/get_v2-client-fundraiser-id-personal-page-pageid-donors | Nav: API Reference > Client Side APIs > Campaign-Specific APIs > Page Donors List | Mirrored 2026-10-14 -->

# Page Donors List

> Retrieve a paginated list of donors for a personal fundraising page within a CrowdChange campaign, returning 10 donors per page with amount details.

**Endpoint:** `GET /v2/client/fundraiser/{id}/personal-page/{pageId}/donors`  
**Surface:** Client Side API · **Auth:** API key — `Authorization: Bearer {api-key}` header  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Path parameters

- `id` (integer, path, **required**) — Campaign ID.
- `pageId` (integer, path, **required**) — Personal Page ID.

## Query parameters

- `page` (integer, query) — Page number. Default: `1`
- `limit` (integer, query) — Number of results to return. Default: `10`
- `sort` (string, query) — Key to sort by. Allowed values: `id`, `amount` Default: `id`
- `direction` (string, query) — Direction of sorting. Allowed values: `asc`, `desc` Default: `desc`
- `min_total` (integer, query) — Minimum total donation amount to include. Default: `0`
- `only_received` (boolean, query) — Include only received transactions. Default: `false`

## Response

Returns an array of objects with the following fields.

- `total` (number) — Donation total.
- `total_formatted` (string) — Formatted donation total, includes currency symbol.
- `amount_match` (number) — Matched amount for campaigns with donation matching enabled.
- `total_with_match` (number) — Donation total including the matched amount.
- `name` (string) — Donor's name or alias.
- `comment` (string) — Donor's comment.
- `is_amount_hidden` (boolean) — True if the donor chose to hide their donation amount.
- `currency` (string) — Currency code.
- `created_at` (string) — Date and time of the donation.

**Other responses**

| Status | Description |
| - | - |
| `400` | Bad Request |
| `403` | Forbidden |

**Response example:**

```json
[
  {
    "total": 100,
    "total_formatted": "$100",
    "amount_match": 100,
    "total_with_match": 200,
    "name": "John Snow",
    "comment": "Happy to support!",
    "is_amount_hidden": false,
    "currency": "USD",
    "created_at": "2021-01-01T00:00:00Z"
  }
]
```

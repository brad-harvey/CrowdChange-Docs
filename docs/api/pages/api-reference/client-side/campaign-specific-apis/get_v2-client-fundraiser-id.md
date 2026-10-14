---
title: Goal / Raised Amounts
slug: api-reference/client-side/campaign-specific-apis/get_v2-client-fundraiser-id
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/client-side/campaign-specific-apis/get_v2-client-fundraiser-id
nav_path:
- API Reference
- Client Side APIs
- Campaign-Specific APIs
- Goal / Raised Amounts
nav_order: 43
page_type: endpoint
endpoint: GET /v2/client/fundraiser/{id}
http_method: GET
endpoint_path: /v2/client/fundraiser/{id}
api_surface: client-side
auth: API key
tags:
- donations
crm_relevant: false
description: Retrieve the goal amount, raised amount, donor count, and core campaign metadata for a specific CrowdChange campaign by its fundraiser ID.
retrieved: '2026-10-14'
word_count: 285
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/client-side/campaign-specific-apis/get_v2-client-fundraiser-id | Nav: API Reference > Client Side APIs > Campaign-Specific APIs > Goal / Raised Amounts | Mirrored 2026-10-14 -->

# Goal / Raised Amounts

> Retrieve the goal amount, raised amount, donor count, and core campaign metadata for a specific CrowdChange campaign by its fundraiser ID.

**Endpoint:** `GET /v2/client/fundraiser/{id}`  
**Surface:** Client Side API · **Auth:** API key — `Authorization: Bearer {api-key}` header  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Path parameters

- `id` (integer, path, **required**) — Fundraiser ID.

## Query parameters

- `only_received` (boolean, query) — Include only received transactions for raised amount. Default: `false`

## Response

- `type` (string) — Goal type. Allowed values: `amount`, `donors`
- `goal` (number) — Goal amount.
- `raised` (number) — Raised amount.
- `donors` (number) — Number of participants.
- `n_teams` (number) — Number of teams in the campaign.
- `n_pages` (number) — Number of personal pages in the campaign.
- `name` (string) — Campaign name.
- `description` (string) — Campaign description.
- `images` (object) — Campaign images.
- `event` (object) — Event dates for the campaign.
  - `start_at` (string) — Event start date and time.
  - `end_at` (string) — Event end date and time.
  - `address` (string | null) — Legacy event address.
- `location_type` (string | null) — Campaign location type. Allowed values: `venue`, `online`, `other`.
- `location` (string | null) — Campaign location details. For a `venue`, this contains venue details; for `online`, online-event details; for `other`, free-form location text.
- `location_data` (object | null) — Structured location data. For `venue`, contains `address` and/or `geo`; for `online`, contains `link`; otherwise `null`. Missing nested fields are omitted.

**Other responses**

| Status | Description |
| - | - |
| `400` | Bad Request |
| `403` | Forbidden |

**Response example:**

```json
{
  "type": "amount",
  "goal": 10000,
  "raised": 5000,
  "donors": 25,
  "n_teams": 10,
  "n_pages": 25,
  "name": "Gala Night",
  "description": "Help us reach our goal and make a difference!",
  "images": {
    "original": "https://img.crowdchange.dev/files/abc.png"
  },
  "event": {
    "start_at": "2024-01-01 18:00:00",
    "end_at": "2024-01-01 22:00:00"
  }
}
```

---
title: Site wide stats
slug: api-reference/client-side/global-apis/get_v2-client-wl-stats
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/client-side/global-apis/get_v2-client-wl-stats
nav_path:
- API Reference
- Client Side APIs
- Global APIs
- Site wide stats
nav_order: 56
page_type: endpoint
endpoint: GET /v2/client/wl/stats
http_method: GET
endpoint_path: /v2/client/wl/stats
api_surface: client-side
auth: API key
tags:
- donations
crm_relevant: false
description: Retrieve site-wide aggregated stats across all CrowdChange campaigns, including total raised, donor count, and number of active fundraisers.
retrieved: '2026-10-14'
word_count: 137
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/client-side/global-apis/get_v2-client-wl-stats | Nav: API Reference > Client Side APIs > Global APIs > Site wide stats | Mirrored 2026-10-14 -->

# Site wide stats

> Retrieve site-wide aggregated stats across all CrowdChange campaigns, including total raised, donor count, and number of active fundraisers.

**Endpoint:** `GET /v2/client/wl/stats`  
**Surface:** Client Side API · **Auth:** API key — `Authorization: Bearer {api-key}` header  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Query parameters

- `templates` (string, query) — Comma separated list of fundraiser template (blueprint) ids.

## Response

- `amount_raised` (number) — Total amount raised by all campaigns.
- `n_fundraisers` (number) — Number of campaigns on the site.
- `n_teams` (number) — Number of teams across all campaigns.
- `n_pages` (number) — Number of personal pages across all campaigns.
- `n_donors` (number) — Number of participants.

**Other responses**

| Status | Description |
| - | - |
| `400` | Bad Request |
| `403` | Forbidden |

**Response example:**

```json
{
  "amount_raised": 10000,
  "n_fundraisers": 50,
  "n_teams": 50,
  "n_pages": 50,
  "n_donors": 2500
}
```

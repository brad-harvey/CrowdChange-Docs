---
title: Heatmap
slug: api-reference/client-side/campaign-specific-apis/get_v2-client-fundraiser-id-heatmap
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/client-side/campaign-specific-apis/get_v2-client-fundraiser-id-heatmap
nav_path:
- API Reference
- Client Side APIs
- Campaign-Specific APIs
- Heatmap
nav_order: 45
page_type: endpoint
endpoint: GET /v2/client/fundraiser/{id}/heatmap
http_method: GET
endpoint_path: /v2/client/fundraiser/{id}/heatmap
api_surface: client-side
auth: API key
tags:
- donations
crm_relevant: false
description: Retrieve aggregated donation counts and amounts raised by country and state for a CrowdChange campaign, suitable for rendering a geographic heatmap.
retrieved: '2026-10-14'
word_count: 121
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/client-side/campaign-specific-apis/get_v2-client-fundraiser-id-heatmap | Nav: API Reference > Client Side APIs > Campaign-Specific APIs > Heatmap | Mirrored 2026-10-14 -->

# Heatmap

> Retrieve aggregated donation counts and amounts raised by country and state for a CrowdChange campaign, suitable for rendering a geographic heatmap.

**Endpoint:** `GET /v2/client/fundraiser/{id}/heatmap`  
**Surface:** Client Side API · **Auth:** API key — `Authorization: Bearer {api-key}` header  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Path parameters

- `id` (integer, path, **required**) — Fundraiser ID.

## Response

Returns an array of objects with the following fields.

- `amount_raised` (number) — Total raised amount
- `n_donors` (number) — Number of donors
- `country` (string) — Country code
- `state` (string) — State or province.

**Other responses**

| Status | Description |
| - | - |
| `400` | Bad Request |
| `403` | Forbidden |

**Response example:**

```json
[
  {
    "amount_raised": 100,
    "n_donors": 10,
    "country": "CA",
    "state": "NY"
  }
]
```

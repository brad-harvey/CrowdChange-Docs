---
title: Get webhooks
slug: api-reference/server-side/webhooks/get_v2-private-webhooks
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/webhooks/get_v2-private-webhooks
nav_path:
- API Reference
- Server Side APIs
- Webhooks
- Get webhooks
nav_order: 35
page_type: endpoint
endpoint: GET /v2/private/webhooks
http_method: GET
endpoint_path: /v2/private/webhooks
api_surface: server-side
auth: API key
tags:
- registration
- webhooks
crm_relevant: true
description: Retrieve a paginated list of every CrowdChange webhook subscription registered on your account, with target URL, subscribed events, and status.
retrieved: '2026-10-14'
word_count: 204
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/webhooks/get_v2-private-webhooks | Nav: API Reference > Server Side APIs > Webhooks > Get webhooks | Mirrored 2026-10-14 -->

# Get webhooks

> Retrieve a paginated list of every CrowdChange webhook subscription registered on your account, with target URL, subscribed events, and status.

**Endpoint:** `GET /v2/private/webhooks`  
**Surface:** Server Side API (server-to-server only; never call from a browser) · **Auth:** API key — `Authorization: Bearer {api-key}` header  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Query parameters

- `q` (string, query) — Search term.
- `page` (integer, query) — Page number. Default: `1`
- `limit` (integer, query) — Number of results to return. Default: `10`

## Response

Returns an array of objects with the following fields.

- `id` (integer) — Webhook ID.
- `url` (string) — Webhook URL.
- `signing_secret` (string) — Webhook-specific secret used to verify `CrowdChange-Webhook-Signature` on outbound deliveries. Store this value securely.
- `language` (string) — Webhook language. Allowed values: `en`, `fr`
- `created_at` (string) — Webhook creation date.
- `events` (object[]) — List of subscribed events.
  - `id` (integer) — Event ID.
  - `name` (string) — Event name
  - `created_at` (string) — Event creation date.

**Other responses**

| Status | Description |
| - | - |
| `400` | Bad Request |
| `401` | Unauthorized |
| `403` | Forbidden |

**Response example:**

```json
[
  {
    "id": 1,
    "url": "https://demo.crowdchange.test/webhooks/handle",
    "signing_secret": "whsec_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ab",
    "language": "en",
    "created_at": "2024-01-01 16:00:03",
    "events": [
      {
        "id": 1,
        "name": "fundraiser_created",
        "created_at": "string"
      }
    ]
  }
]
```

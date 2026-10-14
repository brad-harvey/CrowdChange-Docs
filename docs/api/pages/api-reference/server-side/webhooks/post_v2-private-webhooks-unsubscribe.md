---
title: Unsubscribe webhook
slug: api-reference/server-side/webhooks/post_v2-private-webhooks-unsubscribe
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/webhooks/post_v2-private-webhooks-unsubscribe
nav_path:
- API Reference
- Server Side APIs
- Webhooks
- Unsubscribe webhook
nav_order: 34
page_type: endpoint
endpoint: POST /v2/private/webhooks/unsubscribe
http_method: POST
endpoint_path: /v2/private/webhooks/unsubscribe
api_surface: server-side
auth: API key
tags:
- webhooks
crm_relevant: true
description: Remove an existing CrowdChange webhook subscription so the target URL stops receiving event payloads from the fundraising platform.
retrieved: '2026-10-14'
word_count: 112
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/webhooks/post_v2-private-webhooks-unsubscribe | Nav: API Reference > Server Side APIs > Webhooks > Unsubscribe webhook | Mirrored 2026-10-14 -->

# Unsubscribe webhook

> Remove an existing CrowdChange webhook subscription so the target URL stops receiving event payloads from the fundraising platform.

**Endpoint:** `POST /v2/private/webhooks/unsubscribe`  
**Surface:** Server Side API (server-to-server only; never call from a browser) · **Auth:** API key — `Authorization: Bearer {api-key}` header  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Body

- `url` (string, body, **required**) — URL to unsubscribe.
- `lang` (string, body) — Webhook locale. Allowed values: `en`, `fr` Default: `en`

## Response

- `status` (string) — Status of the operation.

**Other responses**

| Status | Description |
| - | - |
| `400` | Bad Request |
| `401` | Unauthorized |
| `403` | Forbidden |

**Response example:**

```json
{
  "status": "ok"
}
```

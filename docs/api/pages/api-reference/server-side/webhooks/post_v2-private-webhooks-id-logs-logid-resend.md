---
title: Resend logged event
slug: api-reference/server-side/webhooks/post_v2-private-webhooks-id-logs-logid-resend
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/webhooks/post_v2-private-webhooks-id-logs-logid-resend
nav_path:
- API Reference
- Server Side APIs
- Webhooks
- Resend logged event
nav_order: 39
page_type: endpoint
endpoint: POST /v2/private/webhooks/{webhookId}/logs/{logId}/resend
http_method: POST
endpoint_path: /v2/private/webhooks/{webhookId}/logs/{logId}/resend
api_surface: server-side
auth: API key
tags:
- troubleshooting
- webhooks
crm_relevant: true
description: Resend a previously logged CrowdChange webhook event to its subscriber URL, useful for retrying failed deliveries or debugging webhook handlers.
retrieved: '2026-10-14'
word_count: 128
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/webhooks/post_v2-private-webhooks-id-logs-logid-resend | Nav: API Reference > Server Side APIs > Webhooks > Resend logged event | Mirrored 2026-10-14 -->

# Resend logged event

> Resend a previously logged CrowdChange webhook event to its subscriber URL, useful for retrying failed deliveries or debugging webhook handlers.

**Endpoint:** `POST /v2/private/webhooks/{webhookId}/logs/{logId}/resend`  
**Surface:** Server Side API (server-to-server only; never call from a browser) · **Auth:** API key — `Authorization: Bearer {api-key}` header  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Path parameters

- `webhookId` (integer, path, **required**) — Webhook ID.
- `logId` (integer, path, **required**) — Log ID.

## Response

- `status` (string) — Status of the operation. Check the logs if you want to know the HTTP-code returned by your server.

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

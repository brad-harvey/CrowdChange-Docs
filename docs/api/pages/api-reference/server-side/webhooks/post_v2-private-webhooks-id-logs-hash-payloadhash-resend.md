---
title: Resend event by payload hash
slug: api-reference/server-side/webhooks/post_v2-private-webhooks-id-logs-hash-payloadhash-resend
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/webhooks/post_v2-private-webhooks-id-logs-hash-payloadhash-resend
nav_path:
- API Reference
- Server Side APIs
- Webhooks
- Resend event by payload hash
nav_order: 40
page_type: endpoint
endpoint: POST /v2/private/webhooks/{webhookId}/logs/hash/{payloadHash}/resend
http_method: POST
endpoint_path: /v2/private/webhooks/{webhookId}/logs/hash/{payloadHash}/resend
api_surface: server-side
auth: API key
tags:
- webhooks
crm_relevant: true
description: Resend the newest logged CrowdChange webhook delivery that matches a payload hash, creating a new delivery attempt with the same payload.
retrieved: '2026-10-14'
word_count: 188
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/webhooks/post_v2-private-webhooks-id-logs-hash-payloadhash-resend | Nav: API Reference > Server Side APIs > Webhooks > Resend event by payload hash | Mirrored 2026-10-14 -->

# Resend event by payload hash

> Resend the newest logged CrowdChange webhook delivery that matches a payload hash, creating a new delivery attempt with the same payload.

**Endpoint:** `POST /v2/private/webhooks/{webhookId}/logs/hash/{payloadHash}/resend`  
**Surface:** Server Side API (server-to-server only; never call from a browser) · **Auth:** API key — `Authorization: Bearer {api-key}` header  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Path parameters

- `webhookId` (integer, path, **required**) — Webhook ID.
- `payloadHash` (string, path, **required**) — The 32-character MD5 fingerprint returned as `payload_hash` by [Get logs](get_v2-private-webhooks-id-logs.md).

This endpoint finds the newest log for the webhook with the specified `payload_hash` and resends its `event` and `data` payload.

The resend creates a new delivery attempt with a new log `id` and the same `payload_hash`. The payload hash is a lookup value and does not replace the `CrowdChange-Webhook-Signature` header used to verify webhook authenticity.

**Other responses**

| Status | Description |
| - | - |
| `400` | Bad Request |
| `401` | Unauthorized |
| `403` | Forbidden |
| `404` | No matching webhook log found |

**Response example:**

```json
{
  "status": "ok"
}
```

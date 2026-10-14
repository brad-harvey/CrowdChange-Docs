---
title: Get logs
slug: api-reference/server-side/webhooks/get_v2-private-webhooks-id-logs
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/webhooks/get_v2-private-webhooks-id-logs
nav_path:
- API Reference
- Server Side APIs
- Webhooks
- Get logs
nav_order: 38
page_type: endpoint
endpoint: GET /v2/private/webhooks/{webhookId}/logs
http_method: GET
endpoint_path: /v2/private/webhooks/{webhookId}/logs
api_surface: server-side
auth: API key
tags:
- webhooks
crm_relevant: true
description: Retrieve a paginated log of webhook delivery attempts for a CrowdChange webhook subscription, including event type, status, and response details.
retrieved: '2026-10-14'
word_count: 282
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/webhooks/get_v2-private-webhooks-id-logs | Nav: API Reference > Server Side APIs > Webhooks > Get logs | Mirrored 2026-10-14 -->

# Get logs

> Retrieve a paginated log of webhook delivery attempts for a CrowdChange webhook subscription, including event type, status, and response details.

**Endpoint:** `GET /v2/private/webhooks/{webhookId}/logs`  
**Surface:** Server Side API (server-to-server only; never call from a browser) · **Auth:** API key — `Authorization: Bearer {api-key}` header  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Path parameters

- `webhookId` (integer, path, **required**) — Webhook ID.

## Query parameters

- `page` (integer, query) — Page number. Default: `1`
- `limit` (integer, query) — Number of results to return. Default: `10`
- `event` (string, query) — Event name. Allowed values: `fundraiser_created`, `fundraiser_updated`, `fundraiser_deleted`, `transaction_created`, `transaction_refunded`, `fundraiser_team_created`, `fundraiser_team_updated`, `fundraiser_team_deleted`, `fundraiser_page_created`, `fundraiser_page_updated`, `fundraiser_page_deleted`, `tax_receipt_issued`, `milestone_triggered`

See [Event payloads](event-payloads.md) for the JSON payload sent to your webhook URL and stored in each log entry.

Each delivery attempt has its own `id`. The `payload_hash` identifies the normalized payload shared by attempts with the same event data. Use it with [Resend event by payload hash](post_v2-private-webhooks-id-logs-hash-payloadhash-resend.md) to replay the newest matching delivery.

## Response

Returns an array of objects with the following fields.

- `id` (integer) — Log entry ID.
- `webhook_id` (integer) — Webhook ID.
- `webhook_event_id` (integer) — Webhook Event ID.
- `payload_hash` (string | null) — MD5 fingerprint of the normalized payload. This is `null` for logs created before payload hashes were added.
- `created_at` (string) — Event sent date.
- `code` (integer) — HTTP-code of response from your server.
- `payload` (object) — Payload sent to your server.

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
    "webhook_id": 1,
    "webhook_event_id": 1,
    "payload_hash": "0123456789abcdef0123456789abcdef",
    "created_at": "2024-01-01 16:00:03",
    "code": 200,
    "payload": {}
  }
]
```

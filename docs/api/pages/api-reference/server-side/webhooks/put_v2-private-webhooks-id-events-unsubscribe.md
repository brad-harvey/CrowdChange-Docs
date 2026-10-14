---
title: Unsubscribe Webhook events
slug: api-reference/server-side/webhooks/put_v2-private-webhooks-id-events-unsubscribe
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/webhooks/put_v2-private-webhooks-id-events-unsubscribe
nav_path:
- API Reference
- Server Side APIs
- Webhooks
- Unsubscribe Webhook events
nav_order: 37
page_type: endpoint
endpoint: PUT /v2/private/webhooks/{webhookId}/events/unsubscribe
http_method: PUT
endpoint_path: /v2/private/webhooks/{webhookId}/events/unsubscribe
api_surface: server-side
auth: API key
tags:
- webhooks
crm_relevant: true
description: Remove specific CrowdChange system events from an existing webhook subscription so the target URL stops receiving those event payloads.
retrieved: '2026-10-14'
word_count: 205
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/webhooks/put_v2-private-webhooks-id-events-unsubscribe | Nav: API Reference > Server Side APIs > Webhooks > Unsubscribe Webhook events | Mirrored 2026-10-14 -->

# Unsubscribe Webhook events

> Remove specific CrowdChange system events from an existing webhook subscription so the target URL stops receiving those event payloads.

**Endpoint:** `PUT /v2/private/webhooks/{webhookId}/events/unsubscribe`  
**Surface:** Server Side API (server-to-server only; never call from a browser) · **Auth:** API key — `Authorization: Bearer {api-key}` header  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Path parameters

- `webhookId` (integer, path, **required**) — Webhook ID.

## Body

- `events` (string[], body, **required**) — Events to unsubscribe. Allowed values: `fundraiser_created`, `fundraiser_updated`, `fundraiser_deleted`, `transaction_created`, `transaction_refunded`, `fundraiser_team_created`, `fundraiser_team_updated`, `fundraiser_team_deleted`, `fundraiser_page_created`, `fundraiser_page_updated`, `fundraiser_page_deleted`, `tax_receipt_issued`, `milestone_triggered`

## Response

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
```

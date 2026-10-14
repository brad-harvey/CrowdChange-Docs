---
title: Subscribe Webhook events
slug: api-reference/server-side/webhooks/put_v2-private-webhooks-id-events-subscribe
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/webhooks/put_v2-private-webhooks-id-events-subscribe
nav_path:
- API Reference
- Server Side APIs
- Webhooks
- Subscribe Webhook events
nav_order: 36
page_type: endpoint
endpoint: PUT /v2/private/webhooks/{webhookId}/events/subscribe
http_method: PUT
endpoint_path: /v2/private/webhooks/{webhookId}/events/subscribe
api_surface: server-side
auth: API key
tags:
- webhooks
crm_relevant: true
description: Add specific CrowdChange system events to an existing webhook subscription so the target URL starts receiving those event payloads.
retrieved: '2026-10-14'
word_count: 205
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/webhooks/put_v2-private-webhooks-id-events-subscribe | Nav: API Reference > Server Side APIs > Webhooks > Subscribe Webhook events | Mirrored 2026-10-14 -->

# Subscribe Webhook events

> Add specific CrowdChange system events to an existing webhook subscription so the target URL starts receiving those event payloads.

**Endpoint:** `PUT /v2/private/webhooks/{webhookId}/events/subscribe`  
**Surface:** Server Side API (server-to-server only; never call from a browser) · **Auth:** API key — `Authorization: Bearer {api-key}` header  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Path parameters

- `webhookId` (integer, path, **required**) — Webhook ID.

## Body

- `events` (string[], body, **required**) — Events for subscription. Allowed values: `fundraiser_created`, `fundraiser_updated`, `fundraiser_deleted`, `transaction_created`, `transaction_refunded`, `fundraiser_team_created`, `fundraiser_team_updated`, `fundraiser_team_deleted`, `fundraiser_page_created`, `fundraiser_page_updated`, `fundraiser_page_deleted`, `tax_receipt_issued`, `milestone_triggered`

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

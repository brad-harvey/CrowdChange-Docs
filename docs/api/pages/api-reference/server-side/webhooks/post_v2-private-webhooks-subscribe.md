---
title: Subscribe Webhook
slug: api-reference/server-side/webhooks/post_v2-private-webhooks-subscribe
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/webhooks/post_v2-private-webhooks-subscribe
nav_path:
- API Reference
- Server Side APIs
- Webhooks
- Subscribe Webhook
nav_order: 33
page_type: endpoint
endpoint: POST /v2/private/webhooks/subscribe
http_method: POST
endpoint_path: /v2/private/webhooks/subscribe
api_surface: server-side
auth: API key
tags:
- registration
- webhooks
crm_relevant: true
description: Register a new CrowdChange webhook subscription pointing at your target URL to start receiving event payloads from the fundraising platform.
retrieved: '2026-10-14'
word_count: 230
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/webhooks/post_v2-private-webhooks-subscribe | Nav: API Reference > Server Side APIs > Webhooks > Subscribe Webhook | Mirrored 2026-10-14 -->

# Subscribe Webhook

> Register a new CrowdChange webhook subscription pointing at your target URL to start receiving event payloads from the fundraising platform.

**Endpoint:** `POST /v2/private/webhooks/subscribe`  
**Surface:** Server Side API (server-to-server only; never call from a browser) · **Auth:** API key — `Authorization: Bearer {api-key}` header  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Body

- `url` (string, body, **required**) — URL to subscribe. Provided URL should return 200 HTTP-code in order to be subscribed.
- `lang` (string, body) — Webhook locale. Allowed values: `en`, `fr` Default: `en`
- `events` (string[], body) — Events for subscription. Allowed values: `fundraiser_created`, `fundraiser_updated`, `fundraiser_deleted`, `transaction_created`, `transaction_refunded`, `fundraiser_team_created`, `fundraiser_team_updated`, `fundraiser_team_deleted`, `fundraiser_page_created`, `fundraiser_page_updated`, `fundraiser_page_deleted`, `tax_receipt_issued`, `milestone_triggered`

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
| `400` | URL is not available (does not return 200 HTTP-code) |
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

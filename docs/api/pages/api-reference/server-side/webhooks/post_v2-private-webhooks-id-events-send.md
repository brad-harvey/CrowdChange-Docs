---
title: Send event
slug: api-reference/server-side/webhooks/post_v2-private-webhooks-id-events-send
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/webhooks/post_v2-private-webhooks-id-events-send
nav_path:
- API Reference
- Server Side APIs
- Webhooks
- Send event
nav_order: 41
page_type: endpoint
endpoint: POST /v2/private/webhooks/{webhookId}/events/send
http_method: POST
endpoint_path: /v2/private/webhooks/{webhookId}/events/send
api_surface: server-side
auth: API key
tags:
- webhooks
crm_relevant: true
description: Trigger a CrowdChange webhook to fire an event payload based on an existing entity, useful for testing endpoints and replaying historical data.
retrieved: '2026-10-14'
word_count: 282
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/webhooks/post_v2-private-webhooks-id-events-send | Nav: API Reference > Server Side APIs > Webhooks > Send event | Mirrored 2026-10-14 -->

# Send event

> Trigger a CrowdChange webhook to fire an event payload based on an existing entity, useful for testing endpoints and replaying historical data.

**Endpoint:** `POST /v2/private/webhooks/{webhookId}/events/send`  
**Surface:** Server Side API (server-to-server only; never call from a browser) · **Auth:** API key — `Authorization: Bearer {api-key}` header  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Path parameters

- `webhookId` (integer, path, **required**) — Webhook ID.

## Body

- `id` (integer, body, **required**) — Entity ID. (Campaign/Transaction/Tax Receipt/Team/Personal Page/Milestone log)
- `event` (string, body, **required**) — Event name. Allowed values: `fundraiser_created`, `fundraiser_updated`, `fundraiser_deleted`, `transaction_created`, `transaction_refunded`, `fundraiser_team_created`, `fundraiser_team_updated`, `fundraiser_team_deleted`, `fundraiser_page_created`, `fundraiser_page_updated`, `fundraiser_page_deleted`, `tax_receipt_issued`, `milestone_triggered`

## Replaying deletion and refund events

The event must be subscribed on the webhook, and the entity must be accessible to the authenticated partner.

| Event | Body `id` |
| - | - |
| `fundraiser_deleted` | Deleted campaign ID |
| `fundraiser_team_deleted` | Deleted team ID |
| `fundraiser_page_deleted` | Deleted personal page ID |
| `transaction_refunded` | Refund transaction ID with `status: "refunded"` and a `parent_id` |

Deletion events require an entity that has already been deleted. Refund events accept both full and partial refund records.

This endpoint builds a payload from the current entity data. For refunds, the original payment in `data.parent` reflects its current stored state, including any later refunds. To resend a saved payload, use [Resend event](post_v2-private-webhooks-id-logs-logid-resend.md).

## Response

- `status` (string) — Status of the operation. Check the logs if you want to know the HTTP-code returned by your server.

**Other responses**

| Status | Description |
| - | - |
| `400` | Bad Request |
| `401` | Unauthorized |
| `403` | Forbidden |
| `404` | Entity not found, inaccessible, or does not match the selected event |

**Response example:**

```json
{
  "status": "ok"
}
```

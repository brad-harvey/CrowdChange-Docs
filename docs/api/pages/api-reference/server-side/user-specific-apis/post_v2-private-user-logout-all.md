---
title: Sign Out All Devices
slug: api-reference/server-side/user-specific-apis/post_v2-private-user-logout-all
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/user-specific-apis/post_v2-private-user-logout-all
nav_path:
- API Reference
- Server Side APIs
- User-Specific APIs
- Sign Out All Devices
nav_order: 22
page_type: endpoint
endpoint: POST /v2/private/user/logout/all
http_method: POST
endpoint_path: /v2/private/user/logout/all
api_surface: server-side
auth: API key + user token
tags:
- authentication
crm_relevant: true
description: Invalidate every active auth token for the authenticated CrowdChange user, signing them out of all devices and sessions in a single call.
retrieved: '2026-10-14'
word_count: 119
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/user-specific-apis/post_v2-private-user-logout-all | Nav: API Reference > Server Side APIs > User-Specific APIs > Sign Out All Devices | Mirrored 2026-10-14 -->

# Sign Out All Devices

> Invalidate every active auth token for the authenticated CrowdChange user, signing them out of all devices and sessions in a single call.

**Endpoint:** `POST /v2/private/user/logout/all`  
**Surface:** Server Side API (server-to-server only; never call from a browser) · **Auth:** API key + user token — `Authorization: Bearer {api-key}` header, plus the user token in the `auth-token` header or `token` param  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Body

- `email` (string, body, **required**) — User's email.

## Response

- `status` (string) — Status of the operation.

**Other responses**

| Status | Description |
| - | - |
| `401` | Unauthorized |
| `403` | Forbidden |

**Response example:**

```json
{
  "status": "ok"
}
```

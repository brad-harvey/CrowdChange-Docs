---
title: Sign Out
slug: api-reference/server-side/user-specific-apis/post_v2-private-user-logout
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/user-specific-apis/post_v2-private-user-logout
nav_path:
- API Reference
- Server Side APIs
- User-Specific APIs
- Sign Out
nav_order: 21
page_type: endpoint
endpoint: POST /v2/private/user/logout
http_method: POST
endpoint_path: /v2/private/user/logout
api_surface: server-side
auth: API key + user token
tags:
- authentication
crm_relevant: true
description: Invalidate the current CrowdChange auth token to sign the authenticated user out of the active session on a single device or client.
retrieved: '2026-10-14'
word_count: 117
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/user-specific-apis/post_v2-private-user-logout | Nav: API Reference > Server Side APIs > User-Specific APIs > Sign Out | Mirrored 2026-10-14 -->

# Sign Out

> Invalidate the current CrowdChange auth token to sign the authenticated user out of the active session on a single device or client.

**Endpoint:** `POST /v2/private/user/logout`  
**Surface:** Server Side API (server-to-server only; never call from a browser) · **Auth:** API key + user token — `Authorization: Bearer {api-key}` header, plus the user token in the `auth-token` header or `token` param  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Body

- `token` (string, body, **required**) — User's access token.

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

---
title: Sign In
slug: api-reference/server-side/user-specific-apis/post_v2-private-user-login
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/user-specific-apis/post_v2-private-user-login
nav_path:
- API Reference
- Server Side APIs
- User-Specific APIs
- Sign In
nav_order: 20
page_type: endpoint
endpoint: POST /v2/private/user/login
http_method: POST
endpoint_path: /v2/private/user/login
api_surface: server-side
auth: API key
tags:
- authentication
crm_relevant: true
description: Authenticate a CrowdChange user and receive an auth token for user-specific API calls, including the two-factor authentication challenge flow.
retrieved: '2026-10-14'
word_count: 250
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/user-specific-apis/post_v2-private-user-login | Nav: API Reference > Server Side APIs > User-Specific APIs > Sign In | Mirrored 2026-10-14 -->

# Sign In

> Authenticate a CrowdChange user and receive an auth token for user-specific API calls, including the two-factor authentication challenge flow.

**Endpoint:** `POST /v2/private/user/login`  
**Surface:** Server Side API (server-to-server only; never call from a browser) · **Auth:** API key — `Authorization: Bearer {api-key}` header  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Body

- `email` (string, body, **required**) — User's email.
- `password` (string, body, **required**) — User's password.
- `method` (string, body) — Method of 2FA. Required if the first login attempt asks to use 2FA. Allowed values: `sms`, `email`, `authApplication`
- `mfa_code` (string, body) — 2FA code sent to user. Required if the first login attempt asks to use 2FA.

## Response

- `token` (string) — Auth token to User-specific API. Presented if log in process is successful. Expired after 30 days if not used.
- `user_id` (integer) — User ID. Presented if log in process is successful.
- `email` (string) — Disguised user email. Presented if user needs to use 2FA and has email 2FA method.
- `phone` (string) — Disguised user Phone. Presented if user needs to use 2FA and has sms 2FA method.
- `method` (string) — Default 2FA method. Presented if user needs to use 2FA.
- `active_methods` (any[]) — Available 2FA methods to user. Presented if user needs to use 2FA.

**Other responses**

| Status | Description |
| - | - |
| `401` | Unauthorized |
| `403` | Forbidden |

**Response example:**

```json
{
  "token": "1|WQaSlvm1Gl8Pscq0e98K5MQPhiV8Q07CT9t8vR0N",
  "user_id": 10,
  "email": "a***n@crowdchange.co",
  "phone": "Campaign",
  "method": "Description",
  "active_methods": [
    "email",
    "sms",
    "authApplication"
  ]
}
```

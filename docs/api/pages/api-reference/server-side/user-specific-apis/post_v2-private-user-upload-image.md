---
title: Upload Image
slug: api-reference/server-side/user-specific-apis/post_v2-private-user-upload-image
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/user-specific-apis/post_v2-private-user-upload-image
nav_path:
- API Reference
- Server Side APIs
- User-Specific APIs
- Upload Image
nav_order: 23
page_type: endpoint
endpoint: POST /v2/private/user/upload/image
http_method: POST
endpoint_path: /v2/private/user/upload/image
api_surface: server-side
auth: API key + user token
tags:
- page-design
- peer-to-peer
- teams
crm_relevant: true
description: Upload an image file to CrowdChange on behalf of the authenticated user, returning a hosted URL you can attach to personal pages or teams.
retrieved: '2026-10-14'
word_count: 148
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/user-specific-apis/post_v2-private-user-upload-image | Nav: API Reference > Server Side APIs > User-Specific APIs > Upload Image | Mirrored 2026-10-14 -->

# Upload Image

> Upload an image file to CrowdChange on behalf of the authenticated user, returning a hosted URL you can attach to personal pages or teams.

**Endpoint:** `POST /v2/private/user/upload/image`  
**Surface:** Server Side API (server-to-server only; never call from a browser) · **Auth:** API key + user token — `Authorization: Bearer {api-key}` header, plus the user token in the `auth-token` header or `token` param  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Body

- `file` (string, body, **required**) — base-64 encoded image.

## Response

- `id` (string) — Image ID
- `url` (string) — URL to uploaded image
- `success` (boolean) — Flag if uploading is successful
- `message` (string) — Message if uploading is unsuccessful

**Other responses**

| Status | Description |
| - | - |
| `401` | Unauthorized |
| `403` | Forbidden |

**Response example:**

```json
{
  "id": "1eaf5ab2-5d55-11ee-82ef-001c42584fa2",
  "url": 10,
  "success": true,
  "message": "Campaign"
}
```

---
title: Team Donors List
slug: api-reference/server-side/user-specific-apis/get_v2-private-user-fundraiser-id-team-teamid-donors
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/user-specific-apis/get_v2-private-user-fundraiser-id-team-teamid-donors
nav_path:
- API Reference
- Server Side APIs
- User-Specific APIs
- Team Donors List
nav_order: 32
page_type: endpoint
endpoint: GET /v2/private/user/fundraiser/{id}/team/{teamId}/donors
http_method: GET
endpoint_path: /v2/private/user/fundraiser/{id}/team/{teamId}/donors
api_surface: server-side
auth: API key + user token
tags:
- donations
- peer-to-peer
- teams
crm_relevant: true
description: Retrieve a paginated list of donors for the authenticated user's team within a campaign, returning 10 donors per page with names and amounts.
retrieved: '2026-10-14'
word_count: 254
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/user-specific-apis/get_v2-private-user-fundraiser-id-team-teamid-donors | Nav: API Reference > Server Side APIs > User-Specific APIs > Team Donors List | Mirrored 2026-10-14 -->

# Team Donors List

> Retrieve a paginated list of donors for the authenticated user's team within a campaign, returning 10 donors per page with names and amounts.

**Endpoint:** `GET /v2/private/user/fundraiser/{id}/team/{teamId}/donors`  
**Surface:** Server Side API (server-to-server only; never call from a browser) · **Auth:** API key + user token — `Authorization: Bearer {api-key}` header, plus the user token in the `auth-token` header or `token` param  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Path parameters

- `id` (integer, path, **required**) — Campaign ID.
- `teamId` (integer, path, **required**) — Team ID.

## Query parameters

- `page` (integer, query) — Page number. Default: `1`
- `limit` (integer, query) — Number of results to return. Default: `10`
- `sort` (string, query) — Key to sort by. Allowed values: `id`, `amount` Default: `id`
- `direction` (string, query) — Direction of sorting. Allowed values: `asc`, `desc` Default: `desc`
- `only_received` (integer, query) — Include only received transactions. Default: `0`

## Response

Returns an array of objects with the following fields.

- `amount` (number) — Donation amount
- `amount_match` (number) — Matched amount for campaigns with donation matching enabled.
- `name` (string) — Donor's name or alias.
- `date` (string) — Date and time of donation
- `contact_email` (string) — Donor's email
- `fundraiser_team_id` (integer) — Team ID.
- `fundraiser_page_id` (integer) — Page ID.
- `comment` (string) — Donor's comment.

**Other responses**

| Status | Description |
| - | - |
| `400` | Bad Request |
| `403` | Forbidden |

**Response example:**

```json
[
  {
    "amount": 100,
    "amount_match": 100,
    "name": "John Snow",
    "date": "2021-01-01 00:00:00",
    "contact_email": "john@example.com",
    "fundraiser_team_id": 1,
    "fundraiser_page_id": 1,
    "comment": "Comment"
  }
]
```

---
title: Activities Leaderboard
slug: api-reference/client-side/global-apis/get_v2-client-activity-trackers-leaderboard
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/client-side/global-apis/get_v2-client-activity-trackers-leaderboard
nav_path:
- API Reference
- Client Side APIs
- Global APIs
- Activities Leaderboard
nav_order: 53
page_type: endpoint
endpoint: GET /v2/client/activity-trackers/leaderboard
http_method: GET
endpoint_path: /v2/client/activity-trackers/leaderboard
api_surface: client-side
auth: API key
tags:
- activity-tracking
- leaderboards
- peer-to-peer
- registration
crm_relevant: false
description: Retrieve the activity tracker leaderboard of personal pages, returning 10 participants per page ranked by tracked steps, distance, or minutes.
retrieved: '2026-10-14'
word_count: 272
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/client-side/global-apis/get_v2-client-activity-trackers-leaderboard | Nav: API Reference > Client Side APIs > Global APIs > Activities Leaderboard | Mirrored 2026-10-14 -->

# Activities Leaderboard

> Retrieve the activity tracker leaderboard of personal pages, returning 10 participants per page ranked by tracked steps, distance, or minutes.

**Endpoint:** `GET /v2/client/activity-trackers/leaderboard`  
**Surface:** Client Side API · **Auth:** API key — `Authorization: Bearer {api-key}` header  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Query parameters

- `basis` (string, query, **required**) — Basis of activity. Allowed values: `distance`, `time`, `daily`
- `page` (integer, query) — Page number. Default: `1`
- `limit` (integer, query) — Number of results to return. Default: `10`
- `text` (string, query) — Search term.
- `activity_type` (string, query) — Activity type name.
- `include_archived` (integer, query) — Include archived activities. Default: `0`
- `include_finished` (integer, query) — Include finished activities. Default: `0`
- `fundraiser_id` (integer, query) — Filter by campaign ID.
- `lang` (string, query) — API's locale. Allowed values: `en`, `fr`

## Response

Returns an array of objects with the following fields.

- `total` (number) — Tracked value.
- `activity_tracker` (object)
  - `name` (string) — Activity's name.
  - `basis` (string) — Activity basis' name. Allowed values: `daily`, `time`, `distance`
  - `types` (object[]) — List of activity types.
    - `name` (string) — Activity type's name.
    - `total` (number) — Activity type's tracked value.
- `fundraiser_page` (object)
  - `name` (string) — Personal page name.
  - `fundraiser` (object)
    - `name` (string) — Campaign that personal page belongs to.
    - `organization` (object)
      - `name` (string) — Campaign organization's name.
  - `team` (object)
    - `name` (string) — Team name that personal page belongs to (if assigned to a team).

**Other responses**

| Status | Description |
| - | - |
| `400` | Bad Request |
| `403` | Forbidden |

**Response example:**

```json
[
{
    "total": 1000,
    "activity_tracker": {
    "name": "Activity name.",
    "basis": "distance",
    "types": [
{
    "name": "Run.",
    "total": 1000
}
    ]
},
    "fundraiser_page": {
    "name": "Personal page name.",
    "fundraiser": {
    "name": "Campaign name",
    "organization": {
    "name": "Organization name."
}
},
    "team": {
    "name": "Team name."
}
}
}
]
```

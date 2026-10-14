---
title: Find Campaign
slug: api-reference/client-side/global-apis/get_v2-client-fundraisers-search
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/client-side/global-apis/get_v2-client-fundraisers-search
nav_path:
- API Reference
- Client Side APIs
- Global APIs
- Find Campaign
nav_order: 48
page_type: endpoint
endpoint: GET /v2/client/fundraisers/search
http_method: GET
endpoint_path: /v2/client/fundraisers/search
api_surface: client-side
auth: API key
tags:
- donations
- search
crm_relevant: false
description: Search CrowdChange campaigns by keyword and retrieve a paginated list of matching fundraisers with goal, raised, and status data for each.
retrieved: '2026-10-14'
word_count: 465
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/client-side/global-apis/get_v2-client-fundraisers-search | Nav: API Reference > Client Side APIs > Global APIs > Find Campaign | Mirrored 2026-10-14 -->

# Find Campaign

> Search CrowdChange campaigns by keyword and retrieve a paginated list of matching fundraisers with goal, raised, and status data for each.

**Endpoint:** `GET /v2/client/fundraisers/search`  
**Surface:** Client Side API · **Auth:** API key — `Authorization: Bearer {api-key}` header  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Query parameters

- `text` (string, query) — Search term.
- `fundraisers` (string, query) — Comma separated list of fundraiser ids.
- `templates` (string, query) — Comma separated list of fundraiser template (blueprint) ids.
- `page` (integer, query) — Page number. Default: `1`
- `limit` (integer, query) — Number of results to return. Default: `10`
- `sort` (string, query) — Key to sort by. Allowed values: `name`, `amount_raised`, `amount_goal`
- `direction` (string, query) — Direction of sorting. Allowed values: `asc`, `desc`
- `lang` (string, query) — API's locale. Allowed values: `en`, `fr`
- `include_closed` (integer, query) — Include closed campaigns. Default: `0`
- `include_hidden` (integer, query) — Include hidden campaigns. Default: `0`
- `include_subsites` (integer, query) — Include data from subsites. Default: `0`
- `amount_raised` (object, query) — Campaign's amount raised filter.

## Response

Returns an array of objects with the following fields.

- `id` (integer) — Campaign ID.
- `name` (string) — Campaign name.
- `amount_goal` (number) — Goal amount.
- `amount_goal_formatted` (string) — Formatted goal amount of the campaign, includes currency symbol.
- `amount_raised` (number) — Amount raised by the campaign.
- `amount_raised_formatted` (string) — Formatted amount raised by the campaign, includes currency symbol.
- `n_donors` (number) — Number of donors
- `n_teams` (number) — Number of teams in the campaign.
- `n_pages` (number) — Number of personal pages in the campaign.
- `url` (string) — URL to campaign.
- `language` (string) — Campaign language. Allowed values: `en`, `fr`
- `is_hidden` (boolean) — True if campaign is hidden, otherwise false.
- `closed_at` (string) — Campaign closed at
- `user` (object)
  - `name` (string) — Campaign owner's name
  - `first_name` (string) — Campaign owner's first name
  - `last_name` (string) — Campaign owner's last name
  - `title` (string) — Campaign owner's title
- `organization` (object)
  - `id` (integer) — Campaign organization's ID
  - `name` (string) — Campaign organization's name
  - `custom_id` (string) — Campaign organization's Custom ID
- `images` (object)
  - `original` (string) — URL to original campaign's image.
- `location_type` (string | null) — Campaign location type. Allowed values: `venue`, `online`, `other`.
- `location` (string | null) — Campaign location details. For a `venue`, this contains venue details; for `online`, online-event details; for `other`, free-form location text.
- `location_data` (object | null) — Structured location data. For `venue`, contains `address` and/or `geo`; for `online`, contains `link`; otherwise `null`. Missing nested fields are omitted.

**Other responses**

| Status | Description |
| - | - |
| `400` | Bad Request |
| `403` | Forbidden |

**Response example:**

```json
[
  {
    "id": 1,
    "name": "Campaign",
    "amount_goal": 1000,
    "amount_goal_formatted": "$1,000",
    "amount_raised": 550,
    "amount_raised_formatted": "$550",
    "n_donors": 10,
    "n_teams": 5,
    "n_pages": 15,
    "url": "https://demo.crowdchange.dev/2",
    "language": "en",
    "is_hidden": false,
    "closed_at": "2022-03-01 00:00:00",
    "user": {
      "name": "John Snow",
      "first_name": "John",
      "last_name": "Snow",
      "title": "Mr."
    },
    "organization": {
      "id": 1,
      "name": "Crowdchange",
      "custom_id": "CrowdchangeID"
    },
    "images": {
      "original": "https://img.crowdchange.dev/files/abc.png"
    }
  }
]
```

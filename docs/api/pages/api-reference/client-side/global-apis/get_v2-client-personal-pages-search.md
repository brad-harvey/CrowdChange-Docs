---
title: Find Personal Page
slug: api-reference/client-side/global-apis/get_v2-client-personal-pages-search
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/client-side/global-apis/get_v2-client-personal-pages-search
nav_path:
- API Reference
- Client Side APIs
- Global APIs
- Find Personal Page
nav_order: 51
page_type: endpoint
endpoint: GET /v2/client/personal-pages/search
http_method: GET
endpoint_path: /v2/client/personal-pages/search
api_surface: client-side
auth: API key
tags:
- peer-to-peer
- search
crm_relevant: false
description: Search public CrowdChange personal fundraising pages by keyword and retrieve a paginated list of matches with goal, raised, and owner details.
retrieved: '2026-10-14'
word_count: 660
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/client-side/global-apis/get_v2-client-personal-pages-search | Nav: API Reference > Client Side APIs > Global APIs > Find Personal Page | Mirrored 2026-10-14 -->

# Find Personal Page

> Search public CrowdChange personal fundraising pages by keyword and retrieve a paginated list of matches with goal, raised, and owner details.

**Endpoint:** `GET /v2/client/personal-pages/search`  
**Surface:** Client Side API · **Auth:** API key — `Authorization: Bearer {api-key}` header  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Query parameters

- `text` (string, query) — Search term.
- `fundraiser_team_id` (integer, query) — Team id. Returns specific team if provided.
- `fundraisers` (string, query) — Comma separated list of fundraiser ids.
- `templates` (string, query) — Comma separated list of fundraiser template (blueprint) ids.
- `page` (integer, query) — Page number. Default: `1`
- `limit` (integer, query) — Number of results to return. Default: `10`
- `sort` (string, query) — Key to sort by. Allowed values: `name`, `amount_raised`, `amount_goal`
- `direction` (string, query) — Direction of sorting. Allowed values: `asc`, `desc`
- `lang` (string, query) — API's locale. Allowed values: `en`, `fr`
- `include_hidden` (integer, query) — Include personal pages from hidden campaigns. Default: `0`
- `include_subsites` (integer, query) — Include data from subsites. Default: `0`
- `include_description` (boolean, query) — Include the personal page description in the response. The returned `description` is plain text with all HTML removed and truncated to 200 characters. Default: `false`
- `amount_raised` (object, query) — Personal page's amount raised filter.

## Response

Returns an array of objects with the following fields.

- `id` (integer) — Personal page ID.
- `name` (string) — Personal page name.
- `description` (string) — Personal page description as plain text with all HTML removed, truncated to 200 characters. Only returned when `include_description` is set.
- `image` (string) — Personal page image ID
- `amount_goal` (number) — Goal amount.
- `amount_goal_formatted` (string) — Formatted goal amount of the personal page, includes currency symbol.
- `amount_raised` (number) — Amount raised by the personal page.
- `amount_raised_formatted` (string) — Formatted amount raised by the personal page, includes currency symbol.
- `n_donors` (number) — Number of donors
- `url` (string) — Full URL to personal page.
- `language` (string) — Personal page language. Allowed values: `en`, `fr`
- `team` (object) — Team name that personal page belongs to (if assigned to a team).
  - `id` (integer) — Team ID.
  - `name` (string) — Team name.
  - `amount_goal` (number) — Team's goal amount.
  - `amount_raised` (number) — Total amount raised by the team.
  - `amount_raised_formatted` (string) — Formatted amount raised by the team, includes currency symbol.
  - `url` (string) — Full URL to team's page.
  - `language` (string) — Team language. Allowed values: `en`, `fr`
- `fundraiser` (object) — Campaign that personal page belongs to.
  - `id` (integer) — Campaign ID.
  - `name` (string) — Campaign name.
  - `amount_goal` (number) — Campaign's goal amount.
  - `amount_raised` (number) — Total amount raised by the campaign.
  - `amount_raised_formatted` (string) — Formatted amount raised by the campaign, includes currency symbol.
  - `url` (string) — URL to campaign's page.
  - `language` (string) — Campaign language. Allowed values: `en`, `fr`
  - `organization` (object)
    - `id` (integer) — Campaign organization's ID
    - `name` (string) — Campaign organization's name
    - `custom_id` (string) — Campaign organization's Custom ID
  - `location_type` (string | null) — Campaign location type. Allowed values: `venue`, `online`, `other`.
  - `location` (string | null) — Campaign location details. For a `venue`, this contains venue details; for `online`, online-event details; for `other`, free-form location text.
  - `location_data` (object | null) — Structured location data. For `venue`, contains `address` and/or `geo`; for `online`, contains `link`; otherwise `null`. Missing nested fields are omitted.
- `user` (object)
  - `name` (string) — Personal page owner's name
  - `first_name` (string) — Personal page owner's first name
  - `last_name` (string) — Personal page owner's last name
  - `title` (string) — Personal page owner's title

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
    "name": "John Snow",
    "description": "Help us reach our goal and make a difference!",
    "image": "1eaf5ab2-5d55-11ee-82ef-001c42584fa2",
    "amount_goal": 1000,
    "amount_goal_formatted": "$1,000",
    "amount_raised": 550,
    "amount_raised_formatted": "$550",
    "n_donors": 10,
    "url": "https://demo.crowdchange.dev/2/page/1",
    "language": "en",
    "team": {
      "id": 1,
      "name": "Gala Night",
      "amount_goal": 10000,
      "amount_raised": 8000,
      "amount_raised_formatted": "$8,000",
      "url": "https://demo.crowdchange.dev/1/team/2",
      "language": "en"
    },
    "fundraiser": {
      "id": 1,
      "name": "Gala Night",
      "amount_goal": 10000,
      "amount_raised": 8000,
      "amount_raised_formatted": "$8,000",
      "url": "https://demo.crowdchange.dev/1",
      "language": "en",
      "organization": {
        "id": 1,
        "name": "Crowdchange",
        "custom_id": "CrowdchangeID"
      }
    },
    "user": {
      "name": "John Snow",
      "first_name": "John",
      "last_name": "Snow",
      "title": "Mr."
    }
  }
]
```

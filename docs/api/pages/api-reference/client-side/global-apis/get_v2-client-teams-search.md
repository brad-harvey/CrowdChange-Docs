---
title: Find Team
slug: api-reference/client-side/global-apis/get_v2-client-teams-search
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/client-side/global-apis/get_v2-client-teams-search
nav_path:
- API Reference
- Client Side APIs
- Global APIs
- Find Team
nav_order: 49
page_type: endpoint
endpoint: GET /v2/client/teams/search
http_method: GET
endpoint_path: /v2/client/teams/search
api_surface: client-side
auth: API key
tags:
- donations
- peer-to-peer
- search
- teams
crm_relevant: false
description: Search CrowdChange fundraising teams by keyword and retrieve a paginated list of matching teams with goal, raised amount, and campaign details.
retrieved: '2026-10-14'
word_count: 522
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/client-side/global-apis/get_v2-client-teams-search | Nav: API Reference > Client Side APIs > Global APIs > Find Team | Mirrored 2026-10-14 -->

# Find Team

> Search CrowdChange fundraising teams by keyword and retrieve a paginated list of matching teams with goal, raised amount, and campaign details.

**Endpoint:** `GET /v2/client/teams/search`  
**Surface:** Client Side API · **Auth:** API key — `Authorization: Bearer {api-key}` header  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Query parameters

- `text` (string, query) — Search term.
- `fundraiser_page_id` (integer, query) — Returns specific personal page if provided.
- `fundraiser_team_id` (integer, query) — ID of the team to filter by.
- `fundraisers` (string, query) — Comma separated list of fundraiser ids.
- `templates` (string, query) — Comma separated list of fundraiser template (blueprint) ids.
- `page` (integer, query) — Page number. Default: `1`
- `limit` (integer, query) — Number of results to return. Default: `10`
- `sort` (string, query) — Key to sort by. Allowed values: `name`, `amount_raised`, `amount_goal`
- `direction` (string, query) — Direction of sorting. Allowed values: `asc`, `desc`
- `lang` (string, query) — API's locale. Allowed values: `en`, `fr`
- `include_hidden` (integer, query) — Include teams from hidden campaigns. Default: `0`
- `include_subsites` (integer, query) — Include data from subsites. Default: `0`
- `amount_raised` (object, query) — Team's amount raised filter.

## Response

Returns an array of objects with the following fields.

- `id` (integer) — Team ID.
- `name` (string) — Team name.
- `description` (string) — Team description
- `image` (string) — Team image ID
- `amount_goal` (number) — Goal amount.
- `amount_goal_formatted` (string) — Formatted goal amount of the team, includes currency symbol.
- `amount_raised` (number) — Amount raised by the team.
- `amount_raised_formatted` (string) — Formatted amount raised by the team, includes currency symbol.
- `n_donors` (number) — Number of donors
- `url` (string) — URL to team's page.
- `language` (string) — Team language. Allowed values: `en`, `fr`
- `n_pages` (integer) — Number of pages.
- `fundraiser` (object) — Campaign that team belongs to.
  - `id` (integer) — Campaign ID.
  - `name` (string) — Campaign name.
  - `amount_goal` (number) — Campaign's goal amount.
  - `amount_raised` (number) — Total amount raised by the campaign.
  - `amount_raised_formatted` (string) — Formatted amount raised by the campaign, includes currency symbol.
  - `url` (string) — Full URL to campaign's page.
  - `language` (string) — Campaign language. Allowed values: `en`, `fr`
  - `organization` (object)
    - `id` (integer) — Campaign organization's ID
    - `name` (string) — Campaign organization's name
    - `custom_id` (string) — Campaign organization's Custom ID
  - `location_type` (string | null) — Campaign location type. Allowed values: `venue`, `online`, `other`.
  - `location` (string | null) — Campaign location details. For a `venue`, this contains venue details; for `online`, online-event details; for `other`, free-form location text.
  - `location_data` (object | null) — Structured location data. For `venue`, contains `address` and/or `geo`; for `online`, contains `link`; otherwise `null`. Missing nested fields are omitted.
- `user` (object)
  - `name` (string) — Team captain's name
  - `first_name` (string) — Team captain's first name
  - `last_name` (string) — Team captain's last name
  - `title` (string) — Team captain's title

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
    "name": "Team A",
    "description": "Team description",
    "image": "1eaf5ab2-5d55-11ee-82ef-001c42584fa2",
    "amount_goal": 1000,
    "amount_goal_formatted": "$1,000",
    "amount_raised": 550,
    "amount_raised_formatted": "$550",
    "n_donors": 10,
    "url": "https://demo.crowdchange.dev/1/team/2",
    "language": "en",
    "n_pages": 50,
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

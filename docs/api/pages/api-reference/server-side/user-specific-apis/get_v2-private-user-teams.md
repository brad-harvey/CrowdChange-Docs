---
title: Get Teams
slug: api-reference/server-side/user-specific-apis/get_v2-private-user-teams
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/user-specific-apis/get_v2-private-user-teams
nav_path:
- API Reference
- Server Side APIs
- User-Specific APIs
- Get Teams
nav_order: 26
page_type: endpoint
endpoint: GET /v2/private/user/teams
http_method: GET
endpoint_path: /v2/private/user/teams
api_surface: server-side
auth: API key + user token
tags:
- peer-to-peer
- teams
crm_relevant: true
description: Retrieve a paginated list of CrowdChange fundraising teams the authenticated user belongs to, including role, campaign, goal, and raised totals.
retrieved: '2026-10-14'
word_count: 568
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/user-specific-apis/get_v2-private-user-teams | Nav: API Reference > Server Side APIs > User-Specific APIs > Get Teams | Mirrored 2026-10-14 -->

# Get Teams

> Retrieve a paginated list of CrowdChange fundraising teams the authenticated user belongs to, including role, campaign, goal, and raised totals.

**Endpoint:** `GET /v2/private/user/teams`  
**Surface:** Server Side API (server-to-server only; never call from a browser) · **Auth:** API key + user token — `Authorization: Bearer {api-key}` header, plus the user token in the `auth-token` header or `token` param  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Query parameters

- `token` (string, query, **required**) — User's access token.
- `text` (string, query) — Search term.
- `page` (integer, query) — Page number. Default: `1`
- `limit` (integer, query) — Number of results to return. Default: `10`
- `sort` (string, query) — Key to sort by. Allowed values: `name`, `amount_raised`, `amount_goal`
- `direction` (string, query) — Direction of sorting. Allowed values: `asc`, `desc`
- `lang` (string, query) — API's locale. Allowed values: `en`, `fr`

## Response

- `id` (integer) — Team ID.
- `name` (string) — Team name.
- `type` (string) — Team type.
- `url` (string | null) — URL to the team's page.
- `amount_goal` (number) — Goal amount.
- `amount_goal_formatted` (string) — Formatted goal amount, including the currency symbol.
- `amount_raised` (number) — Amount raised by the team.
- `amount_raised_formatted` (string) — Formatted amount raised by the team, including the currency symbol.
- `amount_pledged` (number) — Pending offline donation amount for the team.
- `amount_matched` (number) — Team matched donation amount.
- `n_donors` (integer) — Number of team donors.
- `n_pages` (integer) — Number of personal pages on the team.
- `images` (object)
  - `original` (string) — URL to the original team image.
- `image` (string | null) — Team image ID.
- `description` (string | null) — Team description.
- `is_default_image` (boolean) — Whether the team image is inherited from the campaign.
- `is_default_description` (boolean) — Whether the team description is inherited from the campaign.
- `created_at` (string | null) — Team creation date and time.
- `language` (string) — Team language. Allowed values: `en`, `fr`.
- `custom_data` (object[]) — Custom questions and responses configured for the resource.
  - `field_id` (integer) — Custom field ID.
  - `source_id` (integer | null) — Source field ID when the field was copied from a Blueprint.
  - `name` (string) — Custom field label.
  - `content` (string | null) — Formatted response to the custom field.
  - `field_custom_id` (string | null) — Custom ID for the field.
  - `response_custom_id` (string | null) — Custom ID for the selected response, when applicable.
- `user` (object) — Team owner.
  - `id` (integer) — User ID.
  - `name` (string) — User name.
  - `email` (string) — User email.
  - `contact_email` (string) — User contact email.
  - `first_name` (string) — User first name.
  - `last_name` (string) — User last name.
  - `title` (string) — User title.
- `fundraiser` (object) — Campaign summary.
  - `id` (integer) — Campaign ID.
  - `name` (string) — Campaign name.
  - `url` (string | null) — URL to the campaign.
  - `amount_goal` (number) — Campaign goal amount.
  - `amount_raised` (number) — Total amount raised by the campaign.
  - `amount_raised_formatted` (string) — Formatted amount raised by the campaign.
  - `language` (string) — Campaign language.
  - `tags_list` (any[]) — Campaign tags.
  - `organization` (object | null) — Campaign organization, when applicable.

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
    "amount_raised": 550,
    "amount_raised_formatted": "$550",
    "n_pages": 5,
    "url": "https://demo.crowdchange.dev/1/team/2",
    "language": "en",
    "custom_data": [
      {
        "field_id": 1001,
        "source_id": 11,
        "name": "Phone Number",
        "content": "555-123-4567",
        "field_custom_id": "ABC-123",
        "response_custom_id": null
      }
    ],
    "is_default_image": false,
    "is_default_description": false,
    "images": {
      "original": "https://img.crowdchange.co/files/abc.png?tr=w-[width],h-[height]"
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
      "id": 1,
      "contact_email": "john@example.com",
      "name": "John Snow",
      "first_name": "John",
      "last_name": "Snow",
      "title": "Mr."
    }
  }
]
```

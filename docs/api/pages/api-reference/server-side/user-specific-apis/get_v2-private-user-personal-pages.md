---
title: Get Personal Pages
slug: api-reference/server-side/user-specific-apis/get_v2-private-user-personal-pages
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/user-specific-apis/get_v2-private-user-personal-pages
nav_path:
- API Reference
- Server Side APIs
- User-Specific APIs
- Get Personal Pages
nav_order: 25
page_type: endpoint
endpoint: GET /v2/private/user/personal-pages
http_method: GET
endpoint_path: /v2/private/user/personal-pages
api_surface: server-side
auth: API key + user token
tags:
- peer-to-peer
crm_relevant: true
description: Retrieve a paginated list of the authenticated user's personal fundraising pages across all CrowdChange campaigns, with goals and raised amounts.
retrieved: '2026-10-14'
word_count: 690
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/user-specific-apis/get_v2-private-user-personal-pages | Nav: API Reference > Server Side APIs > User-Specific APIs > Get Personal Pages | Mirrored 2026-10-14 -->

# Get Personal Pages

> Retrieve a paginated list of the authenticated user's personal fundraising pages across all CrowdChange campaigns, with goals and raised amounts.

**Endpoint:** `GET /v2/private/user/personal-pages`  
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

- `id` (integer) — Personal page ID.
- `name` (string) — Personal page name.
- `type` (string) — Personal page type.
- `url` (string | null) — URL to the personal page.
- `amount_goal` (number) — Goal amount.
- `amount_goal_formatted` (string) — Formatted goal amount, including the currency symbol.
- `amount_raised` (number) — Amount raised by the personal page.
- `amount_raised_formatted` (string) — Formatted amount raised by the personal page, including the currency symbol.
- `amount_pledged` (number) — Pending offline donation amount for the personal page.
- `amount_matched` (number) — Personal page matched donation amount.
- `n_donors` (integer) — Number of personal page donors.
- `images` (object)
  - `original` (string) — URL to the original personal page image.
- `image` (string | null) — Personal page image ID.
- `description` (string | null) — Personal page description.
- `is_default_image` (boolean) — Whether the personal page image is inherited from the campaign.
- `is_default_description` (boolean) — Whether the personal page description is inherited from the campaign.
- `registrant` (object | null) — Registrant details, when available.
  - `first_name` (string) — Registrant first name.
  - `last_name` (string) — Registrant last name.
- `archived_at` (string | null) — Personal page archive date and time.
- `closed_at` (string | null) — Personal page close date and time.
- `created_at` (string | null) — Personal page creation date and time.
- `language` (string) — Personal page language. Allowed values: `en`, `fr`.
- `custom_data` (object[]) — Custom questions and responses configured for the resource.
  - `field_id` (integer) — Custom field ID.
  - `source_id` (integer | null) — Source field ID when the field was copied from a Blueprint.
  - `name` (string) — Custom field label.
  - `content` (string | null) — Formatted response to the custom field.
  - `field_custom_id` (string | null) — Custom ID for the field.
  - `response_custom_id` (string | null) — Custom ID for the selected response, when applicable.
- `user` (object) — Personal page owner.
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
- `team` (object | null) — Team summary, when the personal page belongs to a team.
  - `id` (integer) — Team ID.
  - `name` (string) — Team name.
  - `url` (string | null) — URL to the team page.
  - `amount_goal` (number) — Team goal amount.
  - `amount_goal_formatted` (string) — Formatted team goal amount.
  - `amount_raised` (number) — Total amount raised by the team.
  - `amount_raised_formatted` (string) — Formatted amount raised by the team.
  - `language` (string) — Team language.

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
    "description": "Personal page description",
    "image": "1eaf5ab2-5d55-11ee-82ef-001c42584fa2",
    "amount_goal": 1000,
    "amount_raised": 550,
    "amount_raised_formatted": "$550",
    "n_donors": 10,
    "url": "https://demo.crowdchange.dev/2/page/1",
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

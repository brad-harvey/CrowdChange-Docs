---
title: Get Campaigns
slug: api-reference/server-side/user-specific-apis/get_v2-private-user-fundraisers
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/user-specific-apis/get_v2-private-user-fundraisers
nav_path:
- API Reference
- Server Side APIs
- User-Specific APIs
- Get Campaigns
nav_order: 24
page_type: endpoint
endpoint: GET /v2/private/user/fundraisers
http_method: GET
endpoint_path: /v2/private/user/fundraisers
api_surface: server-side
auth: API key + user token
tags:
- registration
crm_relevant: true
description: Retrieve a paginated list of CrowdChange campaigns where the authenticated user is registered, including role, goal, and amount raised per campaign.
retrieved: '2026-10-14'
word_count: 646
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/user-specific-apis/get_v2-private-user-fundraisers | Nav: API Reference > Server Side APIs > User-Specific APIs > Get Campaigns | Mirrored 2026-10-14 -->

# Get Campaigns

> Retrieve a paginated list of CrowdChange campaigns where the authenticated user is registered, including role, goal, and amount raised per campaign.

**Endpoint:** `GET /v2/private/user/fundraisers`  
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

- `id` (integer) — Campaign ID.
- `partner_id` (integer) — Site ID.
- `name` (string) — Campaign name.
- `description` (string | null) — Campaign description.
- `url` (string | null) — Full URL to the campaign.
- `amount_goal` (number) — Goal amount.
- `amount_goal_formatted` (string) — Formatted goal amount, including the currency symbol.
- `amount_raised` (number) — Amount raised by the campaign.
- `amount_raised_formatted` (string) — Formatted amount raised by the campaign, including the currency symbol.
- `goal_type` (string) — Campaign goal type.
- `amount_pledged` (number) — Pending offline donation amount attributed to the campaign.
- `amount_matched` (number) — Amount contributed by donation matching assigned directly to the campaign.
- `n_donors` (integer) — Number of donors.
- `n_teams` (integer) — Number of teams in the campaign.
- `n_pages` (integer) — Number of personal pages in the campaign.
- `images` (object)
  - `original` (string) — URL to the original campaign image.
- `image` (string | null) — Campaign image ID.
- `start_at` (string | null) — Campaign start date and time.
- `end_at` (string | null) — Campaign end date and time.
- `language` (string) — Campaign language. Allowed values: `en`, `fr`.
- `tags_list` (any[]) — Campaign tags.
- `custom_data` (object[]) — Custom questions and responses configured for the resource.
  - `field_id` (integer) — Custom field ID.
  - `source_id` (integer | null) — Source field ID when the field was copied from a Blueprint.
  - `name` (string) — Custom field label.
  - `content` (string | null) — Formatted response to the custom field.
  - `field_custom_id` (string | null) — Custom ID for the field.
  - `response_custom_id` (string | null) — Custom ID for the selected response, when applicable.
- `created_at` (string | null) — Campaign creation date and time.
- `user` (object) — Campaign owner.
  - `id` (integer) — User ID.
  - `name` (string) — User name.
  - `email` (string) — User email.
  - `contact_email` (string) — User contact email.
  - `first_name` (string) — User first name.
  - `last_name` (string) — User last name.
  - `title` (string) — User title.
- `organization` (object | null) — Campaign organization, when applicable.
  - `id` (integer) — Organization ID.
  - `name` (string) — Organization name.
  - `custom_id` (string) — Organization custom ID.
- `closed_at` (string | null) — Campaign close date and time.
- `is_hidden` (boolean) — Whether the campaign is hidden.
- `fundraiser_template` (object | null) — Campaign template summary, when applicable.
  - `id` (integer) — Template ID.
  - `name` (string) — Template name.
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
    "partner_id": 10,
    "name": "Campaign",
    "description": "Description",
    "amount_goal": 1000,
    "amount_goal_formatted": "$1,000",
    "amount_raised": 550,
    "amount_raised_formatted": "$550",
    "amount_pledged": 125,
    "amount_matched": 50,
    "goal_type": "amount",
    "n_donors": 10,
    "url": "https://demo.crowdchange.dev/2",
    "language": "en",
    "start_at": "2022-01-01 16:00:03",
    "end_at": "2022-01-02 16:00:03",
    "tags_list": ["tag1", "tag2"],
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
    "is_hidden": false,
    "closed_at": "2022-03-01 00:00:00",
    "user": {
      "id": 1,
      "name": "John Snow",
      "first_name": "John",
      "last_name": "Snow",
      "title": "Mr.",
      "email": "john@crowdchange.co",
      "contact_email": "john@crowdchange.co"
    },
    "organization": {
      "id": 1,
      "name": "Crowdchange",
      "custom_id": "CrowdchangeID"
    },
    "images": {
      "original": "https://img.crowdchange.co/files/abc.png?tr=w-[width],h-[height]"
    }
  }
]
```

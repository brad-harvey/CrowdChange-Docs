---
title: Get Campaign
slug: api-reference/server-side/campaign-specific-apis/get_v2-private-fundraiser-id
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/campaign-specific-apis/get_v2-private-fundraiser-id
nav_path:
- API Reference
- Server Side APIs
- Campaign-Specific APIs
- Get Campaign
nav_order: 16
page_type: endpoint
endpoint: GET /v2/private/fundraiser/{id}
http_method: GET
endpoint_path: /v2/private/fundraiser/{id}
api_surface: server-side
auth: API key
tags:
- donations
crm_relevant: true
description: Retrieve detailed server-side information about a CrowdChange campaign by its fundraiser ID, including configuration, goal, raised, and donor stats.
retrieved: '2026-10-14'
word_count: 587
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/campaign-specific-apis/get_v2-private-fundraiser-id | Nav: API Reference > Server Side APIs > Campaign-Specific APIs > Get Campaign | Mirrored 2026-10-14 -->

# Get Campaign

> Retrieve detailed server-side information about a CrowdChange campaign by its fundraiser ID, including configuration, goal, raised, and donor stats.

**Endpoint:** `GET /v2/private/fundraiser/{id}`  
**Surface:** Server Side API (server-to-server only; never call from a browser) · **Auth:** API key — `Authorization: Bearer {api-key}` header  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Path parameters

- `id` (integer, path, **required**) — Fundraiser ID.

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
| `401` | Unauthorized |
| `403` | Forbidden |

**Response example:**

```json
{
  "id": 1,
  "partner_id": 10,
  "name": "Campaign",
  "description": "Description",
  "created_at": "2022-01-01 16:00:03",
  "amount_goal": 1000,
  "amount_goal_formatted": "$1,000",
  "amount_raised": 550,
  "amount_raised_formatted": "$550",
  "goal_type": "amount",
  "amount_pledged": 125,
  "amount_matched": 50,
  "url": "https://demo.crowdchange.dev/2",
  "n_donors": 100,
  "n_teams": 5,
  "n_pages": 20,
  "images": {
    "original": "https://img.crowdchange.co/files/campaign.png"
  },
  "image": "campaign-image-id",
  "language": "en",
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
  "closed_at": null,
  "is_hidden": false,
  "fundraiser_template": {
    "id": 1,
    "name": "Template"
  },
  "start_at": "2022-01-01 16:00:03",
  "end_at": "2022-01-02 16:00:03",
  "tags_list": [
    "tag1",
    "tag2"
  ],
  "custom_data": [
    {
      "field_id": 1001,
      "source_id": 11,
      "name": "Phone Number",
      "content": "555-123-4567",
      "field_custom_id": "ABC-123",
      "response_custom_id": null
    }
  ]
}
```

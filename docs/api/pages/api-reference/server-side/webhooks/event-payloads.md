---
title: Event payloads
slug: api-reference/server-side/webhooks/event-payloads
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/webhooks/event-payloads
nav_path:
- API Reference
- Server Side APIs
- Webhook Reference
- Event payloads
nav_order: 42
page_type: reference
endpoint: null
http_method: null
endpoint_path: null
api_surface: server-side
auth: null
tags:
- webhooks
crm_relevant: true
description: Reference the JSON payloads sent by CrowdChange webhook events.
retrieved: '2026-10-14'
word_count: 1980
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/webhooks/event-payloads | Nav: API Reference > Server Side APIs > Webhook Reference > Event payloads | Mirrored 2026-10-14 -->

# Event payloads

> Reference the JSON payloads sent by CrowdChange webhook events.

CrowdChange sends webhook deliveries as JSON with an `event` name and event-specific `data`.
The same object is stored on webhook logs as `payload`. Events are delivered to subscribed webhooks for the campaign's partner and, when applicable, its distinct parent partner.

```json
{
  "event": "transaction_created",
  "data": {}
}
```

## Updated event changes

The `fundraiser_updated`, `fundraiser_team_updated`, and `fundraiser_page_updated` events include a `changes` object in `data`.

- `changes` (object) — Changed fields keyed by dot notation. Each changed field contains `old` and `new` values.

```json
{
  "changes": {
    "name": {
      "old": "Old campaign name",
      "new": "New campaign name"
    }
  }
}
```

## Deleted event details

The `fundraiser_deleted`, `fundraiser_team_deleted`, and `fundraiser_page_deleted` events include the deleted entity's usual fields plus `deleted_at` in `YYYY-MM-DD HH:mm:ss` format.

When deleting a team also deletes its personal pages, each deleted page produces a `fundraiser_page_deleted` event. Pages moved back to the campaign remain active and do not produce a deletion event.

This example shows only the deletion fields; the other campaign fields are described below.

```json
{
  "event": "fundraiser_deleted",
  "data": {
    "id": 1001,
    "deleted_at": "2026-10-07 16:00:03"
  }
}
```

## Campaign events

Events: `fundraiser_created`, `fundraiser_updated`, `fundraiser_deleted`

- `data` (object) — Campaign details.
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
  - `changes` (object) — Included on `fundraiser_updated` events.
  - `deleted_at` (string | null) — Included on `fundraiser_deleted` events. Deletion date and time in `YYYY-MM-DD HH:mm:ss` format.

## Transaction events

Events: `transaction_created`, `transaction_refunded`

- `data` (object) — Transaction details.
  - `id` (integer) — Transaction ID.
  - `ref_id` (string) — Transaction reference ID.
  - `amount` (number) — Transaction total amount. On refund records, this is the amount of this refund. Returned money is negative; a return that moves no money, such as a donation-match-only return, can have an amount of zero.
  - `currency` (string) — Transaction currency.
  - `currency_symbol` (string) — Transaction currency symbol.
  - `frequency` (string) — Donation frequency.
  - `fundraiser_id` (integer) — Campaign ID.
  - `parent_id` (integer | null) — Parent transaction ID, when applicable. For a refund, this is the original payment ID.
  - `fundraiser_page_id` (integer | null) — Personal page ID, when applicable.
  - `fundraiser_team_id` (integer | null) — Team ID, when applicable.
  - `organization_id` (integer | null) — Organization ID, when applicable.
  - `fundraiser_name` (string) — Campaign name.
  - `organization_name` (string | null) — Organization name, when applicable.
  - `organization_code` (string | null) — Organization custom ID, when applicable.
  - `user_id` (integer) — Donor user ID.
  - `email` (string) — Donor email.
  - `mail` (object | null) — Mailing address when a receipt is mailed.
  - `statement_descriptor` (string | null) — Payment statement descriptor.
  - `summary` (object) — Transaction amount breakdown.
  - `upsell` (object | null) — Upsell details, when applicable.
  - `promo_code` (string | null) — Applied promo code, when applicable.
  - `billing_address` (object | null) — Billing address.
  - `dtd` (object | null) — Dedication or tribute data, when applicable.
  - `created_at` (string) — Transaction creation date and time.
  - `status` (string) — Transaction status. Refund records use `refunded`.
  - `is_refunded` (boolean) — Whether CrowdChange has marked this transaction as fully refunded. Use `status` to identify a refund record.
  - `parent` (object) — Included only when `status` is `refunded` and `parent_id` is set. Contains the original payment using the same transaction fields. Its `id` matches `parent_id`.
  - `tickets` (object[]) — Assigned tickets, when applicable.

### Full and partial refunds

`transaction_refunded` is sent when a refund transaction is created in CrowdChange, for both full and partial refunds. Each refund has its own `data.id`. Successive partial refunds share the original payment's `parent_id`; `data.amount` represents only the current refund, not the cumulative refunded amount.

`data.parent` keeps the original payment's amount and status. Its `is_refunded` field exposes CrowdChange's stored full-refund flag. A partial refund can have `data.status: "refunded"` while `data.parent.is_refunded` is `false`. The payload does not calculate a remaining balance.

The standard refund processing flow also emits the existing `transaction_created` event for the same refund record, including `parent`. If you subscribe to both events, use the refund's `data.id` to avoid counting the same refund twice.

These separate examples show only the fields relevant to refunds. Both `data` and `data.parent` also include the other transaction fields above.

**Full refund**

```json
{
  "event": "transaction_refunded",
  "data": {
    "id": 6002,
    "amount": -100,
    "parent_id": 6001,
    "status": "refunded",
    "is_refunded": false,
    "parent": {
      "id": 6001,
      "amount": 100,
      "parent_id": null,
      "status": "completed",
      "is_refunded": true
    }
  }
}
```

**Partial refund**

```json
{
  "event": "transaction_refunded",
  "data": {
    "id": 6003,
    "amount": -25,
    "parent_id": 6001,
    "status": "refunded",
    "is_refunded": false,
    "parent": {
      "id": 6001,
      "amount": 100,
      "parent_id": null,
      "status": "completed",
      "is_refunded": false
    }
  }
}
```

## Team events

Events: `fundraiser_team_created`, `fundraiser_team_updated`, `fundraiser_team_deleted`

- `data` (object) — Team details.
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
  - `changes` (object) — Included on `fundraiser_team_updated` events.
  - `deleted_at` (string | null) — Included on `fundraiser_team_deleted` events. Deletion date and time in `YYYY-MM-DD HH:mm:ss` format.

## Personal page events

Events: `fundraiser_page_created`, `fundraiser_page_updated`, `fundraiser_page_deleted`

- `data` (object) — Personal page details.
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
  - `changes` (object) — Included on `fundraiser_page_updated` events.
  - `deleted_at` (string | null) — Included on `fundraiser_page_deleted` events. Deletion date and time in `YYYY-MM-DD HH:mm:ss` format.

## Tax receipt events

Events: `tax_receipt_issued`

- `data` (object) — Tax receipt details.
  - `id` (integer) — Tax receipt ID.
  - `transaction_id` (integer) — Transaction ID.
  - `amount_donation` (number) — Donation amount.
  - `amount_benefit` (number) — Benefit amount.
  - `amount_eligible` (number) — Tax-eligible amount.
  - `business_name` (string | null) — Business name, when applicable.
  - `name_on_receipt` (string) — Name printed on the receipt.
  - `issued_on` (string) — Receipt issue date and time.
  - `receipt_number` (string) — Receipt number.
  - `status` (string) — Receipt status. Values are `valid` or `cancelled`.
  - `first_name` (string) — Recipient first name.
  - `last_name` (string) — Recipient last name.
  - `title` (string | null) — Recipient title.
  - `email` (string) — Recipient email.
  - `street_address` (string) — Recipient street address.
  - `state` (string) — Recipient state or province.
  - `country` (string) — Recipient country.
  - `postal` (string) — Recipient postal code.
  - `city` (string) — Recipient city.

## Milestone events

Events: `milestone_triggered`

Sent when a milestone notification is triggered for the original recipient. Additional recipient emails configured on the milestone are not included in the webhook payload.

- `data` (object) — Milestone details.
  - `id` (integer) — Milestone log ID.
  - `mail_template_id` (integer) — Mail template ID.
  - `template_name` (string) — Mail template name.
  - `type` (string) — Mail template type.
  - `trigger_id` (string) — Milestone trigger identifier.
  - `trigger_group` (string) — Trigger recipient group.
  - `trigger_type` (string) — Trigger value type, such as `amount` or `percent`.
  - `trigger_value` (string) — Configured milestone trigger value.
  - `trigger_data` (object) — Additional trigger data. Additional recipient emails are excluded.
  - `queued_at` (string) — Date and time the notification was queued.
  - `recipient` (object) — Original milestone recipient.
  - `fundraiser` (object) — Campaign summary.
  - `fundraiser_team` (object | null) — Team that reached the milestone, when applicable.
  - `fundraiser_page` (object | null) — Personal page that reached the milestone, when applicable.

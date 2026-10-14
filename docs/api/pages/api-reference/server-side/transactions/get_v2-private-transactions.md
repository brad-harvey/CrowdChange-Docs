---
title: Get All
slug: api-reference/server-side/transactions/get_v2-private-transactions
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/transactions/get_v2-private-transactions
nav_path:
- API Reference
- Server Side APIs
- Transactions
- Get All
nav_order: 12
page_type: endpoint
endpoint: GET /v2/private/transactions
http_method: GET
endpoint_path: /v2/private/transactions
api_surface: server-side
auth: API key
tags:
- donations
- payments-and-receipts
- transactions
crm_relevant: true
description: Retrieve all CrowdChange transactions within a time window or by payout ID, with full payment processor, donor, and campaign attribution details.
retrieved: '2026-10-14'
word_count: 4613
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/transactions/get_v2-private-transactions | Nav: API Reference > Server Side APIs > Transactions > Get All | Mirrored 2026-10-14 -->

# Get All

> Retrieve all CrowdChange transactions within a time window or by payout ID, with full payment processor, donor, and campaign attribution details.

**Endpoint:** `GET /v2/private/transactions`  
**Surface:** Server Side API (server-to-server only; never call from a browser) · **Auth:** API key — `Authorization: Bearer {api-key}` header  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Query parameters

- `after` (integer, query) — Retrieve transactions after this ID.
- `dt_start` (string, query) — End date in the ISO 8601 format `yyyy-mm-ddThh:mm:ss` (UTC timezone). Retrieves transactions that were made on or after of provided date (UTC).
- `dt_end` (string, query) — End date in the ISO 8601 format `yyyy-mm-ddThh:mm:ss` (UTC timezone). Retrieves transactions that were made on or before of provided date (UTC).
- `payout_account` (string, query) — Payout account - can either be `global` or `user`. Returns transactions that were paid out to specified account. Allowed values: `global`, `user`
- `payout_dt` (string, query) — Payout date in the format `YYYY-MM-DD`. Retrieves transactions that were paid out on provided date. When provided, start and end dates have no effect.
- `fundraisers` (string, query) — Comma separated list of fundraiser ids.
- `page` (integer, query) — Page number. Default: `1`
- `limit` (integer, query) — Number of results to return. Default: `100`
- `sort` (string, query, default: `id`) — Sort key. Allowed values: `id`, `date` Default: `id`
- `direction` (string, query, default: `asc`) — Sort direction. Allowed values: `asc`, `desc` Default: `asc`
- `exclude_subsites` (integer, query) — Exclude subsite transactions. Default: `0`
- `include_pending` (integer, query) — Include pending transactions. Default: `0`
- `tags[]` (string[], query) — List of fundraiser tags.

## Response

- `dt_start` (string) — Start date.
- `dt_end` (string) — End date.
- `count` (integer) — Number of transactions returned.
- `data` (object[]) — List of transactions.
  - `id` (integer) — Transaction ID.
  - `type` (string) — Transaction Type. Allowed values: `charge`, `refund`
  - `status` (string) — Transaction Status. Allowed values: `completed`, `refunded`, `pending`
  - `refund_children_ids` (any[]) — List of transaction refund IDs of current transaction. Presented if transaction has refunds.
  - `parent_id` (integer) — Parent Transaction ID. Presented if current transaction is refund transaction.
  - `partner_id` (integer) — Site ID.
  - `promo_code` (string) — Promo Code.
  - `amount` (object) — Summary of collected funds for transaction.
    - `apparel` (number) — Total amount paid for apparel / merchandise.
    - `covered_fees` (number) — Amount that user paid to help cover transaction fees.
    - `currency` (string) — Currency code. Allowed values: `CAD`, `USD`, `AUD`, `EUR`
    - `donation` (number) — Donation amount.
    - `donation_to_pages` (number) — Donation amount to personal pages (multi-registration).
    - `ecards` (number) — Total amount paid for ecards.
    - `is_recurring` (boolean) — Is this a recurring transaction?
    - `registration` (number) — Total amount paid for registration.
    - `sponsorship` (number) — Total amount paid for sponsorship.
    - `tickets` (number) — Total amount paid for tickets.
    - `total_net` (number) — Total net amount for transaction (after all fees).
    - `total_paid` (number) — Total amount paid by user.
    - `custom_fees` (number) — Total amount paid for custom fees.
  - `billing` (object) — User's billing information.
    - `business_name` (string) — Business name.
    - `is_foundation` (boolean) — Is this transaction made by foundation?
    - `title` (string) — Honorific (i.e. Mr / Miss / etc).
    - `name` (string) — Full user name including honorific.
    - `first_name` (string) — User's first name.
    - `last_name` (string) — User's last name.
    - `street_address` (string) — Street name and number.
    - `city` (string) — City name.
    - `country` (string) — Country code.
    - `state` (string) — State or province..
    - `postal` (string) — ZIP or Postal Code.
    - `email` (string) — User's email address.
    - `phone` (string) — Phone number.
  - `donated_by` (object) — Donor's information.
    - `business_name` (string) — Business name.
    - `title` (string) — Honorific (i.e. Mr / Miss / etc).
    - `name` (string) — Full user name including honorific.
    - `first_name` (string) — User's first name.
    - `last_name` (string) — User's last name.
    - `street_address` (string) — Street name and number.
    - `city` (string) — City name.
    - `country` (string) — Country code.
    - `state` (string) — State or province..
    - `postal` (string) — ZIP or Postal Code.
    - `email` (string) — User's email address.
    - `is_foundation` (boolean) — Is this transaction made by foundation?
    - `user_id` (integer) — User's ID.
    - `phone` (string) — Phone number.
  - `mailing_address` (object) — User's mailing information.
    - `business_name` (string) — Business name.
    - `is_foundation` (boolean) — Is this transaction made by foundation?
    - `title` (string) — Honorific (i.e. Mr / Miss / etc).
    - `name` (string) — Full user name including honorific.
    - `first_name` (string) — User's first name.
    - `last_name` (string) — User's last name.
    - `street_address` (string) — Street name and number.
    - `city` (string) — City name.
    - `country` (string) — Country code.
    - `state` (string) — State or province..
    - `postal` (string) — ZIP or Postal Code.
    - `phone` (string) — Phone number.
  - `card_type` (string) — Debit or credit card type used for transaction.
  - `payment_processor` (string) — Payment processor used for transaction.
  - `processor_transaction_id` (string) — Payment processor's ID.
  - `ref_source` (string | null) — Reference source associated with the transaction, when one was provided.
  - `custom_data` (object[]) — List of custom questions and responses.
    - `field_id` (integer) — Custom field id.
    - `source_id` (integer) — If field was copied from Blueprint, this will reference the source field id from blueprint (similar to group id).
    - `name` (string) — Custom field label.
    - `content` (string) — User's answer to custom field.
    - `field_custom_id` (string) — Custom ID.
    - `response_custom_id` (string) — Custom ID for the response (multiple choice questions).
  - `date` (string) — Date of transaction in format `YYYY-MM-DD HH:MM:SS`.
  - `donation_comment` (string) — Public comment left by user.
  - `fundraiser` (object) — Campaign for which transaction was made.
    - `id` (integer) — Fundraiser ID.
    - `partner_id` (integer) — Site ID.
    - `fundraiser_template_id` (integer) — Template ID.
    - `fundraiser_template` (object) — Template associated with the campaign.
      - `id` (integer) — Template ID.
      - `name` (string) — Template name.
    - `name` (string) — Name of campaign.
    - `dt_start` (string) — Date and time when campaign starts.
    - `dt_end` (string) — Date and time when campaign ends.
    - `location_type` (string | null) — Campaign location type. Allowed values: `venue`, `online`, `other`.
    - `location` (string | null) — Display location. Uses the legacy event address when no display value exists.
    - `location_details` (string | null) — Location instructions or free-form text stored on the campaign.
    - `location_data` (object | null) — Structured location data. For `venue`, contains `address` and/or `geo`; for `online`, contains `link`; otherwise `null`. Missing nested fields are omitted.
    - `goal` (number) — Fundraiser goal. This can be either dollars or number of participants.
    - `campus` (string) — Campus associated with campaign.
    - `national_office` (string) — National Office associated with campaign.
    - `chapter` (string) — Chapter associated with campaign.
    - `chapter_custom_id` (string) — Custom ID provided for chapter.
    - `organization` (string) — Organization associated with campaign.
    - `in_support_name` (string) — Value of `In support of` field associated with campaign.
    - `in_support_code` (string) — Code provided for `In support of` field.
    - `appeal_code` (string) — Appeal code.
    - `language` (string) — Campaign language. Allowed values: `en`, `fr`
    - `custom_data` (object[]) — List of custom questions and responses.
      - `field_id` (integer) — Custom field id.
      - `source_id` (integer) — If field was copied from Blueprint, this will reference the source field id from blueprint (similar to group id).
      - `name` (string) — Custom field label.
      - `content` (string) — User's answer to custom field.
      - `field_custom_id` (string) — Custom ID.
      - `response_custom_id` (string) — Custom ID for the response (multiple choice questions).
    - `user` (object)
      - `id` (integer) — Fundraiser owner's ID
      - `email` (string) — Fundraiser owner's email
      - `first_name` (string) — Fundraiser owner's first name
      - `last_name` (string) — Fundraiser owner's last name
      - `title` (string) — Fundraiser owner's title
      - `name` (string) — Fundraiser owner's name
    - `tags_list` (any[]) — Campaign tags.
  - `fundraiser_team` (object) — Team through which transaction was made.
    - `id` (integer) — Team ID.
    - `partner_id` (integer) — Site ID.
    - `fundraiser_id` (integer) — Fundraiser ID. When cross-fundraiser teams are enabled, this maybe different from transaction's fundraiser id.
    - `name` (string) — Team name.
    - `goal` (number) — Team goal.
    - `url` (string) — Team url.
    - `user` (object) — User that created the team (team captain).
      - `id` (integer) — User ID.
      - `first_name` (string) — User's first name.
      - `last_name` (string) — User's last name.
      - `email` (string) — User's email address.
      - `language` (string) — User's preferred language. Allowed values: `en`, `fr`
      - `title` (string) — User's title
      - `name` (string) — User's name
    - `custom_data` (object[]) — List of custom questions and responses.
      - `field_id` (integer) — Custom field id.
      - `source_id` (integer) — If field was copied from Blueprint, this will reference the source field id from blueprint (similar to group id).
      - `name` (string) — Custom field label.
      - `content` (string) — User's answer to custom field.
      - `field_custom_id` (string) — Custom ID.
      - `response_custom_id` (string) — Custom ID for the response (multiple choice questions).
  - `fundraiser_user_page` (object) — Personal page through which transaction was made.
    - `id` (integer) — Personal page ID.
    - `partner_id` (integer) — Site ID.
    - `name` (string) — Personal page name.
    - `first_name` (string) — First name of personal page's owner.
    - `last_name` (string) — Last name of personal page's owner.
    - `user_name` (string) — Full name of personal page's owner.
    - `title` (string) — Honorific of personal page's owner (i.e. Mr / Miss / etc).
    - `goal` (number) — Personal page goal.
    - `url` (string) — Personal page url.
    - `language` (string) — Personal page language. Allowed values: `en`, `fr`
    - `custom_data` (object[]) — List of custom questions and responses.
      - `field_id` (integer) — Custom field id.
      - `source_id` (integer) — If field was copied from Blueprint, this will reference the source field id from blueprint (similar to group id).
      - `name` (string) — Custom field label.
      - `content` (string) — User's answer to custom field.
      - `field_custom_id` (string) — Custom ID.
      - `response_custom_id` (string) — Custom ID for the response (multiple choice questions).
  - `is_disputed` (boolean) — True if transaction was disputed, otherwise false.
  - `is_refunded` (boolean) — True if transaction was refunded, otherwise false.
  - `is_pending` (boolean) — True if transaction is pending.
  - `is_tax_receipt_issued` (boolean) — True if tax receipt was issued for this transaction.
  - `tax_receipt` (object) — Tax receipt information.
    - `id` (integer) — Unique id.
    - `amount_donation` (number) — Total donation amount.
    - `amount_benefit` (number) — Benefit amount.
    - `amount_eligible` (number) — Eligible amount.
    - `business_name` (string) — Business name.
    - `name_on_receipt` (string) — Name on receipt.
    - `issued_on` (string) — Date when the tax receipt was issued.
    - `receipt_number` (string) — Tax receipt number
    - `status` (string) — Status of tax receipt. Allowed values: `valid`, `cancelled`
    - `title` (string) — Honorific (i.e. Mr / Miss / etc).
    - `first_name` (string) — First name.
    - `last_name` (string) — Last name.
    - `street_address` (string) — Street name and number.
    - `city` (string) — City name.
    - `country` (string) — Country code.
    - `state` (string) — State or province..
    - `postal` (string) — ZIP or Postal Code.
    - `email` (string) — Email address.
    - `user_id` (integer) — User's ID.
    - `transaction_id` (integer) — Transaction's ID.
  - `recurring` (object) — Information about recurring donation.
    - `id` (integer) — Unique id.
    - `amount` (integer) — Recurring amount to be charged.
    - `amount_net` (integer) — Expected net amount.
    - `interval` (string) — Frequency. Allowed values: `month`, `year`
    - `day` (integer) — Day of the month when the charge will be processed.
    - `month` (integer) — Month of the year when the charge will be processed (for annual donations).
    - `status` (string) — Subscription status. Allowed values: `active`, `cancelled`, `paused`
  - `payout` (object) — Payout information. Only available for specific payment processors.
    - `account` (string) — Destination account of the payout - either `global` or `user`. Allowed values: `user`, `global`
    - `date` (string) — Date when the payout was made.
  - `purchased_items` (object) — Breakdown of any items within the transaction, except donation.
    - `apparel` (object) — List of purchased merchandise.
      - `count` (integer) — Total number of items in the transaction.
      - `items` (object[]) — List of items.
        - `id` (integer) — Unique id assigned to item within transaction.
        - `name` (string) — Item name.
        - `option` (string) — Variation of the item.
        - `price` (number) — Original price of the item.
        - `custom_id` (string) — Custom ID or code (i.e. SKU).
    - `registration` (object) — List of purchase registrations.
      - `count` (integer) — Total number of items in the transaction.
      - `items` (object[]) — List of items.
        - `id` (integer) — Unique id assigned to item within transaction.
        - `name` (string) — Item name.
        - `option` (string) — Variation of the item.
        - `price` (number) — Original price of the item.
        - `custom_id` (string) — Custom ID or code (i.e. SKU).
        - `first_name` (string) — Registrant's first name.
        - `last_name` (string) — Registrant's last name.
        - `alias_name` (string) — Registrant's alias name.
        - `comment` (string) — Registrant's comment.
        - `is_amount_hidden` (boolean) — Is registrant's donation hidden?
        - `fundraiser_page` (object) — Personal page that was created during registration.
          - `id` (integer) — Personal page ID.
          - `name` (string) — Personal page name.
          - `goal` (number) — Personal page goal.
          - `self_donation` (object) — Self donation that was made to the page during registration.
            - `id` (integer) — Self donation reference id.
            - `name` (string) — Donor's name
            - `amount` (number) — Amount that was donated.
          - `url` (string) — Personal page url.
          - `team` (object) — Team that was created or joined.
            - `id` (integer) — Team ID.
            - `name` (string) — Team name
            - `goal` (number) — Team goal.
            - `url` (string) — Team url.
            - `language` (string) — Team language. Allowed values: `en`, `fr`
          - `user` (object) — User that created the team (team captain).
            - `id` (integer) — User ID.
            - `first_name` (string) — User's first name.
            - `last_name` (string) — User's last name.
            - `email` (string) — User's email address.
            - `title` (string) — User's title
            - `name` (string) — User's name
        - `mailing_address` (object) — Registrant's mailing information.
          - `street_address` (string) — Street name and number.
          - `city` (string) — City name.
          - `country` (string) — Country code.
          - `state` (string) — State or province..
          - `postal` (string) — ZIP or Postal Code.
        - `custom_data` (object[]) — List of custom questions and responses.
          - `field_id` (integer) — Custom field id.
          - `source_id` (integer) — If field was copied from Blueprint, this will reference the source field id from blueprint (similar to group id).
          - `name` (string) — Custom field label.
          - `content` (string) — User's answer to custom field.
          - `field_custom_id` (string) — Custom ID.
          - `response_custom_id` (string) — Custom ID for the response (multiple choice questions).
        - `registrant_id` (integer) — Original unique id assigned to the previous registration.
    - `tickets` (object) — List of purchased tickets.
      - `count` (integer) — Total number of items in the transaction.
      - `items` (object[]) — List of items.
        - `id` (integer) — Unique id assigned to item within transaction.
        - `name` (string) — Item name.
        - `option` (string) — Variation of the item.
        - `price` (number) — Original price of the item.
        - `custom_id` (string) — Custom ID or code (i.e. SKU).
    - `ecards` (object) — List of purchased eCards.
      - `count` (integer) — Total number of items in the transaction.
      - `items` (object[]) — List of items.
        - `id` (integer) — Unique id assigned to item within transaction.
        - `method` (string) — Method used to send the eCard. Allowed values: `email`, `sms`, `mail`
        - `send_on` (string) — Date when the eCard is to be sent out.
        - `message` (string) — Message on the eCard.
        - `is_anonymous` (boolean) — True if user sent the card anonymously; otherwise, false.
        - `delivery_status` (string) — Allowed values: `na`, `pending`, `sent`, `delivered`, `opened`, `error`
        - `card` (object) — The eCard that was sent.
          - `id` (integer) — ID of the eCard.
          - `name` (string) — Name of the eCard.
          - `price` (number) — Price of the eCard.
        - `recipient` (object) — Recipient of the card.
          - `name` (string) — Name of the recipient.
          - `email` (string) — Email (if the card was sent by email).
          - `phone` (string) — Phone number (if the card was sent by sms).
          - `address` (string) — Mailing address (if the card was sent by mail).
    - `tribute_cards` (object) — List of tribute cards.
      - `count` (integer) — Total number of items in the transaction.
      - `items` (object[]) — List of items.
        - `id` (integer) — Unique id assigned to item within transaction.
        - `method` (string) — Method used to send the eCard. Allowed values: `email`, `sms`, `mail`
        - `type` (string) — Type of tribute card.
        - `honoree` (string) — Name of honoree.
        - `message` (string) — Message on the eCard.
        - `delivery_status` (string) — Allowed values: `na`, `pending`, `sent`, `delivered`, `opened`, `error`
        - `recipient` (object) — Recipient of the card.
          - `name` (string) — Name of the recipient.
          - `email` (string) — Email (if the card was sent by email).
          - `phone` (string) — Phone number (if the card was sent by sms).
          - `address` (string) — Mailing address (if the card was sent by mail).
    - `custom_fees` (object) — List of custom fees.
      - `count` (integer) — Total number of items in the transaction.
      - `items` (object[]) — List of items.
        - `id` (integer) — Unique id assigned to item within transaction.
        - `name` (string) — Item name.
        - `amount` (string) — Custom fee amount.
  - `refunded_items` (object) — Breakdown of any refunded items within the refund transaction. Presented if current transaction is refund transaction.
    - `donations` (object) — List of refunded donations.
      - `items` (object[]) — List of items.
        - `id` (integer) — ID of the initial transaction.
        - `amount` (number) — Refunded amount
    - `covered_fees` (object) — List of covered fees.
      - `items` (object[]) — List of items.
        - `id` (integer) — ID of the initial transaction.
        - `amount` (number) — Refunded amount
    - `apparel` (object) — List of refunded merchandise.
      - `items` (object[]) — List of items.
        - `id` (integer) — Unique id assigned to item within transaction.
        - `name` (string) — Item name.
        - `option` (string) — Variation of the item.
        - `price` (number) — Original price of the item.
        - `custom_id` (string) — Custom ID or code (i.e. SKU).
    - `registration` (object) — List of refunded registrations.
      - `items` (object[]) — List of items.
        - `id` (integer) — Unique id assigned to item within transaction.
        - `name` (string) — Item name.
        - `option` (string) — Variation of the item.
        - `price` (number) — Original price of the item.
        - `custom_id` (string) — Custom ID or code (i.e. SKU).
        - `first_name` (string) — Registrant's first name.
        - `last_name` (string) — Registrant's last name.
        - `alias_name` (string) — Registrant's alias name.
        - `comment` (string) — Registrant's comment.
        - `is_amount_hidden` (boolean) — Is registrant's donation hidden?
        - `fundraiser_page` (object) — Personal page that was created during registration.
          - `id` (integer) — Personal page ID.
          - `name` (string) — Personal page name.
          - `goal` (number) — Personal page goal.
          - `self_donation` (object) — Self donation that was made to the page during registration.
            - `id` (integer) — Self donation reference id.
            - `name` (string) — Donor's name
            - `amount` (number) — Amount that was donated.
          - `url` (string) — Personal page url.
          - `team` (object) — Team that was created or joined.
            - `id` (integer) — Team ID.
            - `name` (string) — Team name
            - `goal` (number) — Team goal.
            - `url` (string) — Team url.
            - `language` (string) — Team language. Allowed values: `en`, `fr`
          - `user` (object) — User that created the team (team captain).
            - `id` (integer) — User ID.
            - `first_name` (string) — User's first name.
            - `last_name` (string) — User's last name.
            - `email` (string) — User's email address.
            - `title` (string) — User's title
            - `name` (string) — User's name
        - `mailing_address` (object) — Registrant's mailing information.
          - `street_address` (string) — Street name and number.
          - `city` (string) — City name.
          - `country` (string) — Country code.
          - `state` (string) — State or province..
          - `postal` (string) — ZIP or Postal Code.
        - `custom_data` (object[]) — List of custom questions and responses.
          - `field_id` (integer) — Custom field id.
          - `source_id` (integer) — If field was copied from Blueprint, this will reference the source field id from blueprint (similar to group id).
          - `name` (string) — Custom field label.
          - `content` (string) — User's answer to custom field.
          - `field_custom_id` (string) — Custom ID.
          - `response_custom_id` (string) — Custom ID for the response (multiple choice questions).
    - `tickets` (object) — List of refunded tickets.
      - `items` (object[]) — List of items.
        - `id` (integer) — Unique id assigned to item within transaction.
        - `name` (string) — Item name.
        - `option` (string) — Variation of the item.
        - `price` (number) — Original price of the item.
        - `custom_id` (string) — Custom ID or code (i.e. SKU).
    - `ecards` (object) — List of refunded eCards.
      - `items` (object[]) — List of items.
        - `id` (integer) — Unique id assigned to item within transaction.
        - `method` (string) — Method used to send the eCard. Allowed values: `email`, `sms`, `mail`
        - `send_on` (string) — Date when the eCard is to be sent out.
        - `message` (string) — Message on the eCard.
        - `is_anonymous` (boolean) — True if user sent the card anonymously; otherwise, false.
        - `delivery_status` (string) — Allowed values: `na`, `pending`, `sent`, `delivered`, `opened`, `error`
        - `card` (object) — The eCard that was sent.
          - `id` (integer) — ID of the eCard.
          - `name` (string) — Name of the eCard.
          - `price` (number) — Price of the eCard.
        - `recipient` (object) — Recipient of the card.
          - `name` (string) — Name of the recipient.
          - `email` (string) — Email (if the card was sent by email).
          - `phone` (string) — Phone number (if the card was sent by sms).
          - `address` (string) — Mailing address (if the card was sent by mail).
    - `sponsorship` (object) — List of refunded sponsorship.
      - `items` (object[]) — List of items.
        - `id` (integer) — Unique id assigned to item within transaction.
        - `option_id` (integer) — Sponsorship tier id.
        - `source_id` (integer) — If the option was copied from Blueprint, this will reference the source option id from blueprint (similar to group id).
        - `name` (string) — Sponsorship tier name.
        - `price` (number) — Sponsorship tier price.
    - `custom_fees` (object) — List of custom fees.
      - `count` (integer) — Total number of items in the transaction.
      - `items` (object[]) — List of items.
        - `id` (integer) — Unique id assigned to item within transaction.
        - `name` (string) — Item name.
        - `amount` (string) — Custom fee amount.
    - `self_donations` (object) — List of self donations associated with personal pages.
      - `items` (object[]) — List of items.
        - `id` (integer) — Unique id assigned to item within transaction.
        - `amount` (number) — Refunded amount
        - `name` (string) — Donor's name
        - `fundraiser_page` (object) — Personal page that was created during registration.
          - `id` (integer) — Personal page ID.
          - `partner_id` (integer) — Site ID.
          - `name` (string) — Personal page name.
          - `first_name` (string) — First name of personal page's owner.
          - `last_name` (string) — Last name of personal page's owner.
          - `goal` (number) — Personal page goal.
          - `language` (string) — Personal page language. Allowed values: `en`, `fr`
          - `custom_data` (object[]) — List of custom questions and responses.
            - `field_id` (integer) — Custom field id.
            - `source_id` (integer) — If field was copied from Blueprint, this will reference the source field id from blueprint (similar to group id).
            - `name` (string) — Custom field label.
            - `content` (string) — User's answer to custom field.
            - `field_custom_id` (string) — Custom ID.
            - `response_custom_id` (string) — Custom ID for the response (multiple choice questions).
  - `sponsorship` (object) — List of purchased sponsorships.
    - `count` (integer) — Total number of purchased sponsorships in the transaction.
    - `items` (object[]) — List of items.
      - `id` (integer) — Unique id assigned to item within transaction.
      - `option_id` (integer) — Sponsorship tier id.
      - `source_id` (integer) — If the option was copied from Blueprint, this will reference the source option id from blueprint (similar to group id).
      - `name` (string) — Sponsorship tier name.
      - `price` (number) — Sponsorship tier price.
  - `fulfillment_transaction_id` (integer) — Fulfillment transaction ID. Presented if transaction is a pledge transaction.
  - `is_pledge_transaction` (boolean) — Is this transaction a pledge? Presented if transaction is a pledge transaction.
  - `pledge_transaction_id` (integer) — Pledge transaction ID. Presented if transaction is a fulfillment transaction.
  - `is_fulfillment_transaction` (boolean) — Is this transaction a fulfillment? Presented if transaction is a fulfillment transaction.
  - `payee` (object) — Information about person who actually paid for the transaction. Property is presented if transaction has pledge or fulfillment transaction
    - `billing` (object) — User's billing information.
      - `business_name` (string) — Business name.
      - `is_foundation` (boolean) — Is this transaction made by foundation?
      - `title` (string) — Honorific (i.e. Mr / Miss / etc).
      - `name` (string) — Full user name including honorific.
      - `first_name` (string) — User's first name.
      - `last_name` (string) — User's last name.
      - `street_address` (string) — Street name and number.
      - `city` (string) — City name.
      - `country` (string) — Country code.
      - `state` (string) — State or province..
      - `postal` (string) — ZIP or Postal Code.
      - `email` (string) — User's email address.
      - `phone` (string) — Phone number.
    - `user` (object) — User who actually paid for the transaction.
      - `id` (integer) — User ID.
      - `first_name` (string) — User's first name.
      - `last_name` (string) — User's last name.
      - `email` (string) — User's email address.
      - `language` (string) — User's preferred language. Allowed values: `en`, `fr`
      - `title` (string) — User's title
      - `name` (string) — User's name

**Other responses**

| Status | Description |
| - | - |
| `400` | Bad Request |
| `403` | Forbidden |

**Response example:**

```json
{
    "dt_start": "2021-01-01T00:00:00",
    "dt_end": "2021-01-31T00:00:00",
    "count": 1,
    "data": [
{
    "id": 10001,
    "type": "charge",
    "status": "completed",
    "refund_children_ids": [
    10001,
    10002
    ],
    "parent_id": 10001,
    "partner_id": 10,
    "promo_code": "PROMO100",
    "amount": {
    "apparel": 29.95,
    "covered_fees": 5.15,
    "currency": "USD",
    "donation": 50,
    "donation_to_pages": 50,
    "ecards": 0,
    "is_recurring": false,
    "registration": 0,
    "sponsorship": 0,
    "tickets": 10,
    "total_net": 99.95,
    "total_paid": 105.15,
    "custom_fees": 15.95
},
    "billing": {
    "business_name": "Company Inc",
    "is_foundation": false,
    "title": "Mr.",
    "name": "Mr. John Snow",
    "first_name": "John",
    "last_name": "Snow",
    "street_address": "100 Main Street",
    "city": "Toronto",
    "country": "CA",
    "state": "ON",
    "postal": "A1A 1A1",
    "email": "john@example.com",
    "phone": "1-555-123-4567"
},
    "donated_by": {
    "business_name": "Company Inc",
    "title": "Mr.",
    "name": "Mr. John Snow",
    "first_name": "John",
    "last_name": "Snow",
    "street_address": "100 Main Street",
    "city": "Toronto",
    "country": "CA",
    "state": "ON",
    "postal": "A1A 1A1",
    "email": "john@example.com",
    "is_foundation": false,
    "user_id": 1,
    "phone": "1-555-123-4567"
},
    "mailing_address": {
    "business_name": "Company Inc",
    "is_foundation": false,
    "title": "Mr.",
    "name": "Mr. John Snow",
    "first_name": "John",
    "last_name": "Snow",
    "street_address": "100 Main Street",
    "city": "Toronto",
    "country": "CA",
    "state": "ON",
    "postal": "A1A 1A1",
    "phone": "1-555-123-4567"
},
    "card_type": "Visa",
    "payment_processor": "Stripe",
    "processor_transaction_id": "ch_xxxxxxx",
    "ref_source": "newsletter",
    "custom_data": [
{
    "field_id": 1001,
    "source_id": 11,
    "name": "Phone Number",
    "content": "555-123-4567",
    "field_custom_id": "ABC-123",
    "response_custom_id": "ABC-123"
}
    ],
    "date": "2021-09-26 16:00:03",
    "donation_comment": "Happy to contribute to a worthy cause!",
    "fundraiser": {
    "id": 100,
    "partner_id": 10,
    "fundraiser_template_id": 1,
    "fundraiser_template": {
    "id": 1,
    "name": "Template"
},
    "name": "Donate Now!",
    "dt_start": "2021-01-01 08:00:00",
    "dt_end": "2021-01-01 16:00:00",
    "location": "100 Main Street, Toronto, ON",
    "goal": 100000,
    "campus": "University of Western Ontario",
    "national_office": "Sigma Delta Tau",
    "chapter": "Gamma Psi",
    "chapter_custom_id": "GPI-12345",
    "organization": "Company Inc.",
    "in_support_name": "Cancer Research",
    "in_support_code": "CR-123",
    "appeal_code": "GEN-123",
    "language": "en",
    "custom_data": [
{
    "field_id": 1001,
    "source_id": 11,
    "name": "Phone Number",
    "content": "555-123-4567",
    "field_custom_id": "ABC-123",
    "response_custom_id": "ABC-123"
}
    ],
    "user": {
    "id": 1,
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Snow",
    "title": "Mr.",
    "name": "John Snow"
},
    "tags_list": [
    "tag1",
    "tag2"
    ]
},
    "fundraiser_team": {
    "id": 1001,
    "partner_id": 10,
    "fundraiser_id": 101,
    "name": "Team A",
    "goal": 10000,
    "url": "https://my.crowdchange.co/abcd1234",
    "user": {
    "id": 1001,
    "first_name": "John",
    "last_name": "Smith",
    "email": "john@example.com",
    "language": "en",
    "title": "Mr.",
    "name": "John Snow"
},
    "custom_data": [
{
    "field_id": 1001,
    "source_id": 11,
    "name": "Phone Number",
    "content": "555-123-4567",
    "field_custom_id": "ABC-123",
    "response_custom_id": "ABC-123"
}
    ]
},
    "fundraiser_user_page": {
    "id": 1001,
    "partner_id": 10,
    "name": "Team A",
    "first_name": "John",
    "last_name": "Snow",
    "user_name": "John Snow",
    "title": "Mr.",
    "goal": 10000,
    "url": "https://my.crowdchange.co/abcd1234",
    "language": "en",
    "custom_data": [
{
    "field_id": 1001,
    "source_id": 11,
    "name": "Phone Number",
    "content": "555-123-4567",
    "field_custom_id": "ABC-123",
    "response_custom_id": "ABC-123"
}
    ]
},
    "is_disputed": false,
    "is_refunded": false,
    "is_pending": false,
    "is_tax_receipt_issued": true,
    "tax_receipt": {
    "id": 1001,
    "amount_donation": 100.99,
    "amount_benefit": 10.49,
    "amount_eligible": 90.5,
    "business_name": "Company Inc",
    "name_on_receipt": "John Smith",
    "issued_on": "2021-01-01 19:00:00",
    "receipt_number": "TAX-0012345",
    "status": "valid",
    "title": "Mr.",
    "first_name": "John",
    "last_name": "Snow",
    "street_address": "100 Main Street",
    "city": "Toronto",
    "country": "CA",
    "state": "ON",
    "postal": "A1A 1A1",
    "email": "john@example.com",
    "user_id": 1,
    "transaction_id": 1
},
    "recurring": {
    "id": 1001,
    "amount": 100,
    "amount_net": 100,
    "interval": "month",
    "day": 1,
    "month": 6,
    "status": "active"
},
    "payout": {
    "account": "user",
    "date": "2021-01-01"
},
    "purchased_items": {
    "apparel": {
    "count": 0,
    "items": [
{
    "id": 10001,
    "name": "T-shirt",
    "option": "XL - Blue",
    "price": 29.95
}
    ]
},
    "registration": {
    "count": 0,
    "items": [
{
    "id": 10001,
    "name": "Bike ride.",
    "option": "200 KM",
    "price": 350,
    "first_name": "John",
    "last_name": "Doe",
    "alias_name": "Family's Friend",
    "comment": "Comment",
    "is_amount_hidden": false,
    "fundraiser_page": {
    "id": 1001,
    "name": "John Smith",
    "goal": 10000,
    "self_donation": {
    "id": 1001,
    "name": "Joe Doe",
    "amount": 100
},
    "url": "https://my.crowdchange.co/abcd1234",
    "team": {
    "id": 1001,
    "name": "Team A",
    "goal": 10000,
    "url": "https://my.crowdchange.co/abcd1234",
    "language": "en"
},
    "user": {
    "id": 1001,
    "first_name": "John",
    "last_name": "Smith",
    "email": "john@example.com",
    "title": "Mr.",
    "name": "John Snow"
}
},
    "mailing_address": {
    "street_address": "100 Main Street",
    "city": "Toronto",
    "country": "CA",
    "state": "ON",
    "postal": "A1A 1A1"
},
    "custom_data": [
{
    "field_id": 1001,
    "source_id": 11,
    "name": "Phone Number",
    "content": "555-123-4567",
    "field_custom_id": "ABC-123",
    "response_custom_id": "ABC-123"
}
    ],
    "registrant_id": 10001
}
    ]
},
    "tickets": {
    "count": 0,
    "items": [
{
    "id": 10001,
    "name": "General admission",
    "option": "Section C",
    "price": 19.98
}
    ]
},
    "ecards": {
    "count": 0,
    "items": [
{
    "id": 10001,
    "method": "email",
    "send_on": "2021-01-01",
    "message": "Happy New Year!",
    "is_anonymous": true,
    "delivery_status": "opened",
    "card": {
    "id": 10001,
    "name": "Happy New Year - 1",
    "price": 1.99
},
    "recipient": {
    "name": "John Snow",
    "email": "john@example.com",
    "phone": "1-555-123-4567",
    "address": "100 Main Str, Toronto, ON"
}
}
    ]
},
    "tribute_cards": {
    "count": 0,
    "items": [
{
    "id": 10001,
    "method": "email",
    "type": "In honor of",
    "honoree": "John Snow",
    "message": "Happy New Year!",
    "delivery_status": "opened",
    "recipient": {
    "name": "John Snow",
    "email": "john@example.com",
    "phone": "1-555-123-4567",
    "address": "100 Main Str, Toronto, ON"
}
}
    ]
},
    "custom_fees": {
    "count": 0,
    "items": [
{
    "id": 10001,
    "name": "Custom fee",
    "amount": 15.95
}
    ]
}
},
    "refunded_items": {
    "donations": {
    "items": [
{
    "id": 10001,
    "amount": 29.95
}
    ]
},
    "covered_fees": {
    "items": [
{
    "id": 10001,
    "amount": 29.95
}
    ]
},
    "apparel": {
    "items": [
{
    "id": 10001,
    "name": "T-shirt",
    "option": "XL - Blue",
    "price": 29.95
}
    ]
},
    "registration": {
    "items": [
{
    "id": 10001,
    "name": "Bike ride.",
    "option": "200 KM",
    "price": 350,
    "first_name": "John",
    "last_name": "Doe",
    "alias_name": "Family's Friend",
    "comment": "Comment",
    "is_amount_hidden": false,
    "fundraiser_page": {
    "id": 1001,
    "name": "John Smith",
    "goal": 10000,
    "self_donation": {
    "id": 1001,
    "name": "Joe Doe",
    "amount": 100
},
    "url": "https://my.crowdchange.co/abcd1234",
    "team": {
    "id": 1001,
    "name": "Team A",
    "goal": 10000,
    "url": "https://my.crowdchange.co/abcd1234",
    "language": "en"
},
    "user": {
    "id": 1001,
    "first_name": "John",
    "last_name": "Smith",
    "email": "john@example.com",
    "title": "Mr.",
    "name": "John Snow"
}
},
    "mailing_address": {
    "street_address": "100 Main Street",
    "city": "Toronto",
    "country": "CA",
    "state": "ON",
    "postal": "A1A 1A1"
},
    "custom_data": [
{
    "field_id": 1001,
    "source_id": 11,
    "name": "Phone Number",
    "content": "555-123-4567",
    "field_custom_id": "ABC-123",
    "response_custom_id": "ABC-123"
}
    ]
}
    ]
},
    "tickets": {
    "items": [
{
    "id": 10001,
    "name": "General admission",
    "option": "Section C",
    "price": 19.98
}
    ]
},
    "ecards": {
    "items": [
{
    "id": 10001,
    "method": "email",
    "send_on": "2021-01-01",
    "message": "Happy New Year!",
    "is_anonymous": true,
    "delivery_status": "opened",
    "card": {
    "id": 10001,
    "name": "Happy New Year - 1",
    "price": 1.99
},
    "recipient": {
    "name": "John Snow",
    "email": "john@example.com",
    "phone": "1-555-123-4567",
    "address": "100 Main Str, Toronto, ON"
}
}
    ]
},
    "sponsorship": {
    "items": [
{
    "id": 10001,
    "option_id": 100,
    "source_id": 100,
    "name": "Platinum Package",
    "price": 1000
}
    ]
},
    "custom_fees": {
    "count": 0,
    "items": [
{
    "id": 10001,
    "name": "Custom fee",
    "amount": 15.95
}
    ]
},
    "self_donations": {
    "items": [
{
    "id": 10001,
    "amount": 29.95,
    "name": "Joe Doe",
    "fundraiser_page": {
    "id": 1001,
    "partner_id": 10,
    "name": "Team A",
    "first_name": "John",
    "last_name": "Snow",
    "goal": 10000,
    "language": "en",
    "custom_data": [
{
    "field_id": 1001,
    "source_id": 11,
    "name": "Phone Number",
    "content": "555-123-4567",
    "field_custom_id": "ABC-123",
    "response_custom_id": "ABC-123"
}
    ]
}
}
    ]
}
},
    "sponsorship": {
    "count": 0,
    "items": [
{
    "id": 10001,
    "option_id": 100,
    "source_id": 100,
    "name": "Platinum Package",
    "price": 1000
}
    ]
},
    "fulfillment_transaction_id": 1,
    "is_pledge_transaction": true,
    "pledge_transaction_id": 1,
    "is_fulfillment_transaction": true,
    "payee": {
    "billing": {
    "business_name": "Company Inc",
    "is_foundation": false,
    "title": "Mr.",
    "name": "Mr. John Snow",
    "first_name": "John",
    "last_name": "Snow",
    "street_address": "100 Main Street",
    "city": "Toronto",
    "country": "CA",
    "state": "ON",
    "postal": "A1A 1A1",
    "email": "john@example.com",
    "phone": "1-555-123-4567"
},
    "user": {
    "id": 1001,
    "first_name": "John",
    "last_name": "Smith",
    "email": "john@example.com",
    "language": "en",
    "title": "Mr.",
    "name": "John Snow"
}
}
}
    ]
}
```

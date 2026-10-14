---
title: Facebook Pixel
slug: analytics/facebook-pixel
collection: api
source_url: https://apidoc.crowdchange.dev/analytics/facebook-pixel
nav_path:
- Documentation
- Analytics & Tracking
- Facebook Pixel
nav_order: 3
page_type: guide
endpoint: null
http_method: null
endpoint_path: null
api_surface: null
auth: null
tags:
- analytics-tracking
- donations
crm_relevant: false
description: Install the Facebook Pixel and Conversions API in CrowdChange to track donations, retarget visitors, and measure ad performance on Meta.
retrieved: '2026-10-14'
word_count: 678
---

<!-- Source: https://apidoc.crowdchange.dev/analytics/facebook-pixel | Nav: Documentation > Analytics & Tracking > Facebook Pixel | Mirrored 2026-10-14 -->

# Facebook Pixel

> Install the Facebook Pixel and Conversions API in CrowdChange to track donations, retarget visitors, and measure ad performance on Meta.

## Facebook Pixel Integration

CrowdChange supports Meta Pixel tracking and optional Meta Conversions API purchase tracking.

Once connected, your Pixel receives browser `PageView` and `Purchase` events as users browse and complete transactions. If a Meta Conversions API access token is configured, CrowdChange also sends completed purchases from the server and uses a shared event ID to help Meta deduplicate browser and server events.

***

## Setup

1. Go to **Admin -> Layout Settings -> Meta & Analytics**
2. Scroll to the **Facebook Analytics** section
3. Enter your **Pixel ID** in the *Facebook Pixel ID* field, for example `1234567890123456`
4. Optional: enter your **Meta Conversions API access token**
5. Optional: enter your **Domain Verification** code in the *FB meta tag domain verification* field. Use only the value from the `content` attribute of the `<meta name="facebook-domain-verification" ...>` tag Meta provides
6. Click **Save**

The browser Pixel snippet is automatically injected into every page once the Pixel ID is saved.

Conversions API tokens are stored as write-only encrypted values; leave the token field blank to keep an existing token.

***

## Tracked Events

### PageView

Fired automatically on page load and virtual page navigation.

| Parameter | Type | Description |
| - | - | - |
| `external_id` | `string \| null` | The `fbclid` click ID from the visitor's landing URL, if present |

**Example payload**

```json
{
  "external_id": "fb-click-id"
}
```

***

### Purchase

Fired when a donor successfully completes a transaction.

| Parameter | Type | Description |
| - | - | - |
| `currency` | `string` | ISO 4217 currency code, for example `USD`, `CAD` |
| `value` | `number` | Total transaction amount |
| `content_ids` | `string[]` | Item IDs included in the transaction |
| `contents` | `object[]` | Array of `{ id, quantity }` objects |
| `content_name` | `string` | Page title at the time of purchase |
| `content_type` | `string` | Always `product` |
| `num_items` | `number` | Number of items in the transaction |
| `external_id` | `string` | The captured `fbclid`, if present |

The browser event is sent with `eventID: transaction_<transaction_id>`.

**Example browser payload**

```json
{
  "currency": "USD",
  "value": 100,
  "content_ids": ["42", "87"],
  "contents": [
    { "id": "42", "quantity": 1 },
    { "id": "87", "quantity": 1 }
  ],
  "content_name": "Annual Gala",
  "content_type": "product",
  "num_items": 2,
  "external_id": "fb-click-id"
}
```

***

## Server-Side Purchase Tracking

When both a Pixel ID and Meta Conversions API access token are configured, CrowdChange sends a matching server-side `Purchase` event to Meta.

| Field | Description |
| - | - |
| `event_id` | `transaction_<transaction_id>` for browser/server dedupe |
| `event_source_url` | Checkout page URL when available |
| `currency` | Transaction currency |
| `value` | Transaction total |
| `order_id` | CrowdChange transaction ID |
| `content_ids` | Purchased content IDs, or `donation` for donation-only flow |
| `contents` | Purchased content quantities |
| `client_ip_address` | Request IP address |
| `client_user_agent` | Request user agent |
| `fbp` / `fbc` | Meta browser cookies when available |
| `em` / `external_id` | SHA-256 hashed donor email and user ID when available |

Ad-network failures are logged and do not interrupt the donor checkout flow.

***

## Click ID Attribution (`fbclid`)

When a visitor arrives via a Meta ad, Meta may append `fbclid` to the URL. CrowdChange captures it in the browser session and uses it for browser Pixel events. For server-side purchases, CrowdChange also forwards `_fbp` and `_fbc` cookies when available, and derives `_fbc` from `fbclid` when the cookie is missing.

***

## Domain Verification

To verify your domain with Meta:

1. In Meta Business Manager, go to **Brand Safety -> Domains** and add your domain
2. Copy the verification code from the `<meta name="facebook-domain-verification" content="...">` tag
3. Paste only the `content` value into the **FB meta tag domain verification** field
4. Click **Save**
5. Return to Meta and click **Verify**

***

## Verifying Your Setup

After saving your Pixel ID:

1. Install the [Meta Pixel Helper](https://chromewebstore.google.com/detail/meta-pixel-helper/fdgfkebogiimcoedlicjlajpkdmockpc) Chrome extension
2. Visit any page on your platform
3. Confirm the extension shows your Pixel ID firing `PageView`
4. Complete a test transaction and confirm `Purchase` fires with the expected value and currency

If you configured Conversions API, also verify in **Meta Events Manager -> Test Events** and confirm browser/server deduplication uses the same `transaction_<transaction_id>` event ID.

***

## Additional Information

See [Meta Pixel docs](https://developers.facebook.com/docs/meta-pixel) and [Meta Conversions API docs](https://developers.facebook.com/docs/marketing-api/conversions-api/get-started) for further information.

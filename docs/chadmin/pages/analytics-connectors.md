---
title: Analytics Connectors - Google Analytics, Google Tag Manager, Facebook/Meta Pixel, Reddit, Pinterest, & TikTok
slug: analytics-connectors
collection: chadmin
source_url: https://chadmin.crowdchange.help/ct/analytics-connectors
nav_path:
- Analytics Connectors - Google Analytics, Google Tag Manager, Facebook/Meta Pixel, Reddit, Pinterest, & TikTok
nav_order: 82
parent: null
children: []
page_type: reference
tags:
- activity-tracking
- purchase-options
- reporting-and-data
- troubleshooting
crm_relevant: true
description: CrowdChange supports integrations with several analytics and advertising platforms, allowing organizations to track website activity, campaign performance, and…
last_modified: '2026-06-15T13:45:32.658Z'
retrieved: '2026-10-14'
audience: Charity Admins (CrowdChange admin help center space CT)
word_count: 813
---

<!-- Source: https://chadmin.crowdchange.help/ct/analytics-connectors | Nav: Analytics Connectors - Google Analytics, Google Tag Manager, Facebook/Meta Pixel, Reddit, Pinterest, & TikTok | Mirrored 2026-10-14 -->

# Analytics Connectors - Google Analytics, Google Tag Manager, Facebook/Meta Pixel, Reddit, Pinterest, & TikTok

CrowdChange supports integrations with several analytics and advertising platforms, allowing organizations to track website activity, campaign performance, and completed transactions.

Analytics connectors can be configured to support both browser-based tracking (Pixels, Tags, and Analytics IDs) and server-side conversion tracking (Conversions APIs and Measurement Protocol integrations), helping improve attribution accuracy and conversion reporting.

## Accessing Analytics Connectors

To access your analytics settings:

1. Log in to your CrowdChange site with an Admin account.

2. Click **Profile → Admin**.

3. Select **Layout Settings** from the left sidebar.

4. Scroll to the **Meta \& Analytics** section.

5. Enter the desired IDs, tags, verification values, or access tokens.

6. Click **Save**.

*** ** * ** ***

## Google Analytics

### Google Analytics 4 Tracking ID

The Google Analytics 4 Tracking ID connects your CrowdChange site to your Google Analytics property and enables visitor and event tracking.

Example:

`G-XXXXXXXXXX`

#### Finding Your GA4 Measurement ID

1. Open Google Analytics.

2. Navigate to **Admin → Data Streams**.

3. Select your website data stream.

4. Copy the **Measurement ID**.

*** ** * ** ***

### GA4 Measurement Protocol API Secret

The Measurement Protocol API Secret allows CrowdChange to send completed transaction events directly to Google Analytics from CrowdChange's servers.

Server-side tracking can improve attribution accuracy and help ensure completed transactions are recorded even when browser-side tracking is unavailable.

#### Creating an API Secret

1. Open Google Analytics.

2. Navigate to **Admin → Data Streams**.

3. Select your website stream.

4. Under **Measurement Protocol API Secrets**, create a new secret.

5. Copy the generated value into CrowdChange.

*** ** * ** ***

## Google Tag Manager

Google Tag Manager allows organizations to deploy custom tracking and marketing tags without modifying website code.

Separate GTM containers may be configured for English and French versions of a site.

Example:

`GTM-XXXXXXX`

### Finding Your GTM Container ID

1. Open Google Tag Manager.

2. Select your container.

3. Copy the Container ID displayed near the top of the workspace.

*** ** * ** ***

## Meta (Facebook) Analytics

### Facebook Pixel ID

The Facebook Pixel tracks visitor activity and conversion events generated through Meta advertising campaigns.

#### Finding Your Pixel ID

1. Open Meta Events Manager.

2. Select your Pixel.

3. Copy the Pixel ID displayed under your Data Source settings.

*** ** * ** ***

### Meta Conversions API Access Token

The Meta Conversions API Access Token allows CrowdChange to send completed transaction events directly to Meta from the server.

Server-side tracking improves attribution accuracy and helps Meta deduplicate events received through both the Pixel and Conversions API.

#### Generating an Access Token

1. Open Meta Events Manager.

2. Select your Pixel.

3. Navigate to **Settings**.

4. Locate the **Conversions API** section.

5. Generate an Access Token.

6. Copy the token into CrowdChange.

*** ** * ** ***

### Meta Domain Verification

Meta may require domain verification for certain advertising features.

Verification values can be entered separately for:

* English (EN)

* French (FR)

#### Obtaining Your Verification Token

1. Open Meta Business Settings.

2. Navigate to **Brand Safety → Domains**.

3. Add and verify your domain.

4. Select **Meta-tag Verification**.

5. Copy the verification value provided by Meta.

*** ** * ** ***

## Reddit Pixel

### Reddit Pixel ID

The Reddit Pixel tracks visitor activity and conversion events originating from Reddit advertising campaigns.

Enter the Reddit Pixel ID associated with your advertising account.

*** ** * ** ***

### Reddit Ads Account ID

The Reddit Ads Account ID identifies the advertising account associated with the configured Reddit Pixel.

Enter the account ID provided within your Reddit Ads Manager account.

*** ** * ** ***

### Reddit Conversions API Access Token

The Reddit Conversions API Access Token allows CrowdChange to send completed transaction events directly to Reddit from the server.

Server-side tracking can improve conversion attribution and reporting reliability.

*** ** * ** ***

## Pinterest Tag

### Pinterest Tag ID

The Pinterest Tag tracks visitor activity and conversion events generated through Pinterest advertising campaigns.

Enter the Tag ID associated with your Pinterest advertising account.

*** ** * ** ***

### Pinterest Ad Account ID

The Pinterest Ad Account ID identifies the advertising account associated with the configured Pinterest Tag.

Enter the account ID provided within Pinterest Business.

*** ** * ** ***

### Pinterest Conversions API Access Token

The Pinterest Conversions API Access Token allows CrowdChange to send completed donation and purchase events directly to Pinterest using secure server-side tracking.

Server-side tracking can improve conversion attribution and reporting accuracy.

*** ** * ** ***

## TikTok Pixel

### TikTok Pixel ID

The TikTok Pixel tracks visitor activity and conversion events generated through TikTok advertising campaigns.

Enter the Pixel ID associated with your TikTok Ads account.

*** ** * ** ***

### TikTok Events API Access Token

The TikTok Events API Access Token allows CrowdChange to send completed transaction events directly to TikTok from the server.

Server-side tracking can improve attribution reliability and help reduce conversion data loss caused by browser privacy restrictions.

*** ** * ** ***

## Best Practices

For the most complete conversion reporting, CrowdChange recommends configuring both:

* Browser-side tracking (Analytics IDs, Pixels, and Tags)

* Server-side tracking (Measurement Protocol and Conversions API integrations)

Using both methods helps advertising and analytics platforms more accurately attribute donations, registrations, ticket purchases, sponsorships, and merchandise sales while reducing data loss caused by browser privacy restrictions.

---
title: Widgets Overview
slug: widgets/overview
collection: api
source_url: https://apidoc.crowdchange.dev/widgets/overview
nav_path:
- Documentation
- Widgets
- Widgets Overview
nav_order: 7
page_type: guide
endpoint: null
http_method: null
endpoint_path: null
api_surface: null
auth: null
tags:
- donations
- widgets
crm_relevant: false
description: Embed CrowdChange fundraising widgets on your website with a single script tag, then add donation forms, progress bars, and thermometers anywhere on the page.
retrieved: '2026-10-14'
word_count: 354
---

<!-- Source: https://apidoc.crowdchange.dev/widgets/overview | Nav: Documentation > Widgets > Widgets Overview | Mirrored 2026-10-14 -->

# Widgets Overview

> Embed CrowdChange fundraising widgets on your website with a single script tag, then add donation forms, progress bars, and thermometers anywhere on the page.

CrowdChange widgets let you embed a donation form, progress bar, or thermometer directly into your own website. You add the embed script once, then drop in as many widgets as you like — either declaratively with a `<crowdchange>` element or programmatically through the `CrowdChange` JavaScript API.

## Step 1 — Enable embedding for your campaign

In your CrowdChange admin, open the campaign and go to **Setup → Embed**. Enable the **Embed** option, save your settings, and copy the snippet provided there.

***

## Step 2 — Add the embed script

Include the embed script once per page, just before the closing `</body>` tag:

```html
<script type="module" crossorigin="anonymous" src="https://[your-site-domain]/js/embed/v2"></script>
```

Replace `[your-site-domain]` with your CrowdChange domain, for example `site.crowdchange.co`.

The script registers the `<crowdchange>` element, exposes the global `CrowdChange` object, and automatically initializes any widgets already on the page (and any added later).

***

## Step 3 — Add a widget

There are two ways to add a widget.

### 1. Using the `<crowdchange>` element

Place a `<crowdchange>` element anywhere on your page and configure it with attributes. This is the simplest approach and works without writing any JavaScript.

```html
<crowdchange widget="donation-form" fundraiser="16" mode="inline"></crowdchange>
```

See each widget's page for its full list of supported attributes.

### 2. Using the JavaScript API

For programmatic control — for example, opening a donation form from your own button — use `CrowdChange.createWidget()`. It returns a widget instance you can act on; in `popup` mode, call `expand()` to open it.

For the fastest first open, create the widget once during page load and only call `expand()` inside your click handler:

```html
<button type="button" id="open-donation-widget">Donate</button>

<script>
  const donationWidget = CrowdChange.createWidget({
    widget: 'donation-form',
    fundraiser: 16,
    colorPrimary: '#ccc',
    colorBackground: '#e3ae7a',
    language: 'en'
  });

  document
    .getElementById('open-donation-widget')
    .addEventListener('click', () => donationWidget.expand());
</script>
```

Attribute names use kebab-case on the `<crowdchange>` element (for example `color-primary`) and camelCase in the JavaScript API (for example `colorPrimary`).

---
title: Thermometer Widget
slug: widgets/thermometer-widget
collection: api
source_url: https://apidoc.crowdchange.dev/widgets/thermometer-widget
nav_path:
- Documentation
- Widgets
- Thermometer Widget
nav_order: 10
page_type: guide
endpoint: null
http_method: null
endpoint_path: null
api_surface: null
auth: null
tags:
- peer-to-peer
- teams
- widgets
crm_relevant: false
description: Embed the CrowdChange thermometer widget to display a live fundraising thermometer with goal and raised amounts for any campaign, team, or personal page.
retrieved: '2026-10-14'
word_count: 247
---

<!-- Source: https://apidoc.crowdchange.dev/widgets/thermometer-widget | Nav: Documentation > Widgets > Thermometer Widget | Mirrored 2026-10-14 -->

# Thermometer Widget

> Embed the CrowdChange thermometer widget to display a live fundraising thermometer with goal and raised amounts for any campaign, team, or personal page.

The `thermometer` widget displays a live fundraising thermometer that fills toward a goal. It renders inline and can track an entire fundraiser, a specific team, or an individual personal page.

New to widgets? Start with the [Widgets Overview](overview.md) to add the embed script.

![CrowdChange thermometer widget](../../assets/311a9195bebcccfcc030348c0462a38265c366657dc0ff8acf52df099afe2af7-image.png)

***

## Usage example

### Thermometer for fundraiser progress

```html
<crowdchange widget="thermometer"
             fundraiser="1000"
             show-name="true"
             color-text="#ffffff"
             color-primary="#e43d31"
             color-background="#212944"
             progress-bar-color="#e43d31"
></crowdchange>
```

***

## Supported settings

| JS Setting | Element Attribute | Description | Default |
| :- | :- | :- | :- |
| `widget` | `widget` | Widget type: `thermometer`. | Required |
| `fundraiser` | `fundraiser` | The ID of the fundraiser. | \* |
| `fundraiserTeam` | `fundraiser-team` | The ID of the team. | \* |
| `fundraiserPage` | `fundraiser-page` | The ID of the personal page. | \* |
| `showName` | `show-name` | Show the name of the fundraiser, team, or personal page: `true` or `false`. | `false` |
| `language` | `language` | The language code, e.g. `en`, `fr`. | `en` |
| `colorPrimary` | `color-primary` | Primary color. | Fundraiser's theme. |
| `colorText` | `color-text` | Text color. | Fundraiser's theme. |
| `colorBackground` | `color-background` | Background color. | Fundraiser's theme. |
| `progressBarColor` | `progress-bar-color` | Progress bar color. | Fundraiser's theme. |

> **Note:** Provide **one** of the following IDs to choose what the widget tracks:
>
> * `fundraiser` — progress of the overall fundraiser.
> * `fundraiser-team` — progress of a specific team.
> * `fundraiser-page` — progress of a specific personal page.
>
> If you provide none of these, the widget shows the overall progress of your site.

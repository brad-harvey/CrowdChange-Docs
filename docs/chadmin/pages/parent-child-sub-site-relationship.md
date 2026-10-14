---
title: Parent - Child / Sub-Site Relationship
slug: parent-child-sub-site-relationship
collection: chadmin
source_url: https://chadmin.crowdchange.help/ct/parent-child-sub-site-relationship
nav_path:
- Parent - Child / Sub-Site Relationship
nav_order: 100
parent: null
children: []
page_type: reference
tags:
- payments-and-receipts
- reporting-and-data
crm_relevant: true
description: CrowdChange is equipped with some very useful functionality whereby organizations can set up child sites, also known as sub-sites, under / within a parent site…
last_modified: '2023-07-19T16:24:19.087Z'
retrieved: '2026-10-14'
audience: Charity Admins (CrowdChange admin help center space CT)
word_count: 778
---

<!-- Source: https://chadmin.crowdchange.help/ct/parent-child-sub-site-relationship | Nav: Parent - Child / Sub-Site Relationship | Mirrored 2026-10-14 -->

# Parent - Child / Sub-Site Relationship

CrowdChange is equipped with some very useful functionality whereby organizations can set up child sites, also known as sub-sites, under / within a parent site.

For our Charity partners this can be very practical for uses cases such as the following:

* Segmenting individual giving programs

* Specific campaigns which need to be segmented / set apart (for marketing purposes)

* Large-scale multi-region campaigns where you want a dedicated site, with a dedicated fundraiser for each region

**IMPORTANT TO NOTE:**  
* A Parent site can have multiple Child Sites.

* A Child site can only be attached to one Parent site.

* Partners can create as many child sites as they want at no additional cost.

## Managing Child Site Features

Most features of a child site are managed from the child site itself and can be configured independently of Parent sites. There are however, the following exceptions, which are governed by the Parent site:  

|     **Feature**      |                                                              **Description**                                                              |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Banking              | Banking in most cases is managed from the Parent site, however, there are different banking settings that can be applied to a child site. |
| Organizations        | Organizations are managed from the Parent site, and cannot be changed, deleted, or added on child sites.                                  |
| Tax Receipt Settings | Tax Receipt settings are managed from the Parent site and pushed to child.                                                                |
| In Support Of values | "In support of" values are managed from the Parent site, and cannot be changed, deleted, or added from child sites.                       |

The above settings are pushed down to child sites regardless of their settings / features.

### Banking

We offer several different banking configurations and integration with different payment processors, depending on the needs of the client. Banking can also be different for the Parent site than the child site if desired.

Our 3 most common configurations for child site banking are:

* **Central / Global Banking** - Banking is set up on Parent site and automatically pushed to child sites. This can be used with any payment processor.

* **Select Global banking** (i.e. Parent vs Child banking) - Fundraiser creators on the child site have the ability to choose when creating a new fundraiser, whether the funds should go to the global / central bank account set at the parent level, or a bank account connected to the child site.

* **Parent Site Central Banking + Child Site Users Manage Banking**- In this instance, every fundraiser created on the child site will be prompted to connect a bank account of their choosing that is then connected to their user profile to be used for any subsequent fundraisers. When using this option, the payment gateway connected to the child site must be Stripe.

### Permissions

Permissions are set on a per site basis. Administrators on the parent site however, always have access to Admin reporting for child sites but not actual Admin access on the child sites themselves.

* **Reports**

  * Admin on Parent site can see all reporting for child sites. If a user is only Admin on a child site, they will only be able to see Admin reports for Fundraisers created on that child site.

* **Tax Receipt settings**

  * Tax Receipt settings are entered and managed from the Parent site. This information is pushed down to child sites automatically.

### Creating Fundraisers

When creating fundraisers on a child site, depending on global admin settings (See [**Admin \> General Settings**](admin-general-settings.md)), you may be given the option to "**Only show on the site this campaign was created on**".

If this option is **enabled** , the fundraiser **will not be**mirrored publicly to the Parent site for donors to see. Admins on the Parent site will still see it, but will not be able to edit it or make any changes from the Parent site this must be done from the Child site (sub-site).

If this option is **disabled** , the fundraiser **will be**mirrored publicly to the Parent site, and can be edited from both the parent and child site.  
Editing child-site created fundraisers from the parent site is **not**possible if one of these is true:

* Parent site has custom fields in the "Start A Fundraiser" process.

* Child site has custom fields in the "Start A Fundraiser" process.

* Fundraiser was created from a Master Template.

## Fundraiser Approval on Subsites (Charity Partners)

**NOTE:** These rules only apply to fundraisers that are created from Child sites.

Fundraisers created from Parent sites have no relevance to Child sites, so these rules do not apply.  

| **Parent Approval Enabled** | **Child (Subsite) Approval Enabled** |  **Can be Approved On**  |
|-----------------------------|--------------------------------------|--------------------------|
| Yes                         | No                                   | Parent                   |
| Yes                         | Yes                                  | Either parent or subsite |
| No                          | Yes                                  | Subsite                  |

If you have questions regarding our Parent / Child Relationship, reach out to your dedicated Partner Success Manager, or our customer support team (support@crowdchange.co).

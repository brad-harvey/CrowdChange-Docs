---
title: How Global Inventory Works
slug: how-global-inventory-works
collection: chadmin
source_url: https://chadmin.crowdchange.help/ct/how-global-inventory-works
nav_path:
- How Global Inventory Works
nav_order: 154
parent: null
children: []
page_type: concept
tags:
- communications
- purchase-options
crm_relevant: true
description: Global inventory allows your organization to use one shared stock pool across multiple fundraisers. It is designed for situations where the same physical inven…
last_modified: '2026-09-22T14:36:16.043Z'
retrieved: '2026-10-14'
audience: Charity Admins (CrowdChange admin help center space CT)
word_count: 729
---

<!-- Source: https://chadmin.crowdchange.help/ct/how-global-inventory-works | Nav: How Global Inventory Works | Mirrored 2026-10-14 -->

# How Global Inventory Works

Global inventory allows your organization to use one shared stock pool across multiple fundraisers. It is designed for situations where the same physical inventory is sold through more than one fundraiser and every sale should draw from the same central supply.

For example, if several fundraisers sell the same t-shirt, hoodie, meal ticket, or merchandise item, global inventory helps prevent your organization from selling more than the total quantity available.

Each fundraiser still controls how the item appears to buyers, including its price, images, description, access code rules, and purchase limits. **Global inventory only controls the shared stock count.**

**Important:** Global inventory does not replace purchase options. Instead, it adds shared stock tracking to purchase options.

**When to Use Global Inventory**

Use global inventory when:

* The same item is sold across multiple fundraisers.

* The item comes from one central stock supply.

* Your organization needs to prevent overselling across fundraisers.

Global inventory may not be necessary when:

* The item is sold through only one fundraiser.

* Each fundraiser has its own separate stock.

* The item does not have a stock limit.

* You only need a per-fundraiser purchase limit.

**Link Global Inventory to Purchase Options**

Once global inventory has been set up, it can be linked to purchase options on a fundraiser or Blueprint.

How you link the inventory depends on whether the purchase option has variations.

**Purchase Options Without Variations**

Use this method when the purchase option represents one item and buyers do not select from different variations.

1. Open the purchase option.

2. Select **Global inventory** as the inventory source.

3. Select the appropriate global inventory item.

4. Select the matching variant.

5. Save the purchase option.

Once saved, purchases made through that fundraiser will reduce the stock for the selected global inventory variant.

**Purchase Options With Variations**

If buyers choose from variations such as size, colour, ticket type, or meal choice, each purchase option variation must be linked to its matching global inventory variant.

1. Open the purchase option.

2. Add or edit the purchase option variations.

3. Link each variation to the matching global inventory variant.

4. Save the purchase option.

**Important:** When a purchase option has variations, link global inventory to **each individual variation**, rather than only to the parent item.

For example:

**Fundraiser variation:** Small t-shirt

**Global inventory:** T-shirt / Small

**Fundraiser variation:** Medium t-shirt

**Global inventory:** T-shirt / Medium

**What Happens at Checkout**

When a buyer selects an item linked to global inventory, CrowdChange checks whether enough shared stock is available.

If sufficient stock is available, the buyer can continue through checkout. When the purchase is completed, the shared stock is updated automatically.

If the available stock changes before the purchase is completed, the buyer cannot purchase more than the quantity remaining.

This helps protect shared inventory when multiple fundraisers are selling from the same stock at the same time.

**What Happens When a Purchase Is Refunded or Rolled Back**

When a purchase linked to global inventory is refunded or rolled back, the shared inventory quantities are updated automatically.

This means the inventory associated with the refunded or rolled-back purchase is returned to the shared stock without requiring a manual inventory adjustment.

**Editing Inventory Links After Purchases**

After an item linked to global inventory has been purchased, some inventory settings may become locked. This helps protect purchase history and prevents inventory from being moved accidentally after sales have already occurred.

The linked inventory can still be viewed, but the inventory source or selected global inventory item may not be freely changed.

**Important:** If an inventory link needs to be changed after purchases have already been made, review the potential impact on existing purchases and inventory before making changes.

**What Happens When Linked Inventory Becomes Unavailable**

When global inventory is archived or deleted, it is no longer available for new inventory links. Existing links are preserved so previous purchases remain associated with the correct inventory.

If unavailable inventory is still linked to an active purchase option:

* A purchase option without variations may become unavailable for sale.

* For a purchase option with variations, the unavailable variation may be hidden.

* Other active variations can continue to be sold if they are still available.

If archived inventory is restored, it becomes available again. However, some linked purchase options may need to be reopened manually before buyers can purchase them again.

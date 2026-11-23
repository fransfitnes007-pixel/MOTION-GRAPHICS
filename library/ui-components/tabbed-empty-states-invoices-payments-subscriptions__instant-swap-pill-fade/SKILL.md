---
name: tabbed-empty-states-invoices-payments-subscriptions-instant-swap-pill-fade
description: A tab row (Invoices, Payments, Subscriptions) above a dashed, pale panel holding an icon tile, a 'No ... Yet' heading, two lines of grey text and one or two buttons. Use for the empty views of a billing or records screen.
---

# Tabbed empty states, invoices payments subscriptions

**Code name:** Instant swap, pill fade.

## What you see
A white page. Top left a row of three tabs, 34px tall, each an 18px outline icon and a 14.5px medium label: Invoices (receipt), Payments (badge with a dollar), Subscriptions (credit card). The selected tab has a `#f4f4f5` pill behind it and black icon and text; the others are grey. Under the row a panel about 503 x 308 (shown 1.75x) with a pale `#fafafa` fill and a 1px dashed `#e3e3e6` border, 13px corners. Centred in it: a 40px grey tile with the tab's icon, a 17.5px 'No Invoices Yet', two lines of 14px grey help text, and the buttons. Invoices has a black 'Create Invoice' with a plus and a white 'Import Invoice' with a tray icon; Payments has a black 'Record Payment'; Subscriptions has a black 'Create Subscription'. In the clip the cursor clicks Payments, then Subscriptions. The content changes on the same frame as the click with no fade, and the highlight pill catches up about 0.2s later. The demo clicks Payments at 1.1s, Subscriptions at 2.9s and Invoices at 4.7s.

## When to use it
The blank state of a screen with several record types, a billing or CRM area before any data exists, or a settings page with empty sections. The tabs keep one panel small instead of stacking three empty boxes.

## How it works
State is just the selected tab index. Content (icon, title, text, buttons) is looked up from an array by that index and swapped at once. The tab highlight is a background colour that fades in on the new tab and out on the old one over about 0.18s, which is why the pill lags the content. Buttons are centred by measuring their widths, so one button or two both sit in the middle.

```js
show(cur)                                   // content swaps instantly
const k = eo(seg(t - since, 0, .18))        // pill fade
newTab.bg = rgba(244,244,245,k);  oldTab.bg = rgba(244,244,245,1-k)
```

The real block is a shadcn-style Tabs with an empty-state block per tab; its source is locked. The copy and icons in the demo follow the clip.

## Numbers that matter
| | |
|---|---|
| Tab | 34px tall, radius 9, 8px side padding, icon 18, text 14.5px 500 |
| Selected | background `#f4f4f5`, text `#0b0b0c`; others `#78787c` |
| Panel | 503 x 308, radius 13, 1px dashed `#e3e3e6`, `#fafafa` |
| Icon tile | 40px, radius 11, `#f1f1f2` |
| Title / text | 17.5px 500 / 14px `#737378`, line height 23 |
| Buttons | 37px tall, radius 9, 12px apart, primary `#171717` |
| Pill fade | 0.18s ease-out |

## Sound
Silent.

## Adapt it
- `tabs`: names, icons, titles, help text and buttons for each tab.
- `width` and `panelH`: the block size.
- `pillFade`: set to 0 to match the content swap exactly, or 0.25 for a softer highlight.
- `clicks`: scripted order, replaced by real clicks in your app.

## Files
- `code/demo.html` runs on its own and loops. Everything it draws is a function of time, with `CONFIG` at the top of the script.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Empty State With Tabs" by shadcnui-blocks on 21st.dev (https://21st.dev/@shadcnui-blocks/components/empty-state-03), MIT. This demo is an original recreation written from the public preview.

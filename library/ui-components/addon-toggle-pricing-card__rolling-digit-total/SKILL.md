---
name: addon-toggle-pricing-card-rolling-digit-total
description: "A white pricing card with a list of included features (locked-on switches) and optional add-ons (live switches), over a grey total box whose price rolls digit by digit as you switch add-ons on and off. Reach for it for one-time purchases with optional extras."
---

# Add-on toggle pricing card

**Code name:** Rolling digit total.

## What you see
A card with a title and three included rows (a grey icon circle, a bold name, "Included", and an indigo switch that is on and locked), then three add-on rows with pale-indigo icons, a one-line description with its price, and a grey switch. A pointer taps the first add-on: its knob springs 20px across while the track turns indigo over 150ms, and the total at the bottom changes from $149 to $198, with only the changed digits rolling (the old digit slides up 60% and fades as the new one rises from below). Switching the second add-on on, the first off and the third on gives $227, $178 and $197.

## When to use it
A single-product checkout with a few optional extras, where the running total should react visibly. Digits rolling draws the eye to the price change without a modal. Wrong with many products (use a cart), or where the total must be announced to a screen reader on every change; the source sets `aria-label` on the whole figure for this.

## How it works
`Toggle` is a `role="switch"` button whose knob is `motion.span layout` with `transition={{ type: "spring", stiffness: 500, damping: 32 }}`. The knob only changes its `left-1` or `right-1` class; framer's layout animation turns that jump into a spring, so there is no x value to manage. The track changes colour with `transition-colors`.

`RollingPrice` renders each character in its own `inline-block` wrapper with `AnimatePresence mode="popLayout" initial={false}`. The key is `ch + i`, so a character only animates when it differs from the one at that index before:

```tsx
<motion.span key={ch + i} initial={{ y: "60%", opacity: 0 }} animate={{ y: 0, opacity: 1 }}
  exit={{ y: "-60%", opacity: 0 }} transition={{ type: "spring", stiffness: 380, damping: 30 }}>
```

The wrapper is `inline-flex overflow-hidden tabular-nums`, so a digit leaving or entering is clipped to the line. The total is derived with `useOrder(product, chosen)`: base price plus the chosen add-ons, formatted with `Intl`. The "Get your site" link carries the choices as `?addons=a,b`.

## Numbers that matter
| | |
|---|---|
| Card | rounded-[28px], white, hairline border black/6, shadow 0 18px 44px -24px |
| Row | padding 14px 0, dividers black/6; icon circle 40px; name 15px semibold; sub 12px |
| Switch | 48 x 28, knob 20px, 4px inset; on = accent #5b5ce6, off = black/15 |
| Knob | layout spring stiffness 500, damping 32 |
| Total box | bg #f4f5f7, rounded-3xl, 20px padding; price 48px bold |
| Digit roll | y 60% to 0, exit to -60%, spring 380 / 30, key = char + index |

## Sound
Silent. Pair it with a soft UI tick on the state change if it sits in a video.

## Adapt it
- The included list and the add-ons (name, description, price in cents).
- The accent colour for switches and the button.
- Spring stiffness for a snappier or softer roll.
- Hide prices on rows by setting `hidePrice`, as the source does for the first visit.

## Files
- `code/demo.html` runs on its own and loops. Product, add-ons and prices are invented.

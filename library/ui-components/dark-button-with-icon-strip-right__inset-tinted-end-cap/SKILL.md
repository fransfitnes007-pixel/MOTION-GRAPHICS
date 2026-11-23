---
name: dark-button-with-icon-strip-right-inset-tinted-end-cap
description: A solid near-black button with a 36px lighter strip at its right end holding a 60%-opacity chevron. Reach for it for Next or Continue actions where the arrow should read as a separate end cap.
---

# Dark button with icon strip on the right

**Code name:** Inset tinted end cap.

## What you see
A 36px tall rounded (8px) button in near-black `#18181b` with white 'Next' in 14px medium. The right 36px is a second panel, white at 15% opacity over the button colour, holding a chevron at 60% opacity. In the demo a cursor moves over it (the fill lightens to `#2d2d30`), clicks (it shrinks 2% for 0.15s), then moves to a white bell button with a black '3' badge. The bell turns light grey on hover and the badge shrinks away on click, and comes back before the loop restarts. The bell is what the 21st.dev preview video for this page shows; the page's own usage example is the Next button.

## When to use it
Wizard steps, pagers and any primary action that moves forward. Swap the side for a back button (see the sibling). The strip is decoration only (it ignores the pointer), so the whole button is one click target.

## How it works
One shadcn Button with extra right padding (`pe-12`, 48px) and an absolutely positioned span on the right edge: `inset-y-0 end-0 w-9`, `bg-primary-foreground/15`, centring the chevron. The button's own overflow clip gives the strip the same corner radius. The demo does the same with a flex box, a 36px strip and a measured width so it stays centred for any label. The press shrink and the bell are demo extras; the original has only the stock hover fade.

## Numbers that matter
- Height 36px, radius 8px, 14px medium text
- Padding: 16px left, 48px right; strip 36px wide
- Strip fill: label colour at 15%; chevron 16px at 60% opacity
- Hover fill `#2d2d30` from `#18181b` (primary at 90%)
- Bell button 36px, border `#e4e4e7`, badge 20px `#18181b`, 11px text

## Sound
Silent.

## Adapt it
- `label` and `stripSide` ('left' or 'right') switch between Next and Previous.
- `primary`, `primaryHover`, `onPrimary` for a brand colour.
- `stripAlpha` and `iconOpacity` for a stronger or quieter end cap.
- `showBell: false` to drop the notification button.

## Files
- `code/demo.html` runs on its own, loops in 6s, and has a `CONFIG` block at the top of the script.

## Credit
Idea: "Button" by originui on 21st.dev (https://21st.dev/@originui/components/button/button-with-highlighted-right-icon), MIT. This demo is an original recreation written from the public preview.

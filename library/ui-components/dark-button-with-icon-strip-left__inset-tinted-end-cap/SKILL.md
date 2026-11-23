---
name: dark-button-with-icon-strip-left-inset-tinted-end-cap
description: A solid near-black button with a 36px lighter strip at its left end holding a 60%-opacity chevron. Reach for it for Previous or Back actions.
---

# Dark button with icon strip on the left

**Code name:** Inset tinted end cap.

## What you see
A 36px tall rounded (8px) button in near-black `#18181b` with white 'Previous' in 14px medium. The left 36px is a second panel, white at 15% opacity over the button colour, holding a left chevron at 60% opacity. In the demo a cursor moves over it (the fill lightens to `#2d2d30`), clicks (it shrinks 2% for 0.15s), then moves to a white bell button with a black '3' badge. The bell turns light grey on hover and the badge shrinks away on click, and returns before the loop restarts. The bell is what the 21st.dev preview video for this page shows (it is the same video as the Next button's page); the usage example is the Previous button.

## When to use it
The back half of a Previous/Next pair, or any back action. Pair it with the right-hand sibling so both ends read as one control.

## How it works
One shadcn Button with extra left padding (`ps-12`, 48px) and an absolutely positioned span on the left edge: `inset-y-0 start-0 w-9`, `bg-primary-foreground/15`, centring the chevron. The button clips the strip to its corner radius. The demo uses a flex box with a measured width so it stays centred for any label. The press shrink and the bell are demo extras.

## Numbers that matter
- Height 36px, radius 8px, 14px medium text
- Padding: 48px left, 16px right; strip 36px wide
- Strip fill: label colour at 15%; chevron 16px at 60% opacity
- Hover fill `#2d2d30` from `#18181b` (primary at 90%)
- Bell button 36px, border `#e4e4e7`, badge 20px `#18181b`, 11px text

## Sound
Silent.

## Adapt it
- `label` and `stripSide` switch between Previous and Next.
- `primary`, `primaryHover`, `onPrimary` for a brand colour.
- `stripAlpha` and `iconOpacity` for a stronger or quieter end cap.
- `showBell: false` to drop the notification button.

## Files
- `code/demo.html` runs on its own, loops in 6s, and has a `CONFIG` block at the top of the script.

## Credit
Idea: "Button" by originui on 21st.dev (https://21st.dev/@originui/components/button/button-with-highlighted-icon), MIT. This demo is an original recreation written from the public preview.

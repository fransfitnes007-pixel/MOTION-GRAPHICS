---
name: glowing-plan-pills-free-pro-ultra-inset-rim-glow-active-select
description: Row of three dark capsule badges (Free green, Pro blue, Ultra purple) with a coloured rim and a bottom glow; clicking one makes it the active, brighter, slightly larger badge. Reach for it for plan labels or a tier picker.
---

# Glowing plan pills: Free, Pro, Ultra

**Code name:** Inset rim glow, active select.

## What you see
Three capsules, each 125 x 72 (radius 36) and 37px apart, in a row on a pale slate page (the video is light; the poster shows them over a dark photo, and the component takes a dark mode too). Each capsule is near-black with a 2.5px coloured rim that also bleeds inward about 20px, so the edge looks like lit glass and the middle stays dark. A small soft ellipse of lighter colour sits on the bottom edge like a lamp under the pill. The label is 24px semibold white: Free on green, Pro on blue, Ultra on purple.

The selected tier (Ultra at the start) is a little brighter, 5% larger, with a stronger coloured shadow beneath it and a slow glow pulse. Clicking another pill moves that state across over 0.35s while the pill dips 5% under the press. In the 1.5s video nothing but the glow changes; the demo loops through clicking Free, Pro and Ultra with a pointer.

## When to use it
Plan or tier labels in an account menu, a pricing comparison header, or a plan picker with three to four options. Works on light or dark pages. The dark centre carries white text well, but with more than four tiers the colours stop being distinguishable.

## How it works
Each pill is four stacked layers inside a rounded box:
```css
.rim   { background:#0a0b10; box-shadow: inset 0 0 0 2.5px RIM, inset 0 0 20px 3px RIM }
.lamp  { left:24px; right:24px; bottom:-1px; height:22px; border-radius:50%;
         background: radial-gradient(ellipse at 50% 100%, GLOW, transparent 72%); filter: blur(3px) }
.sheen { background: linear-gradient(180deg, rgba(255,255,255,.1), transparent 40%) }
```
The active state is one eased number `a` per pill (0.35s) driving `scale(1 + .05a)`, `brightness(.94 + .06a)` and the outer shadow colour and size. Press feedback is a 0.14s dip in scale around each click time listed in `CONFIG.picks`.

## Numbers that matter
| | |
|---|---|
| Canvas | 800 x 600, pills 125 x 72, pitch 162 |
| Rim | 2.5px plus a 20px inset glow |
| Colours | rim #16a06c, #2749d4, #7a2bd6; glow #3ff0a6, #7d97ff, #d072ff |
| Active | scale 1.05, brightness 1.0 (others .94), shadow 14px to 36px blur |
| Timing | state change 0.35s ease-out, press dip 0.14s |

## Sound
Silent.

## Adapt it
- `CONFIG.tiers`: label, rim and glow colours; add a fourth object for a fourth tier.
- `CONFIG.mode` 'dark' for a dark page (the shadow goes flat there).
- `CONFIG.startActive` and `picks` for which tier is lit and when it changes.
- Pill size is in the `.pl` CSS rule and `pitch` for the spacing.

## Files
- `code/demo.html` runs on its own and loops. Placeholder art is CSS and SVG only.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Tier Badge" by abushaidislam7 on 21st.dev (https://21st.dev/@abushaidislam7/components/tier-badge), MIT. This demo is an original recreation written from the public preview.

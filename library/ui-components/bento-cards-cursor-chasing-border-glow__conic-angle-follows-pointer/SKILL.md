---
name: bento-cards-cursor-chasing-border-glow-conic-angle-follows-pointer
description: A grid of five white cards where the border glows with a short coloured arc that points at the cursor. Reach for it on feature grids for a Cursor-style hover highlight.
---

# Bento cards with a border glow that chases the cursor

**Code name:** Conic angle follows pointer.

## What you see
Five cards in a 12-column grid (24px page padding, 16px gaps): two stacked on the left, one tall in the middle, two stacked on the right. Each has a thin grey border, a small icon in a bordered square at top left, and at the bottom a semibold title (24px, tight) and a grey one-line description.

With the pointer far away nothing glows. As it comes within 64px of a card, a 3px arc, about 80 degrees wide, fades in over 0.3s on the card's edge facing the pointer. The arc is pink at one end, gold, then green and blue-grey, and it slides round the border as the pointer circles the card, catching up in about 0.35s. Leaving the zone fades it out. Neighbouring cards can light up together when the pointer sits in the gap.

The demo scripts one lap across and around all five cards in 8s.

## When to use it
Feature grids and pricing cards on light or dark pages where you want a hover reward without moving the layout. It needs a pointer; give touch devices a static border.

## How it works
Each card gets a ring (a 3px transparent border that is masked so only the border shows) containing a fill of coloured blobs. A conic mask reveals only the part of that fill facing the pointer. The mask's start angle chases the pointer's angle from the card centre.

```js
angle = atan2(cy - cardCy, cx - cardCx) * 180 / PI + 90
arc.mask = conic-gradient(from ${angle - spread}deg, #0000 0deg, #000 ${spread}deg, #0000 ${spread * 2}deg)  // spread 40
active = pointer within card + 64px && outside the dead centre
angle += shortestDelta * (1 - exp(-dt / .35));  ringOpacity += (active - ringOpacity) * ...
```

Angle and opacity are integrated at 120 steps a second into a table so playback is deterministic. The colour blobs are matched to the clip by eye.

## Numbers that matter
| | |
|---|---|
| Arc | 40 degrees spread each side, 3px wide |
| Proximity | 64px beyond the card |
| Colours | `#dd7bbb` `#d79f1e` `#5a922c` `#4c7894` |
| Follow | 0.35s catch-up, 0.3s fade |
| Grid | 12 columns, 24px padding, 16px gap, cards radius 24 |
| Loop | 8s |

## Sound
Silent.

## Adapt it
- `CONFIG.gradient` for another palette.
- `CONFIG.spread`, `proximity`, `borderWidth` for arc size and trigger distance.
- `CONFIG.follow` and `fade` for response.
- `CONFIG.cards` for grid areas, text and icons.

## Files
- `code/demo.html` runs on its own and loops; every frame is `render(t)`. Edit the `CONFIG` block at the top of its script.
- `media/poster.jpg` is the page's preview image.
- Similar looks already in the library: `glass-card-border-beam__conic-light-chrome-rim`, `black-chrome-glass-cards__travelling-edge-beam`, `dark-tilt-card-with-cursor-glare__perspective-tilt-radial-glare`.

## Credit
Idea: "Glowing Effect" by manuarora700 on 21st.dev (https://21st.dev/@manuarora700/components/glowing-effect), MIT. This demo is an original recreation written from the public preview.

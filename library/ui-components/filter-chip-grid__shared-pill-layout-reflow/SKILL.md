---
name: filter-chip-grid-shared-pill-layout-reflow
description: Segmented filter chips with live counts above a grid of white cards. Picking a chip slides a black pill to it, fades the cards that no longer match and glides the rest into the freed slots. Reach for it for asset libraries, file lists and any filterable card grid.
---

# Filter chip grid

**Code name:** Sliding pill with layout reflow.

## What you see
A near-white page. Top left, four outlined chips with a count in smaller grey: "All 9", "Images 4", "Clips 2", "Docs 3". The active chip is a near-black `#212121` rounded pill with white text. Under it, nine white cards in three columns, each 230 by 128 with 20px corners, a thin border and a soft shadow, showing a file name (22px) and a size (18px grey).

In the 5.6s clip the cursor clicks Clips at about 0.8s. The black pill slides from All to Clips in about 0.35s, seven cards fade out and shrink slightly, and the two Clips cards ("onboarding", "teaser-cut") glide up to the first two slots. Docs, Images and All follow; Images leaves a fourth card on a second row, and All brings every card back. The demo repeats that order over 6s: Clips at 0.85s, Docs at 1.95s, Images at 3.0s, All at 3.9s.

## When to use it
Any grid where a handful of categories filter a modest set of items, such as assets, templates, integrations or a portfolio. The count on each chip tells people what they will get before they click. Not for filters that combine (multi-select) or lists with hundreds of items.

## How it works
Two shared-layout ideas. The pill is one element whose left and width interpolate between chip rectangles. The cards keep their identity: each card's position is interpolated from its slot in the previous filter to its slot in the new one, with a spring; cards that were hidden fade and scale in from 0.94, and ones that leave fade and shrink to 0.94.

```js
const rq = spring(seg(t, tClick, tClick + .55), 6, 8)
left = lerp(slotPrev.x, slotNow.x, rq)   // top likewise
```

In the framework original this comes from framer-motion's layout animation, with the chips as a radio group (hence "accessible, segmented radio chips" on the page). The usage example filters nine assets by `kind` with `match` functions.

## Numbers that matter
| | |
|---|---|
| Chip | 58px high, 12px radius, 22px/500 text, count 16px `#85858b`, border `#e3e3e6` |
| Pill | `#212121`, slides in 0.38s ease-out |
| Card | 230 x 128, 20px radius, gap 15px across and 16px down, text 22px / 18px |
| Reflow | spring k=6, f=8 over 0.55s; fade 0.33s |
| Order in demo | Clips, Docs, Images, All; 6s loop |

## Sound
Silent.

## Adapt it
- `CONFIG.items` with name, size and kind; `CONFIG.filters` with label and kind key.
- `columns`, `cellW`, `cellH`, `gap` for the grid.
- `pillColor` for a brand colour.
- `clicks` to change the order and timing.

## Files
- `code/demo.html` runs on its own and loops. It is a recreation made from watching the video and reading the usage example.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Filter Grid" by ddoemonn on 21st.dev (https://21st.dev/@ddoemonn/components/filter-grid), MIT. This demo is an original recreation written from the public preview.

---
name: unit-dot-grid-fill-count-one-dot-per-unit-ring-regroup
description: A big number counts up while a grid with one dot per unit lights up orange, then every dot flies into a ring that shows a share with the percentage in the middle. Rebuilt by eye from a public motion video (see Credit); use it in app promos and launch reels.
---

# Unit dot grid fill with count

**Code name:** One dot per unit, regroup into a ring. Rebuilt by eye from a public motion video; original code, credited below.

## What you see
Warm black (#141210). A big heavy number climbs from 0 to 1,089 between 0.35s and 2.2s (fast then slowing) with "places mapped" under it. Below (tall) or beside it (wide) a 33 x 33 grid of dim dots lights up one dot per unit in orange, roughly top to bottom with a scattered edge, each dot doing a small pop as it lights. At 2.7s every dot leaves the grid at its own moment and flies into a four-lane ring; 96.8% of the ring is orange and the rest grey, and "96.8%" counts up in the middle.

## When to use it
When a number should feel like a quantity of things: users, videos posted, places, accounts. The ring beat turns the same dots into a share. Works best vertical. Wrong for numbers over about 3,000 (dots get too small) or for money.

## How it works
Every dot knows when the count passes it: with `n = N * eo(u)`, dot of rank r lights at `u = 1 - (1 - r/N)^(1/3)` (the inverse of ease-out cubic), so the grid and the number never disagree.
```js
const lit = 1 - Math.pow(1 - r / N, 1 / 3)
const tl = c0 + (c1 - c0) * lit                       // the moment this dot turns orange
// ring slot by rank: 4 lanes, so the lit share is one continuous arc
const lane = r % 4, ang = -PI/2 + floor(r/4) / (N/4) * 2*PI
```
Rank order is row index plus a seeded random 0..7, which gives the ragged "data arriving" edge. Each dot's flight to the ring starts at a seeded offset in the first 35% of the move.

## Numbers that matter
| | |
|---|---|
| Count | .35s to 2.2s, ease-out cubic |
| Dot pop | .22s, up to 25% bigger then back |
| Grid | 33 x 33, spacing 25px tall / 18px wide, dot radius 30% of spacing |
| Ring | 2.7s to 3.6s, each dot ease-in-out over 65% of the window, radius 300 (tall) |
| Colours | #f26a1b lit, white 9% unlit |
| Number | 140px weight 900 |

## Sound
A granular tick stream that thins out as the count slows, then one whoosh for the regroup. The demo is silent.

## Adapt it
- `total` and `cols` (cols x rows >= total).
- `label`, `share`, `shareLabel`, `sep`.
- `accent`.

## Files
- `code/demo.html` runs on its own; every value to change is in the `CONFIG` block at the top of the skill script.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "motionvideo.xyz gallery: Ondefica app motion reel" by @jesscaroline7 (https://x.com/jesscaroline7/status/2104336637752955094), Video belongs to its creator; not included. Recreated by eye from watching the public video; this demo is original code and contains none of the video. Full notices: `THIRD_PARTY_NOTICES.md`.

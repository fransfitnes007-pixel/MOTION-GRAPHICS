---
name: photo-tile-grid-paper-map-unfold-center-plus-corners-hinge
description: One big photo shrinks into a tile, then a 3x3 grid unfolds from behind it like a paper map: first up, down, left and right, then the four corners. Rebuilt by eye from a public motion video (see Credit); use it in app promos and launch reels.
---

# Photo tile grid paper map unfold

**Code name:** Centre, plus, corners hinge unfold. Rebuilt by eye from a public motion video; original code, credited below.

## What you see
A large rounded photo fills the middle of an off-white frame. From 0.15s it springs down to a 220px tile. At 0.75s four tiles flip out from behind it, hinged on the edge they share with it (up, down, left, right), each rotating 180 to 0 degrees in 0.26s. At 0.92s the four corner tiles flip out sideways from the up and down tiles. By about 1.2s it is a flat 3x3 grid with 14px gaps that slowly pushes in 3%. At 2.6s it folds back (corners first) and the centre grows back to full size, so the loop closes.

## When to use it
Showing "lots of photos/screens/creators" after one hero: a gallery, a feed, a library, the moment a single result becomes many. Reads as tactile and calm. Wrong for more than 3x3 (the unfold order stops being readable) or for text-heavy cards.

## How it works
Each tile is a DOM box with `backface-visibility:hidden` inside a `perspective:1600px` parent. It rotates 180 degrees around the edge it shares with its parent tile, so at 0 it lies face-down on top of its neighbour and is invisible; it shows from 90 degrees on.
```js
// right-hand tile: hinge on its left edge
e.style.transformOrigin = '0% 50%'; e.style.transform = `rotateY(${-180 * (1 - p)}deg)`
// below: hinge on its top edge
e.style.transformOrigin = '50% 0%'; e.style.transform = `rotateX(${180 * (1 - p)}deg)`
```
Corners use the same sideways hinge as the left/right tiles but start .17s later. The centre tile has the highest z-index so unfolding tiles come out from under it.

## Numbers that matter
| | |
|---|---|
| Shrink | spring f 1.5 zeta .8, from 2.9x (wide) / 3.6x (tall) |
| Plus tiles | start .75s, .26s each, ease-out cubic |
| Corner tiles | start .92s, .26s |
| Tile | 220px, 14px gap, 22px radius at 1920 wide |
| Fold back | .45s ease-in-out, corners in the first 65%, plus in the last 65% |

## Sound
A paper flap or soft card flick per group (two sounds: plus, corners), 40 ms apart, quiet under the music. The demo is silent.

## Adapt it
- `CONFIG.photos`: nine `background` values; use `url(...)` for real photos.
- `tile`, `gap`, `radius`.
- `t.plus`, `t.corners` to put the two flips on beats.

## Files
- `code/demo.html` runs on its own; every value to change is in the `CONFIG` block at the top of the skill script.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "revid.ai Claude Opus 5.5 wall #8: Develop: a photo print app launch" by @twoclipping (https://x.com/twoclipping/status/2103835273813496100), Video belongs to its creator; not included. Recreated by eye from watching the public video; this demo is original code and contains none of the video. Full notices: `THIRD_PARTY_NOTICES.md`.

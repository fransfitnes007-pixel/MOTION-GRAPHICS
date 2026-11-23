---
name: coverflow-poster-ring-preserve-3d-rotatey
description: "A carousel of 14 vertical video covers arranged in a ring around the camera, spinning up from behind, with a niche label under the front cover, a glass caption bar, then the front cover rushing the lens into a white flash."
---

# Coverflow poster ring

**Code name:** Preserve-3d rotateY.

## What you see
Fourteen 280x498 vertical covers sit on a ring of radius 900px, seen from inside-front. The ring tilts 8 degrees down, fades in and pushes up to the camera over 0.55s, and turns 205 degrees in 1.6s while drifting a little more with time. The covers facing the camera are opaque; ones on the far side fade out. Each front cover shows a white pill with its category under it. A frosted caption bar rises under the ring and the words arrive in it. From 2.95s the whole ring flies 1900px toward the lens, blurs, and a white flash covers the cut.

## When to use it
Showing breadth: many categories, templates or products, all at once, before zooming into one. It needs real covers or screenshots to sell it; with blank placeholders it looks empty. The flash at the end is what joins it to the next scene, so keep it if the next scene starts bright.

## How it works
A zero-size wrapper sets `perspective: 1500px`. Inside it a `preserve-3d` ring container carries the camera move. Each tile is placed once with `rotateY(angle) translateZ(900px)` and never changes. Only the ring rotates.

```js
const rot = -lerp(0, 205, eio(seg(t, 1.6, 3.2))) - t * 6
S(ring3d, { transform: `translateZ(${-RR + 60 + (1 - enter) * -260 + exit * 1900}px) rotateX(${-8 + exit * 8}deg) rotateY(${rot}deg)` })
// per tile: facing = cos(angle + rot); opacity = clamp((facing + .35) * 1.4); pill opacity = clamp(facing * 3 - 1.6)
```
`translateZ(-RR + 60)` pulls the ring back by its own radius so the front cover lands at the focal plane. The opacity rule by `cos` hides back-facing covers without needing `backface-visibility`.

## Numbers that matter
| | |
|---|---|
| Ring | 14 tiles, radius 900px, tile 280x498, radius 22px, 3D origin at (960,430) |
| Camera | perspective 1500px, ring tilt -8 degrees, back off 260px at start, +1900px at exit |
| Spin | 205 degrees over 1.6s (`eio`) plus 6 degrees per second drift |
| Enter | 1.6s to 2.15s, `eo5`; exit 2.95s to 3.32s, `ei4`, blur up to 8px |
| Flash | white layer, in 3.08s to 3.25s (`ei`), out to 3.5s |
| Caption | glass bar 800x150 at (560,868), words in via the blur-rise line |

## Sound
A whoosh can peak at the cut into this scene and another can lead into the next.

## Adapt it
- `NICHES` and the cover images (replace `coverBg(i)` with `url(...)`).
- `RN` and `RR`: more tiles need a bigger radius to avoid overlap.
- The total spin (205) and `T0` timing.
- Remove the `flash` if the next scene is dark.

## Files
- `code/demo.html`: covers are gradient placeholders.

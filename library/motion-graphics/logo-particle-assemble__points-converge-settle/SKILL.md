---
name: logo-particle-assemble-points-converge-settle
description: "1,200 glowing points swirl in from the frame edges, converge into the shape of a monogram letter, settle with a shrinking jitter and flash into the solid glowing letter. Reach for it as the logo reveal at the end of a film or the brand beat after a build-up."
---

# Logo particle assemble

**Code name:** Points converge settle. **From:** original build for this library.
Original code; informed by the structure of popular AI-made showreels (see motionvideo.xyz and revid.ai).

## What you see
On a dark stage with a faint blue centre glow, points of white and blue fade in from 0.3 s, scattered across the frame, and spiral inward, each with its own delay (up to 1.1 s) and number of turns (0.6 to 1.3). By about 3.0 s they have all reached positions that spell a large letter A. From 3.0 s to 4.0 s they jitter in place by up to 7 px with the jitter dying away and the points swelling 35 %. At 4.06 s a soft white flash fires, the points hand over to the solid letter (white to pale blue with a blue glow, starting at 105 % scale) which holds until 5.2 s and fades out by 5.85 s, so the loop restarts on an empty stage.

## When to use it
The logo or monogram hit at the end of a film, an app icon reveal, or a name card where the build-up should feel like energy collecting. It is wrong for a quiet, premium beat, and a very thin letterform will not read as dots.

## How it works
The shape comes from the font, not from a path. A big `A` is drawn to an offscreen canvas; `getImageData` collects every third pixel whose alpha is over 128 (about 16,000 candidates); the candidates are shuffled with a seeded RNG and thinned by dart throwing on a hash grid with a minimum distance that starts at 14 px and drops by 0.5 until 1,200 points fit. That gives an even stipple with no clumps. Each particle then has a start angle `a0`, start radius `r0` (0.55 to 1.3 of the half-diagonal), a delay and a turns count. Position at eased progress `e` is polar around the centre:

```js
angle  = at + (a0 - at) * (1 - e) + turns * 2PI * (1 - e)^2
radius = lerp(r0, rt, e)       // rt, at = target polar coordinates
```
so the points spiral and land exactly on their targets. Settling adds `sin`/`cos` offsets with per-particle frequencies scaled by `exp(-3.2 * u)`. Every dot is a small radial gradient drawn additively (`lighter`), so overlaps glow. All randomness is a mulberry32 stream with a fixed seed.

## Numbers that matter
| | |
|---|---|
| Particles | 1,200, radius 1.6 to 3.3 px (halo 3.2x) |
| Swirl in | 0.3 s to 3.0 s, `eio`, delay 0 to 1.1 s each |
| Settle | 3.0 s to 4.0 s, jitter 7 px, decay `exp(-3.2 u)` |
| Flash | peak at 4.06 s, width about 0.1 s |
| Solid letter | in 4.06 s, out 5.2 s to 5.85 s, glow blur 60 px |
| Colours | ink `#0b0b10`, paper `#f2f2f4`, accent `#4f8bff` |

## Sound
Silent in the demo. A rising shimmer under the swirl that peaks at 4.0 s, then a deep hit on the flash.

## Adapt it
- `LETTER` (one capital; two letters work if they are wide).
- `N` for density, and `ACC` / `PAPER` for the colours.
- `T_CONV`, `T_FLASH`: when the letter forms and when it turns solid.
- Replace the offscreen `fillText` with a drawn path or SVG image to assemble any logo shape.

## Files
- `code/demo.html` runs on its own, loops every 6 s, composes at 1920x1080 and at `?w=1080&h=1920`.
- `media/poster.jpg`

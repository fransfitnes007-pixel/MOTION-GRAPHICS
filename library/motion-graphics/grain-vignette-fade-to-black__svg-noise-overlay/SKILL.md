---
name: grain-vignette-fade-to-black-svg-noise-overlay
description: "A film-grain texture layer and a radial vignette over the whole frame, with the vignette gradient rewritten at the end to close the picture to black. Use it to make flat motion graphics feel photographic."
---

# Grain, vignette and fade to black

**Code name:** SVG noise overlay.

## What you see
Over the end card, the corners are darker than the centre and a very fine grain is visible on flat areas. In the last 0.6s the centre of the vignette goes from clear to 90% black and the edges from 60% to 100%, so the picture closes to black from the outside in.

## When to use it
The final layer of any dark video, and the closing fade. The grain is most useful on smooth gradients (the glow blobs) where banding would show in compressed video.

## How it works
Two elements at the top of the stack:

```css
#grain{position:absolute;inset:0;opacity:.07;mix-blend-mode:overlay;pointer-events:none;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='260' height='260'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.95' numOctaves='2' stitchTiles='stitch'/></filter><rect width='260' height='260' filter='url(%23n)'/></svg>")}
#vig{position:absolute;inset:0;pointer-events:none;background:radial-gradient(120% 90% at 50% 45%,rgba(0,0,0,0) 55%,rgba(0,0,0,.6) 100%)}
```
The noise is a static 260px tile (frame to frame it does not move, which keeps renders deterministic). The fade rewrites the vignette each frame: `radial-gradient(120% 90% at 50% 45%, rgba(0,0,0,p*.9) 0%, rgba(0,0,0,.6+.4p) 100%)` with `p = p(t, tEnd-.6, tEnd)`. Everything is a data URI, so there is no network request.

## Numbers that matter
| | |
|---|---|
| Grain | baseFrequency .95, 2 octaves, 260px tile, overlay blend, opacity .07 |
| Vignette | ellipse 120% by 90% at 50% 45%, clear to 55%, 60% black at the edge |
| Fade | last 0.6s, centre to 90% black, edge to 100% |

## Sound
Silent. A drone, if you use one, can fade out over the last 2.5s to match.

## Adapt it
- `opacity` of `#grain` (0.04 to 0.12).
- The vignette stops and strength.
- The fade length (0.6s).

## Files
- `code/demo.html` runs on its own and loops; `?w=1080&h=1920` gives the tall layout. 
- `code/fonts/` holds the fonts the demo loads.

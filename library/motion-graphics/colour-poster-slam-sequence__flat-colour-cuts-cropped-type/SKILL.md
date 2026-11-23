---
name: colour-poster-slam-sequence-flat-colour-cuts-cropped-type
description: "Four flat-colour full-frame posters that hard-cut on the beat every 0.6 s, each carrying one giant word cropped by the frame edges plus a small caption, with a 2-frame white flash on every cut. Reach for it as the fast montage section of a showreel or a beat-synced intro."
---

# Colour poster slam sequence

**Code name:** Flat colour cuts cropped type. **From:** original build for this library.
Original code; informed by the structure of popular AI-made showreels (see motionvideo.xyz and revid.ai).

## What you see
Beat 1 (0 to 0.6 s): orange-red poster, ink type, MOVE so wide that the M and E are sliced by the left and right edges. Beat 2: off-white, FAST pushed low and right so the A and S are cropped on three sides. Beat 3: blue, BOLD turned 90 degrees and running off the top and bottom, in off-white. Beat 4: yellow, ACME cropped at both sides and high in the frame. Every cut starts with two frames of pure white (0.067 s), the word then slams home from 112 % scale and a 9 % sideways offset in 0.2 s and drifts slowly for the rest of the beat; a caption fades in at the bottom-left and a studio tag at the top-right. The last 0.6 s is an ink rest beat with four colour dots so the 3 s loop breathes before restarting.

## When to use it
A fast montage in a showreel, a sting between sections, or any moment where four ideas have to land on four beats. It is wrong for sentences, as each word is only legible by shape, and for anything calm: the cadence is 100 BPM cuts.

## How it works
Each word is sized so its measured width is a chosen multiple of the frame width (1.22 to 1.46), which is what pushes letters past the edge:

```js
fs = (fac * along) / (ctx.measureText(word).width / 100)   // font size for the width you want
```
Posters are picked by `k = floor(t / .6)`; everything inside a poster is a function of `u = t - k * .6`. The slam is `eo5(u / .2)` mapped to scale `1.12 -> 1` and a sideways slide of `.09 * width` that alternates direction per poster; after that a slow `drift` of 5 % scale and 4 % travel keeps the frame alive until the next cut. The flash is a white rectangle drawn while `u < 2 / 30`. Captions use `letterSpacing` where the browser supports it, and the rotated poster rotates the canvas, so its width multiple is measured against the frame height.

## Numbers that matter
| | |
|---|---|
| Cut cadence | every 0.6 s (100 BPM), four posters, one rest beat |
| Flash | 2 frames at 30 fps = 0.067 s, pure white |
| Slam | 0.2 s, `eo5`, 112 % to 100 %, 9 % sideways |
| Word width | 1.22 to 1.46 times the frame (along the long axis when rotated) |
| Type | weight 900 display, 600 captions at 24 px, tracking 0.2 em |
| Colours | `#ff4b2b`, `#f2f2f4`, `#2f5bff`, `#ffd23f`; ink `#0b0b10` |

## Sound
Silent in the demo. A short snare or clap on each cut, locked to the white flash, with the kick on the first.

## Adapt it
- `POSTERS`: colour, word, width multiple, offset, rotation and caption for each poster.
- `BEAT` (0.6 s) and `FLASH` (frames over 30) to match your tempo.
- Colours: keep one background per beat and let type be ink or paper only.
- Number of posters: add one and lengthen `DUR` to match.

## Files
- `code/demo.html` runs on its own, loops every 3 s, composes at 1920x1080 and at `?w=1080&h=1920`.
- `media/poster.jpg`

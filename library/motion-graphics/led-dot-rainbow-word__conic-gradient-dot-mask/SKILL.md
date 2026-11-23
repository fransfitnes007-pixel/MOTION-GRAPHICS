---
name: led-dot-rainbow-word-conic-gradient-dot-mask
description: "A black LED-panel field of dots lit by a slowly spinning rainbow, with white words and a logo popping in on top. Reach for it as a hard pivot beat in a video, such as \"But, what if\"."
---

# LED dot rainbow word

**Code name:** Conic gradient dot mask.

## What you see
The screen cuts to black, covered in a grid of tiny dots. The dots are coloured by a rainbow that turns slowly, so the colour drifts across the panel while the dots stay crisp. "But," lands in bold white, "what if" follows in regular weight, and a round logo spins and springs in beside them. At speed (about 0.34s) it works as a jolt between two bright scenes. The demo slows it to 3s so you can study it.

## When to use it
A pivot in a voiceover, the turn from problem to answer. It is a contrast beat, so it needs light scenes either side. It wears out if held for more than a second or two, or used more than once in a video.

## How it works
Two layers. One draws a faint grey dot grid. The other is a full conic rainbow cut down to dots by a repeating radial-gradient mask, with the same 18px spacing, then rotated.

```css
.led .glow { background: conic-gradient(from 0deg at 50% 50%, #ff2e97, #ff7a3d, #ffd23d, #38bdf8, #7c3aed, #ff2e97);
  mask-image: radial-gradient(circle, #000 2.4px, transparent 3.2px); mask-size: 18px 18px; }
```
```js
S(ledGlow, { transform: `rotate(${t * 60}deg) scale(${1 + .05 * Math.sin(t * 8)})` })
```

The mask rotates with the layer, so the lit dots shimmer against the fixed grey grid. That moire is part of the look.

A layer at `inset: -40%` is the obvious choice, but it, uncovers the stage edges at some angles. That never shows in 0.34s, but it does on a loop, so the demo uses a square as wide as the stage diagonal. Use the square.

## Numbers that matter
| | |
|---|---|
| Dot grid | 18px spacing, grey dots `#2a2a2e` at 2.2px, lit dots at 2.4px |
| Rainbow | `#ff2e97 #ff7a3d #ffd23d #38bdf8 #7c3aed` |
| Rotation | 60 degrees per second, with a 5% scale pulse at `sin(t * 8)` |
| Words | 118px, bold then regular, `spring(k=8, f=12)`, rising 30px and scaling from .7 |
| Logo | 150px, `spring(k=7, f=12)` over .45s, rotating in from -40 degrees |
| Timing | "But" at 0, "what" +.02s, "if" +.22s |

## Sound

## Adapt it
- The words and the logo.
- `T_BUT`, `T_WHAT`, `T_IF`: set them to your voice timings.
- The five rainbow stops, or two stops of one brand colour for a calmer panel.
- Dot spacing: `background-size` and `mask-size` must stay equal.

## Files
- `code/demo.html` runs on its own. The logo is a CSS placeholder.

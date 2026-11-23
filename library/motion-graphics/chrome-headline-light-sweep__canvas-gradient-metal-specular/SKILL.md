---
name: chrome-headline-light-sweep-canvas-gradient-metal-specular
description: "A huge chrome headline on a dark stage that slams in with a scale punch and a short camera shake, then a diagonal light streak sweeps across the letters with a soft bloom. Reach for it as the title or product-name beat of a launch film or showreel."
---

# Chrome headline light sweep

**Code name:** Canvas gradient metal specular. **From:** original build for this library.
Original code; informed by the structure of popular AI-made showreels (see motionvideo.xyz and revid.ai).

## What you see
Dark stage with a faint blue pool of light. At 0.5 s the word LAUNCH appears at 155 % scale and shrinks to 100 % on a spring (it dips just under, then settles) while the frame shakes by up to 15 px for about 0.5 s. The letters are polished metal: bright top, a hard dark horizon band at about half height, a bright lower half, a faint reflection on the floor below. From 1.7 s to 3.0 s a slanted white band with a hot core crosses the word left to right, lighting only the letters; a blurred copy adds bloom and a thin horizontal flare rides the band. The word then holds, drifts 3 % larger and fades out from 4.2 s to 4.85 s so the loop restarts on the empty stage.

## When to use it
The one-word hit in a launch film, the name card in a showreel, or any title that should feel solid and expensive. It is wrong for long headlines (it needs about six letters at full width) and for a flat, paper-light look.

## How it works
The metal is a single vertical linear gradient across the cap height, built once on an offscreen canvas: stops at 0, .14, .30, .44, .485 and .53 (the dark band at `#07090e`), .57, .66, .78, .9, 1. A blue and warm tint is multiplied in with `source-atop`. Each frame the base is copied to a work canvas and the sweep is drawn on top with `globalCompositeOperation = 'source-atop'`, so light only lands on the letters:

```js
w.setTransform(1, 0, -.5, 1, sx + .5 * CY, 0)   // skewed band
gradient: 0 transparent, .45 / .55 white at .55 * I, .5 white at .98 * I, 1 transparent
```
where `I = sin(pi * progress)` fades the sweep in and out. Bloom is the same canvas drawn again with `ctx.filter = 'blur(28px)'` and `'lighter'`, alpha `.16 + .55 * I`. The reflection is the work canvas flipped about the baseline and masked with `destination-in` and a fading gradient. The slam is `scale = 1.55 - .55 * spring(u, 6.5, 10)`. Shake is two summed sines with an exponential decay `15 * exp(-8.5u)`. No stroke is drawn on the glyphs: strokeText exposes the overlapping contours of variable system fonts.

## Numbers that matter
| | |
|---|---|
| Size | 420 px font, scaled down to fit 86 % of the width; weight 900 |
| Slam | 0.5 s start, 0.42 s, spring k 6.5 f 10, from 155 % |
| Shake | 15 px, decay 8.5 per s, about 0.5 s |
| Sweep | 1.7 s to 3.0 s, `eio`, band 20 % of the width, skew -0.5 |
| Bloom | blur 28 px, alpha .16 to .71 |
| Colours | ink `#0b0b10`, metal `#fbfdff` to `#07090e`, blue tint `rgba(70,120,255,.28)` |

## Sound
Silent in the demo. Pair the slam with a low thump about 30 ms early and a short rising whoosh under the sweep.

## Adapt it
- `WORD` (up to about six capitals).
- The tint colours in the `tint` gradient for a gold, rose or green metal.
- `T_SLAM`, `T_SW0`, `T_SW1` to move the beats onto your track.
- Shake amplitude (15) and sweep band width (`W * .2`).

## Files
- `code/demo.html` runs on its own, loops every 5 s, composes at 1920x1080 and at `?w=1080&h=1920`.
- `media/poster.jpg`

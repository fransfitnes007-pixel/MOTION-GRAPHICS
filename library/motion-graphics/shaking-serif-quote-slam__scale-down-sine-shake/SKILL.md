---
name: shaking-serif-quote-slam-scale-down-sine-shake
description: "A huge white western-style serif quote slams onto a photo from 1.8x scale with a short horizontal shake and a red glow. Use it for the one line the whole video turns on."
---

# Shaking quote slam

**Code name:** Scale-down with sine shake.

## What you see
A photo with orange window light has been pushing in. At 0s of the beat the quote appears at 1.8x, snaps down to full size over 0.35s with an overshoot, and shakes left and right by up to 3px at about 10 Hz, dying over 0.8s. The type is Rye, a slab western face, 170px, white with a soft red glow. It fades out over the last 0.3s.

## When to use it
The single line a story pivots on: a warning, a threat, a punchline. Once per video. It needs a quiet frame around it, so do not stack cards on top.

## How it works
One element, `#q1`, positioned by its measured size so it centres on the screen:

```js
const k = backS(p(t, qa, qa + 0.35), 2.2), sh = Math.sin(t * 60) * 3 * S * (1 - p(t, qa, qa + 0.8))
tf(q, { x: W / 2 - q.offsetWidth / 2 + sh, y: H / 2 - q.offsetHeight / 2, s: lerp(1.8, 1, k), a: p(t, qa, qa + 0.1) * (1 - p(t, tEnd - 0.3, tEnd)), ox: '50%', oy: '50%' })
```
CSS: `font-family: Rye; color: #fff; line-height: 1; letter-spacing: .02em; text-shadow: 0 0 40px rgba(216,70,58,.7)`. The shake is horizontal only and uses `sin(t * 60)`, so it is deterministic. Rye must be preloaded before measuring `offsetWidth`.

## Numbers that matter
| | |
|---|---|
| Font | Rye, 170px wide / 150px tall, white |
| Glow | text-shadow 0 0 40px rgba(216,70,58,.7) |
| Slam | 0.35s, `backS(2.2)`, scale 1.8 to 1 |
| Shake | 3px amplitude, sin(t*60), fades over 0.8s |
| Fade in / out | 0.1s / 0.3s |

## Sound
A thud (`thud.wav`, 0.9) on the hit and a whoosh 0.08s later (0.5). Hold the music.

## Adapt it
- The words (two short lines).
- Font and glow colour.
- `qa` timing, shake amount (3) and speed (60).

## Files
- `code/demo.html` runs on its own and loops; `?w=1080&h=1920` gives the tall layout. Rye (SIL Open Font License, from Google Fonts) is copied into `code/fonts/` because the serif headline is half the look. The demo uses the system font stack. The demo draws gradient placeholders in CSS.
- `code/fonts/` holds the fonts the demo loads.

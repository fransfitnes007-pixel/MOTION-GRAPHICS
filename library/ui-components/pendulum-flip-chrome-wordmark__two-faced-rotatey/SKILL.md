---
name: pendulum-flip-chrome-wordmark-two-faced-rotatey
description: "A chrome wordmark floating on a breathing glow that dwells facing forward, sweeps through 180 degrees to a second face, dwells, then swings back, always reading the right way round. Use for a hero brand mark on a dark page."
---

# Pendulum-flip chrome wordmark

**Code name:** Two-faced rotateY card.

## What you see
A chrome wordmark, 620px wide, hovering on black with a white glow around the letters and a soft pool of light behind it that slowly brightens and dims. The whole thing drifts up 10px and back every 7 seconds. Every 13 seconds it swings: it holds still facing you for the first third, turns edge-on and through to the back over the next sixth, holds on the back face, then turns home over the last sixth. The letters never read mirrored, because the back face is a second copy of the artwork that is itself rotated 180 degrees.

## When to use it
A hero logo that should feel like a physical object but must never show its reverse. It suits a dark or near-black page, since the glow carries the effect. Wrong for a logo you want perfectly still, and for anything that has to stay legible during the swing (the mark is edge-on for a moment).

## How it works
Three layers. A backlight div with a radial-gradient bloom animates opacity and scale. A wrapper with `perspective: 1600` floats up and down. Inside it a `preserve-3d` card holds two absolutely positioned faces: the front, and a copy at `rotateY(180deg)`. Both have `backface-visibility: hidden`, so at any angle exactly one face shows, and past 90 degrees it is the back copy, which reads the right way round.

```tsx
<motion.div animate={{ rotateY: [0, 0, 180, 180, 0] }}
  transition={{ duration: 13, repeat: Infinity, ease: 'easeInOut', times: [0, 0.34, 0.5, 0.84, 1] }}
  style={{ transformStyle: 'preserve-3d' }}>
  <img style={{ backfaceVisibility: 'hidden' }} />
  <img style={{ backfaceVisibility: 'hidden', transform: 'rotateY(180deg)' }} />
</motion.div>
```
The `times` array makes the swing quick and the dwells long, so it is edge-on only briefly. One `ease: 'easeInOut'` applies to each segment, so every dwell-to-dwell sweep eases in and out on its own.

The demo changes two things. The artwork is a chrome-gradient text placeholder, with the glow done as two `drop-shadow` filters like the source. The swing is 14s rather than 13s, with the bloom at 5.6s, so the 7s float and the 5.5s bloom both divide the loop evenly and the clip loops without a jump.

## Numbers that matter
| | |
|---|---|
| Width | 620px (460px on the landing page) |
| Swing | 13s (`spinSeconds`), `rotateY [0,0,180,180,0]`, times `[0,.34,.5,.84,1]`, easeInOut |
| Float | `y [0,-10,0]`, 7s, easeInOut |
| Perspective | 1600px |
| Bloom | `1.15w x .42w`, blurred 26px, opacity `.55 > .95 > .55`, scale `1 > 1.06 > 1`, 5.5s |
| Glow filter (dark site) | `drop-shadow(0 0 30px rgba(255,255,255,.30)) drop-shadow(0 0 90px rgba(200,200,210,.14))` |
| Bloom colour (dark site) | `rgba(255,255,255,.16)` to `rgba(160,160,170,.07)` at 42% to transparent at 72% |

## Sound
Silent.

## Adapt it
- The artwork: any transparent PNG or SVG, on both faces.
- `spinSeconds` and the `times` array: widen the dwells for a calmer feel.
- The glow filter and bloom colours (the source has a violet set and a blue-on-white set too).
- Swing to 360 instead of 180 if the mark is symmetrical.

## Files
- `code/demo.html` runs on its own and loops in 14s.

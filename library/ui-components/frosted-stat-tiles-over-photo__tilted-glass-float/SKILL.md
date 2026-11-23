---
name: frosted-stat-tiles-over-photo-tilted-glass-float
description: "A portrait photo in a glass frame with five frosted stat tiles floating over it, each tilted in 3D and bobbing on its own timing while the numbers count up. Reach for it on a personal or founder hero where proof numbers should sit on the face of the page."
---

# Frosted stat tiles over photo

**Code name:** Tilted glass float.

## What you see
Left: location pills, a two-tone headline (name in ink, title in grey), a lede and a row of pill buttons, each sliding up 12 to 16px over .5 to .6s. Right: a white glass frame around a 4:5 photo that scales from .96 to 1. Five translucent tiles sit over the photo, tilted with `rotateY` so the left ones lean one way and the right ones the other. Each tile bobs up and down a few pixels on a 5 to 7s loop, out of phase with its neighbours, and its figure counts up from 0 over 1.5s. At 4.5s the photo crossfades to the next one (the new one eases in from scale 1.04 over .9s) and the pager dot stretches from 6px to 20px.

## When to use it
A creator, founder or agency home page where three to five proof figures are the pitch. It needs a photo with some empty space around the subject, because the tiles cover roughly a third of it. Wrong for a photo you cannot cover, or when there is only one number (use the odometer skill instead).

## How it works
Each tile is two nested elements. The outer one holds the position and the 3D tilt, the inner one holds the bob, so the two transforms never fight. The photo wrapper carries `perspective: 1100px` and the tile wrapper `transform-style: preserve-3d`.

```tsx
<div className="absolute z-10 [transform-style:preserve-3d] left-[4%] top-[6%]" style={{ transform: "rotateY(22deg) rotateX(4deg)" }}>
  <motion.div animate={{ y: [0, -9, 0] }} transition={{ duration: 5, repeat: Infinity, ease: "easeInOut", delay: i * 0.4 }}
    className="rounded-2xl backdrop-blur-xl border border-white/50 bg-white/25 px-5 py-3.5 text-white shadow-[0_24px_60px_-20px_rgba(0,0,0,0.55),inset_0_1px_0_rgba(255,255,255,0.6)]">
```

The fifth tile is positioned `left-1/2` with a Tailwind translate class that the inline `transform` overrides, so its left edge, not its centre, sits at the middle of the card. That is how it looks on the live site, and the demo copies it. In the demo, `render(t)` reproduces the bob as keyframes `[0, a, 0]` with easeInOut on each half, delayed by `i * .4` s, and the count-up as a cubic ease-out over 1.5s.

## Numbers that matter
| | |
|---|---|
| Card | 500 x 625, `rounded-4xl` (36px), 8px padding, inner `rounded-3xl` (28px) |
| Tile | `backdrop-blur-xl` (24px), border white/50, fill white/25, 14px by 20px padding, label 12px, figure 30.4px semibold |
| Tilts | left side rotateY(22 to 24deg), right side rotateY(-22 to -24deg), bottom tile rotateX(12deg) |
| Bob | y of -9, 8, -7, 9, -6 px over 5, 6, 7, 5.5, 6.5 s, delay i x .4 s |
| Photo swap | every 4.5s, .9s easeOut, new image from scale 1.04 |
| Entrance | text rises 12 to 16px (no opacity change), card scales .96 to 1 over .7s with .15s delay |

## Sound
Silent. Pair it with a soft UI tick on the state change if it sits in a video.

## Adapt it
- The photo (the demo uses gradient placeholders) and the five labels and values in `SPOTS`.
- Tilt per tile: swap the `rotateY` sign to mirror a tile, or drop it for flat glass.
- Tile fill and blur: raise white/25 toward white/40 if your photo is busy.
- Bob amplitude and duration in `FLOAT` for a calmer or livelier card.

## Files
- `code/demo.html` runs on its own and loops. Photos and logos are CSS placeholders; copy is placeholder text.

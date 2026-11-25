---
name: holographic-business-card__pointer-tilt-shard-foil-flip
description: A sky-blue business card that tilts toward the pointer on a spring, lifts, lights a pastel holographic shard foil and a glare under the cursor, and flips on click to a back with a QR code. Reach for it for creator and founder intro cards, "meet the team" and link-in-bio beats.
---

# Holographic business card

**Code name:** Pointer tilt, shard foil, flip.

## What you see
A light blue page, a 480x290 card with big rounded corners and a deep soft shadow: sky-blue top with white clouds, a wave and "Hey, I'm Alex", the word "product" in big white type with "designer & developer" in script under it, a round avatar on the right, a white strip at the bottom with "BASED IN REMOTE" and a blue link. Idle, the foil is almost invisible. At 0.7s the pointer enters at the top left: within 0.3s the card tilts toward it about 16 degrees, lifts a little (scale 1.03), a pastel rainbow of glass shards fades in over the whole face and a soft white glare follows the pointer. The pointer sweeps to bottom right at 1.9s, then to the bottom left: the tilt and the foil colours follow. At 3.6s a click flips the card about its vertical axis in about 0.35s with a small overshoot; the back is white with a blue bar on top, a name, a tagline, two links and a QR code on a pale plate. A second click at 5.8s flips back; the pointer leaves at 7.4s and everything settles flat. 9s loop.

## When to use it
Introductions and "link in my bio" beats where a card is handed over: founder, creator, agency. The landscape card fills the width at 9:16 and leaves the sky colour above and below, so put a headline in those bands. Wrong for dark, serious scenes: this is a light, glossy look.

## How it works
A card with `perspective: 1200px` holds a button with `transform-style: preserve-3d` and, inside it, the flipper with the two faces (`backface-visibility: hidden`, back rotated 180 degrees). Pointer position `n` runs -1..1 on each axis:
```
rotateY = nx * 16deg      rotateX = -ny * 16deg      scale = 1 + 0.03 * hover
foil opacity 0.036 -> 0.30, glare opacity 0.06 -> 0.50 (both follow hover)
foil background-position = (50 + nx*50)% (50 + ny*50)%, background-size 300%
```
Everything follows the pointer on a critically damped spring, omega 20 per second (fits the samples: 37% of the tilt at 68ms, 75% at 134ms, 91% at 201ms). The foil is `repeating-linear-gradient(125deg, #99f7ff 0%, #9efacc 5%, #d9f99d ..., ... )` multiplied by a shard mask: a webp of cells with their own brightness and thin dark seams; the demo makes its own seeded Voronoi mask (90 cells) on a canvas and uses it as `mask-image`. The flip angle was sampled: 0, 34.8 (82ms), 95.6 (149), 143.1 (215), 170 (282), 181.5 (349), 184.5 (415), 183.8 (482), 182.3 (549), 181.1 (615), 180.3 (682), 180 (749ms). In the demo the springs are integrated from t=0 each frame, so every frame is repeatable.

## Numbers that matter
| | |
|---|---|
| Card | 480x290, radius 18.46, perspective 1200 |
| Tilt | 16 degrees at the edge, spring omega 20/s, settles ~0.3s |
| Lift | scale 1.03 |
| Foil | opacity 0.036 idle, 0.30 hover, gradient 125deg, bg 300% |
| Glare | radial white, opacity 0.06 idle, 0.50 hover |
| Flip | about 0.35s to 180 with +4.5 degrees overshoot, settled by 0.75s |
| Front | sky #3a7fdc to #6aaaee, white strip 53px at the bottom |
| Back | 8px blue gradient bar #387fd9 / #6db0ec, QR plate 158x194 radius 21 colour #f3f7fd |

## Sound
Silent. A paper flick on the flip, a faint shimmer on hover.

## Adapt it
- `CONFIG.name`, `greeting`, `big`, `script`, `based`, `link`, `tag`.
- `CONFIG.path`: pointer path `[time, x, y]` in card pixels; `CONFIG.flips`: click times.
- `CONFIG.maxTilt`, `lift`, `omega` for a stiffer or looser card.
- `RAINBOW` and the sky gradient for other brand colours; the avatar is an inline SVG.

## Files
- `code/demo.html` runs on its own and loops; the values to change are in its `CONFIG` block.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "Holographic Business Card" by aakashmehra (https://21st.dev/@aakashmehra/components/holographic-business-card), MIT. Recreated by eye from the public preview; this demo is original code. Full notices: `THIRD_PARTY_NOTICES.md`.

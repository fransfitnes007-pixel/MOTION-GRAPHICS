---
name: truchet-arc-tile-field-radial-recolor-quarter-circle-wave
description: A black field of thick white quarter-circle arcs forms an endless maze; a circular wave from the centre turns each tile 90 degrees and paints it orange, then a second wave turns them back to white. Rebuilt by eye from a public motion video (see Credit); use it in app promos and launch reels.
---

# Truchet arc tile field with radial recolour

**Code name:** Quarter-circle tiles turned by a wave. Rebuilt by eye from a public motion video; original code, credited below.

## What you see
Black (#0b0b0c) covered edge to edge by 96px cells, each holding two thick off-white quarter arcs at opposite corners, half the cells flipped, so the arcs join into loops and channels. At 0.5s a circular wave opens from the centre: every tile it passes turns 90 degrees over about two cells of the front and turns orange-red (#ed4938). By 1.9s the whole field is orange and in a new maze. At 2.5s a second wave turns everything another 90 degrees and back to white, which is the starting pattern again.

## When to use it
A one-beat showreel interlude, a title background, or a transition between scenes in a dark reel; the recolour can carry a brand colour in. Wrong behind small text (too busy) unless you dim it.

## How it works
Truchet tiling: each cell draws two quarter circles of radius s/2 centred on opposite corners; a seeded coin per cell rotates the pair 90 degrees. Any choice of coins joins up, so the pattern never breaks.
```js
g.arc(-s/2, -s/2, s/2, 0, PI/2); g.arc(s/2, s/2, s/2, PI, PI*1.5)   // in the cell's frame
const p1 = eo(clamp((r1 - d) / (s * 2.2)))                         // how far inside the wave front this tile is
rot = (p1 + p2) * PI / 2; colour = mix(line, accent, p1 * (1 - p2))
```
Two waves of 90 degrees each make 180, and a 180-degree turn maps the two-arc tile onto itself, so the end frame equals the first frame.

## Numbers that matter
| | |
|---|---|
| Cell | 96px at 1920, stroke 26% of the cell |
| Waves | .5s to 1.9s and 2.5s to 3.9s, ease-in-out radius to half the diagonal plus a cell |
| Turn band | 2.2 cells behind the front, ease-out |
| Colours | line #f3f1ec, accent #ed4938, ground #0b0b0c |

## Sound
A filtered noise swell that follows the wave radius, or nothing; in the source it sits under the music. The demo is silent.

## Adapt it
- `cell`, `stroke`, colours.
- `seed` for another maze.
- Move the wave centre (CX, CY in `render`) to a logo position.

## Files
- `code/demo.html` runs on its own; every value to change is in the `CONFIG` block at the top of the skill script.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "revid.ai Claude Opus 5.5 wall #1: The showreel that started it" by @stephanlivera (https://x.com/stephanlivera/status/2103315922098470926), Video belongs to its creator; not included. Recreated by eye from watching the public video; this demo is original code and contains none of the video. Full notices: `THIRD_PARTY_NOTICES.md`.

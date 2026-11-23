---
name: blueprint-grid-glow-background-drifting-grid-blob-vignette
description: "A near-black field with a faint purple 80px grid creeping diagonally, a large blurred purple ellipse wandering behind it, and a dark vignette on the edges; it sits behind every scene of a video. Behind everything in a dark-mode product or tech video so scenes that have no background of their own still sit in the same world."
---

# Dark blueprint grid with drifting purple glow

**Code name:** Drifting grid, blob and vignette.

## What you see
Near-black (#050509) with a faint purple grid, 80px cells at 6 percent in v2 (64px at 7 percent in v1), creeping diagonally. Behind the grid a 1600 x 1100 purple ellipse, blurred 30px, wanders slowly. A dark vignette darkens the edges.

## When to use it
Behind everything in a dark-mode product or tech video so scenes that have no background of their own still sit in the same world. Subtle: at full view it reads as texture, not a design.

## How it works
Three layers: grid div (a repeating linear-gradient, moved with translate), blob (a radial-gradient ellipse, moved with left and top), vignette (a radial-gradient overlay with a high z-index).

```js
grid.style.transform = `translate(${(-t * 14) % 80}px, ${(-t * 9) % 80}px)`    // v1: 6 and 4 px/s, 64px cells
S(glow, { left: `${160 + Math.sin(t * .5) * 260}px`, top: `${-60 + Math.cos(t * .4) * 140}px` })
```
The long-form drift constants never repeat in a short loop, so in the demo they are changed so that the grid moves by whole cells and the glow by one sine cycle over 12.57s. The long-form values are above.

## Numbers that matter
| | |
|---|---|
| Grid | 80px, rgba(139,92,246,.06) lines; v1 64px, .07 |
| Blob | 1600 x 1100, radial rgba(124,58,237,.30), blur 30px; v1 1400 x 1000, .28, blur 20px |
| Drift | grid 14 and 9 px/s; blob sin(.5t) x 260, cos(.4t) x 140; v1 6, 4 px/s and .3, .25 |
| Vignette | transparent to 60 percent, rgba(0,0,0,.6) at the edge (v1 55 percent, .65) |

## Sound
Silent.

## Adapt it
- The accent colour in the grid and the glow.
- Cell size and line opacity.
- Drift speeds.
- Vignette strength.

## Files
- `code/demo.html` runs on its own with no network. Product screens, covers, logos and the wordmark are CSS placeholders.

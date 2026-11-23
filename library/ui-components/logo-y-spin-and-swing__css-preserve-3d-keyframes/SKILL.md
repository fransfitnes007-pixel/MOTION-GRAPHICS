---
name: logo-y-spin-and-swing-css-preserve-3d-keyframes
description: "Two cheap CSS 3D logo loops: a round monogram that spins a full turn on its vertical axis every 6 seconds, and a wordmark that swings gently between minus and plus 35 degrees every 4 seconds. Reach for it for a header lockup or a small animated brand mark where WebGL would be overkill."
---

# Logo Y spin and swing

**Code name:** CSS preserve-3d keyframes.

## What you see
Left: a silver round monogram. It turns about its vertical axis at a constant speed, so it narrows to a thin ellipse, shows its back (the letter mirrored) and comes round again. Right: a gradient wordmark that tilts left and right by 35 degrees, slowing at each end like a pendulum, and never goes edge-on or shows its back. The demo labels each with its keyframe name and shows the live angles. The two loops are 6s and 4s, so the demo runs 12s, the shortest loop that closes both.

## When to use it
A small brand mark that should feel alive but quiet: the spin for a compact monogram in a header, the swing for a wordmark in a hero. The spin shows the back of the artwork, so use a symmetrical or round mark, or a back face that is meant to be seen. For a mark that must always read correctly, see the sibling skills. Both loops respect `prefers-reduced-motion` in the source, where the animation is switched off.

## How it works
A parent with `perspective`, a child with `transform-style: preserve-3d` and a keyframe on `rotateY`.

```css
@keyframes rl-spin-y { from { transform: rotateY(0deg) } to { transform: rotateY(360deg) } }
.rl-monogram-spin { transform-style: preserve-3d; will-change: transform; animation: rl-spin-y 6s linear infinite }
/* parent: perspective: 600px */

@keyframes logo-swing { 0% { transform: rotateY(-35deg) } 50% { transform: rotateY(35deg) } 100% { transform: rotateY(-35deg) } }
.logo-swing { display: inline-block; transform-style: preserve-3d; animation: logo-swing 4s ease-in-out infinite }
```

Easing note: in `logo-swing` the single `ease-in-out` applies to each segment between keyframes, not to the whole cycle, so each half slows at both ends. The demo does this by easing each half separately. The spin is `linear`, so it has no slowing at all.

## Numbers that matter
| | |
|---|---|
| Spin | `rotateY 0 to 360`, 6s, linear, `perspective: 600px` |
| Swing | `rotateY -35 to 35 to -35`, 4s, ease-in-out per half |
| Wordmark colours | `135deg` from `#f5f5f8` at 30% to `#a5a5f0` at 70% to `#7b7bf7` |

## Sound
Silent.

## Adapt it
- Durations: the spin and swing periods.
- `35deg` for how far the swing goes; `perspective` for how strong the foreshortening is (smaller is stronger).
- The artwork: a monogram or wordmark of your own; for the spin, put a deliberate back face on it.

## Files
- `code/demo.html`: runs on its own, placeholder mark.

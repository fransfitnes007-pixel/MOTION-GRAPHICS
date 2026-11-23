---
name: whip-pan-transition-directional-blur-cut
description: "A fast sideways camera move with horizontal motion blur that carries the viewer from one scene to the next, hiding the cut at the moment of peak blur. Reach for it between two shots in a reel, tour or product story."
---

# Whip pan directional blur cut

**Code name:** Horizontal blur at peak speed. **From:** original build, neutral copy.

Original code; the move name follows the vocabulary catalogued by motionvideo.xyz.

## What you see
Scene one (indigo, big faint numeral, "Scene one", a small line, three bars) holds for 1.8s with a slow drift in its soft orbs. At 1.8s the camera whips right: over 0.72s the picture slides one full screen width, starting and ending almost still and moving about five screens per second at the midpoint. At the peak the whole frame is smeared horizontally by a blur of up to about 120px (standard deviation, horizontal only) and zoomed 4%. It lands on scene two (warm orange to magenta, mirrored layout) and holds until 4.4s, then whips right again onto a copy of scene one. Because that copy equals the start frame, the loop is seamless.

## When to use it
To cut between two related shots with energy: feature to feature, before to after, one phone screen to the next. It works best when both shots have a clear direction of travel and the music has a hit on the cut. It is wrong for sombre or slow content, and the blur needs a fast move: with a slow pan it looks like a bad blur filter.

## How it works
The scenes live on one wide strip that is translated; one blur filter sits on the strip and its strength is driven by the strip's speed, so the blur grows and fades with the move and is exactly zero when the camera is still.

```js
const eio5 = x => x < .5 ? 16*x**5 : 1 - Math.pow(-2*x + 2, 5) / 2   // slow, very fast, slow
x   = W * eio5(seg(t, 1.8, 2.52))                  // camera position along the strip
v   = |dx/dt| / W                                  // numeric derivative, screens per second
blur = 120 * K * (clamp(v / 6)) ** 1.1             // stdDeviation in x only
pan.style.filter = 'url(#whipblur)'                // <feGaussianBlur stdDeviation="blur 0">
```
The SVG filter blurs one axis only (`stdDeviation="80 0"`), which looks like a camera smear; a plain CSS `blur()` would blur both and read as defocus. Only the scenes that overlap the viewport are displayed, so the blur never works on offscreen pixels. A small `scale(1.04)` at peak speed adds push. The scene drift uses `sin(2*pi*t/DUR)` so t = 0 and t = DUR are identical.

## Numbers that matter
| | |
|---|---|
| Whips | 1.8s and 4.4s, 0.72s each |
| Easing | `eio5` (quintic in and out), peak about 5 screens/s |
| Blur | up to 120px standard deviation, horizontal only, zero at rest |
| Push | scale 1.04 at peak |
| Scenes | `#2b2f8f` to `#0d0e2c`, and `#ff8a4c` to `#4a1459`, accents `#a5b4fc` and `#ffd2b0` |

## Sound
A whoosh that starts 0.1s before the move, peaks at the midpoint (when the blur is at its maximum) and ends with a soft thump on landing. Pair with the "whoosh on cut" recipe.

## Adapt it
- Replace the two scene builders with your own screens; keep both the same size.
- `WH1` and `WH2` for timing and `0.72` for speed; shorter is punchier.
- Blur `120` and the `scale` for how violent it is; use the vertical axis by swapping the filter order and translating Y.
- Add a third scene by lengthening the strip and adding another whip.

## Files
- `code/demo.html` runs on its own and loops.
- `media/poster.jpg`

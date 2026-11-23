---
name: perspective-tilt-window-entrance-rotate-perspective-settle
description: "A browser window swings in rotated 22 degrees around its vertical axis, opacity rising, then keeps easing flat while the camera pushes into the page and a pill pops in. Bringing a screen on without a plain fade, particularly the second window of a two-sided story (first one side, then the other) so the two feel like different rooms."
---

# Perspective-tilted window entrance

**Code name:** Rotate perspective settle.

## What you see
A browser window arrives turned 22 degrees around its vertical axis at 90 percent scale and transparent, opening to flat over 0.8s. A leftover 6 degree lean eases out slowly between 1s and 4s, so the window keeps settling after it has landed. Meanwhile the camera pushes into the top right of the page and a pill pops in with an overshoot at 2.6s.

## When to use it
Bringing a screen on without a plain fade, particularly the second window of a two-sided story (first one side, then the other) so the two feel like different rooms. Skip it for dense screens that need to be readable straight away.

## How it works
CSS `perspective()` inside the element's own transform, with two angle terms: the entrance (`1 - inK`) and a slow settle (`1 - seg(lt, 1, 4)`).

```js
transform = `perspective(2200px) rotateY(${(1 - inK) * -22 + 6 * (1 - seg(lt, 1, 4))}deg) scale(${lerp(.9, 1, inK)})`
// business variant: perspective(2000px) rotateX(${(1 - inK) * 18}deg) translateY(${(1 - inK) * 80}px) scale(${lerp(.92, 1, inK)})
// v2 push-in: perspective(2200px) rotateX(${(1 - inK) * 28}deg) scale(${lerp(.55, 1, inK)}), origin on the chart
```

## Numbers that matter
| | |
|---|---|
| Entry | 0 to 0.8s, `eo` |
| Angle | rotateY -22 degrees to 0, plus 6 degrees decaying over 1s to 4s |
| Perspective | 2200px (2000 for rotateX) |
| Window | 1400 x 830 at (260, 140) |

## Sound
Suggested sound: a pink-noise whoosh (high-passed at 600 Hz, low-passed at 5.2 kHz, 0.7s long, volume .22) peaking on every scene cut, over a low A-minor drone pad that ducks under the narration. 

## Adapt it
- Axis: rotateY for side entrances, rotateX for rising from below.
- Angles and the lingering degrees.
- Perspective distance: smaller is more dramatic.

## Files
- `code/demo.html` runs on its own with no network. Product screens, covers, logos and the wordmark are CSS placeholders.

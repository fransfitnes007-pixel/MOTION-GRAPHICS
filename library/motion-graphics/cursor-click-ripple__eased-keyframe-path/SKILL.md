---
name: cursor-click-ripple-eased-keyframe-path
description: "A white arrow cursor travels along a list of timed points, presses to 82% and releases a gold ring from the click. Describe the path as [time, x, y] keyframes. Use it to show a button being clicked."
---

# Cursor click with gold ripple

**Code name:** Eased keyframe path.

## What you see
A cursor fades in at the lower right and glides to a button over 1.2s with ease-in-out, slowing as it lands. At the click it shrinks to 82% for 0.14s, the button presses to 95%, and a gold ring grows from the tip from 10px to 120px while fading over 0.5s. 0.6s after the last keyframe the cursor disappears.

## When to use it
Any "click the button" beat. The keyframe list makes multi-stop paths easy (hover here, then there). The sibling skills differ in ring colour and in being single straight moves.

## How it works
`cursor(t, pts, clickAt)` takes `pts = [[t, x, y], ...]` and eases between each pair:

```js
for (let i = 0; i < pts.length - 1; i++) {
  const [ta, xa, ya] = pts[i], [tb, xb, yb] = pts[i + 1]
  if (t >= ta) { const k = eio(p(t, ta, tb)); x = lerp(xa, xb, k); y = lerp(ya, yb, k) }
}
const press = t > clickAt && t < clickAt + 0.14 ? 0.82 : 1
// ring: rs = lerp(10, 120, eo(k)) * S, opacity 1 - k, border 4px gold, k = p(t, clickAt, clickAt + .5)
```
A good pattern is: start 1.5s before the click, arrive 0.3s before it, click, hold 0.9s. The caller presses the button itself (`0.95` for 0.18s after the click). The click cues a `click` sound.

## Numbers that matter
| | |
|---|---|
| Cursor | 44px (times scale), white fill, dark stroke, drop shadow |
| Press | scale .82 for 0.14s |
| Ring | 10px to 120px, `eo`, 0.5s, 4px #e8b43a |
| Path | `eio` between keyframes; start -1.5s, arrive -0.3s, end +0.9s around the click |

## Sound
Click (`click_002.ogg`, volume 0.55) at the click time.

## Adapt it
- The keyframes and `clickAt`.
- Ring colour (`.ripple`) and size.
- Cursor size (`.cursor`).

## Files
- `code/demo.html` runs on its own and loops; `?w=1080&h=1920` gives the tall layout. 
- `code/fonts/` holds the fonts the demo loads.

---
name: feed-refresh-blur-scroll-ease-in-column-blur
description: "A column of post cards is yanked upward off the screen with an accelerating scroll and a blur that peaks mid-way, while a refresh icon spins and a black word appears. Reach for it as a pull-to-refresh or an endless-scroll cut."
---

# Feed refresh blur scroll

**Code name:** Ease-in column blur.

## What you see
A column of three post cards stands still, one centred and parts of two more at its top and bottom edge. On the voice word "refresh" a black circular-arrow icon appears above the card and spins at 900 degrees a second, and the whole column starts to move up, slowly, then faster and faster over 0.9s until it has travelled more than four card heights and left the frame. As it speeds up it blurs to 22px at the midpoint, then sharpens as it leaves. The icon fades out between 0.5s and 0.8s. A heavy black "REFRESH" word stays over the middle of the frame. At 3.9s it cuts to a dark scene.

## When to use it
A transition out of a card scene that says "the feed moves on": a refresh, a swipe to the next video, a shift to the next topic. It needs a column taller than the frame so there is always another card coming. It is wrong for a slow scroll: the whole effect is the acceleration.

## How it works
The column is a single absolutely positioned element holding the cards stacked in a line (one above, one centred, one below, with 40 to 150px gaps). Each frame sets its `top` and its blur from one progress value:

```js
const scroll = ei(seg(t, T, T + .9)) * (CH * 4.2)      // ease-in cubic: slow start, fast exit
const blur = Math.sin(Math.PI * seg(t, T, T + .9)) * 22  // 0 -> 22 -> 0
feedCol.style.top = colY - scroll + 'px'; feedCol.style.filter = `blur(${blur}px)`
```
The icon is an SVG, rotated by `(t - T) * 900` degrees and faded with `1 - seg(t, T + .5, T + .8)`.

The demo fades the column in over the first 0.3s so the loop does not pop; in a video you would cut in.

## Numbers that matter
| | |
|---|---|
| Scroll | `ei` over .9s, distance 4.2 card heights |
| Blur | `sin(pi * p) * 22` px |
| Icon | 80px, 900 degrees per second, fades .5 to .8s after the start |
| Card gaps | 150px above, 40px below the centred card |

## Sound
A rising noise whoosh, 0.9s long, starting under the scroll's first movement, over the pop of the black word. A single hard cut to the next scene's sound follows.

## Adapt it
- The distance multiplier (`4.2`) so the whole column clears the frame at your card size.
- Peak blur (22) and duration (.9s).
- The stamp word, or remove it.
- Spin speed.

## Files
- `code/demo.html` runs on its own.

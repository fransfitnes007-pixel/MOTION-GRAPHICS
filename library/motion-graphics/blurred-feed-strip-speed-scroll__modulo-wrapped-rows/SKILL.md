---
name: blurred-feed-strip-speed-scroll-modulo-wrapped-rows
description: "Three rows of post thumbnails rush sideways at different speeds under a heavy blur, with two white arrows chasing them. Reach for it for a fast scroll or a flood of content."
---

# Blurred feed strip speed scroll

**Code name:** Modulo-wrapped rows.

## What you see
On the white stage, right after a gradient word has swept through, three rows of post thumbnails fill the frame from the left edge, blurred by 14px so only colours and skin tones show. They stream to the left. The top row moves at 2600px per second, the middle 25% faster, the bottom 50% faster, so they slide against each other. Two white arrows with a black outline hang in the gaps and drift to the right, against the flow. The whole thing lasts 0.44s, so by its end the rows are almost gone off the left side. The demo plays it at half speed.

## When to use it
A fast "so much content" beat: scrolling, flooding, too many options. It is a transition-length effect, under half a second. Because the blur hides the images, it works with any thumbnails, even placeholders. It is wrong where the audience needs to read a thing in the strip.

## How it works
A row is a single element holding nine cards laid out 200px apart (cards 180px wide). Every frame the row's `left` is set from time:

```js
const v = (t - t0) * 2600
row.left = ((-v * (1 + r * .25)) % (9 * 200 * K)) - 100 * K     // r = 0, 1, 2
row.filter = 'blur(14px)'
```
The modulo keeps a long scroll inside the row's width. In the original timing it never wraps, since 0.44s at 3900px per second is 1716px, just under the row's 1800px. Keep the duration short or add more cards if you extend it. The arrows use `((t - t0) * 900) % 300`, a sawtooth that snaps back every third of a second, which the blur and the speed hide.

## Numbers that matter
| | |
|---|---|
| Row speeds | 2600, 3250, 3900 px/s (`1 + r * .25`) |
| Cards | 180px wide, 200px pitch, 9 per row, radius 14px |
| Blur | 14px |
| Rows | 330px apart (360 on tall), top row at `CY - 440` |
| Arrows | 150x112, white fill, black 5px outline, drift 900px/s modulo 300 |
| Duration | .44s |

## Sound
Part of the whoosh that carries the cut from the gradient word, with the strip riding on its tail. Then silence for a beat before the slam word.

## Adapt it
- Card sources and the blur (14px): lower it if you want the thumbnails to read.
- Row speeds, which come from `1 + r * .25`.
- Number of rows and the vertical spacing.
- Replace the arrows with any chase element.

## Files
- `code/demo.html` runs on its own. Thumbnails are gradient placeholders.

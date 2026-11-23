---
name: stamped-word-card-burst-spring-from-huge
description: "A post card slams in from 3.4 times its size with a 9 degree twist while thick uppercase words, one white on a blue block, stamp onto it in time with the voice. Reach for it as the opening beat of an explainer."
---

# Stamped word card burst

**Code name:** Spring from huge.

## What you see
The first frame is a post card at 3.4 times its size, tilted 9 degrees left. In the first half second it springs down to its real size and straightens, overshooting once. A third card peeks in from below the frame edge. At 0.4s "MAKE" lands over the card in white with a heavy shadow and "IT!" under it on a blue block with a darker blue edge. The stamp swaps for "SHARE IT" at 1.26s and "GROW IT" at 2.04s. At 2.8s it becomes a plain black "REFRESH" with no block. Each word starts at 60% size and springs to full while fading in, always at -6 degrees.

## When to use it
The first seconds of a voiced explainer where each spoken verb should hit as a word. It suits short imperative lists of three or four words. It needs a card or image to stamp onto; on an empty stage the stamp loses its point.

## How it works
Two separate motions. The card column scales and rotates around its own centre with a spring that overshoots, which gives the "thrown at the screen" feel:

```js
const inq = spring(seg(t, 0, .55), 7, 9)
transform = `scale(${lerp(3.4, 1, inq)}) rotate(${lerp(-9, 0, inq)}deg)`
```
The stamp is one absolutely positioned element whose text swaps at each word time. The word's second line is wrapped in a `<span>` that gets the blue block (`background:#2f6bff; box-shadow:0 .1em 0 #1a46c9`). The spring `spring(seg(t, t0, t0 + .4), 8, 13)` drives scale `.6 + .4q` and opacity `clamp(q * 2)`. Letter spacing is `-.06em` and line height `.86` so the two lines lock together.

## Numbers that matter
| | |
|---|---|
| Card burst | spring k7 f9 over .55s, scale 3.4 to 1, rotate -9 to 0 |
| Stamp | 190px (150px tall layout), weight 800, rotate -6 degrees |
| Word spring | k8 f13 over .4s, scale .6 to 1 |
| Block | `#2f6bff`, edge `#1a46c9`, padding .02em .12em |
| Word times | .4, 1.26, 2.04, 2.8 (set by the voice) |

## Sound
A soft pop (640Hz rising by 90Hz per word, a tenth of a second) on every stamp, under a bright voice and an intro pluck. Pair with a whoosh at the start of the burst.

## Adapt it
- The four words and their times.
- Block colour and its edge.
- Card images, or swap the card for a product shot.
- The overshoot: raise the spring's `k` (7) for less bounce.

## Files
- `code/demo.html` runs on its own, without the scroll that can follow it (see the feed refresh skill).

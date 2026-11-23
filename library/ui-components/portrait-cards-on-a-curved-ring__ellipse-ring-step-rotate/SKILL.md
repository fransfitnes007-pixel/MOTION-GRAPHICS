---
name: portrait-cards-on-a-curved-ring-ellipse-ring-step-rotate
description: Portrait picture cards laid out on a big elliptical ring that bends round a centred title, stepping one card at a time; near cards are larger and on top. Reach for it as a portfolio or "selected works" strip.
---

# Portrait cards on a curved ring beside a label

**Code name:** Ellipse ring, step rotate.

## What you see
A flat page (dark #151515 in the video, light in the poster) with the label "Selected works" at 33px medium weight at the right of centre. To its left, ten 97 x 135 portrait cards (orange and violet gradients, a black card with an orange arc, a blue planet, a cream card with a head, a rainbow streak) sit along a ring: two long runs of cards, one near the top and one near the bottom, that bend towards each other on the right and meet beside the label. The ring is much wider than the frame, so its left side runs off the edge.

The ring turns one slot at a time: the cards rest for 0.8s, then all slide along the ring for 0.6s with an ease-in-out. Cards at the right (the near side) are full size and sit on top of the others; cards at the far side are scaled down to 75%. In this demo the ring has 20 slots and shows the 10 pictures twice, so the top and bottom runs echo each other. Ten steps bring it back to the start.

## When to use it
A "selected works", case-study or team strip next to a heading, where a few images should feel like a set. It suits dark or light pages and portrait pictures of similar size. It works for up to about ten distinct pictures; fewer repeat on the ring.

## How it works
Each card lives at an angle on an ellipse whose left side is off screen:
```js
th = (k - s) / N * 2*pi                  // s steps by 1 each turn of the reel
x = cx + rx * cos(th);  y = cy + ry * sin(th)       // cx = -190, rx = 620, ry = 135
depth = (cos(th) + 1) / 2
scale = lerp(minScale, 1, depth);  zIndex = round(depth * 100)
```
`s` is a step function with an ease: `k + eio(seg(t - k*P, hold, P))` where `P = hold + step`. Cards past the left edge are hidden. The usage example passes `cardWidth=130`, `cardHeight=180`, `minScale=.4`, `radiusYRatio=.36`, `holdDuration=1000` and `stepDuration=700`; the demo uses its own measured values (97 x 135 on a 960 x 420 canvas, minimum scale .75) so it matches the look of the video, not those props.

## Numbers that matter
| | |
|---|---|
| Canvas | 960 x 420 |
| Cards | 97 x 135, 20 slots, 10 pictures |
| Ring | centre (-190, 210), rx 620, ry 135 |
| Scale | 1 at the near side, .75 at the far side |
| Timing | hold 0.8s, move 0.6s, 14s loop |
| Label | 33px, weight 500, at x 722 |

## Sound
Silent.

## Adapt it
- `CONFIG.label` and the `ART` list (or place `<img>` in each `.c`) for your content.
- `CONFIG.rx`, `ry`, `ringCx` and `ringCy` change the curve; a smaller `rx` makes a rounder ring.
- `CONFIG.hold` and `step` for the rhythm, `direction` to turn the other way.
- `CONFIG.mode` 'light' for the light page.

## Files
- `code/demo.html` runs on its own and loops. Placeholder art is CSS and SVG only.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Halo Reel" by ruixen.ui on 21st.dev (https://21st.dev/@ruixen.ui/components/halo-reel), MIT. This demo is an original recreation written from the public preview.

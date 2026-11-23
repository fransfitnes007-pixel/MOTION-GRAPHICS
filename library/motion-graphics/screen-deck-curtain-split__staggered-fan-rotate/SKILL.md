---
name: screen-deck-curtain-split-staggered-fan-rotate
description: "Eight app screens stack in the centre, then fan out into two tilted wings left and right while a two-line headline blurs in between them. Introducing \"the whole product\" or a multi-part platform right after the logo."
---

# Screen deck curtain split

**Code name:** Staggered fan rotate.

## What you see
Eight app screenshots stack on top of each other in the middle of the frame, appearing 60ms apart with a slight fan from small rotations. From 0.7s to 2.2s they split: the even ones go left, the odd ones right, spreading 520px and further per row, rotating 10 to 22 degrees outward and shrinking to 78 percent, so two tilted columns frame the centre. A two-line headline blurs and scales in between them from 1.4s.

## When to use it
Introducing "the whole product" or a multi-part platform right after the logo. It shows breadth of screens without stopping on any of them, so the screens only need to look like a real product.

## How it works
Each card has a side (-1 or 1) from its index parity and a row from `floor(i/2)`. One `eio` value (`split`) drives position, rotation and scale; stacking uses a separate per-card `eo`.

```js
const split = eio(seg(lt, .7, 2.2))
x = 700 + side * split * (520 + row * 40);  y = 394 + (row - 1.5) * split * 250
rot = side * split * (10 + row * 4)
transform = `rotate(${rot - (1 - split) * (i - 4) * 2}deg) scale(${lerp(1, .78, split)}) translateY(${(1 - stackK) * 60}px)`
```

The `(1 - split) * (i - 4) * 2` term is the pre-split fan: each card in the stack sits a couple of degrees off its neighbour.

## Numbers that matter
| | |
|---|---|
| Cards | 520 x 293, radius 22px, 8 of them |
| Stack-in | 0.5s each, 60ms apart |
| Split | 0.7s to 2.2s, `eio` |
| Spread | x 520 + 40 per row, y 250 per row, rotation 10 + 4 per row degrees |
| Headline | 120px, weight 800, 1.4s to 2.4s, scale .9 to 1, blur 12px to 0 |

## Sound
Suggested sound: a pink-noise whoosh (high-passed at 600 Hz, low-passed at 5.2 kHz, 0.7s long, volume .22) peaking on every scene cut, over a low A-minor drone pad that ducks under the narration. The cut in has the whoosh; the narration carries the scene.

## Adapt it
- The screens: any 16:9 image works.
- Headline text.
- Card count: the row/side maths works for any even number.
- Spread distances if your frame is not 16:9.

## Files
- `code/demo.html` runs on its own with no network. Product screens, covers, logos and the wordmark are CSS placeholders.

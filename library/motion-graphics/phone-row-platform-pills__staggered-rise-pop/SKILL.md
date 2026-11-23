---
name: phone-row-platform-pills-staggered-rise-pop
description: "Five phones rise one after another into a row and bob gently while four coloured platform pills pop in above them. Reach for it to say 'it goes out on every platform'."
---

# Phone row with platform pills

**Code name:** Staggered rise with bob and popping pills.

## What you see
Five phones (250px wide, 512px high) are below the frame. Left to right, each 0.06s after the one before, they rise to the middle of the frame in 0.6s with a hard ease-out and line up with 40px between them. As soon as they arrive they float: each moves up and down by 8px on a sine of its own phase, so the row ripples. Above them a dark chip pops in at the top centre, and on the spoken word "everywhere" four pill labels spring in one after another, 0.07s apart: a black one, a pink one, a red one and a blue one. On the tall layout there are three phones, 300px wide, and the pills sit in the upper part of the frame.

## When to use it
Distribution: "on every platform", "in every feed". The row says many devices, the pills say which ones. It is wrong when the platforms have to be recognisable by logo; the pills here are coloured text.

## How it works
Each phone has its own delayed ease-out for the rise and its own sine phase for the bob:

```js
const q = eo5(seg(t, t0 + i * .06, t0 + .6 + i * .06))
const bob = Math.sin((t - t0) * 2.2 + i) * 8
phone.top = lerp(H + 60, restY, q) + bob
```
`eo5` is `1 - (1 - x)^5`: nearly all of the travel is done in the first third. The pills use a spring (`k8 f12`) on `scale(pq)` only, centred with `translate(-50%,-50%)`, with 0.07s per pill. The phone frame follows the phone drop-in skill: radius `width * .13`, bezel `width * .024`.

## Numbers that matter
| | |
|---|---|
| Phones | 250px wide (300 tall layout), height `width * 2.05`, pitch `width + 40` (`+ 30` tall), 5 on wide, 3 on tall |
| Rise | `eo5` over .6s, .06s stagger, from `H + 60` |
| Bob | 8px, 2.2 rad/s, phase = phone index |
| Pills | font 30px, `#0b0b10`, `#e1306c`, `#ff0000`, `#1877f2`, spring k8 f12 over .5s, .07s apart |
| Position | pills 390px above centre, 290px apart (230 tall); chip 470px above centre |

## Sound
A whoosh on the cut in, then four pops going up the scale (1300 to 1540Hz, 0.11s, 0.07s apart, panned across), one per pill.

## Adapt it
- Platform names and colours, or logos.
- Number of phones and their screen content.
- Bob amplitude, or set it to 0 for a still row.
- The stagger (.06s) and the pill delay (.07s).

## Files
- `code/demo.html` runs on its own. Screens are gradient placeholders.

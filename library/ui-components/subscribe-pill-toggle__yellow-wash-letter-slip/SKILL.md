---
name: subscribe-pill-toggle-yellow-wash-letter-slip
description: "A white \"Subscribed\" pill beside a small round share button. A tap washes the pill bright yellow, narrows it, and the trailing d slips down and fades to read \"Subscribe\" while the rest of the word stays still. A second tap reverses it. Use for follow, subscribe or save toggles."
---

# Subscribe pill toggle

**Code name:** Yellow wash and letter slip. **From:** original build for this library.
Original code; the interaction idea is a common iOS pattern (see 60fps.design for references).

## What you see
Dark stage. A white pill reading `Subscribed` in dark 76px semibold type, and a 86%-height round translucent share button with an up-arrow icon to its right. At .9s a finger taps the pill. Over .6s on a spring the fill goes from white to yellow (`rgb(255,214,10)`) with a yellow glow, the pill's right edge pulls in by one letter width (the share button follows), and the final `d` drops about .5em and fades out in the first third of the move. `Subscribe` never moves. At 3.0s a second tap reverses everything: the `d` rises back in, the pill widens and fades to white. Frames 5s and 0s match.

## When to use it
Binary toggles whose label changes by one suffix: Subscribe/Subscribed, Follow/Following, Save/Saved. Wrong where the two labels differ by more than a letter or two.

## How it works
The label is two inline-block spans: `Subscribe` and `d`. Their widths are measured once with `getBoundingClientRect`. The pill is left-anchored, so the word stays pixel-still; the pill's width is `fullW - dWidth * a`, where `a` is a spring that goes 0 to 1 on the first tap and back on the second. The `d` gets `translateY(a*.5em)` and `opacity = 1 - clamp(a*1.7)`. Colour is a per-channel lerp of green and blue from white to yellow.
```js
w = fullW - wD * a
d.style.transform = `translateY(${a*fs*.5}px)`
```

## Numbers that matter
| | |
|---|---|
| Spring | k6 f10 over .6s, both directions |
| Narrowing | exactly the width of the `d` |
| Slip | .5em down, gone by 60% of the move |
| Yellow | `rgb(255,214,10)`, glow `rgba(255,214,10,.28)` |
| Press | pill scales to .965 during the tap |
| Taps | .9s and 3.0s, loop 5s |

## Sound
A light tick on each tap; a tiny pop when the pill turns yellow.

## Adapt it
- Label text and the dropped suffix (any trailing letters work, spans are measured).
- Yellow `rgb(255,214,10)` to the brand colour.
- Font size `fs`; pill height is `2.1 * fs`.
- Swap the share icon or remove it.

## Files
- `code/demo.html` runs on its own and loops in 5s.
- `media/poster.jpg`

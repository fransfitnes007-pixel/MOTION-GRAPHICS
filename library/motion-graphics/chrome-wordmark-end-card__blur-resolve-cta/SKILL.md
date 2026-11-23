---
name: chrome-wordmark-end-card-blur-resolve-cta
description: "A black end card where a chrome wordmark shrinks and sharpens out of a blur, a blue call-to-action button springs up under it and gets clicked, a URL pill types itself and a quiet tagline fades in, then everything fades out. Reach for it as the closing card of a brand video."
---

# Chrome wordmark end card

**Code name:** Blur resolve, spring button, cursor click.

## What you see
A pure black frame. At 25.4s the brand's chrome wordmark appears 18% too large and blurred by 18px, and over 0.9s it shrinks to size and sharpens with a quintic ease-out, a pale blue glow behind it. At 26.1s a blue gradient pill button, "Book a call", rises 50px and springs to full size with a small overshoot. At 27.0s a white arrow cursor glides in from the lower right, clicks the button (the button dips 6% for 0.2s, a blue ring bursts) and fades. Just after, a dark pill with an arrow and the site address appears under the button and types the address one letter at a time, with a blinking bar. At 27.7s a faint grey tagline fades in. From 28s the whole card fades out to black by 28.9s, and the video ends at 29s.

## When to use it
The last four seconds of a brand video: logo, one action, one address. It gives the viewer something to do after they have watched. It is wrong when there are more than one or two actions; the card is built around a single button. The chrome wordmark needs a dark ground to read.

## How it works
Everything is driven by one clock `t` and one fade-out value:

```js
const q = eo5(seg(t, 25.4, 25.4 + .9)), out = ei(seg(t, DUR - 1, DUR - .1))
logo: scale(1.18 - .18 * q); opacity q * (1 - out); filter: blur((1 - q) * 18px) drop-shadow(0 0 50px rgba(56,189,248,.3))
button: spring(seg(t, end + .7, end + 1.3), 7, 11) -> translateY((1 - b) * 50px), scale .9 to 1; click press 6% from end + 1.55
```
The cursor and its click ring are the cursor skill (`clickAt`, click at `end + 1.6`). The URL pill is the same typewriter as in `url-pill-typewriter-caret__substring-blink`, with a smaller dark pill. The tagline is `eo(seg(t, end + 2.3, end + 2.8))`. Every element multiplies `(1 - out)` so the final fade is the same everywhere.

A real build would use an image of a metal-lettered logo. The demo uses chrome-gradient text as a stand-in.

## Numbers that matter
| | |
|---|---|
| Logo | 900px wide (820 on tall), `eo5` over .9s, scale 1.18 to 1, blur 18px to 0, 170px above centre |
| Button | 600 by 110px (560 by 100 tall), font 50px, spring k7 f11 from .7s, click at 1.6s |
| URL pill | 44px font, `#15151c` with a `#93c5fd` text, 200px below centre, pops at 1.6s, types 1.75 to 2.55s |
| Tagline | 30px weight 500 at 60% white, fades in over .5s from 2.3s |
| Fade out | `ei` from 1s to .1s before the end |

## Sound
A rising whoosh (0.5s) into the card at 25.25s, a soft pad under it, then the button click at 27.0s and 13 small pops (2000 to 2360Hz, quiet) as the address types. The whole mix fades to silence with the picture.

## Adapt it
- The wordmark: put your own logo image in `endG`, keep the blur and scale.
- The button label, the address and the tagline.
- `C_END` and the video length for the out fade.
- Click time: the button's press uses the same time.

## Files
- `code/demo.html` runs on its own. The wordmark is chrome-gradient text.

---
name: end-card-monogram-flip-wordmark-blur-rotatey-spring-blur
description: "A closing logo lockup: mark flips in, wordmark blurs and settles, shine sweeps, address fades up, then a slow fade out. Use it as the last card of a promotional video."
---

# End card with flipping mark

**Code name:** RotateY spring mark, blur-in wordmark, fading address.

## What you see
On the light stage a round mark appears first, 160px, spinning a full 360 degrees about its vertical axis over 1.35s while it rises 40px and springs to size. 0.05s later the wordmark appears at 120% scale and 14px of blur and settles to 100% sharp with a spring. A shine band crosses the wordmark from 0.5s to 1.5s. At 0.7s the address in grey fades up 20px into place beneath. From 2.4s to 3.2s the whole card fades out with a squared curve.

## When to use it
The final card of a promo or explainer, once the call to action has been seen. It reads best with a light, quiet stage and one lockup. If the video ends on a hard CTA button, use this after it, not instead of it.

## How it works
Three independent springs on one clock, started a hair apart so the mark leads the wordmark.

```js
const g = spring(seg(t, .05, .75), 6, 9), w = spring(seg(t, END - .05, END + .6), 8, 12)
mark:     rotateY((1 - eio(seg(t, .05, 1.4))) * 360deg), translateY((1 - g) * 40), scale(.7 + .3 * g)
wordmark: scale(1.2 - .2 * w), blur((1 - clamp(w * 1.3)) * 14)
card:     opacity = 1 - f * f   // f = seg(t, 2.4, 3.2)
```

The rotateY has no `perspective`, so it reads as the mark squashing to a line and back, not as a 3D turn. A vignette sits over everything at full strength. A dark-stage variant is the same with the wordmark simply fading from 125% in.

## Numbers that matter
- Mark: 160px, `spring(k=6, f=9)` over 0.7s, rotateY 360 degrees to 0 with `eio` over 1.35s.
- Wordmark: 920 by 440 box, `spring(k=8, f=12)` over 0.65s, scale 1.2 to 1, blur 14px to 0.
- Address: 46px, weight 600, `#55556a`, `eo5` over 0.5s, rising 20px.
- Fade: `1 - f*f` over 0.8s starting 2.4s.

## Sound

## Adapt it
- The mark, wordmark and address text.
- Stagger between mark and wordmark (`.05` and `END`).
- Spin duration (1.35s) or remove the rotateY for a calmer lockup.
- Fade-out timing, or hold the card if the video continues.

## Files
- `code/demo.html` runs on its own and loops. Mark and wordmark are CSS placeholders.

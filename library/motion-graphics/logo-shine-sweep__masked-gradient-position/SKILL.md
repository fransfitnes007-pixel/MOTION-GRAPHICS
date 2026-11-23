---
name: logo-shine-sweep-masked-gradient-position
description: "A single white shine band crossing a logo, masked to the letter shapes. Use it to make a static logo feel polished on an end card or after a reveal."
---

# Logo shine sweep

**Code name:** Masked gradient position sweep.

## What you see
A silver logo sits still on a pale stage. A narrow white band, tilted about ten degrees, crosses it from left to right in one second, lighting only the letters, never the space around them. Then nothing moves until the loop restarts.

## When to use it
The last beat of a logo reveal or an end card, when the logo has landed and you want it to catch the light once. Do not run it continuously: one pass per appearance. It needs a logo with shape (chrome, glass, metallic); on a flat colour logo the highlight looks like a stripe.

## How it works
A second copy of the logo sits exactly on top of the first. Its background is a wide gradient with one bright band, and the logo image is its mask, so the gradient only shows through the letters. `mix-blend-mode: screen` lets the band brighten the artwork underneath without covering it.

```js
shine.style: background: linear-gradient(100deg, transparent 38%, #fff 50%, transparent 62%)
             background-size: 260% 100%; mask-image: url(logo.png); mix-blend-mode: screen
backgroundPosition = `${lerp(130, -30, seg(t, t0, t0 + 1))}% 0`
```

The usual build masks with the logo PNG (`-webkit-mask-image`). The demo has no image, so it uses `background-clip: text` on a text copy, which is the same idea with letters as the mask.

## Numbers that matter
- Band: 24% of a 260%-wide gradient (38% to 62%), angle 100 degrees, peak white at 50%.
- Sweep: background-position 130% to -30% over 1.0s, linear.
- Blend: `screen`, mask `contain`, centred, no repeat.
- Timing: starts 0.15s after the logo lands (`gk + .1`), ends at `gk + .8`.

## Sound
Silent. It sits well under an end-card music tail, after the whoosh into the end card has finished.

## Adapt it
- The logo image used as mask (any PNG with transparency).
- Band angle (100deg) and width (38% to 62%) for a broader or sharper highlight.
- Sweep timing; start it a beat after the logo lands.
- Reverse the position values to sweep right to left.

## Files
- `code/demo.html` runs on its own and loops. The logo is placeholder text.

---
name: cta-button-press-click-scale-brightness-type
description: "The call-to-action beat: a headline, a gradient pill button with an arrow, a cursor click, and the address typing below. Use it as the final action scene of a promo."
---

# CTA button click with typed address

**Code name:** Spring button, press-scale and brightness flash, typed pill underneath.

## What you see
A two-word headline, "Get yours" with the second word in indigo gradient, lands at 150px. Below it a pill button 700 by 136 in an indigo gradient with a white label and an arrow icon springs up 50px and settles. A cursor glides from the bottom right to the button; on the click the button dips to 95% and flashes 25% brighter, fading back over half a second, and a ring ripples out. Under the button a frosted white pill fades in and types the address with an indigo caret. The cursor fades out as the address finishes.

## When to use it
The last action scene of a promo, once the offer is clear. Time the click to a spoken cue such as "at your address", and the typing to the address being spoken. It follows well after a dark offer scene. Do not put anything else on screen; the button is the focus.

## How it works
Four timelines keyed to the spoken words.

```js
const b = spring(seg(t, .07, .7), 7, 11)                 // button rise
const press = 1 - .05 * Math.sin(Math.PI * seg(t, AT - .02, AT + .16))
btn.filter = `brightness(${1 + .25 * (1 - seg(t, AT, AT + .5)) * (t > AT ? 1 : 0)})`
clickAt(t, AT, 1200, 520, [1700, 1000], .1)               // cursor skill
text = txt.slice(0, Math.round(clamp(seg(t, GROWTH - .1, LINK + .2)) * txt.length))
```

The button has two layers of feedback on the click, the scale dip and the brightness flash, which is what makes the click feel physical with no second state of the button.

## Numbers that matter
- Button: 700 by 136, `linear-gradient(180deg,#6d6ef0,#5b5ce6)`, label 46px bold, glow `0 30px 70px -18px rgba(91,92,230,.7)`.
- Rise: `spring(k=7, f=11)` over 0.63s, 50px. Press: 5% over 0.18s. Flash: +25% brightness fading over 0.5s.
- Address pill: 680 by 104, text 50px bold; typing over about 1.1s.
- Headline: 150px weight 800.

## Sound

## Adapt it
- Button label and the arrow icon.
- The address string and the `GROWTH`/`LINK` times.
- `AT`: the click time.
- Button colour; for a dark stage use a lighter lavender caret and text.

## Files
- `code/demo.html` runs on its own and loops. The address is a neutral placeholder.

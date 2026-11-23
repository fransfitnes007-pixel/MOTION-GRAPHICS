---
name: glass-popup-card-back-ease-blur-card
description: "Small frosted dark card with a gold kicker, serif title and grey subline that pops over a photo with a back-ease overshoot and a click. Use it for facts, chapter labels and stat callouts over footage."
---

# Glass pop-up card

**Code name:** Back-ease blur card.

## What you see
A photo of a room fades in and pushes slowly. 0.3s later a rounded card lands at the lower left: a small gold dot and uppercase kicker ("PART 4"), a two-line serif title, and a grey detail line. It starts at 78% size, 30px low, and overshoots to full size over 0.5s while fading in over 0.18s. When the photo changes, the card shrinks to 90% and fades in 0.3s. A red variant swaps the gold dot for red.

## When to use it
Labelling a beat that sits over a photo or video: a date, a chapter, a one-line fact. It reads best on dark or graded imagery. The same function can draw three cards side by side with `w` set to a third of the width, which makes a stat row.

## How it works
One function, `card(el, t, t0, opts)`, fills a prebuilt `.card` element. All sizes derive from `base = 30 * scale * fs`, so one number resizes the card:

```js
const base = 30 * S * fs
el.style.padding = `${base * 0.9}px ${base * 1.15}px`; el.style.gap = px(base * 0.35)
kicker font = base * 0.52, title = base * 1.5, desc = base * 0.78
const ki = backS(p(t, t0, t0 + 0.5), 1.9), ko = p(t, out, out + 0.3)
tf(el, { x: ox, y: y - (1 - ki) * 30 * S * dir, s: lerp(s0 = .78, 1, ki) * lerp(1, .9, ko), a: p(t, t0, t0 + .18) * (1 - ko) })
```
`backS(x, c1)` is an ease-out-back: `1 + c3*(x-1)^3 + c1*(x-1)^2` with `c3 = c1 + 1`. The glass is `background: rgba(18,20,26,.82)`, a 1.5px white 13% border, `backdrop-filter: blur(18px)` and a deep drop shadow. `align` lets you anchor the card by its left, centre or right edge (the function measures its width). The card also registers a `click` sound cue.

## Numbers that matter
| | |
|---|---|
| Card | radius 22px, fill rgba(18,20,26,.82), blur 18px |
| Type | kicker SF Pro 600 uppercase, tracking .2em, gold #e8b43a; title Playfair 700 white; detail #a9adb8 |
| In | 0.5s `backS(1.9)`, scale from .78, rise 30px, opacity over 0.18s |
| Out | 0.3s, scale .9 |
| Typical timing | each card lands 0.3s after its photo, holds about 5s |

## Sound
A soft mouse click (`click_002.ogg`, volume 0.55) on every card, over the drone bed and narration.

## Adapt it
- `k`, `title`, `desc` text, and `red: true` for the alarm colour.
- `fs` for a bigger or smaller card; `w` for a minimum width (stat rows).
- `align`, `x`, `y` for the anchor point; `s0` and `dir` change the entry.
- The gold in `.card .k`.

## Files
- `code/demo.html` runs on its own and loops; `?w=1080&h=1920` gives the tall layout. Playfair Display (SIL Open Font License, from Google Fonts) is copied into `code/fonts/` because the serif headline is half the look. Small labels suit SF Pro Display; the demo uses the system font stack instead. The demo draws gradient placeholders in CSS instead of photographs.
- `code/fonts/` holds the fonts the demo loads.

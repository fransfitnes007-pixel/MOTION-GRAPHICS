---
name: glass-card-border-beam-conic-light-chrome-rim
description: "The current look of the app: near-black glass cards with a lit top edge, a diagonal sheen, a deep black drop shadow, and a white light that travels round every card's border. Use it as the surface style for a dark dashboard hero."
---

# Glass card border beam

**Code name:** Masked conic light travelling a glass card's edge.

## What you see
A pure black page with two long blurred white arcs at the top left and bottom right. Cards float on it: 3.5% white fill with a diagonal sheen, a bright 1px chrome rim along the top edge, a softer rim below, and a deep black shadow. A hair-thin white light with a short soft tail runs once round each card's border every seven seconds; the cards are offset so no two are in step. Hovering a card in the app speeds its beam to 3.2s per lap.

## When to use it
The hero surface for a premium dark product: stat tiles, panels, a chart card. It is subtle at small sizes and needs room. Do not combine with the older violet `GlowCard` on one screen.

## How it works
A pseudo-element on every card (`::before`, `inset: -1px`, `padding: 2px`, `border-radius: inherit`) carries a conic gradient whose start angle is an animated custom property, then is masked to the border box only:

```css
@property --beam { syntax: '<angle>'; inherits: false; initial-value: 0deg; }
@keyframes beam-turn { to { --beam: 360deg; } }
background: conic-gradient(from var(--beam), transparent 0deg, transparent 190deg, rgb(255 255 255 / 0.18) 240deg, rgb(255 255 255 / 0.75) 285deg, rgb(255 255 255 / 1) 300deg, rgb(255 255 255 / 0.75) 315deg, rgb(255 255 255 / 0.18) 350deg, transparent 360deg);
-webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0); -webkit-mask-composite: xor;
animation: beam-turn 7s linear infinite;
```
The mask leaves only the 2px ring visible. The demo computes the angle from `t` instead of using the registered property, so it renders deterministically. Card fill is `linear-gradient(158deg, white 11% -> 3.5% -> 0 -> 1.5% -> 6%)` over `rgb(255 255 255 / 0.035)`, with `backdrop-filter: blur(22px) saturate(1.5)`. In this skin the accent tokens change too: `--rv-purple` becomes `59 130 246` (blue), muted `161 161 170`, card `18 18 22`, border `48 48 56`.

## Numbers that matter
- Beam: 7s linear, 8 stops (see above); drop-shadow `0 0 7px` white at 70%.
- Card edge `rgb(255 255 255 / 0.12)`; lit top `inset 0 1px 0 rgb(255 255 255 / 0.32)`.
- Shadow `0 30px 60px -24px #000, 0 2px 6px rgb(0 0 0 / .8)`.
- Page `#000` with arcs at 10% and 7% white, 28px blur.
- Per-card offsets in the app use nth-child delays; the demo uses 0, 2.3, 4.6, 1.2, 3.5 seconds.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- `--beam-light` colour (white) for a tinted beam.
- `7` in `(t + ph) % 7` for speed.
- The `SHEEN` and `SHADOW` strings for a flatter card.

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the numbers are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.

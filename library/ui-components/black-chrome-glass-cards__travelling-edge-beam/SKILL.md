---
name: black-chrome-glass-cards-travelling-edge-beam
description: "Near-black glass cards with a lit chrome top edge, a diagonal sheen and a short bright arc of light circling each card's border, every card at its own phase. Use for dark app panels or feature grids that should feel alive without moving content."
---

# Black chrome glass cards

**Code name:** Travelling edge beam.

## What you see
A pure black page with two very faint chrome arcs drifting behind it. Cards are barely lighter than the page: 3.5% white fill, a 1px edge at 12% white, a bright 1px highlight along the top inside edge (32% white) and a dim one along the bottom, plus a diagonal sheen that is brightest in the top-left. On each card a short arc of white light, about 110 degrees long and brightest at its leading end, travels round the 1px border once every 7 seconds with a soft white glow. Neighbouring cards are out of step so the grid never flashes together.

## When to use it
Dark dashboards, settings grids, feature grids, anything made of boxes where you want the surface to read as glass and the border to do the moving. Wrong for light pages (the beam is white) and for more than a dozen boxes on one screen, where it turns into noise.

## How it works
The beam is a `::before` pseudo-element laid over the card, not a border. It has `padding: 2px` and a conic gradient background, and a two-layer mask cuts out everything except the padding ring: `mask: linear-gradient(#000 0 0) content-box exclude, linear-gradient(#000 0 0)`. The conic gradient starts at `from var(--beam)`, where `--beam` is a registered `<angle>` property animated 0 to 360deg, so the lit arc orbits.

```css
@property --beam { syntax: '<angle>'; inherits: false; initial-value: 0deg; }
@keyframes beam-turn { to { --beam: 360deg; } }
.card::before { content:""; position:absolute; inset:-1px; padding:2px; border-radius:inherit; pointer-events:none;
  background: conic-gradient(from var(--beam), transparent 0deg 190deg, rgb(255 255 255/.18) 240deg,
    rgb(255 255 255/.75) 285deg, #fff 300deg, rgb(255 255 255/.75) 315deg, rgb(255 255 255/.18) 350deg, transparent 360deg);
  filter: drop-shadow(0 0 7px rgb(255 255 255/.7));
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0); -webkit-mask-composite: xor;
  mask: linear-gradient(#000 0 0) content-box exclude, linear-gradient(#000 0 0);
  animation: beam-turn 7s linear infinite; }
```
Because it is a pseudo-element on top, nothing is clipped and no stacking context is created, so menus inside the card still open. Phase offsets come from `nth-child`: 2n `-2.3s`, 3n `-4.1s`, 5n `-5.6s`. Hover drops the duration to 3.2s.

Demo changes: the source blurs the two haze arcs 28px and puts `backdrop-filter: blur(22px)` on each card. In headless Chrome both make frames differ between runs, and on near-black they are almost invisible, so the demo feathers the haze edge with a mask and leaves the backdrop blur out. The haze drifts once per 7s loop in the demo (the source takes 72s) so you can see it.

## Numbers that matter
| | |
|---|---|
| Card | radius 16px, fill `rgb(255 255 255/.035)` under a 158deg sheen, border `rgb(255 255 255/.12)` |
| Rim light | inset `0 1px 0 rgb(255 255 255/.32)`, `0 -1px 0 /.09`, sides `/.07` and `/.05` |
| Drop | `0 30px 60px -24px #000, 0 2px 6px rgb(0 0 0/.8)` |
| Beam | 2px ring, arc from 190deg to 360deg of the gradient, peak at 300deg, glow 7px at 70% |
| Speed | 7s per turn, 3.2s on hover |
| Haze | `120vw x 46vw` and `110vw x 40vw` radial arcs at 10% and 7% white, 36s and 44s alternate drift |

## Sound
Silent.

## Adapt it
- `--beam-light`: set a brand colour as RGB channels for a coloured beam.
- `7s` and the three `animation-delay` offsets.
- The gradient stops: widen 190deg-360deg for a longer tail, or narrow it to a comet.
- Fill and edge alpha (`--glass`, `--glass-edge`) for lighter or darker glass.

## Files
- `code/demo.html` runs on its own and loops in 7s (one beam turn).

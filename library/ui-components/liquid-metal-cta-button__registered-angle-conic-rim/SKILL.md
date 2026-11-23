---
name: liquid-metal-cta-button-registered-angle-conic-rim
description: "A black glass button inside a brushed-silver chrome rim, with small gold, blue and violet glints that keep travelling round the edge. Use it as the one primary call to action on a light or dark page."
---

# Liquid metal CTA button

**Code name:** Registered angle conic rim.

## What you see
A 48px-high rounded button with a near-black core (`#1c1c1f` fading to `#000`) and light grey text. Around it is a 3.5px chrome rim, light at the top and darker towards the bottom. Two short bright arcs run round that rim: one gold, white, blue, violet around the 10% mark, and a second blue, white, orange around 60%. They complete a turn every 6 seconds. On hover the lift is 1px, the text goes white, a faint blue glow appears and the arcs speed up to 2.6 seconds per turn. A round version of the same class is the play button on the film card, with a pinging ring behind it.

## When to use it
The single most important action on a page, such as "Book a call". Works on a white page and on a black one, since the core is black and the rim is silver. It is loud, so one per screen.

## How it works
Three stacked backgrounds on one element with a transparent border: the black core clipped to `padding-box`, then a conic gradient clipped to `border-box`, then a static silver linear gradient clipped to `border-box`. Because the conic gradient has transparent stops, the silver shows through everywhere except the glints. The glints move because the conic gradient starts at `from var(--metal-a)`, and `--metal-a` is a registered `<angle>` property animated from 0 to 360deg.

```css
@property --metal-a { syntax: '<angle>'; inherits: false; initial-value: 0deg; }
@keyframes metal-spin { to { --metal-a: 360deg; } }
.cta-glass { border: 3.5px solid transparent; animation: metal-spin 6s linear infinite;
  background: linear-gradient(180deg,#1c1c1f,#000) padding-box,
              conic-gradient(from var(--metal-a), transparent 0 7%, rgba(255,214,120,.95) 9%, ...) border-box,
              linear-gradient(180deg,#f2f2f4,#c6c6cb 30%,#8d8d93 62%,#b9b9be) border-box; }
```
The `@property` registration is what lets the browser interpolate the angle. Without it the variable would jump from 0 to 360 with no steps in between.

In the demo the angle is set from `t` each frame instead of from a CSS animation, so frames render the same every time. The 22px blue hover shadow is drawn as a radial gradient in the demo, because a blurred shadow renders slightly differently from run to run in headless Chrome. The hover section runs the same two speeds the CSS uses and the total is scaled to a whole number of turns so it loops cleanly.

## Numbers that matter
| | |
|---|---|
| Size | `h-12 px-6 rounded-xl`, 14px semibold text; round variant 80 to 96px |
| Core | `linear-gradient(180deg, #1c1c1f, #000)`, text `#d4d4d8`, hover `#fff` |
| Rim | 3.5px, `#f2f2f4 > #c6c6cb 30% > #8d8d93 62% > #b9b9be` |
| Glints | gold `255,214,120`, white, blue `150,190,255`, violet `196,140,255` at 9 to 13.5%; blue `170,210,255`, white, orange `255,190,140` at 58 to 61% |
| Speed | 6s per turn, 2.6s on hover |
| Press | `translateY(1px) scale(.98)`, inset shadow |
| Transition | .25s `cubic-bezier(.34,1.56,.64,1)` on transform |

## Sound
Silent. A short soft click on press suits it.

## Adapt it
- The glint colours in the conic gradient (keep the transparent runs between them).
- `6s` and `2.6s` for calmer or faster travel.
- The core gradient, if you want a white core: swap the two dark stops and the text colour (the site's dark theme does exactly this with `--cta-*` variables).
- Add a second glint pair at 30% and 80% for a busier rim.

## Files
- `code/demo.html` runs on its own and loops in 8s.

---
name: phone-trio-view-counters-spring-flank-count-up
description: "Three phones: an analytics screen in the middle flanked by two video phones that slide in from the sides, each with a pill under it counting views up from zero to a round figure, a \"Big win\" tag popping above one, and a violet frame highlighting a number on the centre screen."
---

# Phone trio with view counters

**Code name:** Spring flank, count up.

## What you see
The centre phone (340px wide) rises 80px and eases from 150% to 100% size out of a 10px blur at 16.62s. The side phones (300px) spring in from left and right, 0.08s and 0.16s later, tilted 10 degrees outward and ending at 3 degrees. Under each side phone a white pill with an eye icon counts up: the left one to 1,000,000 and the right to 4,000,000, using eased numbers that finish at 17.95s and 18.05s and then snap to "1M" and "4M" in violet. At 17.57s a green "Big win" pill pops at the top right and a 4px violet rounded frame closes in on a stat on the centre phone. At 18.3s the three fly out: the sides slide out 300px, the centre blurs.

## When to use it
A proof beat: here are the videos, here is the analytics screen, here are the numbers. Works with any three-up layout where the middle one is a product screen and the sides are results.

## How it works
Counters are eased numbers. Formatting is `toLocaleString('en-US')`; the final value is replaced with a short form so the number lands on something readable.

```js
const ce = 17.95 + i * .1
c.n.textContent = t < ce ? fmt(lerp(0, c.to, eo5(seg(t, 17.2 + i * .12, ce)))) : (c.to / 1e6) + 'M'
c.n.style.color = t >= ce ? '#6d3cff' : ''
```
`font-variant-numeric: tabular-nums` stops the pill from changing width on every digit. Pills are positioned from the phones' own `offsetLeft` and `offsetTop` each frame, so they follow the phone when it moves.

## Numbers that matter
| | |
|---|---|
| Phones | centre 340px at (790,230); sides 300px at (330,300) and (1290,300) |
| Centre | `eo5` 0.58s, scale 1.5 to 1, rise 80px, blur 10px |
| Sides | `spring(k=7, f=11)` 0.65s, slide 160px, rotate 10 degrees to -3 |
| Counters | start 17.2s, 0.35s `eo5` fade-in, finish 17.95s, then "1M"/"4M" in `#6d3cff` |
| Win tag | spring k=8 f=12 from 17.57s, scale .6 to 1, at (1310,262) |
| Highlight | 146x90 frame, 4px `#8b5cf6` plus 8px halo, scale 1.2 to 1 over 0.3s |
| Exit | 18.3s `eio5`, 0.32s |

## Sound
A short soft pop on the "Big win" tag (about 1.2 kHz at 17.67s). The previous cut has a whoosh at 16.7s.

## Adapt it
- Final numbers (`to`) and their short forms.
- Phone content: swap `coverBg` for your own covers and `p7c.im.innerHTML` for an analytics screenshot.
- The highlight's position, to circle a different stat.
- `T_OUT`.

## Files
- `code/demo.html`

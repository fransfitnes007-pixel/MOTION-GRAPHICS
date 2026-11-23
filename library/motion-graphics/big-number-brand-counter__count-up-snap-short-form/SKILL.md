---
name: big-number-brand-counter-count-up-snap-short-form
description: "A brand mark above a 260px number that counts up from a few percent to a round figure in 1.3s, then snaps to the short form (\"12M\"), turns violet and pops; a caption fades in under it. The same layout is then replaced by the next brand and number sliding up from below."
---

# Big brand number counter

**Code name:** Count up, snap to short form.

## What you see
One layout in two beats. A logo (300px rounded icon, or a 720x300 wide mark) drops into place with a slight rotation, the number below it fades in at 0.2s and runs digit by digit: it starts at 4% of the target and eases to 99.99% over about 1.35s with a long deceleration. On the last frame of the count it is replaced by "12M" in violet with a 12% scale pop (spring k=9, f=14). The caption ("views for ...") fades up 0.1s before. The group then lifts away 160px and blurs, while the second brand rises from 140px below. Both beats are tied to the voice: the figure lands on the word that says it.

## When to use it
Results, case studies, social proof with one number per customer. It is built for a voiceover that says each figure. The count gives the number weight; the snap to short form gives it a clean final read. Do not use it for more than two or three in a row; the beats are 2s each.

## How it works
One state function per brand, all driven by time:

```js
const cEnd = i ? WT.second + .1 : WT.first - .05           // when the count finishes: on the spoken word
d.n.textContent = t < cEnd ? fmt(lerp(d.to * .04, d.to, eo5(seg(t, a, cEnd)))) : d.short
const pop = spring(seg(t, cEnd, cEnd + .4), 9, 14); d.n.style.transform = t >= cEnd ? `scale(${1 + (1 - pop) * .12})` : ''
d.n.style.color = t >= cEnd ? '#6d3cff' : '#0b0b10'
```
`eo5` makes the digits run fast then crawl through the last 5%, so the final figure is visible and the snap is clean. `tabular-nums` keeps the digits from jittering sideways.

## Numbers that matter
| | |
|---|---|
| Number | 260px weight 800, letter-spacing -.055em, centred at y=500 |
| Count | from 4% of the target, `eo5`, 1.3s to 1.4s per figure |
| Snap | `spring(k=9, f=14)` 0.4s, pop 12%, colour `#6d3cff` |
| Mark | spring k=7 f=11 over 0.65s, scale .6 to 1, rotate -8 to 0 |
| Caption | 54px weight 600 `#55556a`, fades up 20px in 0.4s |
| Exit | `eio5` 0.32s: -160px, blur 16px; second brand enters from +140px |

## Sound
A low impact hits at the start of each figure (18.53s, 20.53s) and a whoosh covers the swap; music continues.

## Adapt it
- `to`, `short`, and the caption.
- Brand marks: icon or wide wordmark placeholders in the demo are CSS.
- `cEnd`: set to the voice cue for the figure.
- The accent colour for the snapped number.

## Files
- `code/demo.html` (names and figures are placeholders).

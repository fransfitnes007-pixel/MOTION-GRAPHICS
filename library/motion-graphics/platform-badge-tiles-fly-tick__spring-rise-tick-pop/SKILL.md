---
name: platform-badge-tiles-fly-tick-spring-rise-tick-pop
description: "Four white rounded icon tiles, one per platform, fly up out of a row of phones one after another, tumbling straight as they spring into place, and each gets a green tick that pops onto its corner."
---

# Platform badge tiles with ticks

**Code name:** Spring rise, tick pop.

## What you see
Under the headline, four 132px white tiles with a 36px corner radius and a long soft shadow rise from 560px down to y=252. Each starts at 50% size and tilted by up to 21 degrees, then springs to full size and level, 0.12s after its neighbour. 0.3s after a tile lands, a 44px green circle with a white check springs onto its top-right corner with its own overshoot. The tiles sit 168px apart in a centred row. They leave together at 16.3s.

## When to use it
"Works on all of these": platforms, integrations, channels, payment methods. The tick says each one is connected or done, not just supported. It reads best over a busy background, for example with a row of phones shrinking behind it.

## How it works
Two springs per tile, one for travel and one for the tick:

```js
const at = WT.every3 + p.i * .12, q = spring(seg(t, at, at + .6), 7, 11)
S(p, { left: x + 'px', top: lerp(560, 252, q) + 'px', opacity: clamp(q * 1.6) * (1 - o),
  transform: `scale(${.5 + .5 * q}) rotate(${(1 - q) * (p.i - 1.5) * 14}deg)` })
const k = spring(seg(t, at + .3, at + .75), 8, 13); p.tk.style.transform = `scale(${k})`
```
`(p.i - 1.5)` makes the outer tiles tumble in opposite directions and the inner two barely at all. A real build can use the platforms' own logo marks; the demo uses simple line icons so there is nothing to license.

## Numbers that matter
| | |
|---|---|
| Tile | 132x132, radius 36px, white, shadow `0 30px 60px -20px rgba(24,16,52,.45)` |
| Icon | 64px |
| Row | x = 960 - 336 + 168i + 18, final y 252 |
| Travel | spring k=7 f=11 over 0.6s from y=560; scale .5 to 1; rotate (i-1.5) x 14 degrees to 0 |
| Tick | 44px `#16a34a` circle at right/top -10px, spring k=8 f=13 over 0.45s, 0.3s after the tile starts |
| Stagger | 0.12s |

## Sound
Short ascending pops, one per tile (1.04 kHz up in 120 Hz steps), about 0.3s after each tile starts, matching the tick.

## Adapt it
- The icons: replace `svgIcon` with `<img>` logos.
- The number of tiles and the 168px pitch.
- `WT.every3` and the stagger.
- The final y, to put the row elsewhere.

## Files
- `code/demo.html`
- Related: `phone-grid-tilted-row__preserve-3d-stagger-spring`.

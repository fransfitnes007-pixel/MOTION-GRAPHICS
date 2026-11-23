---
name: node-pipeline-sequenced-lightup-wire-scale-sparks
description: "Five dark step boxes in a row light up one by one under a headline, a glowing wire grows between each pair and a white spark runs along it. A process or workflow in steps: brief, build, review, live, done."
---

# Node pipeline light-up

**Code name:** Wire scale with travelling sparks.

## What you see
A headline fades in over a row of five empty step boxes (dim, 25 percent opacity). One by one, every 0.55s, a box rises 16px into place and lights up with a lilac border and glow. As each box lights, the wire to the next grows left to right and a white spark travels along it. By 3.4s all five are lit.

## When to use it
A process or workflow in steps: brief, build, review, live, done. The sequence follows the narration naming each step. Fits any 3 to 6 step list.

## How it works
Everything is a function of one index-shifted timeline: step i turns on at `.5 + i * .55`; wire i grows from `.8 + i * .55`. The wire is a 90px div scaled on x from the left; the spark is a glowing dot whose left position follows the same 0 to 1.

```js
const on = seg(lt, .5 + i * .55, .9 + i * .55)
S(n, { opacity: .25 + .75 * eo(on), borderColor: on >= 1 ? 'rgba(196,181,253,.9)' : 'rgba(167,139,250,.35)', boxShadow: on >= 1 ? '0 0 40px rgba(139,92,246,.55)' : 'none', transform: `translateY(${(1 - eo(on)) * 16}px)` })
w.style.transform = `scaleX(${eo(seg(lt, .8 + i * .55, 1.1 + i * .55))})`
```

## Numbers that matter
| | |
|---|---|
| Boxes | 250 x 120, radius 20px, 340px apart, y 480 |
| Interval | 0.55s per step, 0.4s to light up |
| Wires | 90px x 2px, gradient #8B5CF6 to #C4B5FD, grow in 0.3s |
| Spark | 14px white dot, 18px glow |

## Sound
Suggested sound: a pink-noise whoosh (high-passed at 600 Hz, low-passed at 5.2 kHz, 0.7s long, volume .22) peaking on every scene cut, over a low A-minor drone pad that ducks under the narration. A soft tick per step suits it; a voiceover naming each step ("Brief. Build. Review. Live. Done.") can be timed to the lights.

## Adapt it
- The step names and count (and the x spacing).
- Interval 0.55s to match the voice.
- Border and glow colour.

## Files
- `code/demo.html` runs on its own with no network. Product screens, covers, logos and the wordmark are CSS placeholders.

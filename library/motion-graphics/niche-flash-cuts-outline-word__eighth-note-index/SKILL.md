---
name: niche-flash-cuts-outline-word-eighth-note-index
description: "Five hard cuts at eighth-note spacing, each a tall video cover over a 330px outlined word that slides in 60px, with a label pill under it; the first cut shrinks from 2.4x as if arriving from the previous zoom. A rapid-fire list on a beat: niches, categories, examples."
---

# Eighth-note flash cuts with outlined giant word

**Code name:** Eighth-note index cuts.

## What you see
Five hard cuts at eighth-note spacing (234ms). Each shows a tall portrait cover over a 330px word drawn as an outline only, sliding 60px in from alternating sides. The cover is crooked by 2 degrees (alternating) and punches in 6 percent on each cut, and a pill below it carries the name. The first cut starts at 2.4x and settles, as if arriving from the zoom before it.

## When to use it
A rapid-fire list on a beat: niches, categories, examples. Five items in just over a second is the pace; more than that gets unreadable.

## How it works
A single clock `n = floor(lt / step)` picks which item to show; `cutPhase` (0 to 1 within the step) drives the punch and slide.

```js
const step = B / 2, n = Math.floor(lt / step), cutPhase = (lt % step) / step
const punch = 1 + (1 - eo(cutPhase)) * .06
S(nWord, { transform: `translateX(${(1 - eo(cutPhase)) * (i % 2 ? 60 : -60)}px)` })
// outline word: color transparent; -webkit-text-stroke: 3px rgba(196,181,253,.55)
```

## Numbers that matter
| | |
|---|---|
| Step | 234ms (half a beat at 128 BPM) |
| Cover | 470 x 836 at (725,122), radius 34px |
| Word | 330px weight 800, tracking -.06em, 3px stroke |
| Punch | +6 percent decaying by `eo` each step |
| First cut | scale 2.4 to 1 over 0.21s |

## Sound
Suggested bed: a synthesised 128 BPM groove in A minor (Am F C G): kick on every beat, claps on 2 and 4, open hats on the offbeats, sidechained bass. Impacts (a sine boom plus filtered noise crash) land on beats 12, 40, 48 and 60, and a band-passed noise whoosh peaks on each moving transition. A closed-hat tick is placed on each cut (5 of them, 2x gain).

## Adapt it
- Labels and covers.
- Step length for your tempo.
- Number of items (index cap `4`).

## Files
- `code/demo.html` runs on its own with no network. Product screens, covers, logos and the wordmark are CSS placeholders.

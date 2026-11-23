---
name: giant-cropped-number-beat-cuts-punch-scale-count
description: "Hard cuts every 3 beats between full-frame colour fields, each with a 560px number that counts up, punches in from 118 percent and runs off the right edge, beside a small brand label that slides in. Results shown as numbers, one per beat, in a video cut to music."
---

# Giant cropped number beat cuts

**Code name:** Punch scale count.

## What you see
Three hard cuts, one every three beats (1.4s), the last held for two beats: navy, off-white, purple. Each is a full-frame field with a 560px number that runs off the right edge, counting up from zero, punching in from 118 percent and creeping to 106 percent. Beside it a small brand square, name and caption slide in from 60px left. A white flash hits on every cut.

## When to use it
Results shown as numbers, one per beat, in a video cut to music. The cropped number makes it a graphic rather than a stat card. Use when each customer or figure deserves a whole screen.

## How it works
Cuts are a list of beat times; each field runs its own local clock `l` over its length `len`.

```js
const cuts = [0, 3 * B, 6 * B, 8 * B]                 // B = 60 / 128
const v = n * eo(seg(l, 0, len * .7))
const punch = lerp(1.18, 1, eo5(seg(l, 0, .35))) * lerp(1, 1.06, l / len)
S(big, { transform: `scale(${punch})`, transformOrigin: '0 60%' })
// flash: opacity (1 - k) * .55, k = seg(t, cut, cut + .12)
```
The origin at the left edge makes the number grow to the right and out of frame.

## Numbers that matter
| | |
|---|---|
| Number | 560px weight 800, tracking -.065em, at (640, 230) |
| Count | first 70 percent of each field, `eo` |
| Punch | 1.18 to 1 in 0.35s (`eo5`), then to 1.06 |
| Cuts | 0, 3, 6 beats; end at 8 beats |
| Backgrounds | navy radial, #f4f2ee, purple radial |

## Sound
A suitable soundtrack is a synthesised 128 BPM groove in A minor (Am F C G): kick on every beat, claps on 2 and 4, open hats on the offbeats, sidechained bass. Impacts (a sine boom plus filtered noise crash) land on beats 12, 40, 48 and 60, and a band-passed noise whoosh peaks on each moving transition. Beats 40, 43 and 46 each have a hit; the first is the big impact.

## Adapt it
- Brand, caption and figure per field.
- Beat length `B` for your tempo.
- Number size (560px) and the left offset.
- Field colours.

## Files
- `code/demo.html` runs on its own with no network. Screens, covers, logos and the wordmark are CSS placeholders.

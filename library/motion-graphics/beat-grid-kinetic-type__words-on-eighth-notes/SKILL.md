---
name: beat-grid-kinetic-type-words-on-eighth-notes
description: "A sentence appears one word per eighth note at 120 BPM, each word at a different size and place on a 12-column grid, with a bass-hit scale punch on every beat and a bigger one on the bar downbeat. Reach for it as the manifesto or tagline beat of a showreel, cut to a track."
---

# Beat grid kinetic type

**Code name:** Words on eighth notes. **From:** original build for this library.
Original code; informed by the structure of popular AI-made showreels (see motionvideo.xyz and revid.ai).

## What you see
A near-black frame with twelve faint column bars that brighten on each beat. At 0.25 s, then every 0.25 s, one word of MAKE EVERY SINGLE FRAME LAND ON THE BEAT lands: it arrives at 170 % scale on a spring, a touch high, in the accent colour that cools to paper in about 0.3 s. EVERY is the largest (ten columns wide), MAKE the smallest (two columns), and the last word BEAT stays in the accent. On every quarter note (0.5 s) the whole composition pulses 3.2 % larger and settles in 0.25 s; on the bar downbeats (0 s and 2 s) the pulse is 7.5 %. A strip of eight ticks at the bottom lights the current eighth note. From 3.5 s the words drop out in four quick groups so the loop restarts empty.

## When to use it
A tagline or a list of values in a showreel, the lyric line of a music-cut reel, or the sentence that explains a product between two visual beats. It is wrong for long copy (8 words is already the limit at this scale) and for slow, calm films.

## How it works
The grid maps a word to `[first column, columns spanned, row]`. Each word is measured once at 100 px and scaled so its width equals the span exactly, then capped so its cap height (0.72 em) fits 84 % of its row; rows have unequal heights (42 %, 27 %, 31 % wide) so the sizes differ a lot:

```js
fs = spanWidth / (measureText(word).width / 100)
if (0.72 * fs > rowH * 0.84) fs *= rowH * 0.84 / (0.72 * fs)
```
Timing is a function of the musical grid: word `i` starts at `0.25 + i * 60 / BPM / 2`. The punch uses the quarter index `q = floor(t / (60 / BPM))` and the time since it, `uq`: `scale = 1 + (q % 4 === 0 ? .075 : .032) * exp(-11 * uq)`, applied to the whole canvas about the centre. The column guides use the same `uq` for their pulse. Tall layout uses 7 rows and different spans so each word still fills its slot.

## Numbers that matter
| | |
|---|---|
| Tempo | 120 BPM: eighth 0.25 s, quarter 0.5 s, bar 2 s |
| Word arrival | spring k 6.5 f 10 over 0.3 s from 170 %, accent flash decay `exp(-7u)` |
| Punch | 3.2 % on beats, 7.5 % on downbeats, `exp(-11u)` |
| Grid | 12 columns, 18 px gutters, 90 px margins |
| Exit | 3.5 s, 4 groups 0.06 s apart, `ei` over 0.22 s |
| Colours | ink `#0b0b10`, paper `#f2f2f4`, accent `#ff4b2b` on the arrival and the last word |

## Sound
Silent in the demo. Put a kick on every quarter note and a bigger sub hit on the downbeats, a hi-hat or tick on each eighth, and make the punch frames line up with the transients (the code already uses the same clock).

## Adapt it
- `WORDS` and the `WIDE` and `TALLP` placement tables (column, span, row).
- `BPM`, which moves every time in the piece.
- `ACC`, and which word is held in the accent (the last).
- Row heights `RH` to change how large the big word is against the small ones.

## Files
- `code/demo.html` runs on its own, loops every 4 s, composes at 1920x1080 and at `?w=1080&h=1920`.
- `media/poster.jpg`

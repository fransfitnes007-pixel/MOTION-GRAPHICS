---
name: voiceover-driven-scene-schedule-max-min-vo-duration
description: "Scene start times computed from the narration: each scene lasts the longer of a design minimum and its voice line plus a pad, so a slower narrator stretches the video without drift. Use it for any video with a voiceover that may change."
---

# Voiceover-driven scene schedule

**Code name:** Max of minimum and voice length.

## What you see
A bar made of eight scene blocks (hook, intro, title, setup, timeline, events, value, end card) over a row of gold voice-line bars. Every 2.4s the narrator changes (Andrew, Christopher, Vincent): the blocks ease to their new lengths and the total changes from 90.0s to 98.4s to 102.8s.

## When to use it
A video where narration is a separate recording: swapping the voice, rewriting a line, or making a short cut. The scenes then fit the new audio without re-timing by hand.

## How it works
The page loads each voice line's length into a table (`VOD`, from the files' durations), and every scene start is derived:

```js
o.truth    = Math.max(4.6, 0.35 + vd(hk) + 0.6)
o.book     = o.truth + Math.max(4.2, vd('02_true') + 0.9)
o.setup    = o.book + 7.8
o.timeline = o.setup + Math.max(13, vd('04_setup') + 1.0)
o.events   = o.timeline + Math.max(19, vd('05_timeline') + 1.0)
o.vo = { '01_hook': 0.35, '02_true': o.truth + 0.3, '03_title': o.book + 0.7, '04_setup': o.setup + 0.4, ... }
```
Each scene then runs off `t0` and a ratio `r = (tEnd - t0) / designLength`, so beats inside a scene (timeline ticks, event cards) scale with it. The same renderer dumps the voice start times as `window.VO` so the audio script knows where to place each file. `DUR` is the schedule's end. The demo runs these formulas for three voices and draws them.

## Numbers that matter
| | |
|---|---|
| Hook / intro | min 4.6s / 4.2s; pad 0.6s / 0.9s |
| Title | fixed 7.8s |
| Setup / timeline / events | min 13 / 19 / 22s; pad 1.0 / 1.0 / 1.2s |
| Value / end card | min 9.4 / 8.6s; pad 1.0 / 1.4s |
| Voice start in scene | +0.3 to +0.7s |
| Totals, long cut | Andrew 90.0s, Christopher 98.4s, Vincent 102.8s |

## Sound
Silent. The voice lines are `vo/<voice>_<key>.mp3` and the mixer places each at the time in `VO`.

## Adapt it
- The minimums and pads per scene.
- The `VOD` table: lengths of your own lines.
- The list of scenes and keys.

## Files
- `code/demo.html` runs on its own and loops; `?w=1080&h=1920` gives the tall layout. Playfair Display (SIL Open Font License, from Google Fonts) is copied into `code/fonts/` because the serif headline is half the look. The demo uses the system font stack for small labels.
- `code/fonts/` holds the fonts the demo loads.

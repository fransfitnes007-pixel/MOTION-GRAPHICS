---
name: cue-sheet-mixing-json-cues-to-timeline
description: "The page records every click, key and whoosh with its time as it plays; a script turns that list into a finished sound track. When the sound should be driven by the animation."
---

# Cue-sheet mixing

**Code name:** JSON cues to timeline.

## What you hear
A 9 s demo track from a made-up cue list: a run of key clicks (one duplicated on purpose), a click, a whoosh, a thud, two page flips, an 18-tick run, another click, and a cue with a type that does not exist, with a low drone under it all. The script prints that 38 sounds were mixed from 41 cues, because it drops the duplicates and the unknown type.

## When to use it
When the sound should be driven by the animation. The page already knows when each key is typed and each button is pressed, so it writes that down, and the audio is built from the list and cannot go out of sync. It suits UI demos and screen-recorded videos. It is wrong for a video where the sound leads (a voice-timed edit, see the word-timestamp recipe).

## How it works
The page keeps a list and a one-line function:

```js
const SOUNDS = []   // {t,type}
const snd = (t, type) => { if (!SOUNDS.some((s) => s.t === t && s.type === type)) SOUNDS.push({ t, type }) }
window.SOUNDS = SOUNDS; window.VO = SCH.vo
```

The renderer reads those after playing the page and writes `<video>.sounds.json` containing `{dur, sounds: [{t, type}], vo: {key: startSeconds}}`. The audio script then:

1. Sorts cues by time. Skips repeated `(type, round(t, 2))` and any type not in the table.
2. Maps each type to a sound and a volume: `click .55, key .5, tick .35, whoosh .5, thud .9, flip .8`.
3. Places each at its time (`adelay` in ffmpeg, an offset in numpy).
4. Adds the voice lines, each with a high-pass at 70 Hz and a 3:1 compressor, plus a drone bed (see the dark drone recipe).
5. Mixes without normalising, limits at 0.95 and loudnorms to -15 LUFS (see the final master recipe).

A production version would be an ffmpeg graph over sampled files (key presses, clicks, a tick, a whoosh, a thud, a page flip). `recipe.py` mixes synthesised stand-ins in numpy and accepts your own cue file as a second argument: `python3 recipe.py out.wav cues.json`. A minimal version needs only two types, with keys cycling through 16 samples.

## Numbers that matter
| | |
|---|---|
| Cue format | `{"dur": s, "sounds": [{"t": s, "type": "click"}], "vo": {"hook": 0.4}}` |
| Volumes | click 0.55, key 0.5, tick 0.35, whoosh 0.5, thud 0.9, flip 0.8 |
| Key samples | cycle `k % 16` |
| Dedupe | same type and time rounded to 10 ms |
| Voice chain | high-pass 70 Hz, compressor -18 dB 3:1 attack 10 ms release 120 ms |
| Output chain | alimiter 0.95, loudnorm I=-15 TP=-1.2 LRA=11 |

## Sound
The tracks are only as good as the samples. For anything that repeats (keys, ticks), use more than one sample and cycle through them.

## Adapt it
- The `SFX` table: new types, files and volumes.
- The cue list: from your page, or the file you pass.
- The bed: swap the drone for your own music.
- The dedupe rule and the sample cycle length.

## Files

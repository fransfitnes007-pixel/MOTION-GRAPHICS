---
name: full-film-soundtrack-122bpm-am-f-c-g
description: "A complete 29 s synthesised soundtrack in A minor: intro plucks and a riser, a bright groove, a drop-out joke beat, an end-card pad, and effects timed to the picture. As the model for a whole film's sound: the structure (intro, slam, groove, break, end card), the cue list that puts effects on the picture, and the mix."
---

# Full film soundtrack

**Code name:** 122 BPM Am F C G.

## What you hear
29 s from the first note to the fade. Plucks and hats rise from nothing, a 2 s noise riser reaches a slam at 6.7 s, and the full groove runs under pops, whooshes, clicks and a counter until a cut at 21.3 s drops everything out for a joke. A pad and one more impact carry the end card, then a fade. Without a voice file nothing is ducked, so music and effects play at their top level.

## When to use it
As the model for a whole film's sound: the structure (intro, slam, groove, break, end card), the cue list that puts effects on the picture, and the mix. Copy it and replace the times. It is wrong as a drop-in track for another film: the times belong to one particular picture.

## How it works
Everything is in one script and nothing is sampled. Parts, in order: helper functions (`put`, `env`, `lp`, then the drum, bass, pluck, riser, impact, whoosh, pop, click, tick and pad voices); a beat loop with three branches (intro, drop, groove); the long list of timed effects; the voice and ducking; fade and soft clip. Each part has its own skill in this library:

| Part | Skill |
|---|---|
| whooshes on every cut | whoosh-on-cut |
| pops on words and tiles | pop-on-word-reveal |
| clicks | cursor-click |
| counter ticks | keypress-ticks-under-counter |
| confetti | confetti-burst |
| riser and impact | riser-into-slam |
| drums | kick-and-clap-groove |
| stabs and arp | chord-stab-arp |
| break | groove-drop-out |
| ducking | music-ducking-under-voice |
| fade and soft clip | final-master |

The voice file is optional (`python3 recipe.py out.wav voice.wav`). Variants of the same engine at 128 BPM differ in timings and some gains.

## Numbers that matter
| | |
|---|---|
| Tempo and key | 122 BPM, A minor, Am F C G one per bar |
| Sections | intro 0 to 6.7 s, groove 6.7 to 21.3 s, drop-out 21.3 to 25.4 s, end card 25.4 s on |
| Fade | last 1.4 s |
| Voice | starts at 0.4 s, music ducked to 0.5 |
| Mix | music x 0.75, effects x (0.6 + 0.4 duck), voice x 1.05 |
| Master | `tanh(1.1x)/tanh(1.1)` |
| Run time | about 3 seconds to render |

## Sound
The whole track. Add a voice and a picture on top.

## Adapt it
- The times (cut list, `SLAM`, `DONE`, `JOKE`, `END`).
- `BPM` and the chord table.
- The effect list: every `put(fx, ...)` line is one sound on one frame.
- The voice file, to hear it with the ducking.

## Files

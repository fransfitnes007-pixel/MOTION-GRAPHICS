---
name: half-time-d-minor-bed-pad-and-sixteenth-arp
description: "A slower, heavier bed in D minor at 104 BPM: a saw pad, a quiet 16th-note arp, a half-time kick and clap, and a slow sidechain dip. Where the 122 or 128 BPM groove is too busy: a product explainer, a long film with a lot of voice."
---

# Half-time D minor bed

**Code name:** Pad and sixteenth arp.

## What you hear
One bar of build with a muffled arp under a pad, then a drop: kick on 1 and the 'and' of 3, clap on 3 only, light eighth-note hats, a long bass note every second beat, and the arp opening up. Four bars of groove, then a held chord and a long bass note and an impact. It is calmer and wider than the 122 BPM bed.

## When to use it
Where the 122 or 128 BPM groove is too busy: a product explainer, a long film with a lot of voice. Half-time feels slow but the sixteenth arp keeps it moving. It is wrong for a fast 20 s cut.

## How it works
A chord per bar (Dm, Bb, F, C), played by a three-saw detuned pad (`saw(f) + saw(f*1.006) + saw(f*.994)`, low-passed at 700 Hz before the drop and 1100 Hz after) and by a 16th-note arp that steps through the chord tones an octave up.

```python
f = ch[(beat * 4 + s16) % 3] * (2 if s16 == 3 else 1) * 2
put(mus, pluck([f], B / 4, 900 if t < SLAM else 2600), t + s16 * B / 4, .05 if t < SLAM else .07, pan=(-.4 if s16 % 2 else .4))
```

Drums are the 128 BPM groove's. The kick lands on beat 1 and half a beat after beat 3 (`beat % 4 == 2`, `t + B/2`). The slow sidechain dip is `0.3 + 0.7 * linspace(0,1,0.3 s)^1.5` on every second beat. A fuller mix can thin the clap out two beats before each wipe transition, which the recipe leaves out as it has no wipes.

## Numbers that matter
| | |
|---|---|
| Tempo | 104 BPM |
| Chords | Dm [146.83, 174.61, 220], Bb [116.54, 146.83, 174.61], F [174.61, 220, 261.63], C [130.81, 164.81, 196] |
| Bass roots | 36.71, 29.14, 43.65, 32.7 Hz, 1.6 beats long, every other beat, gain 0.55 |
| Pad | 3 detuned saws, gain 0.12, cutoff 700 then 1100 Hz |
| Arp | 16ths, gain 0.05 then 0.07, bright 900 then 2600 |
| Kick | beat 1 gain 0.95, off-3 gain 0.7 |
| Dip | floor 0.3, 0.3 s |

## Sound
A mid-energy bed that leaves room for voice. Add whooshes at the wipes and pops on the reveals.

## Adapt it
- `BPM`, chord lists and bass roots, to change key and speed.
- `SLAM` and `END`, to your film's drop and finish.
- The pad cutoffs (700 to 1100 Hz).
- The kick pattern, for four on the floor.

## Files

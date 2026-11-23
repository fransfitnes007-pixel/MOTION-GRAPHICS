---
name: chord-stab-arp-detuned-saw-lowpass-pluck
description: "Short bright synth plucks: an eighth-note arpeggio whose filter opens over twelve beats, then off-beat chord stabs. The melodic part over a drum groove, or an intro that builds."
---

# Chord stab and arp

**Code name:** Detuned saw lowpass pluck.

## What you hear
Part one: an eight-note-a-bar arpeggio over Am, F, C, G that starts dull and muffled and opens up until the top of the filter is wide open by beat twelve, with a little hi-hat creeping in from beat four. A short gap, then part two: four bars of groove stabs, a short chord on the offbeat of beats 1 and 3, and a high octave blip on the last sixteenth of beat 4, panned left then right.

## When to use it
The melodic part over a drum groove, or an intro that builds. The filter opening is a free way to build tension over 2 to 3 bars. It is wrong over a voice that is busy in the same range; thin the arp out or play it an octave up.

## How it works
Each note is two saws, one at the pitch and one 0.4% sharp (about 7 cents), averaged, through a one-pole low-pass whose cutoff starts high and falls in 0.12 s: a pluck.

```python
def pluck(freqs, dur, bright):
    x = sum(saw(f, n) + saw(f * 1.004, n) for f in freqs) / len(freqs)
    return lp(x, 350 + bright * env(n, .001, .12)) * env(n, .002, .26)
```

`bright` is the filter-opening parameter. In the intro it rises from 900 to 4900 over 12 beats: `bright = 900 + 4000 * min(1, beat / 12)`. Chords are lists of Hz (Am 220, 261.6, 329.6 and so on). Stabs use `pluck(chord, .25, 2600)`. Panning alternates by beat. A variant has a base cutoff of 300, a 0.28 s decay and a third chord with G3 at the bottom (C over G).

## Numbers that matter
| | |
|---|---|
| Detune | second saw at x1.004 |
| Cutoff | `350 + bright * exp(-t/.12)` Hz (variant: `300 + ...`) |
| Amp envelope | attack 2 ms, decay 0.26 s (variant: 0.28 s) |
| Intro arp | 2 notes a beat, gain 0.16, pan +/-0.35, bright 900 to 4900 |
| Groove stabs | chord at beats 1 and 3, gain 0.22, length 0.25 s; octave stab at beat 4's last 16th, gain 0.12 |
| Chords | Am F C G, one per bar |

## Sound
Plays over drums and bass, and under the voice. Thin it out when the voice is speaking; it is the first thing to remove if the mix is busy.

## Adapt it
- The chord lists, to change key. Keep one chord per bar so it follows the bass roots.
- `bright` (filter) and its ramp: raise the start for a brighter intro.
- The pattern: which beats get stabs.
- The octave doubling `* 2` in the arp, for a higher or lower line.

## Files

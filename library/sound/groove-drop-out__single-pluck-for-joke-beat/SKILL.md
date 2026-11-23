---
name: groove-drop-out-single-pluck-for-joke-beat
description: "The full groove stops dead on a cut, leaving one quiet pluck per bar and two low pops on the punchlines, then an impact and a soft pad take over for the end card. A comedic or serious beat after a busy section."
---

# Groove drop-out for a joke beat

**Code name:** Single pluck for a joke beat.

## What you hear
Two bars of the full groove, then it simply stops at the cut with a whoosh. For the next three bars you hear one soft low pluck at the start of each bar and little else. Two low pops mark the two punchline words (0.52 s and 1.52 s after the cut). Then an impact, and a soft four-note pad rises underneath the end card.

## When to use it
A comedic or serious beat after a busy section. The silence is the effect: take things away rather than adding. It needs the groove to have been going for a while for the drop to register. It is wrong right after a sparse intro.

## How it works
Three branches in the beat loop decide what plays:

```python
intro = t < SLAM; drop = JOKE <= t < END
if intro: ...                                   # plucks, hats, building kick
elif drop:
    if beat == 0: put(mus, pluck(chord, .6, 900), t, .12)   # one muted pluck per bar
else: ...                                       # full groove
put(mus, pad([110, 164.8, 220, 261.6], DUR - END), END, .18)
put(mus, impact(), END, .4)
```

The pad is four sines (A2, E3, A3, C4), each with a slow 0.3 Hz phase wobble, faded in and out over 1.5 s. The recipe starts the groove at 0, so its chords fall in a different place in the progression from a full track.

## Numbers that matter
| | |
|---|---|
| Groove | stops at `JOKE` (21.3 s here) |
| Drop-out pluck | `pluck(chord, .6, 900)`, gain 0.12, beat 1 of each bar |
| Whoosh on the cut | `cut - .18`, gain 0.45 |
| Punchline pops | `pop(500)` 0.52 s after the cut gain 0.18; `pop(420)` at +1.52 s gain 0.22 |
| End card | impact gain 0.4, pad gain 0.18 from 25.4 s to the end |

## Sound
Silence is the sound. Keep the voice in the foreground: the whole point is that nothing competes with the line.

## Adapt it
- `JOKE` and `END`: the cut times from your word table.
- The held pluck's brightness (`900`) and gain.
- The pop pitches (500, 420 Hz) for the punchline words; lower for a heavier line.
- The pad notes and gain for the following scene.

## Files

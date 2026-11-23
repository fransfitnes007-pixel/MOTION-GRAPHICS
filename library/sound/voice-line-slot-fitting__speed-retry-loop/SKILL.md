---
name: voice-line-slot-fitting-speed-retry-loop
description: "Each narration line is rendered, measured, and re-rendered faster if it runs past its slot, up to 1.35x. When the picture is fixed first (scenes on a beat grid) and the voice must fit inside it."
---

# Voice line slot fitting

**Code name:** Speed retry loop.

## What you hear
A 16 s synthetic track of five spoken-sounding lines placed in their slots. The printed table shows what happened: the first line fits at the base 1.1x, two needed a retry (1.17x and 1.30x), one needed the 1.35x cap and only just fits, and the last, a long line in a short slot, still overruns even at 1.35x. The audio is a vowel-buzz stand-in for speech, not a voice.

## When to use it
When the picture is fixed first (scenes on a beat grid) and the voice must fit inside it. Writing the slots down before recording lets you find lines that will not fit before you get to the mix. It is wrong where the voice leads: then cut to the voice instead.

## How it works
The loop:

```python
for a0, a1, text in LINES:                       # start, latest end, text
    sp = base; y = say(text, sp)                 # base 1.1x
    while len(y) / SR > (a1 - a0) and sp < 1.35:
        sp = min(1.35, sp * (len(y) / SR) / (a1 - a0) + 0.01); y = say(text, sp)
    y = y / (np.abs(y).max() + 1e-6) * 0.9       # peak-normalise each line to 0.9
    track[int(a0*SR):...] += y
```

The new speed is the old speed times the overrun ratio, plus 0.01, so it usually converges in one or two tries. `say()` trims leading and trailing silence (`librosa.effects.trim`, 38 dB) so the line starts exactly at `a0`. A local TTS model such as Kokoro-82M on the CPU works well. A different rule is to start each line at `max(cue, previous_end + 0.35)`, so lines never overlap. A hosted TTS take also works; get word timestamps from it (see the word-timestamp recipe). No keys are used or stored here.

## Numbers that matter
| | |
|---|---|
| Base speed | 1.1x (argument 2 of the script) |
| Speed cap | 1.35x |
| Retry rule | `sp = min(1.35, sp * overrun + 0.01)` |
| Silence trim | 38 dB |
| Line level | peak 0.9 |
| Slots | on a 128 BPM grid, e.g. 3.80 to 5.50 s |
| Stand-in in this recipe | 0.09 s per character at 1.0x |

## Sound
Use the track as the voice layer for the ducking recipe.

## Adapt it
- `LINES`: your slots.
- `base` and the 1.35 cap: above 1.35x most voices sound rushed.
- The trim threshold.
- The `say()` function: replace the stand-in with your own TTS call returning a mono array.

## Files
- The recipe's `say()` is synthetic; a real script needs `kokoro` and `librosa`.

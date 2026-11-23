---
name: minor-pad-bed-additive-sines-and-slow-tremolo
description: "A soft A-minor drone of four sine waves that fade in and out, with a second pad that wobbles in phase, for under a voiceover. Under a narration where there is no beat, for the whole film or just the last scene."
---

# Minor pad bed

**Code name:** Additive sines and slow tremolo.

## What you hear
First, a 10 s steady pad: a low open A minor sound (A1, E2, A2, C3), warm and dark, with the top note swelling slowly every 4 s. It fades in over 2.5 s and out over 3 s. Then a gap and a 5 s pad in four sines that shimmer slightly as their phases drift: the end-card pad.

## When to use it
Under a narration where there is no beat, for the whole film or just the last scene. It supports voice without a rhythm. It is wrong where the picture needs drive.

## How it works
Part one is the sum of sines written as the ffmpeg `aevalsrc` expression, then low-passed:

```
0.09*sin(2*PI*55*t) + 0.07*sin(2*PI*82.41*t) + 0.05*sin(2*PI*110*t)
  + 0.035*sin(2*PI*130.81*t)*(0.6+0.4*sin(2*PI*0.25*t))
-> lowpass 900 Hz -> afade in 2.5 s, out 3 s -> volume 0.9
```

This pad works as a sidechain target: `sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400` with the voice as key. Part two is a `pad()`, which adds a slow phase wobble to each sine:

```python
x = sum(np.sin(2*np.pi*f*t + np.sin(2*np.pi*.3*t)*.3) for f in freqs) / len(freqs)
x * np.minimum(1, t/1.5) * np.minimum(1, (dur - t)/1.5)
```

## Numbers that matter
| | |
|---|---|
| Pad notes | A1 55, E2 82.41, A2 110, C3 130.81 Hz |
| Weights | 0.09, 0.07, 0.05, 0.035 (top one has a 0.25 Hz tremolo, gain swinging between 0.2 and 1.0) |
| Filter | low-pass 900 Hz |
| Fades | 2.5 s in, 3 s out |
| End pad | A2 110, E3 164.8, A3 220, C4 261.6; phase wobble 0.3 Hz depth 0.3 rad; fades 1.5 s; gain 0.18 |

## Sound
Held under the voice. A compressor can duck it under the voice by sidechain, or the whole music bed can be ducked by the envelope-follower recipe.

## Adapt it
- The four frequencies, to change the chord (keep roots low).
- The low-pass cutoff (900 Hz) for a darker or brighter pad.
- Fade lengths, to match the video length.
- The tremolo rate on the top note.

## Files

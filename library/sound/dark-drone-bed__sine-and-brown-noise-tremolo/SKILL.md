---
name: dark-drone-bed-sine-and-brown-noise-tremolo
description: "A very low, slowly breathing hum made of a 48 Hz sine and rumbling brown noise, faded in and out, with no rhythm or melody. A bed for a video that has voice and cues but no music: a calm, serious or luxury piece, or any film whose sound effects are the interest."
---

# Dark drone bed

**Code name:** Sine and brown noise with tremolo.

## What you hear
A dark low rumble you feel more than hear, with two slow waves of volume going at different rates, one every 7.7 s and one every 10 s. It fades in over 2 s and out over 2.5 s. Nothing happens in it, which is why it can sit under a voice and sound effects for a minute without competing.

## When to use it
A bed for a video that has voice and cues but no music: a calm, serious or luxury piece, or any film whose sound effects are the interest. It is wrong where energy is needed. Check it on small speakers, where 48 Hz disappears and only the noise remains.

## How it works
The bed is an ffmpeg filter graph, rewritten in numpy.

```
sine=f=48 -> volume=0.07 -> tremolo=f=0.13:d=0.6
anoisesrc=c=brown:a=0.5 -> lowpass=f=220 -> volume=0.16 -> tremolo=f=0.1:d=0.5
amix (normalize=0) -> afade in d=2, afade out st=dur-2.5 d=2.5
```

ffmpeg's `sine` source has a default amplitude of 1/8, so the sine is much quieter than it looks (0.07 x 0.125). The recipe keeps that ratio. The brown noise is leaky-integrated white noise, which is how ffmpeg makes it. The tremolo is `gain = (1 - d/2) + (d/2) sin(2 pi f t)`. The recipe's overall level agrees with the ffmpeg render to within about 3 dB; the exact noise and filter implementation differ.

At the end of a script the whole mix can go through `alimiter=limit=0.95,loudnorm=I=-15:TP=-1.2:LRA=11`, which lifts this very quiet bed to a usable level. See the final master recipe.

## Numbers that matter
| | |
|---|---|
| Sine | 48 Hz, volume 0.07 (of 1/8 amplitude), tremolo 0.13 Hz depth 0.6 |
| Noise | brown, amplitude 0.5, low-pass 220 Hz, volume 0.16, tremolo 0.1 Hz depth 0.5 |
| Fades | in 2 s, out 2.5 s |
| Raw peak | about 0.045 for the 14 s render (a final master lifts it later) |

## Sound
A bed that is always there. It is mixed with the voice first and the loudness is set afterward. Pair it with the cue-sheet mixing recipe, which uses the same bed.

## Adapt it
- The sine frequency (48 Hz) and the noise cutoff (220 Hz): a higher drone is lighter, a lower one darker.
- The two tremolo rates, which decide how slowly it breathes.
- Fade times.
- The levels 0.07 and 0.16, to make noise or tone dominate.

## Files
- This recipe is a numpy copy of the ffmpeg filter graph; a production version needs ffmpeg.

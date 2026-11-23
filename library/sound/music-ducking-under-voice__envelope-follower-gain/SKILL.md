---
name: music-ducking-under-voice-envelope-follower-gain
description: "The music drops about 6 dB while a voice is speaking and comes back in the gaps, by following the voice's loudness. Any mix where a voice has to be understood over music."
---

# Music ducking under a voice

**Code name:** Envelope follower gain.

## What you hear
Before and after with the same music. The first 7 s is the groove at full level with a (synthetic) voice speaking two phrases over it; the voice is partly buried. After a pause, the same 7 s again with ducking: whenever the voice is speaking the drums and bass drop to about half amplitude and return a moment after it stops. The voice in the demo is a made-up vowel buzz in syllables, standing in for a real recording.

## When to use it
Any mix where a voice has to be understood over music. It keeps the music loud enough to feel in the gaps between phrases. It is wrong if the voice is steady and continuous (the music will be flat-ducked the whole time; just set the music lower), or if the voice itself is quiet or distorted.

## How it works
Four lines of numpy, repeated in every script. Take the absolute value of the voice, average it over 50 ms to get a loudness curve, turn that into a gain between 1.0 and 0.5, and smooth the gain over 80 ms.

```python
lvl  = np.convolve(np.abs(vo), np.ones(int(.05*SR)) / int(.05*SR), 'same')
duck = 1 - .5 * np.clip(lvl / .05, 0, 1)
duck = np.convolve(duck, np.ones(int(.08*SR)) / int(.08*SR), 'same')
mix  = mus * duck[:, None] * .75 + fx * (0.6 + 0.4 * duck[:, None]) + np.stack([vo, vo], 1) * 1.05
```

Any voice level above 0.05 on average gets the full duck. The effects bus ducks much less (it only falls to 0.8) so whooshes and clicks still punch through. `mode='same'` convolution is centred, so the smoothed gain starts to fall a few tens of milliseconds before the voice starts: it is a free look-ahead. In the recipe the voice is a stand-in, so the printed gain minimum should read 0.5.

The same job can be done with ffmpeg: the voice gets a 3:1 compressor (threshold -18 dB) and then keys a sidechain compressor on the pad: `sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400`. The numpy version gives a fixed 6 dB dip you can see; the ffmpeg one reacts to level.

## Numbers that matter
| | |
|---|---|
| Level detector | mean of the absolute voice over 50 ms |
| Full duck at | level 0.05 and above |
| Duck depth | music x 0.5 (-6 dB); 0.55 also works |
| Smoothing | 80 ms box |
| Music level | x 0.75 (x 0.8 also works) |
| Effects level | x (0.6 + 0.4 x duck), so 1.0 down to 0.8 |
| Voice level | x 1.05 |
| ffmpeg alternative | `sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400` |

## Sound
The voice is the one thing you do not change. Duck the music and the effects, never the voice. Then run the final master recipe on the sum.

## Adapt it
- `.5`: the duck depth. 0.6 for a bigger dip, 0.3 for a gentler one.
- `.05` in `lvl / .05`: how quiet a voice must be to still trigger.
- The 80 ms smoothing: longer for a slower, smoother swell back.
- Music level (0.75) against voice level (1.05).

## Files
- The recipe's voice is synthetic: replace `vo` with a mono array from your own recording.

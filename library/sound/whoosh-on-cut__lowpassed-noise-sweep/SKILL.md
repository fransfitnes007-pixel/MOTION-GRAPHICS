---
name: whoosh-on-cut-lowpassed-noise-sweep
description: "A short airy sweep of band-passed noise that peaks on a hard cut, with variants for a scroll, a downward sweep and a wipe. Put one on every hard cut or swipe in a video that has no other sound on the cut."
---

# Whoosh on a cut

**Code name:** Lowpassed noise sweep.

## What you hear
Six sweeps in a row, about a second apart. The first two are the standard cut whoosh: a 0.42 s breath of noise that brightens as it rises and is gone as the picture changes. Third is a longer 0.9 s rise, the sound of a feed scrolling. Fourth is a falling sweep that gets duller as it goes. The last two are the swell version: a slower build that peaks and is cut off short on the beat, once short (0.55 s) and once as a wide wipe (0.9 s).

## When to use it
Put one on every hard cut or swipe in a video that has no other sound on the cut. It makes the cut feel intentional and fills the gap between two scenes. It is wrong on a slow dissolve, where a rise with nothing to land on sounds like a mistake, and it is too much if it is on every single cut under a busy music bed. Keep to the cuts that change the subject.

## How it works
White noise, shaped twice. A one-pole low-pass whose cutoff moves over time is subtracted from a fixed low-pass at 300 Hz, which leaves a band that slides up. A sine envelope shapes the loudness.

```python
def whoosh(dur=.42, up=True):
    n = int(dur * SR); t = np.arange(n) / SR; x = rng.standard_normal(n)
    e = np.sin(np.pi * t / dur) ** 1.5
    fc = (800 + 5000 * (t / dur)) if up else (6000 - 5200 * (t / dur))
    return ((lp(x, fc) - lp(x, 300)) * e * .8)
```

The envelope peaks at the middle of the sound, so place it half a sweep early: `put(fx, whoosh(), cut - .18, .45)` for the 0.42 s version puts the loudest point about 0.03 s after the cut. The swell version, `noise_swell(.55, .38, 600, 5500)`, builds as a squared ramp for 0.38 s and then falls with a 0.12 s decay, so it is started 0.38 s before the cut and its peak lands exactly on it.

`lp` is a one-pole filter: `y += a * (x - y)` with `a = 1 - exp(-2 pi fc / SR)`. With an array for `fc` it runs sample by sample. The recipe uses scipy's `lfilter` when the cutoff is a constant; the result is the same filter.

## Numbers that matter
| | |
|---|---|
| Standard whoosh | 0.42 s, cutoff 800 to 5800 Hz, envelope `sin(pi t/d)^1.5`, gain 0.45, placed `cut - 0.18` |
| Scroll whoosh | 0.9 s, same shape, gain 0.6, at 2.8 s |
| Downward whoosh | 0.35 s, cutoff 6000 to 800 Hz, gain 0.5, at 6.0 s (a word sweeping in from the side) |
| Swell whoosh | `noise_swell(.55, .38, 600, 5500)`, gain 0.3, placed `cut - 0.38` |
| Wipe swell | `noise_swell(.9, .62, 400, 8000)`, gain 0.3, started 0.3 s before the wipe time |
| Low cut | 300 Hz high-pass (the subtracted low-pass) |
| Example cuts | 3.9, 5.96, 7.8, 8.16, 10.86, 13.92, 15.68, 17.24, 18.6, 20.08, 21.3 s |

## Sound
Heard under the music, ducked slightly (effects are mixed at `0.6 + 0.4 * duck`). Pair it with an impact or pop on the first frame of the new scene. The riser-into-slam recipe in this library is the longer cousin for a big hit.

## Adapt it
- The cut times: use the word-timestamp table skill to get them from the voice.
- `dur` and the 0.18 s lead: shorter sweep (0.25 s, lead 0.1 s) for fast cuts.
- The cutoff range `800 + 5000 * t/dur`: lower both numbers for a duller, bigger sweep.
- The gain: 0.3 to 0.6 depending on how busy the music is.

## Files

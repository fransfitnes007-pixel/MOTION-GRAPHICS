---
name: riser-into-slam-filtered-noise-sweep
description: "Two seconds of rising band-passed noise that cuts off on the downbeat, where a sine boom with an air tail hits. Before a giant word, a logo or a big reveal that the picture holds still for."
---

# Riser into a slam

**Code name:** Filtered noise sweep.

## What you hear
Three risers, each ending on a hit. The first is a 2 s hiss that grows from nothing, brighter and louder as it goes, squared so most of the rise is at the end, then a deep boom with a puff of air on top at the moment it stops. The second is a shorter, quieter 1 s version with a smaller hit. The third is a 128 BPM version: two beats long, a wider sweep (300 Hz to 9 kHz), and a hit with a short crash tail.

## When to use it
Before a giant word, a logo or a big reveal that the picture holds still for. Start the riser so its peak lands on the frame where the thing appears. It is wrong when the next scene is quiet or when there is already a drop in the music; two builds fighting each other sound like a mistake. Use one big one and maybe one small one per film.

## How it works
Noise with a moving band-pass. The loudness follows `(t / peak_at)^2` until the peak, then falls with a 0.12 s decay, so the sound stops almost dead on the beat. The cutoff rises linearly from `lo` to `hi` over the same time. The band is made by subtracting a low-pass at `0.8 * lo` from the swept low-pass.

```python
def noise_swell(dur, peak_at, lo=500, hi=6000):
    t = np.arange(n) / SR; x = rng.standard_normal(n)
    e = np.where(t < peak_at, (t / peak_at) ** 2, np.exp(-(t - peak_at) / .12))
    fc = lo + (hi - lo) * np.clip(t / peak_at, 0, 1)
    return (lp(x, fc) - lp(x, lo * .8)) * e

put(mus, noise_swell(2.2, 2.0), SLAM - 2.0, .5)   # riser: starts 2.0 s early, peaks at the slam
put(mus, impact(), SLAM, .9)
```

The impact is a sine at 38 Hz plus a fast 60 Hz drop (`38 + 60 exp(-t/.05)`, decay 0.5 s) for the body, plus noise with everything below 300 Hz removed, low-passed at 3.5 kHz, decaying in 0.18 s, for the air. The 128 BPM impact is similar but with a slower drop (0.08 s) and a brighter crash (`>3 kHz`, 0.45 s decay).

## Numbers that matter
| | |
|---|---|
| Big riser | `noise_swell(2.2, 2.0)`, 500 to 6000 Hz, gain 0.5, ends at the slam (6.7 s) |
| Small riser | `noise_swell(1.0, .9)`, gain 0.3, ends at 13.0 s |
| Impact | 1.4 s, gain 0.9 (slam), 0.55 (done), 0.4 (end card at 25.4 s) |
| 128 BPM riser | `noise_swell(2*B + .05, 2*B, 300, 9000)` with B = 60/128, gain 0.35 and 0.3 |
| 128 BPM impact | 1.6 s with crash, gain 0.5 at the logo slam and end, 0.3 between |
| Tail after the peak | 0.12 s exponential |

## Sound
Heard under the music with a kick landing on the same beat. Leave a gap in the groove just before the slam so the riser can be heard. Pair with a whoosh on the cut into the slam scene.

## Adapt it
- The length of the riser and `peak_at`: it should reach the slam exactly when the picture does.
- `lo` and `hi`: raise `lo` for a thinner, tenser sound, lower `hi` for a darker one.
- The impact's base `38` Hz and drop `60` Hz: higher for a smaller hit, lower for a bigger one.
- The gains, to leave room for voice.

## Files

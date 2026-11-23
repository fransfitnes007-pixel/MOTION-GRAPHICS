---
name: final-master-tanh-soft-clip-fade-loudnorm
description: "The last steps before export: a soft clip, a curved fade-out, a limiter and loudness normalisation, with before and after. On the final sum of every video, once."
---

# Final master

**Code name:** Tanh soft clip, fade and loudnorm.

## What you hear
Three versions of the same 4 s of groove, 0.5 s apart. First the raw sum, made too hot and cut flat at full scale: harsh, with the peaks sawn off. Second, the master chain: the sum is faded out over the last 1.4 s and soft-clipped with tanh, which rounds off peaks. Third, that again after ffmpeg's loudnorm: quieter and more even. The printed figures show peak, RMS and LUFS for each.

## When to use it
On the final sum of every video, once. Soft clipping is for catching strays; if the mix has to be turned down to avoid clipping, turn it down. The loudnorm step is for a delivery target (social video is usually around -14 to -16 LUFS). It is wrong to master the parts separately and again on the sum.

## How it works
The chain:

```python
fade = np.ones(N); a = int((DUR - 1.4) * SR); fade[a:] = np.linspace(1, 0, N - a) ** 1.5
mix *= fade[:, None]
mix = np.tanh(mix * 1.1) / np.tanh(1.1)
```

`tanh(1.1 x) / tanh(1.1)` is 1.0 at x = 1, but it keeps rising toward 1.2 for loud input, so this is a soft clip that can still go above full scale. The recipe's second version peaks at about +1.8 dBFS in float; writing that to a 16-bit file clips it, so the recipe saves 32-bit float. A hard stop can follow:

```
alimiter=limit=0.95,loudnorm=I=-15:TP=-1.2:LRA=11
```

(a tighter version uses `alimiter=limit=0.89`). In the sample run the three versions read LUFS -6.8, -9.1 and -16.0 with ffmpeg present. Loudnorm in one pass on a 4 s clip lands near but not exactly on -15.

## Numbers that matter
| | |
|---|---|
| Fade-out | last 1.4 s (or 1.6 s), curve `linspace(1,0)^1.5` |
| Soft clip | `tanh(1.1 x) / tanh(1.1)` |
| Limiter | `alimiter=limit=0.95` (0.89 for a tighter ceiling) |
| Loudness | integrated -15 LUFS, true peak -1.2 dB, LRA 11 |
| Sample rate | 48 kHz |
| Sample run | A hard-clipped: peak 0.0 dBFS, -6.8 LUFS. B: peak +1.8 dBFS, -9.1 LUFS. C: peak -6.3 dBFS, -16.0 LUFS |

## Sound
Everything. Listen on a phone speaker and in headphones at a moderate level; if A and B sound alike, your material is not hot enough to need this.

## Adapt it
- The fade length and curve power.
- The soft-clip drive `1.1`: higher squashes more.
- The loudness target: -14 for streaming, -16 for quieter delivery, -23 for broadcast.
- Whether to run loudnorm at all (it needs ffmpeg; the recipe skips it if it is not found).

## Files

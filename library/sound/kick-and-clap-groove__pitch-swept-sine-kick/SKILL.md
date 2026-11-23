---
name: kick-and-clap-groove-pitch-swept-sine-kick
description: "A four-on-the-floor drum loop with a thumping sine kick, noisy claps on 2 and 4, and open and closed hi-hats, all synthesised. The body of a fast promo or product video once the opening is over."
---

# Kick and clap groove

**Code name:** Pitch-swept sine kick.

## What you hear
Four bars at 122 BPM. Bar one is the kick alone, four to the floor. Bar two adds a clap on beats 2 and 4. Bars three and four add open hi-hats on the offbeats and closed hi-hats on the second and fourth sixteenths. It is tight and bright. A full track plays it all at once; the demo adds the parts in turn so you can hear each.

## When to use it
The body of a fast promo or product video once the opening is over. It starts at the slam and runs until a break. It is wrong for anything slow and warm. Drums with no melody or bass is a skeleton, so pair it with the bass and stab recipes.

## How it works
Each drum is a few lines of numpy.

```python
def kick():                                  # 0.4 s
    f = 48 + 120 * np.exp(-t / .03); ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * env(n, .001, .15) + .25 * np.sin(ph * 2) * env(n, .001, .02)
def clap():                                  # 0.22 s
    x = rng.standard_normal(n)               # three bursts 0, 9 and 18 ms plus a 80 ms tail
    e = sum(env(n, .0005, .012) * (np.arange(n) >= int(k * SR)) for k in (0, .009, .018)) + .6 * env(n, .001, .08)
    return np.diff(np.concatenate([[0], x])) * e * .5
def hat(open_=False):                        # 0.045 s closed, 0.2 s open
    x = rng.standard_normal(n); x = x - lp(x, 7500)
    return x * env(n, .0005, .06 if open_ else .011)
```

The kick's pitch starts at 168 Hz and settles to 48 Hz in about 100 ms; the phase is the running sum of the frequency, so the sweep is clean. The `diff` in the clap is a first-order high-pass; the three quick bursts at 0, 9 and 18 ms are what make it sound like hands. Hat noise is high-passed at 7.5 kHz.

## Numbers that matter
| | |
|---|---|
| Tempo | 122 BPM, B = 0.4918 s |
| Kick | beats 1 to 4, gain 0.85 |
| Clap | beats 2 and 4, gain 0.55 |
| Open hat | offbeat 8ths (`t + B/2`), gain 0.22 |
| Closed hat | at `t + B/4` and `t + 3B/4`, gain 0.1 |
| 128 BPM variant | 128 BPM, kick 0.45 s (45 Hz + 110 Hz drop, 35 ms), clap 0.25 s, hats cut at 7 kHz, kick 0.9 and clap 0.42 |

## Sound
This is the music. Add the sidechained bass and chord stabs on top, and duck the whole thing under the voice. A drop-out (see the groove drop-out recipe) is the break.

## Adapt it
- `BPM`: anything from 104 to 128 BPM works.
- The clap pattern: beats 2 and 4, or only 3 for half-time (see the half-time bed).
- The kick's start and end frequency (`48 + 120 e^(-t/.03)`): lower for a softer thump.
- The hat cutoff `7500` and gains.

## Files

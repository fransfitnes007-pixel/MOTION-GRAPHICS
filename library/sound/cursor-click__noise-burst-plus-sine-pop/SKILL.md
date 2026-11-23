---
name: cursor-click-noise-burst-plus-sine-pop
description: "A dry mouse click made of a 60 ms burst of high-passed noise with a 1600 Hz pop underneath. When a cursor presses a button on screen: submit, launch, book."
---

# Cursor click

**Code name:** Noise burst plus sine pop.

## What you hear
Three clicks, 1.3 s apart. Each is a hard, dry tick with a tiny body to it: a snap of noise on top of a short pitched pop. After the third, a softer pop 0.12 s later stands in for the thing that appears when the button is pressed. Because the noise is random, the three clicks differ a little.

## When to use it
When a cursor presses a button on screen: submit, launch, book. Put it exactly on the frame where the button depresses, not when the cursor arrives. The follow-up pop belongs to the result. It is wrong for touch screens or phone UI, where a softer tap sound suits better, and for a keyboard key (use the keystroke recipe).

## How it works
Noise that has had everything below 2.5 kHz removed (the noise minus its own low-pass), with a 0.3 ms attack and 6 ms decay, plus the first 60 ms of a 1600 Hz pop.

```python
def click():
    n = int(.06 * SR); x = rng.standard_normal(n); x = x - lp(x, 2500)
    return x * env(n, .0003, .006) * .9 + pop(1600)[:n] * .3
```

A sampled click file at volume 0.55 to 0.9 also works; the synthesised click here needs no files.

## Numbers that matter
| | |
|---|---|
| Length | 60 ms |
| Noise | high-passed above 2.5 kHz, attack 0.3 ms, decay 6 ms, level 0.9 |
| Body | `pop(1600)` cut to 60 ms, level 0.3 |
| Gain in the mix | 0.9 |
| Example times | 2.46, 12.88, 27.0 s |

## Sound
Dry and loud in the mix, with no reverb. Follow with a pop or whoosh on whatever the click triggers.

## Adapt it
- The times, to the frame where the button visually presses.
- The noise cut-off `2500`: raise it for a lighter click, lower it for a heavier one.
- The pop frequency `1600`: raise it for a smaller, plastic click.
- Gain 0.9 down to 0.5 if there is a lot of music.

## Files

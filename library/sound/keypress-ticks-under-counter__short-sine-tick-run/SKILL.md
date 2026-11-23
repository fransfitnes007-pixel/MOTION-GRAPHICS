---
name: keypress-ticks-under-counter-short-sine-tick-run
description: "Twenty-eight tiny high ticks 28 ms apart, cycling through four pitches, matching a number that counts up fast. Under any number that counts up on screen: views, money, followers."
---

# Keypress ticks under a counter

**Code name:** Short sine tick run.

## What you hear
A fast rattle of high, short ticks, 28 of them in 0.78 s. The pitch moves in a four-step loop, so it sounds like a mechanical counter rolling over, not a machine gun. After it, in the demo only, a slower run of 16 ticks 70 ms apart, for comparison.

## When to use it
Under any number that counts up on screen: views, money, followers. Start the first tick on the first frame the number moves and end on the last. It is wrong for a counter that moves slowly (one tick every half second is a clock), and with a loud track it just disappears.

## How it works
A 30 ms sine at 2.2 to 2.65 kHz with a 6 ms exponential decay, placed every 28 ms.

```python
def tick(f=2400):
    n = int(.03 * SR); t = np.arange(n) / SR
    return np.sin(2 * np.pi * f * t) * np.exp(-t / .006)

for i in range(28): put(fx, tick(2200 + (i % 4) * 150), 18.64 + i * .028, .35)
```

The four-note cycle `2200, 2350, 2500, 2650` is what stops it sounding like one repeated beep. Match the number of ticks to how long the counter is moving.

## Numbers that matter
| | |
|---|---|
| Tick | 30 ms sine, decay 6 ms |
| Pitches | 2200, 2350, 2500, 2650 Hz, repeating |
| Count and spacing | 28 ticks, 28 ms apart (0.78 s) |
| Gain | 0.35 |
| Example start | 18.64 s |

## Sound
Sits above the music as a light patter. It can be followed 1.3 s later by a payoff pop and a confetti burst.

## Adapt it
- Start time, count and spacing, to match your counter's start, end and duration.
- The four pitches: raise them all for a lighter click, spread them for a more melodic roll.
- The gain, which needs to stay well under the music's loudest part.

## Files

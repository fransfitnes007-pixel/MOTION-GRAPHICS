---
name: typing-keystrokes-eased-character-timing
description: "One key click per typed character, timed from the same ease-in-out curve that reveals the text on screen. Whenever text types itself into a box on screen."
---

# Typing keystrokes

**Code name:** Eased character timing.

## What you hear
A prompt types itself: a slow first few keys, a burst through the middle, a slower finish. You hear a key click for each new letter (not for spaces), so the rhythm of the sound follows the text. Then a click, as the cursor presses the apply button. In the demo each key is a soft tick of noise over a low thump, because the real sound is a set of sampled files.

## When to use it
Whenever text types itself into a box on screen. The point is that audio timing is calculated from the same curve as the typing animation, so they cannot drift apart. It is wrong for pasted text that appears at once.

## How it works
The typing animation reveals `n = len(text) * ease(progress)` characters. The audio script replays that curve in 600 small steps and puts a key at each step where the visible character count has gone up, skipping spaces and anything less than 35 ms after the last key.

```python
eio = lambda x: 4 * x ** 3 if x < .5 else 1 - (-2 * x + 2) ** 3 / 2
for i in range(0, 600):
    t = .5 + i / 600 * 2.7; n = int(len(txt) * eio((t - .5) / 2.7))
    if n > last and txt[n - 1] != ' ' and (not keys or t - keys[-1] > .035): keys.append(round(t, 3))
    last = n
```

A production version cycles through 18 sampled key files at volume 0.45, so no two neighbouring keys are the same. Those files are not bundled. `recipe.py` swaps in a synthesised key so it runs alone; the timing is the part to keep. Another option is to list the key times by hand (`KEYS=(3.70 3.83 3.94 ...)`), which is the right choice when the typing is not smooth.

## Numbers that matter
| | |
|---|---|
| Typing window | 0.5 s to 3.2 s (2.7 s) |
| Curve | ease-in-out cubic |
| Minimum gap | 35 ms |
| Steps replayed | 600 |
| Key volume | 0.28 to 0.55, depending on the mix |
| Result for this text | 29 keys for 50 characters, because the 35 ms gap drops some at the fast middle |
| Enter / click | 3.9 s |

## Sound
Mix keys under the voice and just above the music. Add the cursor click recipe on the button that follows.

## Adapt it
- `txt`, the start (0.5) and length (2.7) so they match your type-on animation.
- The easing function, to the same one your visual uses.
- The key sound: drop in your own set of 10 to 20 key samples and cycle through them with `k % count`.
- The 35 ms minimum gap, which controls how many letters get a sound in a fast stretch.

## Files

---
name: pop-on-word-reveal-pitch-dropping-sine
description: "A tiny bubble-pop made from a sine that drops in pitch, used one per word, in rising steps, in rows or as a spread. One pop per visual arrival: a word, a chip, a tile, a badge."
---

# Pop on a word reveal

**Code name:** Pitch-dropping sine.

## What you hear
Four segments. First, four stamped words with a pop each, climbing in pitch (640, 730, 820, 910 Hz base) and a small high pop on the heart icon. Second, seven soft pops flicking left and right as words arrive in a line. Third, 48 pops in a rattle, four rows of twelve, each row slightly offset, rising and falling through five pitches: the sound of a grid of tiles appearing. Last, four pops spread across the stereo field one after another: label pills.

## When to use it
One pop per visual arrival: a word, a chip, a tile, a badge. The pitch steps tell the ear it is the same sequence, so give each new item in a list a slightly higher base pitch. Use quiet pops (gain 0.06 to 0.13) for crowds and a louder one (0.25) for the hero word. It is wrong under a smooth fade-in with no distinct arrival frame, and it stops working if every element on screen pops at once.

## How it works
A sine whose frequency drops fast right after the start, with a 40 ms exponential decay, 0.11 s long.

```python
def pop(f=880):
    n = int(.11 * SR); t = np.arange(n) / SR
    return np.sin(2 * np.pi * (f + 700 * np.exp(-t / .018)) * t) * np.exp(-t / .04)
```

The frequency term is `f + 700 * exp(-t/.018)`, multiplied by `t` inside the sine as written in the source. That makes the pitch sweep downward very quickly, which gives the bubble sound. It is copied as written. Pitch variety comes from the caller: `640 + i * 90` for stamped words, `900 + (i % 3) * 120` for word-by-word, `1100 + (i % 5) * 90` for the tile rows. Pan comes from `pan=(i % 3 - 1) * .4` or alternating left and right at +/-0.3.

Tile timing: `9.14 + (i % 12) * .035 + (i // 12) * .02`, so 12 pops 35 ms apart per row and each row starts 20 ms after the last.

## Numbers that matter
| | |
|---|---|
| Pop length | 0.11 s, decay 40 ms, pitch drop 700 Hz over 18 ms |
| Stamped words | `pop(640 + i*90)`, gain 0.25, at 0.4, 1.26, 2.04, 2.8 s |
| Heart | `pop(1500)`, gain 0.12, 0.05 s after the word |
| Word pops | `pop(900 + (i%3)*120)`, gain 0.11, pan alternating +/-0.3 |
| Tile cascade | 48 pops, `pop(1100 + (i%5)*90)`, gain 0.06, 35 ms apart, 12 per row |
| Label pills | 4 pops, `pop(1300 + i*80)`, gain 0.12, 70 ms apart, pan -0.45 to +0.45 |

## Sound
Sits on top of the music at low level. Pair with the whoosh on the cut that starts the scene and with a riser if the pops build to a slam.

## Adapt it
- The base frequency `f` and the per-item step (90 Hz for hero words, 80 to 120 Hz for lists).
- The gain, 0.06 for crowds up to 0.25 for a single word.
- The spacing: 35 ms reads as a rattle, 70 ms as separate items, 120 ms and up as individual beats.
- The pitch-drop depth `700`: smaller for a softer tick.

## Files

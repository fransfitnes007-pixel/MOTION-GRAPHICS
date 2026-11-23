---
name: sidechained-bass-bed-kick-triggered-gain-dip
description: "Offbeat bass, plucks and hats that duck with every kick, so the whole bed pumps. When you want a dance-music feel and the bass, pad and plucks are getting in the way of the kick."
---

# Sidechained bass bed

**Code name:** Kick-triggered gain dip.

## What you hear
Two bars of a 128 BPM groove played twice. The first time everything is steady. The second time, the same notes dip every time the kick lands and swell back before the next one, so the bass and plucks seem to breathe in time with the drums. The demo adds a held chord pad so the pump is easy to hear.

## When to use it
When you want a dance-music feel and the bass, pad and plucks are getting in the way of the kick. Write the dip from the kick times, not from the audio, so it is exact. It is wrong for ambient or acoustic beds. If there is a voice on top, the voice ducking is a separate step.

## How it works
A gain curve the same length as the music bus. At every kick, the curve is pulled down to 0.25 and then rises back to 1 over 0.22 s along a power curve. The whole bus is multiplied by it at the end.

```python
side = np.ones(N, np.float32)
# at each kick, time t:
a = int(t * SR); L = int(.22 * SR)
side[a:a + L] = np.minimum(side[a:a + L], .25 + .75 * np.linspace(0, 1, L) ** 1.5)
# after the loop:
mus[:, 0] *= side; mus[:, 1] *= side
```

Two things to know. The dip is applied to the whole bus, so the kick, claps and hats are dipped too, including the kick that triggered the dip (its first 20 ms or so is at roughly a quarter of its level). This is a common simplification, and the recipe copies it. Bass is an offbeat sine plus 35% of a saw low-passed at 900 Hz, 0.35 s decay.

## Numbers that matter
| | |
|---|---|
| Tempo | 128 BPM |
| Dip floor | 0.25 (about -12 dB) |
| Recovery | 0.22 s, `linspace(0,1)^1.5` |
| Bass | offbeat (`t + B/2`), `bass(root, B*.45)`, gain 0.5; roots A1 55, F1 43.65, C2 65.41, G1 49 Hz |
| Bass tone | sine + 0.35 x saw low-passed at 900 Hz, decay 0.35 s |
| Slower variant | floor 0.3, recovery 0.3 s, dip on every second beat at 104 BPM |

## Sound
The pump is heard best on sustained sounds; this is the glue between drums and chords. Voice ducking comes after.

## Adapt it
- The floor (`.25`) and length (`.22`): deeper and longer for a stronger pump.
- The bass roots, to match your chords.
- Which beats trigger the dip, which also decides the pump rhythm.
- Whether the kick itself is in the dipped bus. To keep the kick full, add it after the multiply.

## Files

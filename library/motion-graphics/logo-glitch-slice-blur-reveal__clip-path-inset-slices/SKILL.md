---
name: logo-glitch-slice-blur-reveal-clip-path-inset-slices
description: "A wordmark fades up out of a 10px blur while shrinking from 125 percent, flickering through random horizontal slices for the first half second, with a tagline sliding in under it. A brand name reveal after an opening hook, where the logo needs to feel like it is tuning in."
---

# Logo glitch-slice blur reveal

**Code name:** Clip-path inset slices.

## What you see
The wordmark appears at 125 percent scale, blurred 10px and transparent, and settles to full size and sharp over 0.7s. For the first half second it is cut by random horizontal bands: every 50ms the visible region switches between the full word and a band with a random top (0 to 60 percent) and bottom (0 to 30 percent) trimmed off. A purple glow around the word pulses. At 0.6s a one-line tagline fades up from 20px below.

## When to use it
A brand name reveal after an opening hook, where the logo needs to feel like it is tuning in. Works with any wordmark. It reads best against a dark background; the glow needs room around it.

## How it works
Two parts. The settle is `eo` over 0.7s driving scale, opacity and blur together. The glitch is `clip-path: inset()` toggled on a 20 Hz clock using a seeded hash, so the same frame always gets the same bands.

```js
const rand = (i) => { const x = Math.sin(i * 127.1 + 311.7) * 43758.5453; return x - Math.floor(x) }
word.style.clipPath = lt < .5 && Math.floor(lt * 20) % 2
  ? `inset(${rand(Math.floor(lt * 20)) * 60}% 0 ${rand(Math.floor(lt * 20) + 9) * 30}% 0)` : 'none'
// glow breathes: drop-shadow radius 30 + 30 * sin(lt * 6) px
```

The wordmark can be any image. The demo uses a serif text placeholder; any image or text works, because the effect is all on the container.

## Numbers that matter
| | |
|---|---|
| Settle | 0 to 0.7s, `eo`: scale 1.25 to 1, blur 10px to 0, opacity 0 to 1 |
| Glitch | first 0.5s, switches every 50ms, 10 flickers |
| Glow | `drop-shadow` radius 30 + 30 sin(6t) px, rgba(167,139,250,.6) |
| Tagline | 0.6s to 1.2s, rises 20px, 30px type at 70 percent white |

## Sound
Suggested sound: a pink-noise whoosh (high-passed at 600 Hz, low-passed at 5.2 kHz, 0.7s long, volume .22) peaking on every scene cut, over a low A-minor drone pad that ducks under the narration. The cut into this scene has the whoosh; nothing else sits on the glitch.

## Adapt it
- The wordmark and tagline.
- Glitch window `.5` and rate `20` per second for a longer or calmer flicker.
- Glow colour.

## Files
- `code/demo.html` runs on its own with no network. Product screens, covers, logos and the wordmark are CSS placeholders.

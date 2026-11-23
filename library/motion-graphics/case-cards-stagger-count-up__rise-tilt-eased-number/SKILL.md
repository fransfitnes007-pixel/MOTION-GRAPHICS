---
name: case-cards-stagger-count-up-rise-tilt-eased-number
description: "Three dark cards rise from below one after another, tilted a few degrees outward and levelling out, each with a brand header and a big number counting up from zero. Proof: results for a few named customers side by side."
---

# Three case cards with count-up numbers

**Code name:** Rise, tilt, eased number.

## What you see
Three tall dark cards rise from 90px below one after another, 0.35s apart. Each starts tilted 6 degrees away from the centre (the left card anticlockwise, the right card clockwise, the middle one flat) and levels out. Each has a brand square and name at the top, a one-line result, and a number at the bottom that counts up from zero over 1.8s to its figure with an M suffix and a small label under it.

## When to use it
Proof: results for a few named customers side by side. Three is the right number; a fourth card gets small. It needs real figures to be believable.

## How it works
Per card: one `eo` for rise and tilt, then a count. Decimals show one place only if the final value has them.

```js
const k = eo(seg(lt, i * .35, .7 + i * .35))
S(c, { opacity: k, transform: `translateY(${(1 - k) * 90}px) rotate(${(1 - k) * (i - 1) * 6}deg)` })
const v = n * eo(seg(lt, .6 + i * .35, 2.4 + i * .35))
big.textContent = (n % 1 ? v.toFixed(1) : Math.round(v)) + 'M'
```

## Numbers that matter
| | |
|---|---|
| Card | 520 x 600, radius 30px, padding 44px, gradient #14121f to #0c0b14 |
| Pitch | 580px, left edges at 110, 690, 1270 |
| Rise | 0.7s `eo`, stagger 0.35s |
| Count | 1.8s `eo`, starts 0.6s after the card |
| Number | 140px weight 800, tracking -.04em |

## Sound
A suggested soundtrack has a pink-noise whoosh (high-passed at 600 Hz, low-passed at 5.2 kHz, 0.7s long, volume .22) peaking on every scene cut, over a low A-minor drone pad that ducks under the narration. 

## Adapt it
- Brand, line and figure for each card.
- Suffix (`M`, `K`, `%`, `$`).
- Stagger (`.35`) and count length (`1.8`).
- Card gradient.

## Files
- `code/demo.html` runs on its own with no network. Product screens, covers, logos and the wordmark are CSS placeholders.

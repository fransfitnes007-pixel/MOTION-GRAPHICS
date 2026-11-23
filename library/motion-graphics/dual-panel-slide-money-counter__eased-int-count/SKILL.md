---
name: dual-panel-slide-money-counter-eased-int-count
description: "Two dashboard panels slide in from opposite sides, tilted a few degrees the opposite way, and a big dollar figure counts up beneath them. Money landing: revenue, savings, spend."
---

# Two dashboard panels with a money counter

**Code name:** Eased integer count.

## What you see
Two dashboard panels (an analytics page and a billing page) slide in from opposite sides, the left from 80px left tilted -3 degrees and the right from 80px right tilted +2 degrees, overlapping diagonally. Under them a dollar figure counts up from $0 to its final value between 0.9s and 3s, with a smaller grey caption ("paid to one team") on the same line.

## When to use it
Money landing: revenue, savings, spend. The count-up while two screens sit behind it tells "this is where the number comes from". Better with a single figure than a table of them.

## How it works
Panels use one `eo` each (0.7s, the second delayed 0.3s). The counter is `Math.round(final * eo(seg(lt, .9, 3)))` formatted with `toLocaleString`; the caption is a smaller span in the same element so the number can grow without shifting it.

```js
const n = Math.round(8420 * eo(seg(lt, .9, 3)))
money.innerHTML = '$' + n.toLocaleString('en-US') + '<span style="font-size:44px;color:rgba(255,255,255,.6);font-weight:600;letter-spacing:0"> paid to one team</span>'
S(anWin, { transform: `translateX(${(1 - a) * -80}px) rotate(-3deg)` })
```

## Numbers that matter
| | |
|---|---|
| Panels | 900 x 560 at (110,170) and (910,330), cropped from the top-left of each page |
| Slide | 0.7s `eo`, 80px |
| Count | 0.9s to 3s, `eo` |
| Figure | 130px weight 800, tracking -.04em, purple glow |

## Sound
A suitable soundtrack has a pink-noise whoosh (high-passed at 600 Hz, low-passed at 5.2 kHz, 0.7s long, volume .22) peaking on every scene cut, over a low A-minor drone pad that ducks under the narration. 

## Adapt it
- The figure, caption and currency.
- Count window.
- The two panels and their tilt.

## Files
- `code/demo.html` runs on its own with no network. Screens, covers, logos and the wordmark are CSS placeholders.

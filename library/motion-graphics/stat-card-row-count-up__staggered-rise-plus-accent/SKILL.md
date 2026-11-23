---
name: stat-card-row-count-up-staggered-rise-plus-accent
description: "A headline over a row of four soft white cards that rise in 0.11s apart while their numbers count up from zero, each ending in an indigo plus sign. Reach for it for \"numbers that prove it\" beats on a light video."
---

# Stat card row with count-up numbers

**Code name:** Staggered card rise, eased integer count.

## What you see
A heading ("Your proof on the page.") fades up 30px at 21.45s on the demo's internal clock. Beneath it four white frosted cards, 400 x 250, each with a big bold number and a small grey label, rise 44px and fade in one after another, 0.11s apart. As each card arrives its number counts up from 0 over 1.45s, slowing toward the end, and ends in an indigo "+". The one card that holds text ("1M+") is not counted; it scales from 80% with a slight overshoot. At 24.55s the heading and cards drift up 20px and fade out together.

## When to use it
Social proof or results beat: followers, projects, clients, sales. Three to four numbers is the right range. On a tall frame it becomes a 2 x 2 grid. Wrong for numbers that need a chart.

## How it works
Each card has two progress values: a rise (0.55s, ease-out-cubic) and a count (1.45s, ease-out-cubic), both offset by 0.11s per card. The visible number is `Math.round(target * count)` formatted with thousands separators in tabular-nums so the digits do not jitter in width. The plus sign is a separate span in the accent colour. A value like "1M+" cannot be counted, so it gets a back-ease scale-in instead.

```js
const k = eo(p(t, 21.65 + j * 0.11, 22.2 + j * 0.11))      // rise + fade
tf(c, x0 + col * (L.st.w + L.st.gap), L.st.y + row * (L.st.h + L.st.gap) + (1 - k) * 44 - stOut * 20)
const ck = eo(p(t, 21.8 + j * 0.11, 23.25 + j * 0.11))      // count
c.firstChild.innerHTML = Math.round(st.n * ck).toLocaleString('en-US') + plus
```

Layout: the row is centred from the total of card widths and gaps; on the tall layout there are 2 columns and the cards are larger (470 x 310, value 104px).

## Numbers that matter
| | |
|---|---|
| Heading | 88px wide / 92px tall, weight 700, letter-spacing -0.04em, in at 21.45s over 0.5s |
| Card | 400 x 250 (470 x 310 tall), radius 40px, white at 72%, 1.5px white border |
| Value / label | 84px (104 tall) bold tabular-nums / 26px (31 tall) grey |
| Rise | 0.55s, 44px, ease-out-cubic, 0.11s stagger from 21.65s |
| Count | 1.45s, ease-out-cubic, from 21.8s |
| Exit | 24.55s to 24.95s, 20px up and fade |
| Plus sign | `#5b5ce6` |

## Sound
Silent. A soft tick per card, or one rising tone under the count, would suit it.

## Adapt it
- `STATS`: the numbers, suffixes and labels (use `text` for values that are not counted).
- Heading text and the accent colour.
- Count length (`1.45`) and stagger (`0.11`).
- Columns (`ST.cols`) for 3 cards or 2 rows.

## Files
- `code/demo.html` runs on its own (3.9s loop).

---
name: section-title-sidebar-list-active-dash-stretch
description: "A small step counter, a big title and a one-line description on the left, with a list of all sections underneath where the current one gets a long indigo dash and bold type. Reach for it to narrate a tour of a product or a multi-step process next to a screen."
---

# Section title with progress list

**Code name:** Active dash stretch and text swap.

## What you see
On the left third of the screen: a small indigo uppercase counter ("02 / 06"), a big bold title and a grey one-line description. Under them a vertical list of every section. The current item has a long indigo dash and bold black text; the others have a short grey dash and light grey text. When the section changes (every 2.2s) the old text lifts 14px and fades in the last 0.2s, the new text rises 26px into place over 0.4s, the old item's dash shrinks back while the new item's dash stretches from 32% to 105% of the font size.

## When to use it
Beside any tour of a product or a numbered process, where the viewer should know where they are (a stack of 4 to 7 sections). It orients people in a long video without a chapter bar. A variant adds a lighter indigo dash for steps already done. Wrong for 2 or 3 sections, where the list is bigger than the content.

## How it works
All sections' names are in the list from the start. The current index `si` is derived from time and a list of start times. The title block shows `SECTIONS[si]`: it fades up during the first 0.4s of its section and out in the last 0.2s before the next one starts. Each list row has an "activeness" `a` from 0 to 1 that eases in for the current row and eases out for the one before; dash width, colour and weight all follow `a`.

```js
const si = secIndex(t)
const tin = eo(p(t, SEC_T[si] + 0.1, SEC_T[si] + 0.5))
const tout = p(t, nextT - 0.24, nextT - 0.03)
sx.style.opacity = tin * (1 - tout); tf(sx, L.tx.x, L.tx.y + (1 - tin) * 26 - tout * 14)
// each row
if (j === si) a = eo(p(t, SEC_T[j], SEC_T[j] + 0.35)); else if (j === si - 1) a = 1 - eo(p(t, SEC_T[si], SEC_T[si] + 0.35))
i.style.width = lerp(fs * 0.32, fs * 1.05, a) + 'px'; i.style.height = fs * 0.16 + 'px'
i.style.background = a > 0.5 ? '#5b5ce6' : '#cdd0d8'; sp.style.fontWeight = a > 0.5 ? 700 : 500
```

Titles that would be wider than the column are shrunk to fit by measuring them once. Dash size, gaps and text colour all scale from the list font size. The demo uses that variant, with a "done" state (lighter indigo dash, darker grey text) for rows already visited.

## Numbers that matter
| | |
|---|---|
| Layout wide | text at (100, 190), 540px wide; eyebrow 26px, title 96px, description 34px; list at (100, 560), 34px, rows 60px apart |
| Layout tall | text at (70, 150), 940px wide; eyebrow 28px, title 112px, description 40px; list at (70, 1200), 46px, rows 86px apart |
| Text swap | in 0.1s to 0.5s after the section start, rise 26px; out 0.24s to 0.03s before the next, lift 14px |
| Dash | width .32 x font to 1.05 x font, height .16 x font, 0.35s, ease-out-cubic |
| Colours | accent `#5b5ce6`, idle dash `#cdd0d8`, done dash `#8b8cf0`, idle text rgb(154,158,168), active rgb(11,12,16) |

## Sound
Silent.

## Adapt it
- `SECTIONS` (title and line) and `SEC_T` (when each starts).
- The accent (`#5b5ce6`) for the dash and counter.
- Layout block `L`: column width, font sizes and list position.
- Remove the "02 / 06" counter, or change it to "Step 2 of 7" for a process.

## Files
- `code/demo.html` runs on its own (8s loop, five sections).

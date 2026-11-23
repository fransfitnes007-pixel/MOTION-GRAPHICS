---
name: cost-comparison-big-numbers-before-after-total-row
description: "Three large figures in a row (order, cost one way, cost the other) above two bordered tables whose last rows carry a heavy navy rule and the effective total. Reach for it when you need a two-option cost case on one example."
---

# Cost comparison big numbers and tables

**Code name:** Before and after total rows.

## What you see
A grey caps heading and a one-line subtitle. Below, three figures in a row count up: the order value to $350.00, "up to $30" in red and "about $0.50" in green. At 2.4s the first table (current method) opens row by row, every cost cell in red or black; the bottom row has a 2px navy rule above it and reads "Effective cost per order, up to 8.6%". At 4.3s the second table (new method) fills the same way in green, ending with "under 0.3%".

## When to use it
A business case in one screen: this option versus that one, priced on a single real example. Works for fee comparisons, time saved, before and after migration costs. Use one example order, not an average, so the numbers feel concrete. Avoid it when there are more than two options; use a matrix instead.

## How it works
Two layers of emphasis. The big row gives the headline numbers at 38px and tight tracking, with colour doing the verdict (navy neutral, red bad, green good). The tables repeat the same colour code but in monospace right-aligned cells so the numbers line up.

```css
.big{font-size:clamp(26px,6.5vw,38px);font-weight:700;color:var(--navy);letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.bigrow{display:flex;flex-wrap:wrap;gap:14px 40px}
td.n{font-family:"IBM Plex Mono",monospace;font-variant-numeric:tabular-nums;text-align:right;white-space:nowrap}
td.g,td.n.g{color:var(--good);font-weight:600}
td.b,td.n.b{color:var(--bad);font-weight:600}
tr.total td{border-top:2px solid var(--navy);font-weight:600;color:var(--ink)}
```

The wrapper has `overflow-x:auto`, so a wide table scrolls inside its card on a phone. In the demo it is `overflow:hidden` and the figures are scaled to 42px. The counting and row reveals are added; the original is static. It loads its typefaces from Google Fonts; the demo has no network, so it falls back to the system sans, serif and mono stacks. Proportions are close, glyph shapes are not.

## Numbers that matter
| | |
|---|---|
| Big figure | 38px (demo 42px), weight 700, `-.02em`, navy `#002B4E` |
| Table card | white, radius 10px, 1px `#DFE5EB` border, soft navy shadow |
| Header cell | 10.5px uppercase, .1em, `#7C8996` |
| Total row | 2px navy top border, weight 600 |
| Demo timing | figures count 0.3 to 2.6s, table A rows 2.4s on (.28s each), table B from 4.3s, loop 7s |

## Sound
Silent.

## Adapt it
- The example value and both sets of rows.
- Which side is red and which is green.
- The total row's wording; keep it the single most important number.
- Navy to the brand colour.

## Files
- `code/demo.html` runs on its own and loops; 7s. All data is placeholder.

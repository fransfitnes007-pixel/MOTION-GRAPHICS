---
name: dark-ops-scenario-cards-cyan-lime-mono-console
description: "A deep navy, monospace console page: cyan letterspaced tag, a huge two-line sans title, a lime-edged notice bar, a lime status line and three gradient scenario cards each with a cyan run button. Reach for it for a technical tool landing screen, a test runner or a sandbox launcher."
---

# Dark ops scenario cards

**Code name:** Cyan lime mono console.

## What you see
Near-black navy (`#06101c`) with a faint blue glow in the top right corner. A small cyan caps tag with wide tracking, then a title in heavy system sans, two lines at 88px with 0.9 line height. A grey-blue lede in monospace. A bar with a 4px lime left edge holds a one-line boundary notice. Under it a lime status line and a three-column grid of cards: each has a cyan tag id, a bold title, a grey description and a flat cyan button with near-black text.

- 0 to 1.1s: status reads "Loading bundled scenarios…" and the grid is empty.
- 1.1s: it reads "3 scenarios ready" and the cards rise 8px and fade in, 80ms apart.
- 3.6s: the cursor presses the second card's button. The button dims to 45% and the status becomes "Running SC-102…".
- 6.2s: "Complete: run-7f3a · 1,240 events · 4 findings", and the button returns to full strength.

The source page has no animation of its own, only these status changes and the disabled state, so the timings and the cursor are scripted for the demo, and the card rise is added.

## When to use it
Developer and security tooling, CI dashboards, test harnesses, anything that should look like a terminal that grew a UI. The status line in lime is the one moving part, so write it as plain progress text. It is wrong for consumer products: the mono body text is dense and the contrast between lime and cyan is deliberately harsh.

## How it works
Only CSS variables and three borders.

```css
:root { --bg:#06101c; --panel:#0c1b2c; --line:#173b54; --ink:#edf8ff; --muted:#88a4b9; --cyan:#3edcff; --lime:#bafb64 }
body { background: radial-gradient(circle at 90% 0, #173a51, transparent 32%), var(--bg);
  font: 15px/1.55 ui-monospace, SFMono-Regular, Menlo, monospace }
.notice { border:1px solid var(--line); border-left:4px solid var(--lime); background:#091827 }
.card { border:1px solid var(--line); border-radius:10px; background:linear-gradient(145deg,#10253a,#0a1726) }
button { background:var(--cyan); color:#04111c; font-weight:800; border-radius:6px } button:disabled { opacity:.45 }
```

Sans for display, mono for everything else; the mix is what sets the tone. Copy in the demo is invented and neutral.

## Numbers that matter
| | |
|---|---|
| Colours | bg `#06101c`, panel `#0c1b2c`, line `#173b54`, ink `#edf8ff`, muted `#88a4b9`, cyan `#3edcff`, lime `#bafb64` |
| Title | 800 weight, `clamp(46px, 8vw, 88px)` at 0.9 line height |
| Cards | 10px radius, 22px padding, 145deg gradient `#10253a` to `#0a1726` |
| Notice | 4px lime left border |
| Disabled | opacity .45 |

## Sound
Silent.

## Adapt it
- The two accents: swap cyan and lime for any pair that stays bright on navy.
- Title and the card list.
- The glow position and strength in the body gradient.

## Files
- `code/demo.html`: runs on its own.

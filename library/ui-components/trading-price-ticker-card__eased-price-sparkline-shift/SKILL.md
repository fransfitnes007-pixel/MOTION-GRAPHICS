---
name: trading-price-ticker-card__eased-price-sparkline-shift
description: A tiny market card: name, a change chip that flips teal or red, a big price that eases to each new value, a 24-point sparkline that shifts left as a point is added, and a volume line. Reach for it for crypto, stocks, forex, earnings or any "number going up or down" watchlist beat.
---

# Trading price ticker card

**Code name:** Eased price, sparkline shift.

## What you see
White page, a 220px card: "Space" at the left and a rounded chip "▲ 0.00%" in teal at the right; below, $184.20 in 36px medium type; below that a thin teal flat line; at the bottom "Vol 1.5M" in small grey. At 0.45s a tick lands: the price eases down to $183.50 over about half a second, the chip turns red "▼ 0.38%", the line turns red and its newest point drops. At 2.65s another tick (183.40, -0.43%). At 4.85s the price rises to 185.60, chip and line go teal "▲ 0.76%". At 7.05s it returns to 184.20. The line always keeps 24 points: each tick drops the first and adds the new one, so the whole line steps left by one slot. 9.4s loop.

## When to use it
Watchlist, "my coin is moving", portfolio, earnings reveal. The red/teal flip is the story, so let two or three ticks run. Works at 9:16 where the card scales to 72% of the width. Do not use for money someone really holds without a source; it is a design piece.

## How it works
Tick every ~2.2s (the demo uses real timings read from the page). On a tick: the price tweens from the previous value to the new one with ease-out cubic over ~0.55s starting 30ms after the tick; the chip shows the change against the day's open (183.50 against 184.20 = -0.38%, so it is not tick to tick); colour is teal #2dd4bf with a 10% teal chip background when the change is 0 or up, red #ef4444 with 10% red when down; the sparkline polyline is drawn in a 100x22 viewBox with `y = 20 - (p - min)/(max - min) * 18`, a flat series sits on y 20; x spacing is 100/23. Volume is shown as a rounded figure that changes each tick.

## Numbers that matter
| | |
|---|---|
| Card width | 220px (max-w-55), gap 12px |
| Price | 36px / 500 / -0.025em, tabular, 0.55s ease-out cubic |
| Chip | mono 12px / 600, padding 2px 8px, fully round |
| Sparkline | 24 points, 100x22 viewBox, stroke 1.5, height 24px |
| Colours | teal #2dd4bf, red #ef4444, muted #737373 |
| Tick | every ~2.2s |

## Sound
Silent. A short tick per update; a lower tick on red.

## Adapt it
- `CONFIG.name`, `CONFIG.open` (the day's open the chip is measured from), `CONFIG.vol0`.
- `CONFIG.ticks`: `[time, price, volume]`.
- To show money going up only, make every tick higher than the last.

## Files
- `code/demo.html` runs on its own and loops; the values to change are in its `CONFIG` block.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "Trading Number Ticker" by shadcnspace (https://21st.dev/@shadcnspace/components/number-ticker-07), MIT. Recreated by eye from the public preview; this demo is original code. Full notices: `THIRD_PARTY_NOTICES.md`.

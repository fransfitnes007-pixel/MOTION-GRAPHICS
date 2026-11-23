---
name: stock-price-chart-with-moving-averages-crosshair-scrub-tooltip
description: "A trading chart card: ticker and company, a price line with a blue 60 SMA and amber 200 SMA, a right-hand price axis, the last price with a green change pill, and a scrub crosshair with tooltip. Use for stock, crypto or any price-history screen."
---

# Stock price chart with moving averages

**Code name:** Crosshair scrub tooltip.

## What you see
A dark card (the original also ships a light theme). Top left 'AMZN' in bold and 'Amazon.com Inc.' in grey; top right a legend with a blue dot '60 SMA' and an amber dot '200 SMA'. Below it a 120-point price line in white, with a blue line and an amber line that start on the price and lag behind it as it climbs from $144.69 to $179.28. Five faint horizontal gridlines with the values on the right (179.28, 170.63, 161.99, 153.34, 144.69). Under the chart '$179.28' in bold, '+$7.34' in green and a '+4.27%' pill with a green tint. When the cursor enters the chart a thin vertical line snaps to the nearest bar from top to bottom, three dots mark the price and both averages on that bar, and a tooltip headed 'bar 21 / 120' lists Price, 60 SMA and 200 SMA with a colour tick for each. The tooltip flips to the left of the line near the right edge. The demo scrubs from bar 21 to 66, 92, 120, back to 69, 40 and 12, then lets go.

## When to use it
Price history, portfolio value or any metric that has a trend line plus smoothed lines to compare against. Not for a candlestick screen, and the snap-to-bar tooltip needs a pointer.

## How it works
Price is an array; each simple moving average at bar i is the mean of the last n values (it starts with a shorter window, which is why both lines begin on the price). All three are SVG paths built from `X(i)` and `Y(price)`. On pointer move the nearest bar index is `round((x - plotX) / plotW * (bars - 1))`; the vertical line, the three dots and the tooltip all read from that index.

```js
const sma = (n) => price.map((_, i) => { const a = Math.max(0, i - n + 1); /* mean of price[a..i] */ })
const idx = Math.round((px - P.x) / P.w * (bars - 1))   // snap to bar
tooltipLeft = right ? X(idx) - 160 : X(idx) + 10            // flip near the right edge
```

The price series is a seeded random walk scaled to the axis range, so it resembles but does not copy the original data.

## Numbers that matter
| | |
|---|---|
| Bars | 120, plot 840 x 270 on the 1280 board |
| Axis | 144.69 to 179.28, five ticks 8.65 apart |
| Windows | 60 and 200, expanding at the start |
| Lines | 2px, price `#f4f4f5`, 60 SMA `#5b9cf5`, 200 SMA `#e5b45c` |
| Tooltip | 150px wide, radius 7, 12px text, `#18181b` with `#2b2b30` border |
| Crosshair | 1px line `#9a9aa2`, a + mark that follows the pointer height |
| Pill | `+4.27%` green on 14% green tint, radius 8 |

## Sound
Silent.

## Adapt it
- `theme`: 'dark' or 'light'.
- `symbol`, `company`, `change`, `pct`, `lo`, `hi`: the numbers in the header and footer. In your app, derive `change` and `pct` from the data.
- `fast` and `slow`: the SMA windows and their legend labels.
- `scrub`: the scripted cursor path, replaced by real pointer events in an app.

## Files
- `code/demo.html` runs on its own and loops. Everything it draws is a function of time, with `CONFIG` at the top of the script.
- `media/poster.jpg` is one frame.

## Credit
Idea: "SMA Chart" by ssychui on 21st.dev (https://21st.dev/@ssychui/components/sma-chart), MIT. This demo is an original recreation written from the public preview.

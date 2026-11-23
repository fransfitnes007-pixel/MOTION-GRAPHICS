---
name: price-chart-range-navigator-drag-window-minimap-edge-zoom
description: "A dark price-history line chart with a minimap of the whole series under it. A blue outlined window on the minimap sets what the main chart shows: drag it to pan, pull an edge to zoom, and the y-axis and date labels follow. Reach for it for trading, analytics and long time series."
---

# Price chart with range navigator

**Code name:** Draggable window on a minimap, edges zoom.

## What you see
A near-black page. A 23px title "Price history · drag to navigate" sits top left. Below it a main chart 870 wide by 251 tall draws a 3px blue line (`#1f40e0`) with a dark navy gradient under it; the right side has five faint price labels ($161, $156, ...). Under the chart is a 78px minimap with the whole series as a thin grey line and a window rectangle with a blue outline, a faint blue fill and two thick blue handles at its edges. Date labels for the window's start and end sit under the minimap, left and right.

In the 7.6s clip, the cursor first moves over the chart: a dashed vertical crosshair follows with a dot on the line and a dark tooltip above, "$158.13 · Jul 4". It then goes to the window (the cursor becomes a hand), drags it left from May 19 to Jul 30 to Mar 7 to May 18 and further, and the main chart and the price labels re-fit as it goes. Then it pulls the left edge outwards (the cursor shows a left-right arrow) until the window covers Dec 3 to May 6. When the range spans a year end the date labels add the year ("Dec 3, 25" and "May 6, 26").

The demo uses an invented price series of 240 days with the same shape, and runs 12s: hover 0 to 2.7s, pan 3.1 to 4.7s, pull the left edge 5 to 6.2s, then it puts itself back (left handle in, then pan right) so it loops.

## When to use it
Any long time series where people need both the overview and a close look: prices, traffic, sensor data, spend. The minimap shows where you are in the whole series. For short series a plain chart with a range picker (1M, 3M, 1Y) is simpler.

## How it works
One series, two views. The minimap draws every point; the main chart draws the slice between the window's start and end days, with the y-axis re-fit each time:

```js
const rg = hi - lo, top = hi + rg * .12, bot = lo - rg * .16      // padding above and below
y = y0 + (top - p) / (top - bot) * (y1 - y0)
x = x0 + (day - winStart) / (winEnd - winStart) * width
```

Window start and end are the only state. Dragging the body moves both by the same number of days; pulling an edge moves one. The five axis labels are the padded range split in four. In the demo the start and end are keyframe tracks over time (`winStart`, `winEnd`), eased with `eio`, and the cursor path is a list of points that matches them. The price series is generated from `anchors` with a cosine blend and seeded noise.

## Numbers that matter
| | |
|---|---|
| Main chart | x 207 to 1077, y 318 to 569 (1280 x 960 design) |
| Line | 3px `#1f40e0`; area gradient `#1b2d9a` 30% to 0 |
| Minimap | y 597 to 675; series `#3d3e44` 1.6px |
| Window | stroke `#2b40b8` 1.6px, fill rgba(30,50,160,.16), handles 5 x 30px |
| Tooltip | 30px high, `#17171a`, border `#2b2c31`, 15.5px white |
| Axis labels | 14.5px `#4d4e55`, 5 of them |
| Date labels | 16px `#8d8e95` |
| Demo window | 73 days wide at the start, 154 days at the widest |

## Sound
Silent.

## Adapt it
- `CONFIG.anchors`, `days`, `noise`, `seed`: the data (swap in your own array to `price`).
- `line`, `area`, `frame`: the colours.
- `winStart` and `winEnd` keyframes: where the window goes and when.
- `hover`: the crosshair path before the drag.

## Files
- `code/demo.html` runs on its own and loops. It is a recreation made from watching the video and reading the usage example.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Range Navigator" by ssychui on 21st.dev (https://21st.dev/@ssychui/components/range-navigator), MIT. This demo is an original recreation written from the public preview.

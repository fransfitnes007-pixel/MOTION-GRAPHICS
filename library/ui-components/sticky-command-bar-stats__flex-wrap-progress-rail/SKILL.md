---
name: sticky-command-bar-stats-flex-wrap-progress-rail
description: "A sticky top bar holding a title, three right-aligned stat blocks, a save-state pill and a thin progress rail that fills as work gets done. Reach for it when you need a working console with its totals always visible."
---

# Sticky command bar with live stats

**Code name:** Flex-wrap progress rail.

## What you see
A pale green-grey bar drops in from above (0 to .6s). It holds a bold title with a small uppercase subtitle on the left, then three stacked stat blocks on the right: a rust-coloured days-left count, a monospace "priced" fraction and a monospace running total. After them sit a pill with a dot and a state word, and a square dark-mode button. A 5px rail under the stats fills left to right as the fraction climbs from 0/22 to 22/22 between 1.0s and 5.2s, while the total counts up with it. The list underneath scrolls up beneath the bar and the bar stays put. The pill reads Connecting, then Saved (green outline), flickers to Saving… (amber dot) twice at 2.2s and 4.0s, and returns to Saved.

## When to use it
A working console where one person grinds through a list and wants the totals always in view: pricing sheets, review queues, onboarding checklists, content calendars. It suits a single-page tool with 10 to 100 rows. It is wrong for a marketing page, and wrong when the stats are not tied to the list below.

## How it works
One sticky element holds everything. The title takes all the free space with `margin-right:auto`, which is what pushes the stats and buttons to the right edge; `flex-wrap` lets the same row fold onto two lines on a phone with no media query for layout.

```css
.bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:40;background:var(--bg);
  border-bottom:1px solid var(--line);margin-inline:-16px;padding:12px 16px 10px}
.bar-in{max-width:1080px;margin:0 auto;display:flex;flex-wrap:wrap;gap:12px;align-items:center}
.brand{display:flex;flex-direction:column;margin-right:auto;min-width:0}
.stat{display:flex;flex-direction:column;align-items:flex-end;line-height:1.15}
.prog{height:5px;border-radius:99px;background:var(--line);overflow:hidden;margin-top:10px}
.prog i{display:block;height:100%;background:var(--accent);width:0;transition:width .35s ease}
```

The bar's background must be opaque and the negative `margin-inline` cancels the page gutter so the bar runs edge to edge while its content stays aligned with the column below. The rail is one `<i>` whose width is `priced / total * 100%`; the .35s ease is from the source. The save pill is a class swap (`ok`, `busy`, `off`) that recolours the dot, text and border.

## Numbers that matter
| | |
|---|---|
| Bar padding | 12px top, 10px bottom, 16px sides; stat gap 12px |
| Title | 17px, weight 800, letter-spacing -.02em; subtitle 11.5px uppercase, .06em |
| Stat value / label | 18px weight 700 / 10.5px uppercase, .07em, weight 600 |
| Rail | 5px high, fully rounded, width transition .35s ease (source) |
| Save pill | 10.5px uppercase, dot 7px; states neutral, ok (green), busy (amber), off (red) |
| Palette | bg `#EEF2EF`, accent `#0F6E4F`, urgent `#A83C14`, line `#D7E0DB` |
| Demo timing | bar in 0 to .6s, scroll and fill 1.0 to 5.2s, loop 6s |

## Sound
Silent.

## Adapt it
- The three stat labels and values.
- `--accent` and `--urgent`; the rail and pill take their colour from them.
- Which state the pill shows and when; wire it to your save logic.
- Number of stats: the row wraps by itself, so two to four all work.

## Files
- `code/demo.html` runs on its own and loops; 6s. All data is placeholder.

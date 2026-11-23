---
name: headline-card-with-app-window-tabs-click-tab-blur-swap
description: A feature card showing an app window that cuts off at the card edge, with a cursor clicking through four sidebar tabs and the content swapping with a blur-in. Use it for a product feature tile in a bento grid.
---

# Headline card with app window tabs

**Code name:** Click tab blur swap.

## What you see
A large white card with a thin grey border and very round corners (about 44px). Top left: a small grey caps line "PROJECT DASHBOARD" and a two-line headline, "High-performance analytics and team collaboration tools in one place." Below, an app window with a thick pale-grey frame, three dots and a faint "WORKSPACE" title sits lower than the card and runs off the right and bottom edges, with a second paler panel peeking out behind it on the left. The sidebar lists Dashboard, Manage... (10), Threads (12) and Resources, the active one with a light pill and a black bar on its left edge. A black cursor clicks Manage at about 1s, Threads at 2.6s and Resources at 4.1s, and each click swaps the right-hand pane: Project Overview with a 94.2% tile, Team Management with a user list, Communications with two create cards, System Assets with a file list. The new pane arrives blurred (about 8px) and sharpens over 0.45s.

## When to use it
A bento grid or feature section where each tile should show the product doing something, without video. The tabs tell a small story in 4 to 5 seconds. Wrong when the window needs to be readable in full; the card deliberately crops it.

## How it works
Four pane elements sit stacked in the window; only the one for the current tab is visible. On each click the new pane goes from `opacity 0, blur(8px), translateY(6px)` to sharp over `blurSec`. The old pane is hidden at once. Tab state is derived from the click list, so `render(t)` is pure. The cursor eases between the tab positions and shrinks 15% for 0.12s around each click.

```js
const k = seg(t, clickT, clickT + .45)
pane: { opacity: eo(k), filter: `blur(${(1-eo(k))*8}px)`, transform: `translateY(${(1-eo(k))*6}px)` }
```

In the original the clicks are a real hover or click; here they are scripted. Icons in the sidebar are plain squares.

## Numbers that matter
| | |
|---|---|
| Card | 690x540, 44px radius, 1px `#e4e4e7` border |
| Window | 740x420 at left 100, top 232 inside the card, 7px `#ececee` frame, sidebar 162px |
| Clicks | Manage 1.0s, Threads 2.6s, Resources 4.1s, back to Dashboard 5.5s |
| Pane swap | blur 8px to 0, rise 6px, 0.45s |
| Type | headline 30px medium, eyebrow 15px caps grey |

## Sound
Silent.

## Adapt it
- `eyebrow`, `headline`, `tabs`, `badges`.
- `clicks`: times and tab indexes. Add a tab by adding a pane string in `panes`.
- `blurSec` for how soft the swap feels.
- Pane contents in the `panes` array; they are plain HTML.

## Files
- `code/demo.html` runs on its own and loops. Everything is read from the `CONFIG` object at the top of the script.
- `media/poster.jpg` is one frame of it.

## Credit
Idea: "Bento Card" by 0xUrvish on 21st.dev (https://21st.dev/@0xUrvish/components/bento-card), MIT. This demo is an original recreation written from the public preview.

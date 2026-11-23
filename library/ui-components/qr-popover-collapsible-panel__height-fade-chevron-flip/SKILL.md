---
name: qr-popover-collapsible-panel-height-fade-chevron-flip
description: A secondary pill trigger that expands a dark panel with a QR code and a blue button, then collapses it again. Reach for it as a compact show-and-hide section.
---

# QR popover collapsible panel

**Code name:** Height fade chevron flip.

## What you see
A blue-text pill (`Preview HeroUI Native`, 36px tall, #2b2b2e, QR icon at the left, chevron at the right) sits above a 340px dark panel (#141417, 24px radius). Inside, centred: a two-line intro in soft blue, a 216px white QR tile, `Expo must be installed on your device.`, and a blue `Download on App Store` pill (36px, #0a84ff) with an Apple icon.

Watching the clip: it is open for about 1.7s, then collapses in roughly 0.35s. The panel height goes to 0 while its content fades to nothing (the QR dims to grey first), the chevron flips from up to down, and because the group is vertically centred the trigger drifts to the middle of the page. It re-opens near 2.4s.

The demo does the same with a pointer: click at 1.5s to collapse, click at 3.3s to expand, 0.34s each way.

## When to use it
Optional detail you want one click away: a mobile preview code, advanced settings, long help text. It is a single section; for a stack of them use an accordion.

## How it works
The panel sits inside a `clip` wrapper (`overflow:hidden`) whose height is animated from the panel's natural height to 0. Opacity follows height to the power 1.6, so the content is nearly gone before the box closes.

```js
const o = eio(seg(t, closeAt, closeAt + .34))          // 0..1 open amount
clip.height  = fullH * o
panel.opacity = o ** 1.6;  panel.translateY = -(1 - o) * 10
chevron.rotate = 180 * (1 - o)
column.top = 400 - totalHeight(o) * scale / 2         // keeps the group centred
```

The QR is a seeded random pattern with three finder squares, not a real code.

## Numbers that matter
| | |
|---|---|
| Trigger | 36px tall, 24px radius, `#2b2b2e`, text `#8fbcf5` |
| Panel | 340px wide in the demo, 24px radius, `#141417`, 16px padding |
| Collapse / expand | 0.34s, ease in-out |
| QR tile | 216px |
| Loop | 5.6s |

## Sound
Silent.

## Adapt it
- `CONFIG.trigger`, `intro`, `note`, `button` for the words.
- `CONFIG.closeAt`, `CONFIG.openAt`, `CONFIG.animSec` for timing.
- `CONFIG.seed` for a different placeholder QR pattern, or swap the SVG for a real image.

## Files
- `code/demo.html` runs on its own and loops; every frame is `render(t)`. Edit the `CONFIG` block at the top of its script.
- `media/poster.jpg` is the page's preview image.
- Similar looks already in the library: `accordion-listing-row-copy-fields__caret-rotate-copy-flash`, `faq-accordion-glass__height-auto-fade`.

## Credit
Idea: "Disclosure" by hero_ui on 21st.dev (https://21st.dev/@hero_ui/components/heroui-disclosure), MIT. This demo is an original recreation written from the public preview.

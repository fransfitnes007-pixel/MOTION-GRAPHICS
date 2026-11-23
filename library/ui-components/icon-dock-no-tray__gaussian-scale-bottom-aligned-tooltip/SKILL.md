---
name: icon-dock-no-tray-gaussian-scale-bottom-aligned-tooltip
description: Seven app icons in a bare row (no tray) that swell toward the pointer, up to about double size, sitting on a shared baseline with a small label over the biggest one. Reach for it as a macOS-style dock or an app-launcher row on a light page.
---

# Icon dock without tray

**Code name:** Gaussian scale bottom-aligned tooltip.

## What you see
A white page with seven colourful app icons in a row, about 46px each with 14px gaps and nothing behind them, centred. As the pointer enters from the right and moves left, the icon under it grows to roughly 2x (a 28px icon becomes about 55px in the video), the neighbours grow to roughly 1.3 to 1.5x, and the whole row widens to make room. Icons grow upward from a shared bottom line. A tiny white label with a hairline border (Figma, Webflow, Spotify, and so on) sits above the biggest icon and follows it. Moving on to the next icon shifts the size and the label smoothly. When the pointer leaves, the row relaxes back to equal sizes in about half a second. The clip runs the pointer across all seven in about 4.7 seconds.

## When to use it
App launchers, integrations strips, a bottom nav that wants the Mac dock feel, a tools row on a landing page. It has no tray, so it suits a white or open background; with a tray, see the sibling `bottom-icon-dock__spring-distance-magnify`. Needs a real pointer. On touch, fall back to flat icons.

## How it works
Each icon's scale comes from its distance to the pointer, a bell curve: `scale = 1 + (max - 1) * exp(-d^2 / (2 s^2))`, with d the pointer's x minus the icon's resting centre. Icons keep their bottom edge fixed (transform-origin bottom), and the row is laid out with flex so the scaled widths push neighbours apart and re-centre the row. The label is placed over whichever icon is largest and fades in once its scale passes about 1.25.

```js
const scale = 1 + (MAX - 1) * Math.exp(-(d * d) / (2 * SIGMA * SIGMA))
// MAX 1.95, SIGMA about 62px for 56px icons
```

The original is a framer-motion dock (useMotionValue, useTransform, spring). The demo computes the same curve from `t`, with the pointer path scripted. The icons are simple SVG placeholders, not the real logos; the labels read Notes, Tasks, Chat, Video, Music, Web, Design.

## Numbers that matter
| | |
|---|---|
| Icon | 56px in the demo (about 46px in the preview), gap 16px |
| Max scale | 1.95 under the pointer |
| Reach | sigma about 62px, so about 2 neighbours on each side grow noticeably |
| Label | 12px text, white, 1px `#e6e6e6` border, 6px radius, 12px above the icon |
| Pointer path in the demo | enters at 0.3s, crosses the row 0.8s to 4.6s, leaves by 5.3s, 6.4s loop |

## Sound
Silent.

## Adapt it
- `CONFIG.items`: your labels and icons (replace the SVG strings with `<img>` elements).
- `CONFIG.base`, `gap`: size and spacing.
- `CONFIG.maxScale` and `spread`: how big and how far the magnify reaches.
- `CONFIG.sweep`: the scripted pointer path; in real use take the pointer from `mousemove`.

## Files
- `code/demo.html` runs on its own and loops. The pointer path is scripted and the icons are SVG placeholders.
- `media/poster.jpg` is a still of the component.

## Credit
Idea: "Dock Nav" by soralabs on 21st.dev (https://21st.dev/@soralabs/components/dock-nav), MIT. This demo is an original recreation written from the public preview.

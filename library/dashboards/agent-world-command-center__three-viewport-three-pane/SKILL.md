---
name: agent-world-command-center-three-viewport-three-pane
description: "A dark violet desktop-app layout built around a live 3D scene: title bar with stats and a clock, an agent list with business filter chips, a central viewport with minimap, camera buttons and toasts, and a right panel streaming terminal output. Reach for it to show an AI-agent product as a place you can look into."
---

# Agent world command center

**Code name:** Three viewport, three pane.

## What you see
A 44px title bar with a green pulsing dot, a gradient "NORTHSTAR HQ" wordmark, small stats, a "Commands  K" chip and a time readout on the right. Left, a 260px panel: a small caps "Agents" heading with a violet plus button, four filter chips, a search box and cards with a name, role and a "running" status chip. In the middle, the 3D island (see the sibling skill) with a 140x90 minimap top left, three camera buttons top right (Aerial is outlined), a hint label bottom left, and chat toasts stacking in at the top right. On the right, a 320px detail panel with the agent name, a role chip and a business chip, a black terminal area and a message box with Send and Kill.

- 0 to 1.5s: a full-screen loading card with the title, a "Building the world" line, a 4px violet bar filling and a status line. It fades out over 0.6s from 1.7s.
- From 1.0s: toasts slide in 20px over 0.3s (ease-out) as the characters speak, last 3.5s, then fade. The status dots on the cards pulse between 100% and 40% opacity every 2s.
- 1.9s: the first agent's terminal types its log.
- 8.2s: the selection moves to another card (violet border, left bar and soft glow) and the right panel switches and types a new log.
- The sky runs a whole day in 16s, the clock follows it and the minimap dots follow the characters.

## When to use it
A product film or landing page for an agent platform, where "your agents live here" is the idea. The 3D window sells presence; the side panels sell control. It is a poor fit for a utility app that needs no personality.

## How it works
A plain three-column CSS grid, `260px 1fr 320px` under a 44px bar, with one `<canvas>` in the middle cell. Panels are flat surfaces (`#161625`, `#1e1e30`) with 8% white borders and one accent, `#8b5cf6`. Everything the app animates is small:

```css
.status-dot.running { animation: pulse 2s infinite }   /* opacity 1 -> .4 -> 1 */
.toast { animation: toastIn .3s ease-out; transition: opacity .3s }  /* translateX(20px) -> 0 */
.agent-card.selected { border-color: var(--accent); border-left-color: var(--accent); box-shadow: 0 0 12px rgba(139,92,246,.15) }
.loading-overlay { transition: opacity .6s }  .loading-fill { transition: width .3s }
```

In the demo the canvas is sized to the middle cell in device pixels and shown at the design size, so the whole layout can be scaled for any stage. All animation is a function of `t`. The 3D part is the same scene as the diorama skill, with the camera set back and the corner clock moved into the title bar.

## Numbers that matter
| | |
|---|---|
| Grid | 260px / 1fr / 320px, title bar 44px |
| Colours | bg `#0d0d1a`, surface `#161625`, surface 2 `#1e1e30`, accent `#8b5cf6`, running `#22c55e` |
| Type | Inter 12 to 16px, mono 11.5px for terminal and clock |
| Toast | 250px max, 3.5s life, 4 max |
| Loading bar | 300x4px, violet to `#a78bfa` |
| Terminal stream | 34 characters a second in the demo |

## Sound
Silent. A soft chime per toast and a keyboard-click bed under the terminal would suit it.

## Adapt it
- Accent colour, title, and the `NAMES` table.
- The scene: swap the island for any three.js scene by replacing `renderWorld`.
- Log text in `LOG`; selection time `8.2`.
- Drop the left panel (it is hidden in the tall layout, which stacks the viewport over the detail panel).

## Files
- `code/demo.html`: runs on its own, including from a double-click. `code/three.global.js` is three.js (MIT) bundled as a plain script, so no server is needed.

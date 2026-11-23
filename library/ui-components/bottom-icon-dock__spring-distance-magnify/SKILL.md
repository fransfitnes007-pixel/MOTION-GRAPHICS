---
name: bottom-icon-dock-spring-distance-magnify
description: "A floating black-glass dock of icon buttons that swell toward the pointer on springs, with a tooltip over the hovered button, a dot under the active one and a blue accent button at the end. Use for app navigation that should feel like a launcher."
---

# Bottom icon dock

**Code name:** Spring distance magnify.

## What you see
A rounded 24px glass bar sits at the bottom of the screen with seven rounded-square buttons, 46px each, 6px apart. Move the pointer along it and every button grows according to how close it is: 68px under the pointer, back to 46px when 150px away or more. The icons inside scale with the button. The bar stays centred, so it widens as the buttons swell, and the buttons grow upward past the bar's top edge because they are bottom-aligned. The button under the pointer gets a small dark tooltip above it. The active button is brighter, with a glowing blue dot 6px beneath it. The last button is a blue accent button for the main action. When the pointer leaves, everything springs back to 46px.

## When to use it
Primary navigation for an app with five to eight sections, in place of a sidebar. On touch screens nothing magnifies, so use the same buttons at fixed size with labels under them (the source does this). Not for long menus.

## How it works
One shared motion value holds the pointer's x. Each button measures its centre, turns the distance into a size with a three-point range map, and a spring smooths it. The icon scale is size divided by 46.

```tsx
const mouseX = useMotionValue(Infinity)                       // onMouseMove sets clientX, onMouseLeave sets Infinity
const distance = useTransform(mouseX, v => v - rect.left - rect.width / 2)
const size = useSpring(useTransform(distance, [-150, 0, 150], [46, 68, 46]),
                       { mass: 0.1, stiffness: 170, damping: 13 })
const scale = useTransform(size, v => v / 46)
```
Infinity maps to the clamped end of the range, so an idle dock is all 46px. The spring is light (mass 0.1) and not very damped, so each button overshoots a little and settles.

The demo simulates the pointer along a fixed path and integrates the same spring with small fixed steps from 0 to `t` each frame, so a frame is still a pure function of time.

## Numbers that matter
| | |
|---|---|
| Sizes | `DOCK_SIZE` 46, `DOCK_MAG` 68, `DOCK_DIST` 150 |
| Spring | mass 0.1, stiffness 170, damping 13 |
| Bar | height 66px, padding `0 10px 9px`, radius 24px, gap 6px, fill `rgb(10 10 14 / .70)` over a 158deg sheen, `backdrop-filter: blur(44px) saturate(1.6)` |
| Button | radius 15px, 11% to 4% white gradient, 1px 11% white border, inset top highlight |
| Active | 24% to 8% white gradient, 30% white border, blue-300 icon, 4px dot with `0 0 8px` glow |
| Accent | `rgb(96 165 250 / .96)` to `rgb(37 99 235 / .96)` |
| Tooltip | 12px semibold, `rgb(14 14 18 / .94)`, appears `10px` above the button, fades in .15s |

The demo leaves out the bar's `backdrop-filter`, which renders differently from run to run in headless Chrome and does nothing over a black page.

## Sound
Silent. A faint tick as each button passes under the pointer would suit it.

## Adapt it
- `DOCK_SIZE`, `DOCK_MAG`, `DOCK_DIST` for a gentler or stronger swell.
- The spring: raise damping to 20 for no overshoot.
- The icons and labels, and which button is `act`.
- The accent gradient for another brand colour.

## Files
- `code/demo.html` runs on its own and loops in 6s.

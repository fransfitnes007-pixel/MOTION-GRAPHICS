---
name: gradient-tile-magnetic-dock-radius-scale-lift-idle-wave
description: A dark pill-shaped dock with seven colourful rounded gradient tiles that swell and lift as the pointer sweeps past, with a white tooltip above the nearest tile and a slow idle wave when untouched. Reach for it as an app dock, a toolbar or a bottom navigation on a dark page.
---

# Gradient tile magnetic dock

**Code name:** Radius-based scale and lift with idle wave.

## What you see
A near-black page (`#0a0a0b`). In the middle, a dark pill 776 by 123 with a 42px radius, a hairline border and a faint blue glow underneath. Inside it are seven rounded tiles about 76 to 80px, each a diagonal two-colour gradient: blue to cyan (Finder), cyan to sky (Search), green to cyan (Deploy), amber to coral (Insights), coral to red (Audio), periwinkle to blue (Vault) and cyan to blue (Send). Each has a thin black line icon. Under the dock, grey text reads "Sweep the dock, or Tab through it."

In the 4.7s clip the cursor sweeps across. The tile under it grows to about 125px wide and rises 35px or so; the tiles on each side grow less, so they overlap. A white pill label ("Audio", "Insights", "Send") sits 12px above the hovered tile. When the cursor leaves, a smaller wave of the same grow-and-lift travels left to right across the tiles (it starts at Finder at 3.4s and is near the middle at 4.6s), also with a label on the peak.

The demo runs 6s: idle at the start, a sweep from 0.5s to 3.2s (Search, Audio, Send, Insights), then the idle wave.

## When to use it
An app dock or tool strip on a dark, product-style page. The magnet gives a sense of weight and makes small targets easy to hit. Skip it on touch devices, where there is no hover, and keep the labels because the icons alone are abstract.

## How it works
Each tile's scale is a cosine bump of its distance from the pointer. The page's props are `magnetRadius={140} maxScale={1.65} lift={16} idleWave tooltip`.

```js
const bump = (d, R) => d >= R ? 0 : Math.cos(Math.PI * d / (2 * R)) ** 2
scale = 1 + (maxScale - 1) * bump(|tileX - pointerX|, radius)
translateY(-lift * bump)      // transform-origin: bottom centre, so tiles grow upward
```

Tiles scale about their bottom edge and are not re-laid out, so big tiles overlap neighbours; z-index follows the bump. The idle wave uses the same bump with a centre moving at 2.8 tiles per second and a smaller peak (1.18). The label belongs to whichever tile has the largest bump above 0.55. Page props are in the page's own pixels, which look about 1.15 times smaller than the preview video, so the demo sets the radius to 200 and the peak scale to 1.55 to match what the video shows.

## Numbers that matter
| | |
|---|---|
| Dock | 776 x 123, 42px radius, `#0e1118`, border rgba(255,255,255,.07) |
| Tile | 80px, 22px radius, gradient 160deg, icon 38px stroke 1.9 `#07070a` |
| Pitch | 104px between tile centres |
| Hover | peak scale 1.55, lift 18px, radius 200px |
| Idle wave | peak 1.18, 2.8 tiles per second |
| Label | white, 40px high, 14px radius, 19px / 600 |
| Gradients | `#4f7cff` `#22c7d9` `#38bdf8` `#32d583` `#f6b94a` `#ff6b5e` `#e9564a` `#7f9fff` `#45d5e4` |

## Sound
Silent.

## Adapt it
- `CONFIG.items`: label, two gradient colours and an icon path for each tile.
- `maxScale`, `lift`, `radius` for a stronger or subtler magnet.
- `idleScale` and `idleSpeed`, or set `idleScale: 1` to turn the wave off.
- `sweep`: the cursor script; `tooltip: false` to hide labels.

## Files
- `code/demo.html` runs on its own and loops. It is a recreation made from watching the video and reading the usage example.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Magnetic Dock" by rmahammad on 21st.dev (https://21st.dev/@rmahammad/components/magnetic-dock), MIT. This demo is an original recreation written from the public preview.

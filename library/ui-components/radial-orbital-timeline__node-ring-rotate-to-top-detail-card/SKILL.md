---
name: radial-orbital-timeline-node-ring-rotate-to-top-detail-card
description: "A dark orbital diagram: five labelled icon nodes on a thin ring around a purple-blue-teal orb. Clicking a node rotates it to the top, enlarges it, and opens a card with a status badge, date, text, an energy bar and links to related nodes, whose own nodes pulse. Reach for it for a roadmap, process or relationship map on a dark page."
---

# Radial orbital timeline

**Code name:** Node ring that rotates the picked node to the top.

## What you see
A black page. A 1px ring (about 472px across in the 1280 by 720 clip, `rgba(255,255,255,.1)`) holds five nodes at 72 degrees apart: Planning, Design, Development, Testing, Release. In the centre is an 80px orb with a violet to blue to teal gradient and a grey inner disc, with two faint rings that expand and fade around it. Each node is a 50px black circle with a thin white-grey border and a white line icon (calendar, document, code, person, clock), with its name in 16px semibold letter-spaced text under it. Nodes at the top of the ring are dimmer (opacity 0.4) and nodes at the bottom brighter (up to 1). The ring turns slowly, about 6 degrees a second.

Click a node (the clip clicks Testing at 1.2s): the ring spins about 120 degrees in about 0.6s so that node sits at the top, and it turns solid white with a black icon and scales to 1.5. A card 316 wide drops in 74px below it with a connector line: a "PENDING" pill, the date "Apr 2024" in mono, the title, a one-line description, a rule, "Energy Level" with "30%" and a 4px blue to violet gradient bar, a rule, "CONNECTED NODES" and outlined buttons for the related items ("Development →", "Release →"). The related nodes get a pulsing translucent white fill. Rotation stops while a card is open. Clicking empty space closes the card and the ring turns again.

The demo runs 9s: Testing selected at 1.25s, closed at 3.0s, Release selected at 4.3s, closed at 6.2s, with a fade at the wrap.

## When to use it
A roadmap, a lifecycle, or a hub-and-spokes relationship on a dark landing page or dashboard, with five to eight items. The rotate-to-top gives every item the same stage, and the connected nodes show relations. It does not scale to many items, and the labels need room, so avoid it on narrow screens.

## How it works
Node `i` sits at angle `startAngle + i * 72 + R` on a circle of radius 236. Selecting node `i` eases `R` to the value that puts it at 270 degrees, taking the shorter way round:

```js
target = 270 - startAngle - i * 72;  target += 360 * Math.round((R - target) / 360)
R = lerp(from, target, eo((t - tClick) / 0.6))
```

Opacity follows height on the ring: `max(.4, min(1, .4 + .6 * (1 + sin(angle)) / 2))`. The card is positioned at the selected node's position plus 74px, so it follows the node as it travels. In the demo the whole rotation and selection are a pure function of the event list (`state(t)` replays the events up to `t`). The data shape from the usage example is `{ id, title, date, content, category, icon, relatedIds, status, energy }` with status `completed`, `in-progress` or `pending`; the page is rendered by `<RadialOrbitalTimeline timelineData={...} />`.

## Numbers that matter
| | |
|---|---|
| Ring | radius 236, centre (633, 342) in 1280 x 720, `rgba(255,255,255,.1)` |
| Node | 50px, border 2px `rgba(255,255,255,.55)`, icon 20px |
| Selected node | white fill, black icon, scale 1.5 |
| Orb | 80px, `#7c3aed`, `#3b82f6`, `#14b8a6`, inner disc 40px |
| Auto rotation | 6 degrees per second, stops while a card is open |
| Travel | 0.6s ease-out |
| Card | 316 x 310, 9px radius, `rgba(0,0,0,.92)`, border `rgba(255,255,255,.28)` |
| Energy bar | 4px, `#3b82f6` to `#8b5cf6` |
| Demo loop | 9s |

## Sound
Silent.

## Adapt it
- `CONFIG.nodes`: titles, dates, text, status, energy, related ids, icons.
- `radius`, `center`, `spinDegPerSec`, `travelSec`.
- `events`: when each node is picked and when the card is closed.
- `accent` for the energy bar colours; the orb gradient in the `core` style.

## Files
- `code/demo.html` runs on its own and loops. It is a recreation made from watching the video and reading the usage example.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Radial Orbital Timeline" by jatin-yadav05 on 21st.dev (https://21st.dev/@jatin-yadav05/components/radial-orbital-timeline), MIT. This demo is an original recreation written from the public preview.

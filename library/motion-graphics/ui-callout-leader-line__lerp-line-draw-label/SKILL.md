---
name: ui-callout-leader-line-lerp-line-draw-label
description: "Annotation callouts for UI footage: dot, leader line, label. Use them on a laptop or phone shot to name three things the viewer should look at, as the voice says them."
---

# UI callout with leader line

**Code name:** Pulsing dot, drawn leader line and label pill.

## What you see
A laptop with a dashboard sits on the right and the voice lists three things. As each is spoken, a 20px dot with a lavender ring and a pale halo pops onto the matching tile on the screen (scale .5 to 1 with a spring), a 2.5px lavender line draws out of it toward a point 200 to 380px away over 0.4s, and a dark pill label with a faint lavender outline fades in at the end of the line ("Page views", "Link clicks", "Inquiries"). All three stay until 4.0s, then disappear together. The laptop is already zooming in on the tiles when the first one lands.

## When to use it
Annotating real UI footage in a voiced walkthrough, where each label is a short noun the voice says. It points exactly at the thing, which a highlight box would not. It needs a camera that has already zoomed to a scale where the target is big enough; callouts on a full-page shot are too small.

## How it works
A callout is a dot, an SVG path and a label inside one container. `callAt` places it from a target point (tx, ty), a label point (lx, ly), its start time and its end time. Points come from `lpt(L, x, y)`, which converts a point in the 1440 by 900 capture into stage coordinates through the current camera, so the callout follows the zoom.

```js
const p = eo5(seg(t, at, at + .4)), l = eo(seg(t, at + .08, at + .5)), q = ei(seg(t, out, out + .2))
dot: scale(.5 + .5 * spring(seg(t, at, at + .5), 8, 12)), opacity p * (1 - q)
line: M tx,ty L lerp(tx, lx, l),lerp(ty, ly, l)
label: translate(lx < tx ? -100% : 0, -50%) scale(.85 + .15 * l), opacity clamp(l * 1.5) * (1 - q)
```

The label hangs to the left of the dot if the label point is left of it, so one function serves both sides. Keep labels inside the frame: clamp them with `Math.min`.

## Numbers that matter
- Dot 20px, 3px `#a5b4fc` border, 35% indigo fill, 8px halo; spring(k=8, f=12).
- Line 2.5px `#a5b4fc`, round caps, draws over 0.42s starting 0.08s after the dot.
- Label 24px bold, padding 11px 18px, radius 14, fill `rgba(18,18,30,.92)`, outline `rgba(165,180,252,.35)`.
- Exit `ei` over 0.2s. A "Sample data" chip is shown whenever the numbers are fake.

## Sound
None.

## Adapt it
- The capture and the three target points in capture coordinates.
- Label texts and label positions.
- The `at` times (set them to the voice) and the end time.
- Accent colour (`#a5b4fc`) for a different palette.

## Files
- `code/demo.html` runs on its own and loops. The dashboard is a CSS placeholder. The demo uses the system font stack.

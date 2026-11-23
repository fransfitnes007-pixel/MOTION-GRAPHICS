---
name: spotlight-product-tour-svg-mask-spring-hole
description: "The page dims to 78% black with a rounded hole around one element; the hole springs to the next target on each step, ringed in violet, with a tooltip card that places itself beside it and shows step count, progress dots and Back/Next. Use for first-run product tours."
---

# Spotlight product tour

**Code name:** SVG mask spring hole.

## What you see
A full-screen veil at `rgba(5,5,9,.78)` over the app, with a rounded 12px hole around one element, padded 6px on each side. A 1.5px violet outline traces the hole with a soft 14px glow. A 320px card sits beside it, with a small rotated square pointing at the target: "STEP 2 OF 4" in tiny violet capitals, a bold title, two lines of grey copy, a row of progress dots (current one 20px wide and solid, finished ones half-opacity, upcoming ones faint), and Skip, Back and Next buttons. Press Next and the hole slides and resizes to the next target on a spring while the card fades up in its new place. The card goes right of the target if it fits, below if not, above if that fails, and centres with no arrow on small screens. Escape skips; arrow keys step.

## When to use it
First-run walkthroughs in an app with a sidebar or toolbar to point at. It dims everything else, so keep steps to five or six. Not for tours that need the user to click through the highlighted thing; the veil blocks it.

## How it works
One SVG covers the viewport. A `<mask>` holds a white full-size rect and a black rounded rect (the hole); a dark rect uses that mask, so the hole is genuinely transparent. A second rect with no fill draws the outline. Both rects are `motion.rect` and animate `x`, `y`, `width`, `height` with the same spring, so the hole and outline travel as one.

```tsx
<mask id="hq-walkthrough-mask"><rect width="100%" height="100%" fill="white" />
  <motion.rect initial={false} animate={{ x: box.x, y: box.y, width: box.w, height: box.h }}
    transition={{ type: 'spring', stiffness: 380, damping: 34 }} rx={12} fill="black" /></mask>
<rect width="100%" height="100%" fill="rgba(5,5,9,0.78)" mask="url(#hq-walkthrough-mask)" />
```
The target is found by `[data-walkthrough=key]`, then by the sidebar link's href, then by a CSS selector, measured with `getBoundingClientRect()` and re-measured on resize and scroll and again 350ms after a step so layout can settle. The card position is computed before paint from the box and the card's measured height: try right, then below, then above, clamped 12px from the screen edges, with the arrow offset clamped at least 18px from the card corners. The card is keyed on the step, so it remounts and plays `opacity 0, y 6 to 1, 0` in .2s with `[0.16, 1, 0.3, 1]`.

The demo springs between the stored target boxes with the same stiffness and damping, runs the same `place()` function, and draws a placeholder app shell instead.

## Numbers that matter
| | |
|---|---|
| Veil | `rgba(5,5,9,.78)`, whole overlay fades .18s |
| Hole | pad 6px, radius 12px, spring stiffness 380 damping 34 |
| Outline | `rgba(167,139,250,.85)`, 1.5px, `drop-shadow(0 0 14px rgba(139,92,246,.55))` |
| Card | 320px wide, radius 16px, border `rgb(139 92 246 / .3)`, shadow `0 25px 50px -12px rgba(0,0,0,.6)` |
| Placement | gap 14px, edge 12px, arrow 12px rotated square |
| Dots | current `w-5` solid violet, done `w-1.5` violet at 50%, todo `w-1.5` white at 10% |

## Sound
Silent.

## Adapt it
- The step list: title, body and the element each points at.
- Veil alpha and the outline colour.
- Spring stiffness and damping: raise damping for no overshoot.
- Pad and radius to match the highlighted element's shape (use a large radius for round buttons).

## Files
- `code/demo.html` runs on its own and loops in 11s.

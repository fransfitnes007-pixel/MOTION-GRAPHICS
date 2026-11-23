---
name: dark-checkbox-with-label-and-states-rounded-box-stroke-draw-tick
description: "A checkbox on a near-black page: a 22 px rounded box with a thin grey border and a 16 px label, which fills blue and draws a white tick when clicked. The demo also shows the checked, indeterminate (dash) and invalid (red, with a message) states. Reach for it for terms, age confirmation and option lists."
---

# Dark checkbox with a label and its states

**Code name:** Rounded box with a stroke-drawn tick.

## What you see
The 21st.dev preview shows nothing but the resting state: a `#131313` page with one unchecked box (about 20 px, rounded, thin grey border, slightly lighter fill) and the white label "Accept terms and conditions" beside it. The clip is 4 seconds of that single still picture, so the motion below is the demo's, not the clip's.

In the demo a pointer comes in and the box border brightens on hover (`#55555c` to `#8a8a92`). At 1.0s it clicks: the box dips to 92% and fills blue (`#0485f7`) over 0.18s while a white tick draws itself along its path in 0.22s. At 3.3s it clicks again and the fill and tick reverse. Under the first row, three static rows show the other states named in the description: a checked box, an indeterminate box with a short white dash, and an invalid box with a red border (`#f0526a`) and the message "You must confirm your age to continue."

## When to use it
Terms and consent, a "21 or older" confirmation at checkout, settings lists, bulk select with a parent "Select all" in the indeterminate state. For on-off settings that apply at once use a switch instead.

## How it works
The usage example is one line: `<Checkbox id="basic-terms">Accept terms and conditions</Checkbox>`. The component description says it covers binary choices, form options, indeterminate states, labels and validation messaging, and HeroUI v3 builds on React Aria, which provides the keyboard and screen reader behaviour. Its colours are not visible in the unchecked preview, so the blue, the red and the border greys are choices made for this demo.

The tick is one SVG path with `pathLength="1"`, so the draw is a single number:

```js
path.setAttribute('stroke-dashoffset', 1 - draw)      // draw goes 0 to 1 over 0.22s
box.style.background = mix('#1b1b1d', accent, on)     // on goes 0 to 1 over 0.18s
```

For the indeterminate state the same path is swapped for a horizontal dash `M6 12h12`.

## Numbers that matter
| | |
|---|---|
| Page | `#131313`, label `#f2f2f3` 16px |
| Box | 22px, 7px radius, 1.5px border `#55555c`, fill `#1b1b1d` |
| Checked | fill and border `#0485f7`, white tick stroke 3 |
| Invalid | border and message `#f0526a`, message 13.5px |
| Click | box scales to 92% and back over 0.25s, fill 0.18s, tick 0.22s |
| Gap | box to label 12px, 74px between rows |

## Sound
Silent.

## Adapt it
- `label` and `rows` (text, `checked`, `indeterminate` or `invalid`, and a message).
- `accent`, `idleBorder`, `hoverBorder`, `invalid` for the palette; on a light page change `#1b1b1d` and the page and label colours.
- `boxSize`, `radius` for the size.
- `clickOn`, `clickOff`, `popMs`, `drawMs` for the click timing.

## Files
- `code/demo.html` runs on its own and loops. All imagery is CSS or SVG placeholder.
- `media/poster.jpg` is a preview image showing the component.

## Credit
Idea: "Checkbox" by hero_ui on 21st.dev (https://21st.dev/@hero_ui/components/heroui-checkbox), MIT. This demo is an original recreation written from the public preview.

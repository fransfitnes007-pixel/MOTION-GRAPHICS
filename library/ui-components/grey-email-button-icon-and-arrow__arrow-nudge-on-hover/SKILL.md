---
name: grey-email-button-icon-and-arrow-arrow-nudge-on-hover
description: A light grey button with a mail icon on the left, a label, and an arrow on the right that slides 2px right on hover. Reach for it for secondary actions that lead somewhere.
---

# Grey email button with icon and arrow

**Code name:** Arrow nudge on hover.

## What you see
A 36px tall button, 8px radius, fill `#f4f4f5`, with a 16px mail icon at 60% opacity, 'Email' in 14px medium dark text, and a 16px arrow at 60% opacity, 8px gaps. When the cursor enters, the fill goes a touch lighter (`#f7f7f8`) and the arrow slides 2px right over 0.15s; when the cursor leaves it slides back. The demo adds a 2% press shrink on click.

## When to use it
A secondary button that goes to another place: contact, learn more, view all. The nudge is tiny, so it works in quiet layouts where a big arrow animation would be too loud.

## How it works
A secondary Button with the `group` class. The arrow has `transition-transform group-hover:translate-x-0.5` (2px). Both icons carry negative outer margins (`-ms-1`, `-me-1`) so the button does not look padded on the icon sides. The demo computes one hover value `h` from the cursor times and uses it for the fill and for `translateX(2px * h)`.

## Numbers that matter
- Height 36px, radius 8px, padding 16px, fill `#f4f4f5`
- Icons 16px at 60% opacity; gaps 8px, outer margin -4px
- Arrow slides 2px in 0.15s
- Hover fill `#f7f7f8`

## Sound
Silent.

## Adapt it
- `label` and the two icons (`mail`, `arrowR` in the icon table).
- `arrowNudge` for a bigger slide, e.g. 4.
- `fill`, `fillHover`, `text` for a dark or brand version.
- `hoverIn`, `hoverOut`, `pressAt` to retime the scripted cursor.

## Files
- `code/demo.html` runs on its own, loops in 4.6s, and has a `CONFIG` block at the top of the script.

## Credit
Idea: "Button" by originui on 21st.dev (https://21st.dev/@originui/components/button/button-with-icon-and-arrow), MIT. This demo is an original recreation written from the public preview.

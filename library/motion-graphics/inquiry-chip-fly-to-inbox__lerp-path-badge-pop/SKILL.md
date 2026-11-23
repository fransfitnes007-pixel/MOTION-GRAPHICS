---
name: inquiry-chip-fly-to-inbox-lerp-path-badge-pop
description: "A message travelling between two app windows: a chip leaves the first, the windows swap, a highlight frame lands on the new row and a counter badge springs in. Use it to show data moving from one product surface to another."
---

# Inquiry chip flying to inbox

**Code name:** Lerp path chip, window swap and row highlight.

## What you see
Window one, a contact form, is on screen. On the word "form" a white pill chip with an envelope icon and a name rises out of it, scaling from 70%. Then the form window slides 260px left, blurring, while the inbox window swings in from 500px to the right, rotated 26 degrees. The chip crosses from lower left to the top row of the inbox in 0.75s and fades as it arrives. A thick indigo frame with a soft halo snaps onto the new row, and a "1 New inquiry" badge springs in at the top right. Everything then scales up 30% and blurs away.

## When to use it
Showing a message, order, lead or file moving from where a customer acts to where a team sees it. The windows can be any two screens. It tells a before and after story in three seconds, so keep the chip text short.

## How it works
Two window transitions on shared `eio5` ramps, one chip on three linked ramps, then two spring pops.

```js
const mf = eo5(seg(t, FORM + .05, FORM + .45)), mt = eio5(seg(t, 1.6, 2.35))
chip.left = lerp(620, 900, mt); chip.top = lerp(lerp(860, 800, mf), 520, mt)    // mf lifts it, mt carries it
chip.opacity = mf * (1 - ei(seg(t, 2.35, 2.55)))
hl: appears at 2.3s with eo5 over 0.3s, scale 1.15 to 1
badge: scale(.6 + .4 * spring(seg(t, DASH + .05, DASH + .5), 8, 13))
```

The chip's top is a nested lerp: first it rises (`mf`), then flies (`mt`). With a real screenshot, place the highlight frame from the camera point of the row; the demo fixes it.

## Numbers that matter
- Window 1 out: `eio5` over 0.7s, 260px left, scale .86, blur 8px. Window 2 in: 0.7s, 500px, rotateY -26 degrees, scale .9 to 1.
- Chip: 25px heavy text, pill padding 14px 24px 14px 15px; lift 0.4s, flight 0.75s.
- Highlight: 4px border `#5b5ce6`, 8px halo at 16%, eo5 over 0.3s.
- Badge: spring(k=8, f=13) over 0.45s.
- Exit: `eio5` over 0.35s, scale +30%, blur 10px.

## Sound

## Adapt it
- The chip text and icon.
- The window contents, positions, and the chip's start and end points.
- Highlight position: it must sit on the row the chip lands on.
- The badge text.

## Files
- `code/demo.html` runs on its own and loops. The two windows are CSS placeholders.

---
name: layout-flash-cut-pill-tabs-beat-cut-punch-zoom
description: "Hard cuts between screenshots inside a fixed window, each cut with a small zoom punch, and a glass pill bar whose active tab follows. Use it to show a list of options or layouts in under two seconds."
---

# Layout flash-cut with pill tabs

**Code name:** Beat-synced cut with punch zoom and active pill.

## What you see
A window sits still while the page inside it changes hard, with no transition, to the next of six layouts at each cut. On every cut the page scales up 3.5% and settles back over 0.16s, which makes each cut feel like a hit. Under the window a frosted pill bar lists the six layout names; the active one is filled indigo and enlarged to 106% and the others are grey. The six cuts can land 0.16s apart on eighth notes; the demo spaces them 0.5s apart.

## When to use it
Showing a set of alternatives fast: themes, layouts, templates, colourways. Works because the viewer only needs a glance at each. It would be wrong for anything that needs to be read carefully.

## How it works
Cuts are an array of times. Every frame finds the latest cut that has passed and shows that capture, hiding the others with `display:none`.

```js
let li = 0; LCUT.forEach((c, i) => { if (t >= c) li = i })
show(w3, li)
const punch = 1 - eo5(seg(t, LCUT[li], LCUT[li] + .16))
cam(w3, 720, 420, lerp(1, 1.12, eio(seg(...))) * (1 + punch * .035))
pill.style: background = on ? '#5b5ce6' : 'transparent'; transform = on ? 'scale(1.06)' : ''
```

The slow push-in (zoom 1 to 1.12) keeps running under the punches, so each cut starts from a slightly different scale. Make the cut times from the beat grid of the music.

## Numbers that matter
- Cuts: times in `LCUT`; example values 7.21, 7.39, 7.51, 7.67, 7.83, 7.99 (0.16s apart after the first two).
- Punch: +3.5% scale decaying with `eo5` over 0.16s.
- Pill bar: 1100 by 96, radius 48, `rgba(255,255,255,.74)` with a 24px backdrop blur; text 27px bold.
- Active pill: `#5b5ce6` fill, white text, scale 1.06.

## Sound

## Adapt it
- The captures and the pill labels; keep the count equal.
- `LCUT`: set them to your beat grid.
- Punch strength (.035) and length (.16s).
- Active colour `#5b5ce6`.

## Files
- `code/demo.html` runs on its own and loops. The six pages are CSS placeholders; use real screenshots in practice.

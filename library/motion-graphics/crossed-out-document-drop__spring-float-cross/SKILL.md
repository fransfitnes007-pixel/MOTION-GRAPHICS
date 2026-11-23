---
name: crossed-out-document-drop-spring-float-cross
description: "A document card springs in, a red X pops over it while it greys out, then it tumbles down and blurs away. Use it to reject the old way of doing something before the new one arrives."
---

# Crossed-out document drop

**Code name:** Spring float, red cross, blurred drop.

## What you see
A white paper card, 400 by 500, with a grey header strip reading a file name and blocks standing in for content. It rises from 120px low with a slight tilt and a spring settle (0.2s to 0.9s). At 1.65s a red X, 300px across, pops over it with an overshoot while the card desaturates to grey over 0.3s. At 2.17s the card falls 520px, tumbling 24 degrees anticlockwise, shrinking to 70% and blurring to 10px, and a white flash covers the cut at 2.72s to 3.1s.

## When to use it
Rejecting a bad habit or an old tool in the first seconds of an explainer: the file nobody opens, the PDF, the spreadsheet. The beat before the product appears. Do not use it for neutral content; the red cross is a verdict.

## How it works
Three transforms driven by three small curves, plus a CSS filter chain.

```js
const di = spring(seg(t, .2, .9), 6, 9), drop = ei(seg(t, T_SITE + .12, T_SITE + .7))
doc: translateY((1 - di) * 120 + drop * 520), rotate(-4 + 4 * di + drop * -24), scale((.9 + .1 * di) * (1 - drop * .3))
doc.filter = `blur(${drop * 10}px) grayscale(${seg(t, T_CROSS, T_CROSS + .3)})`
cross: scale(.4 + .6 * spring(seg(t, T_CROSS + .02, T_CROSS + .45), 9, 14))
```

The cross is a separate element that shares the drop transform, so it falls with the card. The grey-out and the cross are both keyed to one spoken cue, the fall to a later one, so they follow the voice.

## Numbers that matter
- Card: 400 by 500, radius 14px, starts rotated -4 degrees.
- Entry: `spring(k=6, f=9)` over 0.7s. Cross: `spring(k=9, f=14)` over 0.43s.
- Grey-out: 0 to 100% over 0.3s starting on the cross.
- Drop: `ei` over 0.58s, 520px down, -24 degrees, scale -30%, blur 10px.
- Flash: white at up to 0.7 opacity, in over 0.16s, out over 0.22s.

## Sound

## Adapt it
- The file name in the header strip and the blocks inside the card.
- `T_CROSS` and `T_SITE`: set them to the words you want the cross and the fall to hit.
- The cross colour `#ef4444`, or swap the X for a tick to endorse instead of reject.
- Drop distance and rotation for a gentler or harder exit.

## Files
- `code/demo.html` runs on its own and loops. The file name is a neutral placeholder.

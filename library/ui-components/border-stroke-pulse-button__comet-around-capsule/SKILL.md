---
name: border-stroke-pulse-button-comet-around-capsule
description: "A dark capsule button \"Start with payment\". The background dims, the button grows a little, and a bright streak with a soft glow enters on the right and runs once around the border, lengthening as it goes and fading near its start. Use to draw attention to a primary action."
---

# Border stroke pulse button

**Code name:** Comet around capsule. **From:** original build for this library.
Original code; the interaction idea is a common iOS pattern (see 60fps.design for references).

## What you see
Dark screen with faint ghost rows behind. A 760x176 capsule with a 1.5px faint border and white label. A finger taps at .55s; from .65s to 1.1s the background dims by 62% and the button scales to 1.06. At 1.0s a streak appears at the right end of the capsule and travels clockwise (down, then left along the bottom, up, back along the top) in 1.7s with an ease-in-out that is partly linear. It starts at 7% of the perimeter long and grows to 43%, brightest at the head and fading toward the tail, with a blurred pale-blue copy behind as a halo. In the last 18% of the lap it fades, ending near the start. From 3.0s the dim and scale ease back.

## When to use it
A single primary action that needs one confident beat of attention: start a payment, confirm, upgrade. Wrong as a looping attention-grabber; one pass is the point.

## How it works
One capsule path (`M right-mid, arc, line, arc, line, arc`) is drawn in SVG. A dash is a window on the stroke, so a comet is `stroke-dasharray: len, bigGap` with `stroke-dashoffset: -tail`. To get a tail that fades, the streak is cut into 14 consecutive dash segments whose opacity ramps up to the head. The same segments are duplicated into a group with `feGaussianBlur` for the glow.
```js
head = LEN*p; len = LEN*(.07+.36*p); tail = max(0, head-len)
seg i: dasharray = `${len/14} ${2*LEN}`, dashoffset = -(tail + len*i/14), opacity = ((i+1)/14)^1.6
```

## Numbers that matter
| | |
|---|---|
| Button | 760x176, fully round |
| Dim | 62% black, .45s in, .6s out |
| Grow | 1.06 |
| Lap | 1.0s to 2.7s |
| Streak length | 7% to 43% of the perimeter |
| Streak | white 3.4px core, `#9fd2ff` 9px halo, blur 9 |
| Loop | 5s |

## Sound
A rising whoosh that follows the head, with a tiny click at the end of the lap.

## Adapt it
- Streak and halo colours.
- `BW`, `BH`, and the label.
- Lap time and the 0.07 to 0.43 length range.
- Number of segments (14) for a smoother or harder tail.

## Files
- `code/demo.html` runs on its own and loops in 5s.
- `media/poster.jpg`

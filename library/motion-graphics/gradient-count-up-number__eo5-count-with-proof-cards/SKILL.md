---
name: gradient-count-up-number-eo5-count-with-proof-cards
description: "A huge blue gradient number races from 0 to a billion on a strong ease-out, with a label under it and two white stat cards tilting in at the lower corners. Reach for it for the big number in a results scene."
---

# Gradient count-up number

**Code name:** Quintic count with proof cards.

## What you see
The scene cuts to white. A 210px number in a blue to cyan gradient (`#2f6bff` to `#38bdf8`) starts at 0 and climbs so fast it is unreadable: 719 million after 0.5s, 998 million at 1s. It slows hard near the top and lands at "1,000,000,000+" with a plus sign at 19.65s. The number itself scales from 90% to 100% on a spring during the first half second. Under it the words "views tracked" pop up. On the left, at 18.93s, a white card tilts in 4 degrees anticlockwise with a small logo, a view count and "views for ..." in small grey type; on the right at 19.45s a second card tilts in 3 degrees clockwise.

## When to use it
The result: views, revenue, users, anything with a huge figure. The count makes the size feel earned. The cards are social proof for the number, two examples of it. It is wrong for small numbers (count time is the same, so 40 would blur by) and for precise figures where the digits matter.

## How it works
The count is a single eased value multiplied by the target; tabular figures keep the number from jittering sideways:

```js
const q = eo5(seg(t, t0, t1))                  // quintic ease-out: fast start, a long slow finish
counter.textContent = q >= 1 ? '1,000,000,000+' : Math.round(q * 1e9).toLocaleString('en-US')
```
```css
.num { font-variant-numeric: tabular-nums }
```
The text swaps to the final string at exactly `q = 1` to add the "+", which avoids the number ever showing the target without it. The gradient is `background-clip: text` on a `.big` element, so the number is real text and its width changes freely as digits are added; it is centred with `translate(-50%,-50%)` so it grows from the middle.

On the tall layout (150px type) the finished string "1,000,000,000+" is as wide as the 1080px frame and touches both edges; drop the size to about 130px if you want a margin.

The cards each use one spring (`k7 f11` over .55s) for opacity (`clamp(q * 2)`), tilt (`-4 * q` and `3 * q` degrees) and scale (`.7 + .3 * q`). A line chart (see that skill) can draw under this scene at the same time.

## Numbers that matter
| | |
|---|---|
| Count | `eo5` from 18.64s to 19.65s (1.01s), target 1e9 |
| Number | 210px (150 on tall), weight 800, tracking -.055em, centred 110px above middle |
| Number entrance | spring k7 f11 over .5s, scale .9 to 1 |
| Label | 46px weight 600, the pop-in from the LED word: spring k8 f12, rises 30px |
| Cards | 54px base, radius 1em, tilt -4 and +3 degrees, positions 640px left and right of centre |

## Sound
A run of 28 short ticks (2.2 to 2.65kHz, 30ms each, 0.028s apart) under the count, like a keyboard, then a pop (1700Hz) for the last number. Keypress samples layered on the synthetic tick give a typed feel.

## Adapt it
- The target (`1e9`) and the final string.
- The count duration and the easing (`eo5` for a hard finish, `eo` for gentler).
- The gradient colours.
- The label and the two proof cards; replace the placeholder icon with a logo.

## Files
- `code/demo.html` runs on its own. The brand icons and counts on the cards are placeholders, not real data.

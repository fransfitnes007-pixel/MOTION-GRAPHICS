---
name: check-chip-trio-settle-spring-scale-row
description: "A row of three tick chips (\"One payment\", \"Setup included\", \"Nothing monthly\") that pop in on the voice and sit in a line under a headline. Use it to summarise three reassurances at the end of a pitch."
---

# Check chip trio settling in a row

**Code name:** Spring scale-in chips that settle from a stack into a row.

## What you see
On the dark stage two lines of white 116px type arrive word by word: "Setup is included" and "on your own terms." with the last word of each in lavender. Along the bottom, three dark glass pills, each with a 38px green tick circle, pop in at the speaker's points: "One payment" first (which glides 80px down and 430px left to take the left slot), then "Setup included" in the middle, then "Nothing monthly" on the right. Each scales from 60% with a spring overshoot. All of them leave together after 3.0s.

## When to use it
The reassurance beat before a call to action: what is included, what you do not pay. Three items is the right count; with more, the chips are too small to read. They need a dark or neutral stage to stand off.

## How it works
Each chip has its own spring on its own time, and the first chip is the only one that travels.

```js
const q = spring(seg(t, r.at, r.at + .5), 8, 12)         // scale .6 + .4 * q, opacity clamp(q * 1.5)
const settle = eio5(seg(t, .6, 1.0))                     
chip0.left = lerp(760, 330, settle); chip0.top = lerp(680, 760, settle)
```

The first chip is created under the huge statement of the scene before it (see dark-stage-circle-reveal__clip-path-circle-wipe), so the viewer sees one item, then the rest. A variant stacks the same three chips vertically beside the headline, with no settle.

## Numbers that matter
- Chips: 34px heavy text, padding 16px 30px 16px 16px, fill `rgba(14,12,22,.86)`, 1px white outline at 12%, tick circle 38px `#16a34a`.
- Pop: `spring(k=8, f=12)` over 0.5s, from scale .6.
- Slots: x 330, 760, 1220 at y 760.
- Headlines: 116px weight 800, y 250 and 390.

## Sound

## Adapt it
- The three chip texts and their `at` times.
- Slot positions, if you want a vertical stack.
- Tick colour, for a different tone.
- The headline words.

## Files
- `code/demo.html` runs on its own and loops. Chip texts are neutral placeholders.

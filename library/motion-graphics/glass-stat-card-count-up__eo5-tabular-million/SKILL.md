---
name: glass-stat-card-count-up-eo5-tabular-million
description: "A white glass stat tile with a big number counting up and a small uppercase label. Use it for one headline metric, spoken by a voiceover."
---

# Glass stat card counting up

**Code name:** Eo5 count-up in a frosted card with tabular numerals.

## What you see
A frosted white card, 470 by 210 with 28px corners, slides 80px in from the left while growing from 90% and fading in. In the card a number in 84px heavy type counts 0, 1, ... up through the hundreds of thousands, fast at first and slowing hard as it nears 1,000,000, over 0.76s. When it lands the number switches from black to indigo. A small grey uppercase label sits under it.

## When to use it
One headline number, read out by a voice, where the counting is the point: views, revenue, users. Because the ease-out is so steep (quintic), the last 10% of the value takes most of the time, which reads as "it keeps going". Not for a dashboard with several numbers.

## How it works
The number is text rewritten every frame; `tabular-nums` keeps the digits the same width so the number does not jitter sideways as it changes.

```js
stat.textContent = Math.round(lerp(0, 1000000, eo5(seg(t, RES, DONE)))).toLocaleString('en-US')
stat.style.color = t > DONE ? '#5b5ce6' : '#0b0b10'
card: translateX((1 - sq) * -80px) scale(.9 + .1 * sq), opacity clamp(sq * 1.4), sq = spring(seg(t, RES - .05, RES + .5), 7, 11)
```

The glass look is `rgba(255,255,255,.74)` with `backdrop-filter: blur(24px)`, a 1px outline at 7% and a long soft shadow. It needs something coloured behind it to look like glass.

## Numbers that matter
- Count: 0 to 1,000,000, `eo5`, from the word "results" to the word "your" (0.76s).
- Card: 470 by 210, radius 28px, padding 34px 40px, blur 24px.
- Number 84px weight 800, letter-spacing -.05em; label 26px 600 uppercase, letter-spacing .06em.
- Colour flip to `#5b5ce6` at the end of the count.

## Sound

## Adapt it
- The target number, the label, and `RES`/`DONE` times.
- The accent colour at the end.
- Card size and position; the same number also works at 210px with no card, on a dark stage.
- Remove `toLocaleString` for decimals or units.

## Files
- `code/demo.html` runs on its own and loops. The label is neutral placeholder copy.

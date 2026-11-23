---
name: stat-tile-shine-border-conic-beam-count-up
description: "A bento stat tile with a 2px ring that a coloured light travels around (a rotating conic gradient), a number that counts to its new value, and a green or red trend pill. Use it for the one metric that should feel alive."
---

# Stat tile with shine border

**Code name:** Rotating conic beam ring with count-up number.

## What you see
Four tiles in a 2 x 2 grid. A light of each tile's tone colour (blue, blue, green, violet) runs round its border continuously, one lap every four seconds, fading from nothing to full over the last 40% of the turn. Inside, an uppercase label with a tinted icon square, a 30px bold number and a pill ("+8% wk"). At 3.2s and 5s the figures change: the numbers roll from the old value to the new in 0.6s, and the trend pills change with them (a "-4%" turning into "+2%" then "+6%").

## When to use it
Hero metrics and live counters: the beam says "this updates". It is deliberately subtle at small sizes. Do not put beams on every tile of a page; the app turns them on selectively.

## How it works
The tile is `relative overflow-hidden rounded-2xl border p-[2px]`. Behind the body a `200% x 200%` square centred on the tile holds a `conic-gradient(from 90deg, transparent 0%, transparent 60%, var(--beam) 100%)` and rotates with `@keyframes kit-rotating-beam` from 0 to 360 degrees in 4s linear; the 2px gap between the body and the ring shows the beam as a border light.

```js
transform: `translate(-50%,-50%) rotate(${(t % 4) / 4 * 360}deg)`
```

The body is `rounded-[calc(1rem-2px)] bg-rv-card p-5`. `MotionNumber` runs framer's `animate(from, to, { duration: 0.6, ease: [0.16,1,0.3,1] })` when `value` changes and formats each frame. The trend pill is `rounded-full px-2 py-1 text-xs font-semibold` with `bg-emerald-500/10 text-emerald-400` or `bg-red-500/10 text-red-400`.

## Numbers that matter
- Palette: Page `#050509`, card `#0D0D1A`, card hairline `#1A1A2E`, muted text `#6B7280`, accent `#8B5CF6` with light `#A78BFA`.
- Beam: 4s linear, `from 90deg`, transparent until 60% then full tone colour.
- Ring thickness 2px; tile radius 16px, body radius 14px.
- Count: 0.6s ease `[0.16,1,0.3,1]`.
- Tones: purple `139,92,246`, blue `59,130,246`, green `16,185,129`, amber `245,158,11`.

## Sound
Silent. A dashboard on screen sits under voice-over; a soft tick on each tab or filter change is the only sound that suits it.

## Adapt it
- `TILES`: label, icon, tone, three successive values, format, sub, trend.
- `T_CHG` sets when values change.
- Beam period (`t % 4`) and the 60% stop for a longer or shorter tail.
- In the glass variant the beam turns white (see the glass skill).

## Files
- `code/demo.html` runs on its own and loops, no build step. Every frame is `render(t)`; the numbers are invented. The shared kit at the top of the script (icons, spline and chart helpers) is inlined so the file has no dependencies.

---
name: wordmark-slam-shock-ring-spring-scale-shake
description: "The reveal slam for a brand name: spring scale-down from 1.5x, a tiny screen shake, a shock ring, a shine sweep, then a tuck into the corner as a watermark. Use it on the beat where the product name first appears."
---

# Wordmark slam with shock ring

**Code name:** Spring scale-down, camera shake and expanding ring.

## What you see
A small grey "This is" fades in on a light stage. At the name (3.45s on the demo's clock) the round mark spins a full turn about its vertical axis while springing in, and the wordmark drops in from 150% size and 14px of blur, settling to 100% over about 0.65s. The whole frame jolts for 0.35s, a thin indigo ring 400px wide expands to 2000px while fading out, and a white shine band runs across the wordmark. From 4.0s to 4.42s both pieces fly to the top-left corner and shrink to 6% and 40% of their size, leaving a small watermark.

## When to use it
The first reveal of a brand or product name in a voiced video, on the exact word. Use it once; the shake and ring are loud. It needs a light, quiet stage around it so the ring is visible. It is a bad fit when you cannot afford a second of screen time for the logo.

## How it works
Four effects share one clock and the name time `GK`.

```js
const s = spring(seg(t, GK - .1, GK + .55), 8, 13)             // scale 1.5 -> 1
wm.transform = `translate(${sx}px,${sy}px) scale(${(1.5 - .5 * s) * lerp(1, .06, go)})`
wm.filter = `blur(${(1 - clamp(s * 1.4)) * 14}px)`
camShake: p = seg(t, at, at + .35); d = (1 - p) * amp; [sin(t * 90) * d, cos(t * 77) * d]
ring: p = eo(seg(t, GK, GK + .9)); diameter = 400 + p * 1600; opacity = 1 - p
```

The shake is two sine waves at unrelated frequencies with a linear decay, so it has no random numbers and repeats exactly. The tuck into the corner (`go`) is a plain translate plus scale, using `eio5`. The shine is covered in its own skill.

## Numbers that matter
- Slam: `spring(k=8, f=13)`, scale 1.5 to 1, blur 14px to 0, opacity in over 0.16s.
- Mark: `spring(k=6, f=9)`, one full turn of rotateY over 0.9s, scale .6 to 1.
- Shake: 9px amplitude, 0.35s, `sin(t*90)` and `cos(t*77)`.
- Ring: 400px to 2000px over 0.9s with `eo`, 3px border `rgba(91,92,230,.5)`, glow 60px.
- Tuck: `eio5` over 0.42s, wordmark to 6% scale, mark to 40%.

## Sound
None.

## Adapt it
- The wordmark and mark artwork. The demo uses placeholder text and a plain mark; swap in your own images.
- `GK`: the time of the word you slam on.
- Ring colour and the shake amplitude (9px).
- Corner target in `go`, if your watermark sits somewhere else.

## Files
- `code/demo.html` runs on its own and loops. The wordmark and round mark are CSS placeholders.

---
name: chrome-logo-spin-rise-shock-rings-rotatey-ring-expand
description: "A big chrome logo mark spins a full turn on its vertical axis while it rises and shrinks up the frame, with three thin violet rings expanding from behind it. An opening logo sting on a light stage."
---

# Chrome logo spin, rise and rings

**Code name:** RotateY ring expand.

## What you see
Over a pale stage with soft orbs, the logo starts 170px below its final spot, blurred 18px and at 60% size. In 1.15s it makes one full rotation about its vertical axis, rises, and shrinks to about 70% of its start size. A white shine band slides across it between 0.25s and 1.1s. Three violet outline rings grow from 300px to 1400px behind it, each starting 0.16s after the last, and fade as they grow. At 1.5s the logo lifts, blurs and fades out.

## When to use it
The first second of a video, before the first headline. The spin gives a logo some weight without a heavy reveal. It is a short sting, not a hold: the headline words can arrive under it while it is still travelling.

## How it works
One element carries the whole move: translate, scale, `rotateY` and blur are built from four eased progress values.

```js
const a = spring(seg(t, 0, .7), 6, 9), up = eio5(seg(t, .1, .7)), spin = eio(seg(t, 0, 1.15)) * 360
S(g1, { transform: `translateY(${lerp(170, -10, up) - out * 120}px) scale(${(.6 + .4 * a) * lerp(1.15, .62, up) * (1 - out * .4)}) rotateY(${spin}deg)`,
        opacity: clamp(a * 1.3) * (1 - out), filter: `blur(${(1 - clamp(a * 1.2)) * 18 + out * 10}px)` })
```
There is no `perspective` on the parent, so the rotation reads as a flat squash to zero width and back rather than a 3D turn. That is how it looks as built; add `perspective: 1200px` to the parent if you want depth.

The shine is a second copy of the logo filled with a transparent-white-transparent gradient and blended with `screen`; the whole copy is translated sideways, so it is a ghost passing over the mark. Rings are circles sized by `p = eo(seg(...))`: `d = 300 + p*1100`, opacity `(1-p)*.9`.

## Numbers that matter
| | |
|---|---|
| Logo box | 360x450 at (780,120) in a 1920x1080 frame |
| Spin | 360 degrees over 1.15s, `eio` (cubic in-out) |
| Rise | y from +170px to -10px, scale 1.15 to .62, `eio5`, 0.1s to 0.7s |
| Entrance | `spring(k=6, f=9)` over 0.7s drives opacity, 60 to 100% size and the blur |
| Rings | 3 rings, 300 to 1400px, 2px border `rgba(124,58,237,.35)`, centred at (960,340), 0.16s apart, 1.12s each, `eo` |
| Exit | 1.5s to 1.86s, rises 120px, blurs 10px, shrinks 40% |

## Sound
Silent by itself. A noise riser can build under this scene toward the next cut.

## Adapt it
- The mark: replace the `G` glyph elements with your logo image (mask the shine copy with it).
- Ring colour and the three ring starts.
- Spin duration, or `spin * 2` for two turns.
- Add `perspective` for a true 3D turn.

## Files
- `code/demo.html` runs on its own; the logo is a chrome-gradient text glyph.
- Related: `end-card-g-flip-wordmark-blur__rotatey-spring-blur` (a matching closing spin) and `logo-shine-sweep__masked-gradient-position`.

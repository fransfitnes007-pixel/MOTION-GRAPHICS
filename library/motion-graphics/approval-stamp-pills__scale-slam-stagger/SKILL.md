---
name: approval-stamp-pills-scale-slam-stagger
description: "Dark glowing pills with a green status dot reading Approved or Live slam onto a wall of video covers one after another, each starting 1.8x large and a few degrees off, then settling. Labelling content in a grid: reviewed, approved, live, paid."
---

# Approval stamp pills

**Code name:** Scale slam stagger.

## What you see
Dark capsule pills with a glowing green dot and a status word (Approved, Live) land on a wall of video covers one after another. Each starts 1.8x large and a few degrees off, snaps to size in 0.3s and stays until the scene ends.

## When to use it
Labelling content in a grid: reviewed, approved, live, paid. The staggered slam gives the feeling of someone working through the wall. Works over any dense grid; it would be lost over a clean white page.

## How it works
Each pill has its own start time, half a beat after the last (234ms at 128 BPM), and one `eo5` over 0.3s. Opacity goes up in a quarter of that so it appears at once.

```js
const k = seg(lt, t0, t0 + .3)
S(p, { opacity: clamp(k * 4), transform: `scale(${lerp(1.8, 1, eo5(k))}) rotate(${(rand(i) - .5) * 10}deg)` })
```
```css
.pill{padding:14px 24px;border-radius:999px;background:rgba(16,12,30,.9);border:1px solid rgba(167,139,250,.5);box-shadow:0 0 40px rgba(139,92,246,.45)}
.pill .dot{width:12px;height:12px;border-radius:50%;background:#34D399;box-shadow:0 0 14px #34D399}
```

Variant: pills start at 60 percent and pop with a back ease with no rotation, one every 450ms, and fade out at 4.3s.

## Numbers that matter
| | |
|---|---|
| Pill | 26px weight 700, padding 14 x 24, radius 999px |
| Slam | 0.3s, `eo5`, scale 1.8 to 1, rotation within +-5 degrees |
| Stagger | 234ms |
| Dot | 12px #34D399 with a 14px glow |

## Sound
A suggested soundtrack is a synthesised 128 BPM groove in A minor (Am F C G): kick on every beat, claps on 2 and 4, open hats on the offbeats, sidechained bass. Impacts (a sine boom plus filtered noise crash) land on beats 12, 40, 48 and 60, and a band-passed noise whoosh peaks on each moving transition. A short tick can go on each stamp, or leave them silent under narration.

## Adapt it
- Words and dot colours (green for approved, lilac for live).
- Stagger interval to match your beat.
- Positions on the wall.

## Files
- `code/demo.html` runs on its own with no network. Product screens, covers, logos and the wordmark are CSS placeholders.

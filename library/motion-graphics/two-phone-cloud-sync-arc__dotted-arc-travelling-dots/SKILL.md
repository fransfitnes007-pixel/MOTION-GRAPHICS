---
name: two-phone-cloud-sync-arc-dotted-arc-travelling-dots
description: An old phone and a new phone stand together under a two-line headline; a dotted arc runs between them through a cloud badge, coloured dots ride along it and the badge arrow turns into a tick. Rebuilt by eye from a public motion video (see Credit); use it in app promos and launch reels.
---

# Two phone cloud sync arc

**Code name:** Dotted arc with travelling dots. Rebuilt by eye from a public motion video; original code, credited below.

## What you see
Dark navy with a faint square grid. "New phone? Welcome back." builds word by word from 0.15s (0.13s apart, each word rising out of a 10px blur), the question mark and full stop in violet. At 0.55s two phones spring up from below: the old one smaller, tilted -4 degrees, slightly behind; the new one in front, tilted 2 degrees. At 1.05s a dotted line draws from the top of the old phone up to a violet cloud badge (which pops in) and down to the new phone. From 1.45s five coloured dots leave the old phone one after another, ride over the badge and land in the new phone (1.5s each, ease-in-out). At 3.0s the badge's download arrow fades and a tick draws in with a small pop. Everything drops away at 4.6s.

## When to use it
Any "it moves with you" feature: backup, restore, cross-device sync, account transfer, moving an account to a new device. Works as one beat of a vertical app-update reel. Wrong for one-device stories.

## How it works
The path is two quadratic Beziers (old phone top to badge, badge to new phone top) in one SVG `path` with a dotted dash pattern (`2 9`, round caps). The dots are evaluated on the same curve analytically, not with `getPointAtLength`, so they are exact and cheap:
```js
const q = (p0, c, p1, u) => [(1-u)*(1-u)*p0[0] + 2*(1-u)*u*c[0] + u*u*p1[0], ...]
const p = u < .5 ? q(A, C1, M, u * 2) : q(M, C2, B, u * 2 - 1)
```
The line "draws" with a left-to-right `clip-path: inset()` on the SVG, which reads the same because the path runs left to right. Wide layout puts the headline left and the phones right (`PX = W * .66`).

## Numbers that matter
| | |
|---|---|
| Headline | 78px heavy at 1080 wide, words .13s apart, .4s eo5 blur 10 to 0 |
| Phones | 390 x 810, spring f 1.6 zeta .8, old phone .1s earlier, scale .9, -4 degrees |
| Arc draw | .5s ease-in-out from 1.05s |
| Dots | 5, .14s apart, 1.5s each, ease-in-out, 7px radius |
| Tick | .35s draw at 3.0s with a sin-bump pop of 14% |

## Sound
Soft upward blips as each dot leaves, one bright "done" chime on the tick. Keep the dots under the music. The demo is silent.

## Adapt it
- `words` (the `|` is the line break; trailing ? or . takes the accent).
- `accent` and `dots` colours.
- Replace the phone rows with screenshots (`background:url(...)` on `.scr`).
- `t.tick` to land the tick on a beat.

## Files
- `code/demo.html` runs on its own; every value to change is in the `CONFIG` block at the top of the skill script.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "revid.ai Claude Opus 5.5 wall #31: HabitKit: a vertical app update" by @sebastianroehl (https://x.com/sebastianroehl/status/2103912457836323096), Video belongs to its creator; not included. Recreated by eye from watching the public video; this demo is original code and contains none of the video. Full notices: `THIRD_PARTY_NOTICES.md`.

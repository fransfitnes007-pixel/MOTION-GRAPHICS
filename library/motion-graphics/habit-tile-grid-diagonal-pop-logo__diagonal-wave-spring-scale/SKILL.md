---
name: habit-tile-grid-diagonal-pop-logo-diagonal-wave-spring-scale
description: A grid of rounded tiles in four colour bands pops in as a diagonal wave from the top-left, some cells left dim, then a two-colour wordmark rises letter by letter beneath it. Rebuilt by eye from a public motion video (see Credit); use it in app promos and launch reels.
---

# Habit tile grid diagonal pop logo

**Code name:** Diagonal wave spring scale. Rebuilt by eye from a public motion video; original code, credited below.

## What you see
Tall 1080x1920, near-black navy (#0d0e13) with faint coloured glows and a ghost grid of dots. At 0.2s tiles start popping in from the top-left corner: each one scales up from 0 with a little overshoot and a few degrees of twist, one diagonal every 0.032s, so the whole 7x8 grid is in by about 0.65s. Rows come in colour pairs: lime, lavender, green, coral, with some cells only 22% bright (habits not done). A small spaced monospace label fades in under the grid at 0.82s and the wordmark ("Your" white, "Brand" violet) rises letter by letter from 0.9s, 0.045s apart. From 3.4s the wave runs backwards (bottom-right first) and the type drops away.

## When to use it
The open of a vertical app promo for anything with a grid of progress: habits, streaks, posting calendars, a fleet of accounts, a creator's 30-day plan. Also an end card. Wrong when the brand has no grid idea; then it is just confetti.

## How it works
One closed-form spring per tile, delayed by its diagonal index `r + c`:
```js
const tin = wave + (r + c) * .032
const s = sstep(t - tin, 2.3, .55)                     // f 2.3Hz, zeta .55: ~15% overshoot
e.style.transform = `scale(${s}) rotate(${(1 - s) * (c % 2 ? 18 : -18)}deg)`
```
Which cells are dim comes from a string map in CONFIG (`x` done, `.` dim), one row per `|`, so the pattern is art-directed, not random. Exit uses `(maxDiag - d)` so it leaves from the bottom-right.

## Numbers that matter
| | |
|---|---|
| Wave | starts .2s, .032s per diagonal (14 diagonals = .45s) |
| Tile spring | f 2.3 Hz, zeta .55, plus 18 degree twist that settles to 0 |
| Grid | 7 x 8, tile 74px, gap 12px, radius 17px at 1080 wide |
| Colours | #a6e05b, #b28cf6, #5fd38b, #f2735a; dim cells 22% |
| Wordmark | 104px heavy, letters .045s apart, .32s eo5 rise from 70% |

## Sound
A run of very short soft ticks (one per diagonal, rising in pitch) reads as the grid "filling"; the source sat it under the music's intro. See `keypress-ticks-under-counter__short-sine-tick-run` in motion-reel-kit. The demo is silent.

## Adapt it
- `bands` colours and the `done` map.
- `word` parts and `wordColors`.
- `cols`, `rows`, `tile` for a different grid (a 30-day calendar is 7 x 5).

## Files
- `code/demo.html` runs on its own; every value to change is in the `CONFIG` block at the top of the skill script.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "revid.ai Claude Opus 5.5 wall #31: HabitKit: a vertical app update" by @sebastianroehl (https://x.com/sebastianroehl/status/2103912457836323096), Video belongs to its creator; not included. Recreated by eye from watching the public video; this demo is original code and contains none of the video. Full notices: `THIRD_PARTY_NOTICES.md`.

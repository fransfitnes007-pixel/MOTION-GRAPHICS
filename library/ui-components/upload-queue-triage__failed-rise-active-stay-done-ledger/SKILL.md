---
name: upload-queue-triage-failed-rise-active-stay-done-ledger
description: A white file-upload card sorts seven files into groups as they go: the too-large one is red at the top, two uploads run with a third peeking behind them, finished ones drop into a green-ticked ledger, and the slow one fails at 62% and rises to the top with Retry. Use for file upload, upload list and upload queue beats in app promos.
---

# Upload queue triage

**Code name:** Failed rise, active stay, done ledger.

## What you see
Beige page, white card with a drop zone ("Drop files here or browse", "Up to 25.0 MB each") and a 2px overall progress line under it. The card rises in at 0.2s, files land at 1.0s: "interview-recording.mov" is red under NEEDS ATTENTION ("Too large — the limit is 25.0 MB", Remove); UPLOADING · 2 · 4 WAITING shows campus-wayfinding-v3.png and thesis-draft-v4.pdf with percentages, bars and Cancel, a pale next row and a thin edge peeking behind them, and "3 more waiting: survey-results.csv, budget-2026.xlsx, q3-roadmap.pdf" under. As files finish they slide into UPLOADED with a green tick (last three shown, "Show all", "Clear") and the next waiting file steps up. site-photos.zip is 18 MB and slow; at 62% it drops: its row turns red, jumps up into NEEDS ATTENTION with "Connection dropped at 62% — retry to resume" and Retry / Remove, the Uploading group disappears and "Retry all" shows. 10s loop; the source runs the whole queue in 2.7s, this is stretched 2.4x so it can be read.

## When to use it
Upload, import and sync screens; the "failed rises to the top" moment is the story. Also a good pattern for any list where status changes the order. At 9:16 it fills the width; leave it 6s or more.

## How it works
Three kinds of state are derived from time: each file has a list of [kind, from, to] stages (waiting, next, active, done, fail), progress tables read off the live run (campus 0, 17, 47, 67, 85, 100 % at .24/.42/.6/.66/.84 s, site-photos 0 to 62 % over 2.2s), and the layout is recomputed at each of six events (.42, .84, 1.02, 1.44, 2.6 s of model time). Between two events every row slides from its old slot to its new one with `cubic-bezier(.2,.8,.2,1)` (the source's `--us-ease`, ~0.38s on screen), cross-fading when a row changes kind. Concurrency is two, three finished rows show, the overall line is bytes done / bytes total.

## Numbers that matter
| | |
|---|---|
| Card | white, radius 18, padding 14, ring rgba(27,26,23,.09), 13.5px text, 34rem max width |
| Row | min 58px, radius 12, glyph 36px (radius 9, mono 10px label), name 500, meta 12px #77736b |
| Error ring | rgba(180,35,24,.45), text #b42318 |
| Next row | 46px high, #faf9f6, glyph 28px at 70%; edge strip 6px |
| Done row | compact: 7px 10px padding, tick #15803d |
| Bars | 3px, fill #1b1a17 |
| Group heading | 11.5px, 600, uppercase, 0.05em |

## Sound
Soft click when a file lands in the ledger, a low buzz on the failure.

## Adapt it
- `CONFIG.files` names, glyph labels, colours, sizes
- `LIFE` and `PROG` to re-order who finishes when
- `CONFIG.speed` (2.4) and `startAt`
- `failAt` and the limit text

## Files
- `code/demo.html` self-contained, loops, `?w=1080&h=1920` for 9:16 (a 540-wide phone column), `?w=1280&h=800` for wide.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "Upload Stack" by ham7a311 (https://21st.dev/@ham7a311/components/upload-stack), MIT. Recreated by eye from the public preview; this demo is original code. Full notices: `THIRD_PARTY_NOTICES.md`.

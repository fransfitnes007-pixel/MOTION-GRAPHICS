---
name: hook-ab-variants-query-param-hook-table
description: "A way to test several opening lines on one video: the hook is a small table keyed by a URL parameter, and the scene start shifts to fit that variant's voice line. Use it when you want three hooks of the same ad."
---

# Hook A/B variants

**Code name:** Query-param hook table.

## What you see
Three frames at once. A: "Every winter, the silence came back." with a report card. B: "Would you sleep in that room?" with a records card. C: "A National Landmark. And it hid a secret." in smaller type. Each hook holds until just before its voice line ends, so B hands over to "Here is the full story." slightly later than A, and C much later.

## When to use it
Paid social tests where the first 3 seconds decide the result. Everything after the hook is shared, so the variants cost almost nothing to produce.

## How it works
The hook is an object per variant, chosen from `?hook=`:

```js
const HOOK = ['B', 'C'].includes(Q.get('hook')) ? Q.get('hook') : 'A'
const HK = { A: { l1, l2, k, title, desc, t2: 1.25, tc: 2.85 }, B: {...}, C: {...} }[HOOK]
```
The schedule then reads that variant's narration length, so nothing overlaps or leaves a gap:

```js
const hk = '01_hook' + (HOOK === 'A' ? '' : HOOK)             // voice file: 01_hook, 01_hookB, 01_hookC
o.truth = Math.max(4.6, 0.35 + vd(hk) + 0.6)                   // next scene = voice end + 0.6, but never before 4.6s
if (HOOK !== 'A') { SCH.vo['01_hook' + HOOK] = SCH.vo['01_hook']; delete SCH.vo['01_hook'] }
```
A render queue can produce each variant by passing the parameter through the URL, for example `?w=1080&h=1920&hook=B`. A voice A/B works the same way (`&voice=` or the fifth argument). Hook timing fields `t2` and `tc` stagger line 2 and the card. Only the nine-second window around the hook changes; the rest of the video is shared. The demo draws all three variants at once, with the hook passed as an argument instead of a global.

## Numbers that matter
| | |
|---|---|
| Hook length | max(4.6s, 0.35 + voice + 0.6): A 4.6s, B 4.65s, C 6.11s (with the narration lengths in the demo) |
| Line 2 / card (A, B, C) | 1.25 / 2.85s, 1.05 / 2.6s, 1.9 / 3.1s |
| Type | A and B 128px; C 0.78x wide, 0.64x tall |
| Poster | frame at 3.6s |

## Sound
Each hook has its own narration file (`01_hook`, `01_hookB`, `01_hookC`); the demo is silent. Add your own narration.

## Adapt it
- Add variants as new keys in the table and new voice files.
- The shared minimum (4.6s) and pad (0.6s).
- Pass `&hook=D` through the job list.

## Files
- `code/demo.html` runs on its own and loops; `?w=1080&h=1920` gives the tall layout. Playfair Display (SIL Open Font License, from Google Fonts) is copied into `code/fonts/` because the serif headline is half the look. Small labels suit SF Pro Display; the demo uses the system font stack instead.
- `code/fonts/` holds the fonts the demo loads.

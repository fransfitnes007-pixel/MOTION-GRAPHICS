---
name: logo-marquee-counterscroll-big-number-opposing-translatex
description: "A 270px number counts up to 10,000+ in the middle while two rows of client logos run in opposite directions above and below it, with a small label fading in underneath. Scale: how many customers, teams, brands."
---

# Big number between two counter-scrolling logo rows

**Code name:** Opposing translateX.

## What you see
A 270px figure counts to 10,000+ between 0 and 1.1s in the middle of the frame, scaling down from 125 percent with a purple glow. A row of brand logos runs along the top edge and another along the bottom, moving in opposite directions at 420px per second. A smaller line of text fades in under the figure at 0.5s.

## When to use it
Scale: how many customers, teams, brands. The two logo rows say "and here are some of them" without a slide of logos. Needs recognisable logos to work; the demo uses placeholders.

## How it works
Two long rows, each the list twice so the loop is unbroken. Row A moves left from 0; row B starts at a negative offset and moves right.

```js
lineA.style.transform = `translateX(${-lt * 420}px)`
lineB.style.transform = `translateX(${-2600 + lt * 420}px)`
nBig.textContent = fmt(10000 * eo(seg(lt, 0, 1.1))) + '+'
```
For a continuous loop, the row offset must reach a whole repeat of the list, and the demo's 2.4s loop does not do this; for a real loop use `(-t * v) % rowWidth`.

v1 version: rows at 120px per second over 4.8s, the figure counts over 2s and has a longer label with a third stat.

## Numbers that matter
| | |
|---|---|
| Figure | 270px weight 800, scale 1.25 to 1 in 0.4s (`eo5`) |
| Rows | y 150 and 860, gap 110px, 56px tall logos, 90 percent opacity |
| Speed | 420px per second (v1: 120px per second) |
| Label | 44px weight 700, 80 percent white |

## Sound
Suggested bed: a synthesised 128 BPM groove in A minor (Am F C G): kick on every beat, claps on 2 and 4, open hats on the offbeats, sidechained bass. Impacts (a sine boom plus filtered noise crash) land on beats 12, 40, 48 and 60, and a band-passed noise whoosh peaks on each moving transition. The beat-48 impact lands on the figure's first frame.

## Adapt it
- Figure, label and logos.
- Row speed and rows direction.
- Number of rows, row y positions.
- Count window `1.1`.

## Files
- `code/demo.html` runs on its own with no network. Product screens, covers, logos and the wordmark are CSS placeholders.

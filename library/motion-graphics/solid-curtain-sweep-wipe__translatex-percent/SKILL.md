---
name: solid-curtain-sweep-wipe-translatex-percent
description: "A flat purple gradient panel sweeps left to right across the whole frame in 0.45 seconds, and the next page scales up from 92 percent behind it as the panel leaves. A transition between two screens that wants a graphic cue instead of a straight cut or a fade: a colour wipe on a beat."
---

# Solid colour curtain sweep

**Code name:** translateX percent sweep.

## What you see
A flat purple panel covers the full frame and slides from left to right off-screen in 0.45s. Behind it the sign-up page is hidden at first, appears at 0.2s at 92 percent, and scales up to full size by 0.7s.

## When to use it
A transition between two screens that wants a graphic cue instead of a straight cut or a fade: a colour wipe on a beat. Use the brand colour so it feels intentional.

## How it works
A full-frame div moved with `translateX` in percent, so the same code works at any resolution.

```js
const c = eio(seg(lt, 0, .45))
curtain.style.transform = `translateX(${lerp(-100, 100, c)}%)`
```
It starts fully off-screen left and ends fully off-screen right; the panel covers the frame only around the middle of the move, and that is when the page behind it switches on.

## Numbers that matter
| | |
|---|---|
| Sweep | 0.45s, `eio` |
| Panel | linear-gradient(90deg, #6D28D9, #8B5CF6) |
| Page | appears 0.2s, scale .92 to 1 over 0.5s (`eo`) |

## Sound
Suggested bed: a synthesised 128 BPM groove in A minor (Am F C G): kick on every beat, claps on 2 and 4, open hats on the offbeats, sidechained bass. Impacts (a sine boom plus filtered noise crash) land on beats 12, 40, 48 and 60, and a band-passed noise whoosh peaks on each moving transition. Each moving transition has the noise whoosh peaking 0.38s after it starts.

## Adapt it
- Panel colour or gradient.
- Direction (swap -100 and 100, or use translateY).
- Duration `.45`.

## Files
- `code/demo.html` runs on its own with no network. Product screens, covers, logos and the wordmark are CSS placeholders.

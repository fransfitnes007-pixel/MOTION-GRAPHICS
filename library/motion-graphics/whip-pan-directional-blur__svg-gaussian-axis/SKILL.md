---
name: whip-pan-directional-blur-svg-gaussian-axis
description: "Full-frame windows whip in and out: one flies up from below smeared vertically, exits sideways to the left smeared horizontally, and the next arrives from the right, each blur fading as the move settles. Fast cuts between screens on a beat, where a plain slide would look flat."
---

# Whip pan with directional motion blur

**Code name:** SVG gaussian blur on one axis.

## What you see
A full-frame window flies up from 1300px below in 0.35s, smeared vertically by a 40px blur that clears as it lands. It sits, then in the last 0.28s it flies off to the left with a 50px horizontal smear. The next window comes in from the right, 2200px away, with a 50px horizontal smear that clears in 0.32s.

## When to use it
Fast cuts between screens on a beat, where a plain slide would look flat. The one-axis blur sells the speed. Keep each travel under 0.4s.

## How it works
An SVG `feGaussianBlur` with `stdDeviation="x 0"` or `"0 y"` blurs only along one axis. Two filters live in the page; a helper picks one and sets its strength, and CSS `filter: url(#id)` applies it.

```js
function blur(elm, amt, axis) {
  if (amt < .5) { elm.style.filter = ''; return }
  if (axis === 'x') { mbx.setAttribute('stdDeviation', amt + ' 0'); elm.style.filter = 'url(#mbx)' }
  else { mby.setAttribute('stdDeviation', '0 ' + amt); elm.style.filter = 'url(#mby)' }
}
blur(an, (1 - inK) * 40 + out * 50, (1 - inK) > out ? 'y' : 'x')   // in from below, out to the left
```
Blur strength is proportional to distance left to travel, and the motion uses `eo5` (in) and `ei` (out).

## Numbers that matter
| | |
|---|---|
| In | 0.35s, `eo5`, translateY 1300px to 0, blur 40px to 0 |
| Out | last 0.28s, `ei`, translateX 0 to -2200px, blur to 50px |
| Next in | 0.32s, `eo5`, translateX 2200px to 0, blur 50px to 0 |
| Filter region | x -20 percent to 140 percent so the smear is not clipped |

## Sound
A band-passed noise whoosh suits each whip, with its peak on the cut (0.38s into a 0.55s swell). A synthesised 128 BPM groove in A minor under it works well; see the sound recipes in this library.

## Adapt it
- Distance and blur strengths.
- Directions (swap x and y).
- Durations.
- Both filters share one definition; add more for diagonal travel.

## Files
- `code/demo.html` runs on its own with no network. Product screens, covers, logos and the wordmark are CSS placeholders.

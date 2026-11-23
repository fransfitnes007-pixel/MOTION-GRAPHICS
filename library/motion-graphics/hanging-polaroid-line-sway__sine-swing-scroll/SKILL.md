---
name: hanging-polaroid-line-sway-sine-swing-scroll
description: "A row of polaroid prints hangs from a thin string across the top, slides in from the right and drifts left, each swinging on its own pivot, with a large headline blurring in below. Showing variety, a lot of examples of one kind of thing (topics, categories, use cases)."
---

# Hanging polaroid line

**Code name:** Sine swing scroll.

## What you see
A thin string runs across the top. Polaroid prints with a photo and a caption hang from it, sliding in from the right over 1.2s and then drifting left at 160px per second. Each print swings on a pivot just above its top edge: a 4 degree swing that dies away over 5s plus a constant 2 degree wobble, each print on its own phase and with its own fixed crooked angle. "Every niche." blurs in below at 2.2s.

## When to use it
Showing variety, a lot of examples of one kind of thing (topics, categories, use cases). The hanging motion is tactile and slow, so it fits a calm beat rather than a fast one.

## How it works
Pivot is set with `transform-origin: 50% -40px`, so a rotation swings the print from the string. Position is a linear scroll plus an `eo` slide-in; rotation is a sum of two sines per print, and prints off-screen are hidden.

```js
const x = 80 + i * 250 + (-lt * 160) + 600 * (1 - eo(seg(lt, 0, 1.2)))
const swing = Math.sin(lt * 2.2 + i) * 4 * (1 - seg(lt, 0, 5)) + Math.sin(lt * 1.3 + i * 2) * 2
S(d, { left: x + 'px', top: (262 + Math.sin(i) * 6) + 'px', transform: `rotate(${swing + (rand(i) - .5) * 8}deg)`, display: x > -300 && x < 2000 ? '' : 'none' })
```

## Numbers that matter
| | |
|---|---|
| Print | 210px wide, 12px border, 44px caption strip, #f5f2ea, radius 6px |
| Pitch | 250px apart |
| Scroll | 160px per second |
| Swing | 4 degrees decaying over 5s, plus 2 degrees constant |
| String | 2px, rgba(255,255,255,.35), y 250 |

## Sound
A suitable soundtrack has a pink-noise whoosh (high-passed at 600 Hz, low-passed at 5.2 kHz, 0.7s long, volume .22) peaking on every scene cut, over a low A-minor drone pad that ducks under the narration. 

## Adapt it
- Photos and captions.
- Pitch and scroll speed.
- Paper colour for a different mood.
- Title.

## Files
- `code/demo.html` runs on its own with no network. Screens, covers, logos and the wordmark are CSS placeholders.

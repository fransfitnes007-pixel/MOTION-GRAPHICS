---
name: dark-ember-title-beat-word-reveal-inline-card
description: "A near-black screen with an orange and pink glow rising from the bottom edge, a small white sentence that arrives word by word, then a bigger line with a tiny post card sitting in it that drops away. Reach for it as the bad-news beat in a problem and solution video."
---

# Dark ember title beat

**Code name:** Word reveal with inline card.

## What you see
After a bright first scene the video cuts to a near-black frame. Along the bottom a hot orange glow comes in from the left and a pink one from the right, blurred together into a band. At 4.06s a small white sentence builds in the middle one word at a time: "And", "just", "like", "that ...". A white arrow cursor drifts from left to right underneath it on a small wave. At 5.34s the sentence is replaced by a bigger line, "You lose it", whose last word is a 96px post card with a white ring around it. The card springs in, holds, then at 5.73s falls 500px, shrinks to 40% and turns 40 degrees as it fades. At 5.96s it cuts to white.

## When to use it
The moment where something is lost, goes wrong or ends, between two bright scenes. The dark break makes it land. It is wrong for a positive beat, and it only works where the neighbouring scenes are light. The glow gives it a warm, urgent tone, not a cold one.

## How it works
The background is three gradients stacked: two radial gradients anchored at the bottom corners (one orange at 10% x, one pink at 95% x, each fading to transparent by 55 to 60%) over a vertical dark gradient from `#0e0a12` to `#2a0f23`.

```css
radial-gradient(120% 90% at 10% 100%, #ff6a3d 0%, rgba(255,106,61,0) 55%),
radial-gradient(110% 90% at 95% 100%, #ff2e97 0%, rgba(255,46,151,0) 60%),
linear-gradient(180deg,#0e0a12 0%,#2a0f23 100%)
```
The words come from the word-by-word sentence reveal (see that skill): one flex row, each word its own span with its own start time. The card is an element placed inside the row like a word, so spacing stays natural. After its own reveal the card gets an extra transform: `drop = ei(seg(t, WT.in - .25, WT.in + .05))` drives `translateY(drop * 500px)`, scale `* (1 - drop * .6)`, rotate `drop * 40deg` and fades it out. The cursor path is `x = lerp(-300, 200, g)` and `y = 70 + 50 * sin(g * 6)` from the centre, with `g = eio(seg(t, and, that + .3))`.

## Numbers that matter
| | |
|---|---|
| First line | 58px, weight 500, white; words at 4.06, 4.16, 4.44, 4.68 |
| Second line | 96px, weight 600; words at 5.34, 5.46, 5.74 (card), with a spring over .5s |
| Card | 96px wide, ring `0 0 0 3px #fff, 0 0 0 6px rgba(255,255,255,.35)`, radius 10px |
| Card exit | `ei` over .3s starting .25s before the next voice word |
| Glow | orange `#ff6a3d`, pink `#ff2e97`, base `#0e0a12` to `#2a0f23` |

## Sound
A whoosh on the cut in (about 0.18s early) and a soft pop on each word. The music drops to plucks only. Leave the voice alone: this beat is about the sentence.

## Adapt it
- The two lines of copy and what the inline card is (a card, an icon, a product thumb).
- The glow colours, or one colour for a calmer beat.
- The word times, which come from your voice track.
- The scene length: it is 2s here.

## Files
- `code/demo.html` runs on its own. The card photo is a gradient placeholder.

---
name: reel-post-card-heart-comment-rail
description: "A 9:16 short-video post card with a dark fade at the bottom, a handle and caption bottom left, a column of heart, comment, save and share counts down the right edge, and a big red heart popping beside it. Reach for it whenever a video needs to show a social post."
---

# Reel-style post card

**Code name:** Heart and comment rail.

## What you see
A tall 9:16 card with 28px rounded corners and a soft drop shadow sits on a light stage. The photo fills it, fading to near black over the bottom 55%. Bottom left: a bold handle with a smaller caption under it. Down the right edge: a heart, a comment bubble, a bookmark and a share arrow, each with a count under it. At 1.26s a red heart springs in on the card's right edge and stays for 0.78s.

## When to use it
Any time the video has to say "a post": a short video, a social feed, a review queue. It is a base card for burst, feed-scroll and strip scenes. It is wrong for landscape video, and the rail icons are too small to read below about 260px card width.

## How it works
One function builds the card from a width. Everything inside is sized in `em` from `font-size = width * .085`, so the same card works at 96px (the tiny inline card) and at 470px.

```js
S(e, { width: px(w), height: px(w * 16 / 9), fontSize: px(w * .085) })
```
The bottom fade is a `linear-gradient(180deg, transparent 45%, rgba(0,0,0,.72))` layer. The rail is a flex column with the icons as inline SVG. The big heart is a separate 150px element: `spring(.5s, 7, 12)` drives both scale (`h * 1.1`) and opacity (`clamp(h * 2)`), placed at `card centre + (.34 * width, .15 * height)`.

In the demo the photo is a gradient with a head and shoulders. A real build would use a video frame.

## Numbers that matter
| | |
|---|---|
| Card width | 470px wide layout, `W * .62` tall layout |
| Radius, shadow | 28px, `0 40px 90px -30px rgba(0,0,0,.55)` |
| Rail | right 4.5%, bottom 5%, gap .55em, counts at .62em |
| Handle | left 5.5%, bottom 5%, bold, caption .78em |
| Big heart | `#ff3056`, 150px, spring k7 f12 over .5s, shows .78s |
| Entrance (review card) | spring k7 f11 over .5s, scale .8 to 1 |

## Sound
Suggested sound: a short high pop (1500Hz, a tenth of a second) when the heart lands.

## Adapt it
- Replace the gradient with a video frame or image in `phDiv`.
- The handle, caption and the four counts.
- Heart colour and position, or swap the heart for another reaction.
- Card width: everything else follows.

## Files
- `code/demo.html` runs on its own. The photo is a placeholder gradient.

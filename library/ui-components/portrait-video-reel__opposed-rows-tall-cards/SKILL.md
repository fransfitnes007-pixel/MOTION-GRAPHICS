---
name: portrait-video-reel-opposed-rows-tall-cards
description: "Two rows of 9:16 video cards in thin glass frames scrolling in opposite directions, each with a niche pill, a creator name and a bottom shade, edges faded, hover lifts one card and pauses the row. Use for a wall of vertical short-form videos."
---

# Portrait video reel

**Code name:** Opposed rows, tall cards.

## What you see
Two lines of phone-shaped cards, 210px wide, 16px apart. The top line scrolls left and the bottom one scrolls right. Every card is a glass frame (1px edge at 10% white, 4% white fill, 25.6px radius, 6px padding) around a 9:16 video with a 19.2px radius. On the video: a dark pill at the top left with the niche, the creator's name at the bottom left, and a black-to-clear shade 80px tall along the bottom. Hovering a card lifts it 4px, turns its border blue, shows a round play button at the top right, and pauses that whole row. Clicking opens the video in a sheet with sound. Edges fade into the page over 112px.

## When to use it
A wall of creator or customer clips under a headline, where vertical video is the product. Wrong for landscape footage, and for fewer than seven clips: the source switches to a still swipeable strip below that, so a card is never shown twice.

## How it works
The same duplicated-track trick as a logo strip, done in CSS: the list is rendered twice and `@keyframes ticker` moves it from `translateX(0)` to `translateX(-50%)`. The second row adds `animation-direction: reverse`. Duration is `line.length * 7` seconds. `.reel-row:hover .reel-track { animation-play-state: paused }` freezes the row under the pointer.

```css
@keyframes ticker { 0% { transform: translateX(0) } 100% { transform: translateX(-50%) } }
.reel-track { animation: ticker 120s linear infinite; }      /* inline animationDuration overrides 120s */
.reel-track.reel-reverse { animation-direction: reverse; }
.reel-row:hover .reel-track { animation-play-state: paused; }
```
Each real card also attaches its video `src` only when an IntersectionObserver says it is about to be on screen and removes it 600px after it leaves, so a visit downloads only what was seen. The demo draws gradient placeholders with a silhouette instead of video, runs one half-width per 8s loop, and pauses row 1 from 2.5s to 5s to show the hover. The 1s lift and border colour change are drawn from a .3s ease-in-out.

## Numbers that matter
| | |
|---|---|
| Card | 168px on phones, 210px from 640px up, aspect 9:16 inside, gap 16px |
| Frame | radius `1.6rem`, padding 6px, border `ink/10`, fill `ink/[0.04]` |
| Video | radius `1.2rem`, bottom shade `h-20 from-black/70` |
| Pill | 11px semibold white, `bg-black/40`, `border-ink/20`, blur on the real one |
| Hover | `-translate-y-1`, border `rv-purple/40`, play button fades in, row pauses |
| Speed | `line.length * 7`s per half-width, rows split by odd and even index |

## Sound
Silent in the strip. A card opens with sound on click.

## Adapt it
- Seconds per card (7) for faster or slower rows.
- Card width and radius.
- Row split: one row for under 14 clips (`rows={1}`).
- Pill content: niche, view count, or platform.

Sibling: `video-card-marquee__counter-scrolling-rows` is the same wall of tall cards with a spring-up player sheet; this one uses glass frames and is driven by CSS keyframes with pause on hover.

## Files
- `code/demo.html` runs on its own and loops in 8s.

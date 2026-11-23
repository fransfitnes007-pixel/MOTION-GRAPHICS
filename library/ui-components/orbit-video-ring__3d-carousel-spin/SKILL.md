---
name: orbit-video-ring-3d-carousel-spin
description: "A dark hero with a huge name and, behind it, ten vertical video cards standing on a circle that turns slowly in 3D with the cards facing outward. Reach for it as a bold video-first hero where the clips are the proof."
---

# Orbit video ring

**Code name:** 3D carousel spin.

## What you see
A black page with a violet glow in the middle. A small uppercase tagline, then the name at 152px, bold with tight tracking. Below it, ten 170px portrait cards stand around an invisible ring, each rotated to face outward, so you see about four of them at once: the front ones large, the ones at the sides narrowing and foreshortened, the back ones hidden. Every card has a niche chip, a white play button and a result line. The ring turns steadily to the left. A positioning line and two buttons close the hero. The demo turns the ring in 8 seconds so one loop is one turn; the live ring takes 48.

## When to use it
A dark, video-first personal or agency hero with at least 6 clips. It gives the impression of a large body of work behind a single name. Wrong for fewer than 6 clips (the ring gets sparse), light pages, and anything that has to be read, because the cards keep moving.

## How it works
Pure CSS. The stage has `perspective: 1400px`. The ring is a zero-size box at its centre with `transform-style: preserve-3d` and one animation:

```css
@keyframes orbit-spin { from { transform: rotateX(-10deg) rotateY(0deg); } to { transform: rotateX(-10deg) rotateY(360deg); } }
.orbit-ring { animation: orbit-spin 48s linear infinite; transform-style: preserve-3d; }
.orbit-stage:hover .orbit-ring { animation-play-state: paused; }
```

Each card sits at `rotateY(360 / n * i deg) translateZ(radius px)` with `backface-visibility: hidden`, so cards on the far side are not drawn. The radius grows with the count so cards never overlap: `radius = max(260, round(190 / (2 * sin(PI / n))))`, since the chord between neighbours is `2R sin(PI/n)` and a card is about 170px wide. Reduced motion drops the animation and holds the ring at `rotateX(-10deg)`. The name and tagline use `motion` entrances that only move on y (8 and 14px), never opacity, so the hero text is visible even if JavaScript is slow.

## Numbers that matter
| | |
|---|---|
| Name | 152px at lg (9.5rem), bold, line-height .9, tracking -.04em |
| Stage | perspective 1400px, 480px high (380 on phones) |
| Ring | rotateX(-10deg), rotateY 0 to 360 in 48s, linear, paused on hover |
| Cards | 170px wide (130 on phones), 9:16, rounded-3xl, shadow 0 30px 60px -30px rgba(0,0,0,.7) |
| Radius | max(260, 190 / (2 sin(PI / n))): 307px for 10 cards |
| Glow | radial ellipse accent at 35% over ink |

## Sound
Silent. Pair it with a soft UI tick on the state change if it sits in a video.

## Adapt it
- The clips and their count (the radius recalculates); keep `n` at 8 to 12.
- Turn time: 48s is calm, 24s is lively.
- Tilt (-10deg) for a flatter or steeper ring.
- Accent colour of the glow.

## Files
- `code/demo.html` runs on its own and loops. The cards are gradient placeholders with invented view counts; the name is a placeholder. The ring runs 6x faster than live so one loop is one turn.

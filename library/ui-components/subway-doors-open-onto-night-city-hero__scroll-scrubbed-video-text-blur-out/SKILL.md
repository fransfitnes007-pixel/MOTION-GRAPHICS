---
name: subway-doors-open-onto-night-city-hero-scroll-scrubbed-video-text-blur-out
description: "A full-bleed hero whose video is tied to the scroll position: a title over closed subway doors blurs out, the doors open on a night city, and a second line fades in; scrolling back rewinds it. Reach for it for cinematic scroll storytelling."
---

# Subway doors opening onto a night city, scroll hero

**Code name:** Scroll-scrubbed video, title blurs out.

## What you see
The page opens on a full-screen frame of a rain-streaked subway car: two door leaves with arched windows in the middle, side windows and blue seats at the edges, a "SCROLL" label with a thin line at the bottom centre and a small credit bottom right. "THE CITY OPENS" sits across the doors in 62px bold white.

As the page scrolls, the film advances. Over the first 16% of progress the title blurs, grows 6% and fades out. From 6% to 42% the doors slide apart by their own width, revealing warm station light that fades into a night skyline (towers with lit windows, neon signs in orange, cyan and pink, a road with white and red light trails running toward you). From 40% to 88% the camera moves forward: the car interior scales up 2.5x and fades out while the city settles. From 72% a second line, "Every door in the city is already open.", fades in over the city at 18px. A thin white bar along the bottom edge tracks progress. Scrolling back reverses everything.

The demo scripts the scroll: rest 1s, scroll to the end over 4.8s, rest 2s, scroll back over 3.2s. The real piece plays a video (a pre-rendered film of this scene); here the film is replaced by a CSS and SVG painting.

## When to use it
A cinematic landing page or story where one object or place opens up as the visitor scrolls, and the text is minimal. It needs a good pre-rendered video or image sequence; the effect is only as good as the footage. The page is pinned for the length of the scroll, so keep the film short.

## How it works
The key idea is that nothing is time-based: one number, scroll progress `p` from 0 to 1, drives video time and text. In the original `video.currentTime = p * duration` is set from the scroll position of a sticky, locked section (the usage example only renders <MetroHero />, so the exact wiring is not shown). In the demo each layer maps `p` to its own band using `eio(seg(p, a, b))`:
```js
open  = eio(seg(p, .06, .42));   doorL.x = -open * 300;  doorR.x = open * 300
car   = scale(1 + 1.5 * eio(seg(p, .4, .88)));  car.opacity = 1 - eo(seg(p, .78, .92))
title = { opacity: 1 - eo(seg(p, 0, .16)), blur: (1 - opacity) * 14 }
line  = eo(seg(p, .72, .84))
```
`CONFIG.scroll` is the scripted scroll curve as `[second, progress]` pairs. In production, swap this for the real scroll position and a `<video>` with `currentTime`, preferring a video encoded with frequent keyframes so scrubbing is smooth.

Simplified from the original: the real component scrubs a rendered film of a subway car and a city, which is not reproducible here. This demo paints a flat CSS and SVG version of the same sequence (doors, warm light, skyline, traffic) and scripts the scroll position.

## Numbers that matter
| | |
|---|---|
| Canvas | 1280 x 800 |
| Title | 62px bold, tracking -1.5px, blur up to 14px |
| Doors | 300px each, open between progress .06 and .42 |
| Camera push | scale 1 to 2.5 between .40 and .88 |
| Second line | 18px, from .72 |
| Scripted scroll | 1.0s, 5.8s, 7.8s, 11.0s keyframes, 12s loop |

## Sound
Silent.

## Adapt it
- `CONFIG.title`, `line`, `credit` and `scrollLabel` for your copy.
- Replace `city` and `car` with a `<video>` and drive `currentTime` from scroll; keep the title and line rules.
- `CONFIG.titleFadeBy` and `lineFrom` for where the text changes.
- `CONFIG.scroll` to change the pacing of the scripted scroll.

## Files
- `code/demo.html` runs on its own and loops. Placeholder art is CSS and SVG only.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Scroll-Locked Video Hero" by gughigug on 21st.dev (https://21st.dev/@gughigug/components/scroll-locked-video-hero), MIT. This demo is an original recreation written from the public preview.

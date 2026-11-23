---
name: site-inside-site-scroll-dive-exponential-zoom-wrap
description: A landing-page section where the page contains a smaller copy of itself in a browser window, and scrolling zooms into that window level after level on a path that wraps, so it never ends. Reach for it for a "this site contains itself" scroll moment, a product that embeds itself, or a recursive hero.
---

# Site inside site scroll dive

**Code name:** Exponential zoom that wraps every level.

## What you see
A cream page (`#fcfbf7`). At the top, a small blue monospace label ("loop 00"), a 62px headline ("This site contains itself."), a grey sub line, and a red gradient "Get early access" button, 192 by 52. Lower down, from y 570, is a white-edged window 586 by 372 with a long soft shadow. Inside it is the same page drawn smaller, and inside that another window, and so on. "scroll" in spaced mono sits under the window and a counter "0:00 / 3" sits bottom right.

As the page scrolls, the camera zooms into the window. The browser bar (three traffic lights and a "yoursite.com ×1" pill) fades in as the dive starts and is not shown while the page sits at the top. The headline changes per level: "This site contains itself.", "You are inside the site now.", "Deeper. Still the same site.", "It loops forever." with sub lines "Same page, one level down.", "Only the scale changed." and "Scroll back up to climb out." Below the section is a beige strip reading "out of the loop".

The clip is 9.5s: about 0.6s idle, three levels of dive until about 3.9s, the beige strip scrolled into view at about 5s, then it scrolls back up through the levels. The demo follows the same timeline.

## When to use it
A landing page for something that can show itself: a website builder, a screen-recording tool, an embeddable widget. It makes one point very well, "it contains itself", and works as a one-off section. It costs a lot of scroll length, so use it once, and give mobile a plain fallback.

## How it works
The page is built as nested copies of itself. Each window holds the page scaled by `s = windowHeight / pageHeight` (372 / 1014 = 0.367), centred in the window. The camera is one transform: scale by `(1/s)^q` where `q` is the fractional part of how many levels you have dived, around a fixed point so that at `q = 1` the first window exactly fills the screen.

```js
const s = 372 / 1014, k = 1 / s
const zoomOrigin = [k * (346 + offX) / (k - 1), k * 570 / (k - 1)]   // about (640, 900)
root.style.transform = `scale(${(1 / s) ** q})`     // q = p - floor(p)
```

At `q = 1` the picture equals `q = 0` one level later, so the demo only changes the text: level `n = floor(p) + depth` shows copy `n % 4`, and the loop counter and URL number follow. Five nested levels are built, which is enough for one scale step. The browser bar's opacity is `q / 0.3`, so it is hidden at the top of each step and the wrap shows no pop. The original is driven by scroll position; the demo drives `p` from time. It is described on the page as one transform driven by scroll on an exponential zoom path.

## Numbers that matter
| | |
|---|---|
| Page | 1280 x 1014 design, cream `#fcfbf7` |
| Eyebrow | 16px mono, `#5b4bf0`, letter-spacing .1em, y 142 |
| Headline | 62px / 500, `#16130f`, y 205 |
| Sub | 20px `#5a574f`, y 272 |
| Button | 192 x 52, 9px radius, `#d4361b` to `#bd2a12` |
| First window | x 346, y 570, 586 x 372, shadow 0 22px 60px rgba(60,45,20,.16) |
| Nested scale | 0.367 per level |
| Browser bar | 22px high at level 0, lights 6px, URL pill 190 x 14 |
| Exit strip | 405px, `#f3efe6`, mono 13px "out of the loop" |
| Demo timeline | dive 0.6s to 3.9s, hold, strip 4.3s to 5.9s, climb back 5.9s to 8.3s |

## Sound
Silent.

## Adapt it
- `CONFIG.levels`: headline and sub line per level (any count; the loop repeats them).
- `button`, `url`, `exitText` and the colours in the CSS.
- `dive` keyframes: how fast each level passes.
- `win`: size and position of the first window; the zoom origin is derived from it.

## Files
- `code/demo.html` runs on its own and loops. It is a recreation made from watching the video and reading the usage example.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Scroll Loop Inception" by serafimcloud on 21st.dev (https://21st.dev/@serafimcloud/components/scroll-loop-inception), MIT. This demo is an original recreation written from the public preview.

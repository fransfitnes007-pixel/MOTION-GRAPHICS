---
name: phone-beside-browser-synced-screens-rise-in-crossfade-rise
description: "A phone frame rises in at the corner of a browser window and shows the mobile version of whatever section the browser is on, each new screen fading up from 46px below the last. Reach for it to show a responsive site or app as desktop and phone at once."
---

# Phone beside browser with synced screens

**Code name:** Rise-in phone, crossfading screens.

## What you see
A browser window sits to the right of centre. At 8.35s a black phone (rounded body, camera island, 2px lighter inner edge) rises 120px into the browser's lower right corner while fading in over 0.7s. Its screen shows the mobile version of the page. Each time the browser jumps to a new section, the phone's new screen fades in from 46px below over 0.42s on top of the old one, so the phone and the browser always show the same section.

## When to use it
Showing that a site or app works on both desktop and phone, or any "same thing, two devices" beat. Needs a browser and a phone image per section, so it suits a section tour of 4 to 6 stops. Wrong for a single static screen: just show the phone alone.

## How it works
The phone is a 458 x 960 box: a dark rounded body, an inner screen inset 14px, and a pill-shaped island. It is scaled as a whole (250px wide on a 1920 frame). All screens are stacked inside the screen, and each frame decides which is current. The current screen fades and rises in over a short window after the section starts (0.18s to 0.6s), the previous one stays fully visible underneath until it is covered, and every other one is hidden. Nothing ever cross-fades out.

```js
phImgs.forEach((im, j) => {
  if (j === si) { const k = j === 0 ? 1 : eo(p(t, SEC_T[j] + 0.18, SEC_T[j] + 0.6)); im.style.opacity = k; im.style.transform = `translateY(${(1 - k) * 46}px)`; im.style.zIndex = 2 }
  else if (j === si - 1) { im.style.opacity = 1; im.style.transform = 'none'; im.style.zIndex = 1 }
  else { im.style.opacity = 0; im.style.zIndex = 0 }
})
```

A real build uses mobile screenshots (430 x 932). The demo draws four stand-in screens and the browser uses the same scroll as the page-scroll skill (this demo scrolls without blur).

## Numbers that matter
| | |
|---|---|
| Phone | 458 x 960 body, radius 76px; screen 430 x 932 at inset 14px, radius 62px; island 126 x 36 |
| Phone size and place | 250px wide at (1616, 414) on 1920 x 1080; 410px wide at (610, 1010) on 1080 x 1920 |
| Rise in | 8.35s to 9.05s, ease-out-cubic, 120px up and fade |
| Screen change | starts 0.18s after the section start, 0.42s, 46px rise |
| Browser beside it | 1130px wide at (700, 150) on wide, 980px at (50, 500) on tall |

## Sound
Silent.

## Adapt it
- Your phone screens in place of `shapes`, and their count.
- Section start times `ST`.
- Phone size and corner (`L.ph`) and body colour (`#phbody`).
- The rise (`120`) and the screen rise (`46`) for more or less movement.

## Files
- `code/demo.html` runs on its own (8s loop).

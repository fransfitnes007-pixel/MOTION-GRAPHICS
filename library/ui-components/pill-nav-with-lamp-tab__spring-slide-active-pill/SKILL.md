---
name: pill-nav-with-lamp-tab-spring-slide-active-pill
description: A floating pill nav (Home, About, Projects, Resume) with a sliding grey active background and a small black lamp tab with a soft shadow glow on top. Use it as a header menu on a light page.
---

# Pill nav with lamp tab

**Code name:** Spring slide active pill.

## What you see
A white pill bar, 800px wide in the demo, with a thin light border and a faint shadow, centred on a white page. Four labels in grey: Home, About, Projects, Resume. The active one is bold black on a light grey rounded pill, and above it a short black tab about 58px wide sits on the bar's top edge with a blurred grey glow just below it, so it looks like a lamp shining down. A cursor clicks About at about 1.0s, Projects at 2.3s, Resume at 3.4s and Home at 4.5s. Each click slides the grey pill and the lamp across to the new tab over about 0.55s with a small overshoot, resizing the pill to fit the label, while the label weights and colours swap. The cursor becomes a hand over the bar.

## When to use it
A floating header menu on a marketing site or a portfolio, with a few top-level links. Works on a light page; the dark-bar version of the same idea is the spotlight icon nav. Wrong with more than about six labels; the equal tab widths run out of room.

## How it works
One fractional tab position drives the grey pill and the lamp. Between click times it interpolates left and width between the old and new tab rectangles with `spring(k=7.5, f=9)`, so it overshoots a little. The original gets the same slide from a framer-motion `layoutId` element shared between tabs, and shows icons instead of text on mobile. Tabs share the bar width equally; the pill is the label width plus 72px, centred on its tab.

```js
x = lerp(rect[a].x, rect[b].x, spring(seg(t,tClick,tClick+.55),7.5,9))
w = lerp(rect[a].w, rect[b].w, same)
lamp.left = x + w/2 - 29;  glow = blurred radial gradient under it
```

Labels are measured once at bold weight so the layout does not jump when the active one turns bold.

## Numbers that matter
| | |
|---|---|
| Bar | 800x90, white, 1px `#e9e9ec`, soft shadow |
| Pill | 70px tall, `#e8e8e8`, label plus 72px wide |
| Lamp | 58x10 `#141414`, glow 116x38 radial gradient at 38% black, blurred 4px |
| Labels | 27px, idle `#606064`, active bold `#0c0c0c` |
| Motion | spring k 7.5, f 9, .55s; clicks at 1.0, 2.3, 3.4, 4.5s; loop 5.6s |

## Sound
Silent.

## Adapt it
- `items`: the labels (the original also takes an icon per item).
- `bar` size and font size in the CSS.
- `lampW`, `lampH`, and the glow gradient for a stronger or softer lamp.
- `spring`: raise f for more wobble; set `clicks` or bind the position to your router.

## Files
- `code/demo.html` runs on its own and loops. Everything is read from the `CONFIG` object at the top of the script.
- `media/poster.jpg` is one frame of it.

## Credit
Idea: "Tubelight Navbar" by ayushmxxn on 21st.dev (https://21st.dev/@ayushmxxn/components/tubelight-navbar), MIT. This demo is an original recreation written from the public preview.

---
name: notification-card-stack-staggered-spring-rise
description: "Two white app-notification cards rise one after the other from below, each tilting a few degrees as it settles, with overlapping round avatars on the right. Reach for it for 'new matches', 'ready for review' and similar alerts."
---

# Notification card stack

**Code name:** Staggered spring rise with tilt.

## What you see
A white card with a 1em radius and a deep soft shadow rises 120px from below while growing from 80% to 100% and turning 3 degrees anticlockwise. It holds an app icon (a dark rounded square), a bold title, a smaller grey line, and on the right a row of round avatars that overlap by half their width with a white ring. A second card does the same 0.45s later, 140px lower, turning 2.5 degrees clockwise and with two avatars. They overlap slightly, so together they read as a loose pile of two alerts.

## When to use it
To show that the product sends you something: "24 items matched", "6 files ready". Two or three cards in a stack is enough; more reads as a list. It is wrong for a single big announcement. The same card is also used as an inline word in a sentence (see the word-by-word skill).

## How it works
Each card has one spring and uses it for four things:

```js
const n = spring(seg(t, t0, t0 + .6), 7, 11)
card.style.top = y + (1 - n) * 120 + 'px'                     // rises 120px
card.style.transform = `translate(-50%,-50%) rotate(${-3 * n}deg) scale(${.8 + .2 * n})`
card.style.opacity = clamp(n * 2)
```
The second card uses the same code with `+3`, `2.5` instead of `-3` (tilting the other way) and a later start. The avatar row is a flex container whose children have `margin-left: -.55em`. Font size on the card (34px, 30px on tall) sets everything else in `em`.

If the two cards are made before the dashboard window, so the window paints on top and hides them for their whole 0.8s, and only the sentence's inline card shows. This demo draws them in front. To avoid that, create the cards after whatever else is on screen, or give them `z-index`.

## Numbers that matter
| | |
|---|---|
| Spring | k7 f11 over .6s, second card .45s later |
| Rise | 120px, scale .8 to 1, tilt -3 and +2.5 degrees |
| Card | font 34px (30 tall), radius 1em, padding .55em .9em .55em .6em, icon 2.4em square |
| Avatars | 1.9em, 2px white ring, overlap -.55em |
| Shadow | `0 30px 70px -25px rgba(0,0,0,.45)` plus a hairline ring |

## Sound
Suggested sound: pops (1250Hz, 0.11s) at the card times, with a mid-level pop later for any follow-up chips.

## Adapt it
- Title, body text and icon.
- Number and position of cards; add a third with a `+.45s` offset each.
- Tilt directions and angles.
- Avatars (photos or initials).

## Files
- `code/demo.html` runs on its own. Icon and avatars are placeholders.

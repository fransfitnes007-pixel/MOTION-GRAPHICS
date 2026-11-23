---
name: phone-mockup-spring-rise-tilt-rotate-translate-spring
description: "A phone mockup entering with a springy lift and a small tilt, with a pill chip labelling it. Use it for single-screen mobile moments."
---

# Phone mockup spring rise with tilt

**Code name:** Spring translate and rotate from below.

## What you see
A headline, "A links page for your bio.", sits on the left. A phone, 340 by 734, starts 200px low and tilted 8 degrees, and in 0.7s rises and swings through upright to rest leaning 3 degrees the other way, overshooting a little on the spring. At the end of the headline a pill chip with a gradient app icon and a short link pops in below the headline from 70% size. The whole group is pushed in from the right and out to the left by the strip animation.

## When to use it
Any single phone screen: a mobile view, a link page, a form, a notification. The lean makes the phone feel placed on a table instead of pasted. Use the same move for every phone in a video so they feel like one set.

## How it works
One spring and two linear mappings of it:

```js
const pp = spring(seg(t, .05, .75), 7, 11)
phone.transform = `translateY(${(1 - pp) * 200}px) rotate(${(1 - pp) * 8 - 3}deg)`     // pp = 1 gives 0px and -3deg
chip: spring(seg(t, BIO - .1, BIO + .4), 8, 12) -> scale(.7 + .3 * iq), opacity clamp(iq * 1.5)
```

The final angle is baked into the formula (the `-3`), so the resting pose and the entry share one expression; the spring's overshoot swings the angle past the final lean and back. For other phones, flip the sign (`-6 - 3`) for phones on the left. The phone itself is a rounded rect with an inner bezel and a black island, 2.16 times its width tall.

## Numbers that matter
- Phone 340 wide (190 to 340 also works), height width times 2.16, radius 52px, bezel 10px, island 34% by 28px.
- Spring: k=7, f=11 over 0.7s; lift 200px; angle 8 degrees at start, -3 at rest.
- Chip: 25px bold, radius full, `rgba(18,18,30,.92)`, spring(k=8, f=12).

## Sound

## Adapt it
- The phone screen; use a screenshot.
- Lift (200px), tilt start (8 degrees) and rest (-3 degrees); flip signs for the other side.
- The chip text and icon.
- Phone width.

## Files
- `code/demo.html` runs on its own and loops. The phone screen is a CSS placeholder. The demo uses the system font stack.

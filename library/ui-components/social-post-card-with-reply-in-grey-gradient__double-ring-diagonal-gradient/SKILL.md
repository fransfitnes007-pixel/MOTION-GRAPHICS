---
name: social-post-card-with-reply-in-grey-gradient-double-ring-diagonal-gradient
description: "A static social post card: author avatar, bold name with a blue verified tick, handle, X logo top right, a few lines of post text, a date, a hairline divider and a reply row, on a grey diagonal gradient with a bevelled white outer ring. Reach for it for testimonials and social proof."
---

# Social post card with reply, grey gradient

**Code name:** Double ring, diagonal gradient.

## What you see
A card 764 by 471 (960 by 720 frame) with 22px corners on a diagonal gradient from `#d9d9d9` at the top left to `#f1f1f1` at the bottom right. Around it, 10px out, a white translucent ring with 30px corners and a soft shadow (about 40px blur, 16% black), so the card looks like a glass tile set in a frame. Inside: a 64px round avatar, the name in 26px bold with a blue verified tick, the handle in 22px, an X logo at the right edge; 26px post text in four lines with 38px line height; the date in 22px; a hairline at 14% black; then a smaller avatar with 'name tick @handle · date' and the reply text at 22px. In the 1.7s preview nothing on the card moves; only the pointer passes over it. The demo adds a 0.5s fade-up at the start of each loop so the loop has a start, and keeps the scripted pointer.

## When to use it
A testimonial wall, a 'what people say' strip, or any place a real post should be quoted as proof. A static card is easy to stack in a grid or a marquee. Replace the copy and images with a real post; do not use invented quotes as if they were real.

## How it works
Two nested rounded boxes. The outer one is a translucent white ring with a hairline border and a drop shadow. The inner one carries the `linear-gradient(135deg, light grey, lighter grey)` plus an inset top highlight (`inset 0 1px 0 rgba(255,255,255,.6)`) and an inset bottom shade, which together give the slightly raised bevel. Text is plain absolutely placed rows in the demo; the real component renders the same layout from props (author, content lines, timestamp, an optional reply). The names, handles, avatars and copy in the demo are placeholders.

## Numbers that matter
- Outer ring 784 by 490, radius 52px; inner card 764 by 471, radius 22px
- Gradient 135 degrees `#d9d9d9` to `#f1f1f1`
- Avatars 64px; name 26px bold; body 26px / 38px; meta 22px
- Divider 1px, 14% black; verified tick `#4da3ff`
- Shadow: 40px blur, 16% black, 18px down

## Sound
Silent.

## Adapt it
- `author`, `lines`, `date`, `reply` for the post content.
- `gradient` and `outer` for a different surface or a dark card.
- `radius` for rounder or squarer corners.
- `enter` to change or remove the fade-up (set to 0).

## Files
- `code/demo.html` runs on its own, loops in 5s, and has a `CONFIG` block at the top of the script.

## Credit
Idea: "X Gradient Card" by kokonutd on 21st.dev (https://21st.dev/@kokonutd/components/x-gradient-card), MIT. This demo is an original recreation written from the public preview.

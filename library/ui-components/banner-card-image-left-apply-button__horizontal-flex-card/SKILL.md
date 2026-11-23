---
name: banner-card-image-left-apply-button-horizontal-flex-card
description: A wide dark banner card with a rounded square image, headline, two lines of text, a small stats line, a white pill button and a close X. Reach for it for dismissible announcements and sign-up prompts.
---

# Banner card, image left, Apply button

**Code name:** Horizontal flex card.

## What you see
A card up to 720px wide (#18181a, 30px outer radius, 12px padding) holds a 120px square image with 18px corners on the left. Beside it: the title `Become an ACME Creator!`, grey two-line text, then a footer row with `Only 10 spots` over `Submission ends Oct 10.` and a white `Apply Now` pill (36px, fully rounded). A 28px round close button sits at the top right. The clip is still.

The demo uses a mint tile with two drawn cherries in place of the photo. It fades the card in, hovers Apply Now (button darkens to `#e4e4e7`, shrinks 4%), then hovers and clicks the X: the card scales down 6% and fades over 0.35s, stays gone for a beat and returns.

## When to use it
A dismissible banner at the top of a dashboard or a promo row in a feed. It stacks vertically on narrow screens, with the image on top at 140px high.

## How it works
Plain flexbox: image `flex:none`, content column `flex:1` with `justify-content:space-between` so the footer sits at the bottom whatever the text length. The close button is absolutely positioned at the top right.

```css
.card { display:flex; gap:12px; padding:12px; border-radius:30px; }
.main { flex:1; display:flex; flex-direction:column; justify-content:space-between; }
```

The photo in the original is scaled 125% inside its rounded box (`scale-125 object-cover`), which crops in on the subject.

## Numbers that matter
| | |
|---|---|
| Card | 720px max, 30px radius, 12px padding |
| Image | 120px square, 18px radius |
| Button | 36px tall, 16px side padding, white on dark |
| Dismiss | scale to 94% and fade, 0.35s |
| Loop | 7.5s |

## Sound
Silent.

## Adapt it
- `CONFIG.title`, `body`, `stat`, `note`, `button` for the words.
- `CONFIG.buttonBg` and `buttonText` for the button colours.
- `CONFIG.imageBg` for the placeholder tile, or drop a real `<img>` in the `.img` box.

## Files
- `code/demo.html` runs on its own and loops; every frame is `render(t)`. Edit the `CONFIG` block at the top of its script.
- `media/poster.jpg` is the page's preview image.

## Credit
Idea: "Card" by hero_ui on 21st.dev (https://21st.dev/@hero_ui/components/heroui-card/horizontal), MIT. This demo is an original recreation written from the public preview.

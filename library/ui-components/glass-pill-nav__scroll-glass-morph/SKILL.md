---
name: glass-pill-nav-scroll-glass-morph
description: "A floating rounded-full header that is transparent at the top of the page and turns into a frosted glass pill once you scroll 12px, with a glass dropdown menu on phones. Reach for it on any light page with soft background colour behind it."
---

# Glass pill nav

**Code name:** Scroll glass morph.

## What you see
Scene one: a 56px-high pill with a logo mark and name on the left, ten text links in the middle and a black "Work with me" button on the right. At the top of the page it has no background at all. As the page scrolls past 12px the pill fades into white glass over .3s, with a blur and a hairline border, and page content slides up under it. One link gets a white/70 hover chip. Scene two, on a phone: the pill holds the logo and a hamburger. Tapping it turns the burger into an X, the pill goes glass, and a rounded glass panel drops in underneath (opacity 0 to 1, y -8 to 0) listing the links with a full-width black button at the bottom.

## When to use it
Marketing sites with a pastel or photo background where a solid bar would feel heavy. The effect needs content scrolling underneath to read as glass. Wrong over a busy photo with no overlay, or for apps that need a persistent toolbar.

## How it works
One boolean, `scrolled`, set from a passive scroll listener (`scrollY > 12`). The class swap is the whole effect, softened by `transition-all duration-300`:

```tsx
<div className={cn("container-x flex h-14 items-center justify-between rounded-full px-4 transition-all duration-300 sm:px-5",
  scrolled || open ? "glass-strong" : "bg-transparent")}>
```

`glass-strong` is `bg-white/75 backdrop-blur-2xl border border-white/80` plus a soft shadow. On mobile the open state also forces the glass, so the pill matches the panel under it. The panel is an `AnimatePresence` child with `initial={{opacity:0,y:-8}} animate={{opacity:1,y:0} exit={{opacity:0,y:-8}}` and no explicit transition, so framer uses its defaults (a spring on y, a short tween on opacity). The demo approximates that with a spring of stiffness 500 and damping 25 and a .3s ease-out on opacity.

## Numbers that matter
| | |
|---|---|
| Pill | h-14 (56px), rounded-full, horizontal padding 16 to 20px, sits 12 to 16px from the top edge |
| Glass | white/75, blur 40px (`backdrop-blur-2xl`), border white/80 |
| Threshold | scrollY above 12px |
| Fade | 300ms, Tailwind default ease (.4, 0, .2, 1) |
| Links | text-sm, px-3 py-1.5, hover bg white/70 |
| Mobile panel | glass-strong, rounded-3xl, 8px padding, rows rounded-2xl px-4 py-3 text-base |

## Sound
Silent. Pair it with a soft UI tick on the state change if it sits in a video.

## Adapt it
- The 12px scroll threshold.
- The glass recipe: opacity of the white and the blur radius.
- The link list and the primary button.
- Use `rounded-3xl` instead of `rounded-full` if the pill grows taller than about 64px.

## Files
- `code/demo.html` runs on its own and loops. Photos and logos are CSS placeholders; copy is placeholder text.

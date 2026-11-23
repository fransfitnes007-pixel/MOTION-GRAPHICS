---
name: onboarding-dialog-step-pager-dot-pagination-next-skip
description: A centred white onboarding modal with a dark hero picture, a title and two lines of text, four dots and Skip and Next buttons. Reach for it for a short first-run tour in a popup.
---

# Onboarding dialog step pager

**Code name:** Dot pagination with Next and Skip.

## What you see
A plain page with one outlined button, "Onboarding". A pointer clicks it and a white rounded dialog (740 px wide in the demo) fades in over a page dimmed to about 83% black. Inside: a dark gradient hero picture with a grey ring in the middle and an X at its top right, a bold title, two lines of grey text, and a footer with four small dots on the left and "Skip" (ghost) and "Next" (black, arrow icon) on the right.

The pointer clicks Next twice. Each click swaps the title and text at once, with no transition, and moves the dark dot one place right while the other three sit at 20% opacity. On the last step the button reads "Okay" and loses its arrow. The pointer then clicks the X and the dialog fades out.

## When to use it
A first-run tour of three or four screens where you do not want to leave the current page, or a "what's new" popup. Skip must always close it. It is wrong when each step needs a form, since the content swap has no transition and no back button.

## How it works
One piece of state, `step`, from 1 to the number of steps. The text comes from an array indexed by step, the dots are `[...Array(total)]` with `opacity-20` on every dot except the current one, and Next either increments the step or, on the last step, becomes a `DialogClose` button. Reopening the dialog resets `step` to 1 (`onOpenChange`). The hero is a picture in an 8px-padded slot above the text, and the footer stacks to a column below the `sm` breakpoint with the dots under the buttons.

```js
const step = Math.min(nextClicksSoFar, steps.length - 1)
dots.forEach((d, i) => d.style.opacity = i === step ? 1 : .2)
nextLabel.textContent = step === last ? 'Okay' : 'Next'
```

The arrow on Next nudges 2px right on hover (`group-hover:translate-x-0.5`). The demo draws a cursor that clicks each button with a small press dip, since the real hover and click cannot run in a render.

## Numbers that matter
| | |
|---|---|
| Dialog | 740 by 747 in the demo box, 18px radius, white |
| Overlay | black at about 83%, page below is white |
| Hero | 707 by 399, 13px radius, `#1d1d20` to `#3b3b44` |
| Title / text | 27px semibold, 21px grey `#737373` on 37px lines |
| Dots | 11px, 22px apart, inactive at 20% opacity |
| Buttons | Next 152 by 67, black `#171717`, white text, arrow at 70% |
| Demo timing | trigger click 0.9s, Next clicks 2.0s and 2.8s, X click 4.0s, loop 5.4s |

## Sound
Silent.

## Adapt it
- `steps`: titles and body text, any number of them (the dots follow).
- `heroTop` and `heroBottom`, or put a real image in `hero`.
- `accent` for the Next button and active dot.
- `clickTrigger`, `nextClicks`, `clickClose` to retime the scripted pointer.

## Files
- `code/demo.html` runs on its own and loops. All imagery is CSS or SVG placeholder.
- `media/poster.jpg` is a preview image showing the component.

## Credit
Idea: "Dialog" by originui on 21st.dev (https://21st.dev/@originui/components/dialog/onboardin-dialog), MIT. This demo is an original recreation written from the public preview.

---
name: danger-confirm-dialog-over-red-gradient-blur-backdrop-alert-dialog-custom-backdrop
description: "A destructive-action confirm: a white 394 px dialog with a pink warning icon, centred heading, grey explanation, a red \"Delete Forever\" pill and a blue \"Keep Account\" pill, over a page that is blurred and washed from grey at the top to deep red at the bottom. Reach for it for deleting an account, workspace or project."
---

# Danger confirm dialog over a red gradient backdrop

**Code name:** Alert dialog with a custom gradient blur backdrop.

## What you see
White page with one red pill button, "Delete Account". When it is clicked, in about 0.25s the whole page gets a blurred overlay (4 px) that is black at 50% across the top and shifts into a dark red toward the bottom (`#4a1414` at the edge), and a white dialog (394 by 300 in the demo, 30 px radius) fades and scales in from 94%.

Inside the dialog, centred: a 40 px pink circle with a red warning triangle, the heading "Permanently delete your account?" in 18 px semibold, four lines of 14.5 px grey text, then two 34 px full-width pills stacked 8 px apart: the red "Delete Forever" on top and the blue "Keep Account" below. A small grey round X sits at the top right. The preview video holds the closed page for about 1.8s and then opens the dialog, so the dialog moment is the last 0.4s of the clip; the demo adds a close through "Keep Account" and loops.

## When to use it
Irreversible actions where you want the screen to feel heavy: deleting an account, wiping data, cancelling a subscription. The red wash tells people the stakes before they read. It is too loud for routine confirmations. The safe choice is the lower, blue button, and "Delete Forever" is the one that sits on top.

## How it works
The usage example puts the colour entirely in a class on `AlertDialog.Backdrop` with `variant="blur"`:

```tsx
className="bg-linear-to-t from-red-950/90 via-red-950/50 to-transparent dark:from-red-950/95 dark:via-red-950/60"
```

`bg-linear-to-t` runs from the bottom up, so the strongest red is at the bottom edge. The demo keeps that gradient over a flat 50% black dim:

```js
background: linear-gradient(to top, rgba(69,10,10,.9), rgba(69,10,10,.5) 50%, rgba(69,10,10,0)), rgba(0,0,0,.5)
backdrop-filter: blur(4px)
```

The dialog uses the compound parts `AlertDialog.Dialog` (`sm:max-w-[420px]`), `CloseTrigger`, `Header` (centred), `Icon status="danger"`, `Heading`, `Body` and `Footer` with `flex-col-reverse`, which is why "Keep Account" is written first in the code but shown second. Both buttons use `slot="close"` so either closes the dialog. The demo's open and close times are read from the video and the pointer clicks are scripted.

## Numbers that matter
| | |
|---|---|
| Backdrop | black 50% base, red `69,10,10` at 90% at the bottom, 50% at the middle, 0 at the top, blur 4px |
| Dialog | 394 by 300, 30px radius, shadow `0 20px 60px rgba(0,0,0,.35)` |
| Icon | 40px circle `#fde1e1`, triangle `#b42318` |
| Heading / body | 18px semibold, 14.5px `#6e6e73` on 18.8px lines |
| Buttons | 350 by 34, pills, red `#ff3b3b`, blue `#0a84ff`, 8px apart |
| Open and close | 0.25s fade, dialog scale .94 to 1 |
| Demo timing | open click 0.8s, close click 3.7s, loop 5.4s |

## Sound
Silent.

## Adapt it
- `trigger`, `heading`, `body`, `confirm`, `cancel` for the copy.
- `backdropRGB`, `baseDim`, `blur` for the wash: a dark blue gives a calm confirm, black a plain modal.
- `danger` and `accent` for the button colours.
- `openAt`, `closeAt`, `fade` to retime it.

## Files
- `code/demo.html` runs on its own and loops. All imagery is CSS or SVG placeholder.
- `media/poster.jpg` is a preview image showing the component.

## Credit
Idea: "HeroUI AlertDialog" by hero_ui on 21st.dev (https://21st.dev/@hero_ui/components/heroui-alert-dialog/custom-backdrop), MIT. This demo is an original recreation written from the public preview.

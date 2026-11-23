---
name: setup-wizard-chip-stepper-live-preview-theme
description: "A seven-step setup wizard: a row of pill chips shows where you are (done steps get a check, future steps are faded), one glass card holds the current form, and a live mini-preview of the finished site beside it changes as you type and as you pick a palette. Reach for it for any onboarding where people fill in a form to get a site, profile or page."
---

# Setup wizard with chip stepper

**Code name:** Live preview theme.

## What you see
A floating glass pill at the top with a logo and product name. Below, two columns. Left: seven chips (Your account, About you, Your look, Contact and socials, Your numbers, Your videos, Web address); finished ones carry a check, the current one is solid black, later ones are at 60% opacity. Under them a big glass card reads "STEP 2 OF 7" and "About you" over a grid of inputs, with Back and Continue buttons at the foot. Right: a "Preview" label over a small copy of the finished hero. As the name, title and one-liner are typed, the preview text changes with them. Continue moves to "Your look", where picking the Sunset palette recolours the preview instantly; Continue again for contact details, then the numbers step, where two stats typed in appear as floating tiles over the preview photo.

## When to use it
Any onboarding that ends in something visual: sites, profiles, storefronts. The live preview is what makes seven steps feel short. Wrong for a two-field sign-up, or where the thing being built has no useful miniature.

## How it works
State is one `draft` object saved after each change (so a refresh keeps your place) with a `step` number. Chips are `ol > li > button.chip` with `chip-active` for the current step, a check icon instead of the step icon for earlier steps, and `opacity-60` for later ones; only earlier chips are clickable. The card is `glass-strong rounded-4xl p-5 sm:p-8` and each step is a block rendered by `step.key`. There is no step transition: the block swaps instantly, which keeps typing responsive.

The preview is the point. `buildContent(draft)` turns the answers into the same content object the real site reads, and `MiniPreview` draws a small static hero from it, styled with the draft's theme colours (`ink`, `accent`, `mist` and three blob colours become CSS variables through `ThemeStyle`):

```tsx
<aside className="hidden lg:block"><div className="sticky top-24">
  <p className="mb-2 text-xs font-semibold uppercase tracking-wider text-ink-3">Preview</p>
  <MiniPreview content={preview!} theme={draft.theme} />
```

The layout picker and palette grid both write `draft.theme`, so the preview and the final site cannot drift apart. Palette tiles show three swatches (ink, accent, mist) and the name. The demo types text on a timer and redraws the preview from the same fields.

## Numbers that matter
| | |
|---|---|
| Chip | min-h 38px, rounded-full, 12px medium, border ink/10, fill white/60; active = black; done = check icon |
| Card | `glass-strong`, rounded-4xl, 32px padding |
| Inputs | rounded-2xl, border ink/10, fill white/70, 14px; focus ring accent/40 |
| Labels | 12px semibold uppercase tracking-wider ink-3 |
| Layout | grid `1fr` and `.8fr` at lg, gap 24px, preview column sticky at top-24 |
| Preview | rounded-3xl, three radial blob gradients from the theme, hero text, two buttons, 4:5 photo, up to two floating stat tiles |
| Steps | account, about, look, contact, numbers, videos, address |
| Persistence | draft saved after each edit |

## Sound
Silent. Pair it with a soft UI tick on the state change if it sits in a video.

## Adapt it
- The step list (`STEPS`) and the fields in each block.
- What the preview draws: swap `ClassicPreview` for a thumbnail of your own output.
- Palette presets: any set of ink, accent, mist and three blob colours.
- Make later chips clickable by removing the `i < draft.step` guard.

## Files
- `code/demo.html` runs on its own and loops. Names, emails and figures are placeholders; the palettes are invented. The excerpt is the real, complete wizard.

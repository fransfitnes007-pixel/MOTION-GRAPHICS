---
name: icon-in-context-scenes__chips-tab-bar-notification-9x16
description: Three ready-to-record 9:16 compositions that put the animated icons to work - lock-screen notification bubbles, label chips that land one by one, and an app tab bar whose active icon plays. Use it when a short app-promo needs icons shown in a believable screen, not on a grid.
---

# Icon in context scenes

**Code name:** Chips, tab bar, notification bubbles at 9:16.

## What you see
12 s, three scenes of 4 s each, on a dark purple-glow 9:16 canvas (1080 x 1920).

**0 to 4 s, notification bubbles.** A lock screen: big clock "9:41", date, a round bell button top right with a red count badge. Three rounded glass banners drop in from above with a spring, at 0.6 s, 1.4 s and 2.2 s: a pink heart tile ("Aria liked your video"), a blue message tile ("New message from Jay"), a green dollar tile ("Payout sent"). Each tile's icon starts playing 0.2 s after its banner lands. The bell swings again every time a banner arrives and the badge pops to 1, 2, 3. The scene lifts and fades at 3.55 to 4 s.

**4 to 8 s, label chips.** Headline "Everything in one app". Five rows of pill chips spring up from below, 0.22 s apart per row and 0.1 s apart within a row: Likes, Share, Growth, Payouts, Creators, Fast, Schedule, Verified, AI captions. Each chip has a tinted round icon well and its icon plays 0.12 s after the chip lands (heart beats, send plane flies with a trail, trend line draws, tick draws in the calendar and shield, sparkles blink).

**8 to 12 s, tab bar.** A placeholder feed (three cards with grey lines) and a floating glass tab bar that springs up from the bottom with Home, Search, Create, Inbox, Me. A purple pill springs from tab to tab at 8.5, 9.25, 10.0, 10.75 and 11.4 s; the arriving tab's icon and label turn white and the icon plays its own motion (home door draws, search lens circles, plus spins half a turn, message bubble tilts, user figure draws). The screen title above changes with each tab. At 11.7 to 12 s it fades, and 0 s fades the lock screen back in, so the clip loops.

Wide render (1280 x 800): the same 9:16 canvas as a centred phone-shaped frame with rounded corners and a soft backdrop, so the tall clip and the wide clip are the same composition.

## When to use it
- Showing a notification, a like, a payout, a feature list or the app's nav inside a short vertical video: render a tall clip of `code/demo.html` at 1080x1920, or use one scene's block as an overlay.
- The chips scene is a ready feature-list beat; swap the labels in `CONFIG.chips`.
- Not for a grid of many icons (use the kits) or a spinner.

## How it works
Everything is laid out in a 1080 x 1920 box, then scaled: `SC = W / 1080` when tall, `SC = H * .93 / 1920` in a centred frame when wide. Every frame is `render(t)`:

1. Scene blocks A, B, C are shown by time windows and faded with `seg()` ramps; entries use the library spring `1 - e^(-7x) cos(11x)`.
2. Each icon is registered with `icon(parent, name, size, colour, start)` where `start(t)` returns how many seconds the icon has been playing (negative before). `render` seeks all of its CSS animations with `a.currentTime = max(0, start(t)) * 1000`. Rest state is the first frame of the loop, so an icon that has not started is the plain icon.
3. The bell's `start` is "time since the most recent banner", so it replays on each arrival with no timers.
4. The tab pill uses `spring(x, 9, 12)` between slot centres; icon and label colour use a hex mix on the "active" ramp.

```js
for (const a of svg.getAnimations({ subtree: true })) { a.pause(); a.currentTime = ms }   // same t, same frame
```

## Numbers that matter
| | |
|---|---|
| Canvas | 1080 x 1920, scaled; DUR 12 s, 30 fps clips |
| Banner | 960 x 210, radius 56, tile 140 x 140 radius 38, icon 80 px, glass blur 20 |
| Banner entry | spring(7, 11) over 0.7 s, y from -140 px, scale 0.9 to 1 |
| Chip | height 150, radius 75, icon well 102 px, icon 60 px, label 50 px bold; spring over 0.6 s, y from 90 px |
| Tab bar | 960 x 210 at y 1590, radius 105; slots 192 px; icon 76 px; pill 170 x 166 |
| Pill move | spring(9, 12) over 0.5 s; tabs at 8.5, 9.25, 10.0, 10.75, 11.4 s |
| Icons used | bell, heart, message-circle, dollar-sign, send, trending-up, wallet, users, zap, calendar-check, shield-check, sparkles, home, search, plus, user |
| Colours | bg #0c0e16, card #181b28, accent #7c6cff, tiles pink #ff6b93, blue #6aa5ff, green #3fe39a, amber #ffc857 |

## Sound
Silent. Pair with a soft notification ping per banner, a pop per chip, a tick per tab switch.

## Adapt it
- Copy: `CONFIG.banners` (icon, colours, title, body, arrival second), `CONFIG.headline`, `CONFIG.chips`, `CONFIG.tabs`, `CONFIG.clock`, `CONFIG.date`.
- Icons: any name that exists in `ICONS` (16 are embedded; paste another from `code/svg/` of the kit plus its CSS to add more).
- Timing: `at` values and `CONFIG.scenes`; DUR stays 12 unless you change the scene windows.
- Brand colours: `CONFIG.bg`, `accent`, and the tile gradients.
- Only one scene: set `CONFIG.scenes` windows so the others never show, and lower DUR.

## Files
- `code/demo.html` all three scenes; `CONFIG` at the top.
- `code/svg/*.svg` the 16 standalone auto-playing icons used here.
- `media/poster.jpg` one frame. Render a clip with `node engine/tools/render_demo.cjs video <demo.html> out.mp4 1080 1920` (tall) or `1920 1080` (wide).

## Credit
Idea: "Lucide Animated (icon motion reused from the kit)" by pqoqubbw (shown as dmytro on 21st.dev) (https://21st.dev/community/icons), MIT. "Lucide" by Lucide Contributors (https://lucide.dev/), ISC. Original scenes built with these icons. Full notices: `THIRD_PARTY_NOTICES.md`.

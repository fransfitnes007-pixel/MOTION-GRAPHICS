---
name: day-in-the-life-app-subscriptions-creator-tools-low-poly-3d-parked-car-word-timed-captions
description: Part thirty of the low-poly "day in the life of a UGC creator" reels. In his parked car on a rooftop deck, a creator pays for four apps to make one video (a teleprompter, a hashtag app, a script writer, a pitch writer). His bank sends four renewal emails in a row; the apps made more from his video than he did, and his seat drops flat. Then YourBrand: the tools are already in it (scripts, hashtags, pitch templates), in the same menu as his campaigns. He cancels three apps. He still pays for the teleprompter: he can't find the cancel button. Reach for it when a reel needs the subscription-stack story, a car interior, a rooftop parking deck, a phone in a dash mount with stacking banners, a seat that reclines flat, or phone sheets for a subscriptions list, renewal emails, a tools page, an app sidebar or an account page with no cancel button.
---

# Day in the life, part thirty: the cancel button (low-poly 3D)

**Code name:** three.js rooftop parking deck (lines, parapets, a lamp post, parked cars, a skyline), a box-built hatchback with the driver door swung open, a slanted windshield, dashboard, steering wheel and a dash-mounted phone, a seat back that reclines, box-built creator in a backwards red cap and a denim jacket, floating phone sheets, hard cuts on voiceover word times. **From:** original build, part 30 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-app-subscriptions-creator-tools__low-poly-3d-parked-car-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 37.5 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 4.6s.** An overcast rooftop parking deck; a man films himself in his car. "Part thirty." 1 VIDEO.
2. **4.6 to 10.2s.** Subscriptions: Teleprompter Pro, TagBoost, ScriptBot, PitchPal, one per word, each Active with a monthly price. "4 apps for 1 video" (APPS: 4).
3. **10.2 to 15.2s.** The dash-mounted phone (BANK: 4 EMAILS), then the inbox: four "Your subscription renewed" mails, each stamped RENEWED (RENEWED ×1 to ×4).
4. **15.2 to 17.7s.** "The apps made more from my video than I did": his seat drops flat. APPS: PAID · ME: NOT.
5. **17.7 to 19.3s.** He sits up; the chrome monogram; the sky turns blue.
6. **19.3 to 24.8s.** YourBrand Tools, CREATOR TOOLS: UGC Script Generator, Hashtag Research, Brand Pitch Templates (each lights on its word), Content Style Guide (ALREADY IN IT). The menu: Home, Getting started, Find deals, My campaigns, Content, Earnings, Analytics, My profile, Tools (SAME MENU).
7. **24.8 to 26.3s.** Subscriptions again: TagBoost, ScriptBot and PitchPal struck through, Cancelled. Teleprompter Pro still Active. CANCELLED: 3.
8. **26.3 to 29.0s.** Out of the car, he swats away a credit card (✕ SUBSCRIPTIONS) and a renew arrow (✕ RENEWALS), then crosses his arms: "No bullshit."
9. **29.0 to 32.5s.** Back at the wheel, pointing at the phone (STILL PAYING: 1). Teleprompter Pro's account page: Active, a huge "Upgrade to Pro+", Restore purchases, Rate us, Invite a friend, Help center, no cancel. "Cancel: not found" (CANCEL: ???).
10. **32.5 to 37.5s.** Black end card: chrome monogram, wordmark, "The tools are in it. Next to your campaigns.", yourbrand.com.

## How it works
Same structure as parts one to twenty nine. New here:

- **The car** is built round the usual desk spot: the driver's hips sit at the old desk position, the steering wheel and dashboard stand where the desk was, the roof clears his cap. The driver door (`doorL`) is hinged open so the side camera can see him recline.
- **Recline:** `seatBack.rotation.x` and the `FLAT` pose follow `recline`, which drops on "did" and comes back up on the YourBrand reveal.
- **The dash phone** (`drawMount`) stacks a "Renewed" banner for each renewal beat.
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice B (men) (see `_engine/VOICES.md`), take 1 of 2 (raw 37.1 s), sped 1.1x (the floor), so the voice runs 33.4 s and the reel 37.5 s. `code/recipe.py` lays faint city traffic under everything, a pop and a small cash chime per subscription, a vibration for the bank, a stamp, chime and buzz per renewal, a falling slide and thud for the seat, the reveal chord, pops as the tools light up, a ding for the menu, three falling blips for the cancellations, swats, a chime for the teleprompter and a low tone for "cancel: not found". No music. The mux uses the limiter. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.

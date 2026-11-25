---
name: day-in-the-life-scam-dms-hello-dear-invitations-low-poly-3d-lake-dock-word-timed-captions
description: Part twenty four of the low-poly "day in the life of a UGC creator" reels. On a lake dock at dawn, a "brand" slides into his DMs: hello dear, be our ambassador, just pay the shipping. Another sends the brief, and it is a .exe. Another sends a cheque that is too big and wants the difference back. The fourth is a prince. Every message arrives dangling from a fishing line. Then YourBrand: invitations land in one place, he reads the deal before he says yes, signs right there or declines, and there is a real team he can message. The prince still writes; he is doing well. Reach for it when a reel needs the fake-brand-deal story, a DM thread building up, a document swinging on a hook, an overpayment cheque, a tab bar with a count, sign and decline buttons, or a lake set.
---

# Day in the life, part twenty four: hello dear (low-poly 3D)

**Code name:** three.js lake at dawn (dock, far shore of pines and mountains, reeds, rowboat, a duck crossing, a rod and bobber), box-built character in a yellow sou'wester, scam DM / brief email / cheque / prince / My Campaigns invitations / agreement with Sign and Decline / ticket chat on a floating sheet that hangs from a fishing line, hard cuts on voiceover word times. **From:** original build, part 24 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-scam-dms-hello-dear-invitations__low-poly-3d-lake-dock-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 38.3 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 3.6s.** A lake in grey mist: a wooden dock, pines and mountains on the far shore, a rod propped over the water, a lantern still lit. A man in a yellow sou'wester works at a camp table. "Part twenty four."
2. **3.6 to 9.4s.** A sheet is reeled up on a fishing line, swinging: a DM from brand_official_real_1 (0 followers · joined today). "Hello dear" · "We want YOU as our AMBASSADOR!!!" · "FREE products. Just pay shipping:" · a yellow PAY $49.99 button. “FREE”: $49.99.
3. **9.4 to 10.9s.** Another catch: Inbox, "YOUR BRIEF IS ATTACHED!! Open it right away", attachment brief_FINAL.pdf.
4. **10.9 to 12.3s.** He recoils, hands up: brief_FINAL.pdf.exe · DO NOT OPEN.
5. **12.3 to 15.7s.** In the mail: a pale green cheque made out to "You" for $4,500.00 (agreed fee: $500), then a yellow note: "Oops, sent too much! Just wire back the $4,000 :)".
6. **15.7 to 17.6s.** HRH The Prince (verified, by himself): "Greetings. I am a prince." · "I seek one UGC creator." · "And your bank details." A PRINCE.
7. **17.6 to 19.4s.** The chrome monogram; the sun comes up gold over the water.
8. **19.4 to 21.5s.** My Campaigns: the Invitations tab (1) lights up and a card lands: Sunny Soda, INVITATION, "You have been invited. Two steps to join." ONE PLACE.
9. **21.5 to 25.4s.** The agreement: What you make, How long, What it pays (three rows, no figures); "Read ✓"; "Sign the agreement" is pressed and turns into "Signed ✓"; then the Decline button pulses. MY CALL.
10. **25.4 to 27.6s.** Tickets: "Quick question before I sign." · YourBrand team: "Sure. Ask away." · "Take your time." A REAL TEAM.
11. **27.6 to 31.2s.** He swats away a "Hello dear" speech bubble and a file marked .EXE: ✕ HELLO DEAR, ✕ .EXE. Arms crossed: "No bullshit."
12. **31.2 to 33.3s.** Callback, on the hook again: "Greetings again, my friend." · "The kingdom is well." · "Still need the bank details." BANK DETAILS SENT: 0.
13. **33.3 to 38.3s.** Black end card: chrome monogram, wordmark, "Real invitations. One place.", yourbrand.com.

## How it works
Same structure as parts one to twenty three. New here:

- **`showDoc(t0, hooked)`** has a second entrance. With `hooked` the sheet is not scaled in: it rises from below the frame on a `back` ease, swings as a pendulum that settles over about a second, and `hookG` (a nine-unit line, a hook and a red bead, children of the sheet) is shown. YourBrand's pages use the normal pop with no hook.
- **`bub(x, X, Y, w, lines, font, k, opts)`** draws a chat bubble of one or more lines and returns its height; the DM, the prince and the ticket are built from it.
- **The cheque** is drawn on the canvas with a slight tilt; the amount box turns red on "too big" and an "agreed fee" chip appears beside it.
- **The lake:** one water box, a dock box with a drawn plank texture and posts, a far bank with 46 cones for pines, three mountains with caps, a duck that crosses the frame over the whole reel (`duck.position.x = -9 + t * 0.42`), a bobber and a rowboat that bob. The mood flip takes the sky from mist to gold and switches the lantern off.
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice B (men) (see `_engine/VOICES.md`), sped 1.1x (raw 38.1 s; the rule gave 1.03, raised to the 1.1 floor), take 1 of 2. "D Ms" and "dot E X E" are spaced so they are spelled out. `code/recipe.py` lays slow water against the dock under the story, a plop and a reel ratchet each time a message is pulled up, a tacky jingle for "AMBASSADOR", buzzers on the shipping fee, the .exe (with three alarm beeps), the cheque and the difference, a tiny fanfare for the prince (twice), then a click and a ding for the Invitations tab, pops for the agreement rows, a click and two dings for Sign, a click and one low tone for Decline. No music. The mux uses the limiter. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.

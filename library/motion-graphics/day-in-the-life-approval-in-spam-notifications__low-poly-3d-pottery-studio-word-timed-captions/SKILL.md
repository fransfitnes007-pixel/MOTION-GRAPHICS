---
name: day-in-the-life-approval-in-spam-notifications-low-poly-3d-pottery-studio-word-timed-captions
description: Part twenty seven of the low-poly "day in the life of a UGC creator" reels. In a pottery studio, a creator sends her draft at nine and waits for one word. She checks email, socials, message requests (a man selling sunglasses) and the brand's group chat (two hundred people saying thanks); every time she checks, the pot on her wheel falls in. At four she finds it in the spam folder: approved at 9:15, post by noon. Face in the clay. Then YourBrand: the draft goes in the app, a notification in the app when it is approved, and a chat message. Her hands stay on the clay. The pot is done, her phone buzzes, she jumps: it's an ashtray now. Reach for it when a reel needs the scattered-inboxes story, a pottery wheel, a pot that collapses or squashes, a wall clock that spins forward, clay fingerprints on a phone screen, a notification bell and its menu, a chat DM card or a phone lock-screen banner.
---

# Day in the life, part twenty seven: an ashtray now (low-poly 3D)

**Code name:** three.js pottery studio (plaster walls, shelves of bisque and glazed pots, a kiln, a wedging table, a window, a wall clock, a tripod camera), box-built character with curly hair, a rust bandana, gold hoops and a sage smock, a pottery wheel with a lathe-built pot that collapses / grows into a vase / squashes into an ashtray, a phone in her hand and a phone on the bench with a lock-screen canvas, floating sheets for mail / socials / message requests / group chat / spam / YourBrand content / the notification bell / a chat DM, hard cuts on voiceover word times. **From:** original build, part 27 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-approval-in-spam-notifications__low-poly-3d-pottery-studio-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 42.2 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 3.2s.** A pottery studio on a flat grey day. A woman throws a pot on her wheel. "Part twenty seven."
2. **3.2 to 4.5s.** The pot on the wheel: POTTERY CHANNEL.
3. **4.5 to 6.0s.** The wall clock ticks to 9:00. DRAFT SENT.
4. **6.0 to 7.5s.** She picks up her phone with clay hands: WAITING FOR: APPROVED.
5. **7.5 to 15.1s.** Her phone: Mail, "No new mail". socials, "No new messages". Message requests: sunnyshades.4u (0 followers), "hey gorgeous", SUNGLASSES 90% OFF!!! DM ME. The brand's group chat (200 members) filling with "thanks!!", "ty", "thank youuu": THANKS ×200. A clay fingerprint lands on the screen with every check.
6. **15.1 to 17.2s.** She lifts the phone again and the pot on the wheel slumps: POT #4: COLLAPSED.
7. **17.2 to 17.9s.** The clock spins to 4:00. 4:00 PM.
8. **17.9 to 20.8s.** The spam folder: a cruise, a million-dollar prize, and Brand Team, "Approved ✓ Please post by 12:00 PM", 9:15 AM. "Found at 4:00 PM".
9. **20.8 to 21.4s.** MISSED. She face-plants into the clay; clay flies.
10. **21.4 to 22.8s.** She looks up with clay on her face. The chrome monogram on her laptop; the light turns warm.
11. **22.8 to 27.5s.** YourBrand: Content, "Submit a draft for review", pot-day.mp4, In review. The bell gets a dot and its menu opens: NOTIFICATIONS · CONTENT · "Content approved", "The content review passed this video.", Open (IN THE APP). A chat DM from YourBrand: "Yes, good to post", Open in YourBrand (IN CHAT).
12. **27.5 to 30.8s.** Her hands on the clay, a vase rising: HANDS: ON THE CLAY. Her phone on the bench lights up: "YourBrand · Content approved". ONE PLACE TO LOOK.
13. **30.8 to 33.5s.** She swats away an envelope (✕ INBOXES) and a SPAM folder (✕ SPAM FOLDER), then crosses her arms: "No bullshit."
14. **33.5 to 37.2s.** The vase is done: POT #5: DONE. The phone buzzes ("chat · New message"), she jumps, the vase squashes. ASHTRAY.
15. **37.2 to 42.2s.** Black end card: chrome monogram, wordmark, "Approved? You'll know. One place to look.", yourbrand.com.

## How it works
Same structure as parts one to twenty six. New here:

- **The pot** is three `LatheGeometry` meshes on the spinning wheel head (`whead`): `potRaw` (squashed and tilted by `col` on "falls in"), `vase` (grows from a short lump while her hands stay on it, then `squash` flattens it on the jump) and `ashtray`. Only one is visible at a time.
- **The wall clock** is a canvas texture redrawn only when the time changes (`drawClock(hr)`); `hr` ticks to 9:00 on "nine" and spins to 4:00 on "four PM".
- **Clay fingerprints** (`prints`) stack on the pain-half phone sheets, one per check.
- **Two phones:** `P.phone` sits in her right hand during the checks; `phoneB` lies on the bench after the turn with its own lock-screen canvas (`drawBench`) for the banners.
- **Face in the clay:** the `PLANT` pose leans the torso and head into the wheel, `puff` throws clay lumps, and `P.clay` (a pale patch on the face) shows until the YourBrand reveal.
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice A (see `_engine/VOICES.md`), take 1 of 2. The raw take was 55.7 s, so pauses longer than 0.3 s were cut down to 0.3 s (48.3 s) and the result sped 1.3x (the ceiling). `code/recipe.py` lays the wheel's motor hum under each wheel shot, then a whoosh and pop per phone check with a small clay squelch, a low "nothing" tone, pops for each "thanks", a slump squelch for the collapse, clicks as the clock spins, a ding for the spam-folder approval, a stamp and a splat for MISSED and the face-plant, a ding for the bell, a two-note chat chime, a vibration and ding for the banner, a vibration for the buzz, a squelch for the squash. No music. The mux uses the limiter. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.

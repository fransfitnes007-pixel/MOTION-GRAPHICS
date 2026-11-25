---
name: day-in-the-life-follower-count-leaderboard-by-views-low-poly-3d-living-room-cat-word-timed-captions
description: Part eleven of the low-poly "day in the life of a UGC creator" reels. She applies to a brand and the first question is her follower count. Two thousand: they went with someone bigger. Her videos get views and nobody asks about views, every form wants a media kit and a follower count, her cat has more followers than she does, and she thinks about buying some. Then YourBrand: every campaign has a leaderboard, ranked by views, not followers. The cat still has more followers; the cat is not on the leaderboard (and pushes her mug off the table). Reach for it when a reel needs the small-account story, a low-poly cat, a form that only wants one number, or a leaderboard with no counts shown.
---

# Day in the life, part eleven: how many followers (low-poly 3D)

**Code name:** three.js living room at dusk, box-built character, a box-built cat with a blink, a tail and one working paw, application / forms / leaderboard pages on a floating sheet, profile and follower-shop pages on a floating phone, hard cuts on voiceover word times. **From:** original build, part 11 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-follower-count-leaderboard-by-views__low-poly-3d-living-room-cat-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 40.6 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 3.5s.** A living room at dusk: city window, green sofa, bookshelf, cat tree. She works at a wooden table; an orange cat sits next to the laptop. "Part eleven."
2. **3.5 to 7.9s.** "Creator application": portfolio attached, best videos attached. A black QUESTION 1 box types itself: "How many followers do you have?"
3. **7.9 to 9s.** Her face, hopeful: 2,000.
4. **9 to 10.4s.** The reply: "Thanks so much! We went with someone bigger. Best of luck :)". TOO SMALL stamp.
5. **10.4 to 13.7s.** Her profile: 2,000 followers, four videos with yellow view badges. Then her flat face: VIEWS: NOT ASKED.
6. **13.7 to 17s.** Three brands' forms slide in; "Media kit (PDF)" then "Follower count" turn red on all three: required.
7. **17 to 18.9s.** The cat, close. MR. BISCUIT · 14.2K. ME · 2,000. The cat blinks slowly.
8. **18.9 to 20.4s.** A purple shop, FOLLOWERZ 4 U, "+500 followers", three users named user_48213 and up; the cursor drifts to ADD TO CART. TEMPTED.
9. **20.4 to 21.9s.** The chrome monogram; the lamp comes on and the room turns warm.
10. **21.9 to 26s.** A dark campaign page: Leaderboard. Five rows land, hers marked "You" at number three. The VIEWS column lights up yellow and the bars turn green; the FOLLOWERS column is struck through in red and fades.
11. **26 to 28.7s.** Her at the table: THE HOOK (green), then a wave of the hand: NUMBER IN MY BIO (red).
12. **28.7 to 32s.** She swats away a "+500" box of grey bot heads and a framed photo of the cat: ✕ FAKE FOLLOWERS, ✕ CAT ENVY. Arms crossed: "No bullshit."
13. **32 to 35.6s.** Callback: the cat again. STILL 14.2K. A paw comes out, the mug slides off the table and breaks off screen. LEADERBOARD: NOT RANKED.
14. **35.6 to 40.6s.** Black end card: chrome monogram, wordmark, "Ranked by views. Not by followers.", yourbrand.com.

## How it works
Same structure as parts one to ten. New here:

- **The cat** is a group on the table at (0.92, 1.55, -1.1): body, striped back, head with cone ears, eye groups (`catEyes`, scaled on y for the blink), a `paw` group that rotates out, a `tail` that swings. The `cat` camera frames it against the sofa. `mug` slides along z and falls with a squared drop when `mugT` goes positive.
- **Pages:** `drawDoc` 0 the application (the question types itself; the reply card covers the form), 1 three brand forms whose two rows turn red in turn, 2 the leaderboard (bars for views and followers, the followers column struck out); `drawPhone` 'profile' and the follower shop.
- **Props for the finale:** `fbox` (a cardboard box with a "+500" label and three bot heads) and `frame` (a gold frame with a drawn cat).
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice A (see `_engine/VOICES.md`), sped 1.244x (raw 46.0 s, aimed at 37 s), take 2 of 2 (the shorter one). `code/recipe.py` adds typing clicks for the question, a buzzer on TOO SMALL, a ding per view badge, clicks and buzzers as the form rows turn red, a synthetic meow, a tacky jingle and a low drone for the follower shop, a ding per leaderboard row, a ceramic slide and a smash when the mug goes, a second smaller meow. No music. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.

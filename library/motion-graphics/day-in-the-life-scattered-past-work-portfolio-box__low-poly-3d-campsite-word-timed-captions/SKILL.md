---
name: day-in-the-life-scattered-past-work-portfolio-box-low-poly-3d-campsite-word-timed-captions
description: Part twenty eight of the low-poly "day in the life of a UGC creator" reels. At a campsite, a camping creator is asked for his past work. He has made three videos: one is on an old account (page not found), the brand deleted one, and one is on his laptop at home. No signal, so he climbs the cooler, the canoe and a tree to send three links; the brand asks for one link and he falls in the lake. Then YourBrand: his portfolio sits on his profile (a link or a PDF, set once), and when he applies for a deal that one link goes in the form. There's a fish in his boot. He can stay. Reach for it when a reel needs the scattered-past-work story, a campsite at dusk or night, a campfire, a climb for phone signal, a fall into a lake with a splash and a floating hat, a fish dropping out of a boot, or phone sheets for "page not found", a deleted post, a portfolio box or an apply form.
---

# Day in the life, part twenty eight: a fish in my boot (low-poly 3D)

**Code name:** three.js campsite (pines, a lake, a tent, a campfire with cone flames and a flickering point light, an upturned canoe on two stumps, a cooler, a camp chair, a tall tree with a branch over the water, hills, a moon and stars that fade in), box-built camper in a flannel-check shirt (canvas texture), orange beanie and a big moustache, climbing poses with the phone held up, a fall into the lake (splash drops, a ring, the beanie floating), a towel on his head after, a fish prop, floating phone sheets, hard cuts on voiceover word times. **From:** original build, part 28 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-scattered-past-work-portfolio-box__low-poly-3d-campsite-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 40.8 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 4.7s.** A campsite at dusk. A man in a flannel shirt films himself in a camp chair by the fire. "Part twenty eight." CAMPING CHANNEL.
2. **4.7 to 8.0s.** Mail from Ridge Jerky Co.: "Love your camping videos! Can you send us your past work?" (highlighted). VIDEOS MADE: 3.
3. **8.0 to 14.6s.** Video 1, @tentguy_old: a sad tent, "Page not found" (VIDEO 1: GONE). Video 2, the brand's posts: one tile crossed out, "Post unavailable, deleted by the account" (VIDEO 2: DELETED). Video 3: "On: my laptop", then a map card "Home · 212 mi" (VIDEO 3: AT HOME). Every sheet says No Service.
4. **14.6 to 19.2s.** He holds the phone up: SIGNAL: NONE. He stands on the cooler (1 BAR), on the canoe (2 BARS), on a branch of the tall tree over the lake (SENT ×3).
5. **19.2 to 21.2s.** The chat: three blue link bubbles, each with a red error. Their reply: "Can you send it as one link, please?" ONE LINK?
6. **21.2 to 22.5s.** He falls off the branch into the lake. SPLASH; his beanie floats.
7. **22.5 to 24.2s.** Back in the chair with a towel on his head; the chrome monogram; night falls, the stars come out and the fire grows.
8. **24.2 to 28.0s.** YourBrand, Profile: "Your portfolio (optional) · Show brands your best work. Paste a link, or upload a PDF. You can do both." The link types in, ✓ Link saved, Your PDF, "PDF, up to 20 MB", On your profile (LINK + PDF).
9. **28.0 to 28.6s.** Hands behind his head by the fire: SET ONCE.
10. **28.6 to 30.8s.** Find deals, "Apply to Trail Coffee", Experience links (up to 3): his one portfolio link, the other two not needed, ✓ Sent (ONE LINK).
11. **30.8 to 33.6s.** He swats away a broken chain link (✕ DEAD LINKS) and a little pine (✕ TREES), then crosses his arms: "No bullshit."
12. **33.6 to 35.8s.** He pulls up his boot and tips it: a fish drops out by the fire (FISH: 1). "He can stay." CREW: 2.
13. **35.8 to 40.8s.** Black end card: chrome monogram, wordmark, "Your best work. One link. On your profile.", yourbrand.com.

## How it works
Same structure as parts one to twenty seven. New here:

- **Climbing for signal:** `UP(x, y, z, ry)` makes a standing pose with the right arm straight up holding the phone; `ONCOOL`, `ONCANOE` and `ONTREE` stand him on the cooler, the canoe and the branch, each stepped up from lower with `step()` and swaying with `sway()`. The pills count the bars.
- **The fall:** from `T.lakeHit - 0.48` the root drops from the branch to below the water with a gravity curve while the arms flail; on `lakeHit` ten drops arc out, a torus ring spreads on the water, the body hides and `hatF` (a copy of the beanie) bobs up. From `T.found` he has `P.towel` on and `P.hat` off.
- **The fish:** after `applyPose`, `P.lR.knee.localToWorld` gives the boot opening; `fishP` arcs from there to the ground by the fire, flops, then settles.
- **Night:** `good` fades the sky and background from dusk blue to night, fades in the stars and moon, cools the sun to moonlight and lifts the fire (`flames` scale, `glow` intensity).
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice B (men) (see `_engine/VOICES.md`), take 1 of 2, raw 41.6 s, sped 1.123x. `code/recipe.py` lays a crackling fire under everything (louder after the turn), a whoosh and pop per phone sheet, a low tone for each lost video, a buzz for no signal, two footsteps per climb and a rising tone per bar, three send blips, a falling whistle and a splash for the lake, the reveal chord, dings for link saved, PDF and sent, swats, a small splash and flops for the fish. No music. The mux uses the limiter. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.

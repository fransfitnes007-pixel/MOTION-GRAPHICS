---
name: day-in-the-life-login-codes-captcha-home-screen-app-low-poly-3d-park-golden-hour-word-timed-captions
description: Part fifteen of the low-poly "day in the life of a UGC creator" reels. In a park at golden hour she has forty minutes of good light and first has to log in: wrong password, a reset code sent to an email she cannot open, which needs a code too, then a traffic-light CAPTCHA (is the pole part of the light?). A timer runs to zero while the sun sets into night. Then YourBrand: sign in once, add it to the home screen, tap the icon, it opens already signed in. She is still not sure she is human. Reach for it when a reel needs the login story, a countdown tied to the light, nested code dialogs, a CAPTCHA grid, or an add-to-home-screen flow.
---

# Day in the life, part fifteen: forty minutes of good light (low-poly 3D)

**Code name:** three.js park whose sky, sun, stars and lamp post are driven by a countdown, box-built character, login / nested code dialogs / share sheet / home screen / app opening on a floating phone, a CAPTCHA grid on a floating sheet, hard cuts on voiceover word times. **From:** original build, part 15 of the Day in the Life series (`pipelines/day-in-the-life/`).

## What you see
Render it: `node engine/tools/render_demo.cjs video library/motion-graphics/day-in-the-life-login-codes-captcha-home-screen-app__low-poly-3d-park-golden-hour-word-timed-captions/code/demo.html out.mp4 1080 1920` (about 40.5 seconds, 1080x1920; no voice is included, see `pipelines/day-in-the-life/PLAYBOOK.md`).

1. **0 to 4s.** A park at golden hour: striped grass, trees, hills, a low sun, a tripod with a phone. She works at a picnic table. "Part fifteen."
2. **4 to 6.3s.** She points at the sun. A green pill appears and stays: GOOD LIGHT 40:00, counting down.
3. **6.3 to 10.2s.** A login screen: the password types itself, the fields shake, "Wrong password. Attempt 3 of 3", the button becomes "Reset password", then "Code sent". The sky is already pinker.
4. **10.2 to 14s.** "Enter the 6-digit code, sent to o•••••@oldmail.com". A second dialog lands on top ("oldmail: sign in, enter the code we texted"), then a third ("New device detected"). Dusk.
5. **14 to 20s.** A CAPTCHA: "Select all squares with traffic lights". Two tiles get blue ticks. The two tiles that hold only the pole pulse amber with question marks. Stars are out; the pill has turned red.
6. **20 to 21s.** The header turns red: "Please try again. You missed one." The pole tile is outlined in red.
7. **21 to 23s.** Night. She sits lit by the laptop, eyes shut. GOOD LIGHT 00:00.
8. **23 to 24.9s.** The chrome monogram, and a clear morning.
9. **24.9 to 26.1s.** Her point of view of the laptop: Sign in, then "Welcome back · Signed in ✓". ONCE.
10. **26.1 to 27.5s.** A share sheet slides up; "Add to Home Screen" turns yellow.
11. **27.5 to 28.6s.** A home screen of coloured icons; the YourBrand icon pops into a gap and is tapped (a ring spreads).
12. **28.6 to 30.8s.** The app grows out of the icon: Home, "Welcome back", a green "Signed in ✓". ALREADY SIGNED IN.
13. **30.8 to 33.9s.** She swats away a "482 915" code block and a traffic light: ✕ CODES, ✕ TRAFFIC LIGHTS. Arms crossed: "No bullshit."
14. **33.9 to 35.5s.** Callback: close on her face as she studies her own square hand. HUMAN: UNVERIFIED.
15. **35.5 to 40.5s.** Black end card: chrome monogram, wordmark, "Sign in once. Add it to your home screen.", yourbrand.com.

## How it works
Same structure as parts one to fourteen. New here:

- **`LEFT` and `minsLeft(t)`**: a list of (time, minutes left) keyed to each obstacle. `state` turns it into the pill text and into `night = eio(1 - mins / 40)`, which drives everything in the sky: background colour through gold, dusk and night, the sun's height, cloud colour, star opacity, the lamp post and its point light, and the key light. `good` then blends all of it to a morning.
- **Pages:** `drawPhone` 'login', 'codes' (three stacked dialogs via `dlg`), 'share', 'homescreen', and the opening app (a rounded rectangle that scales up from the icon's position); `drawDoc` the CAPTCHA, with `tile(x, i, X, Y, s)` drawing each of the nine street tiles.
- **The closing pose** raises her left arm so the hand sits beside her face in the `face` camera (`alx -2.4, ale 0.4, alz 0.21`); smaller `alz` pushes it out of frame, larger covers her eye.
- **Props for the finale:** `codeP` (a block reading 482 915) and `tl` (a traffic light).
- `code/demo.html` is built from `code/demo.src.html` plus `code/_shared_ui.js`: replace `/*SHARED_UI*/` with the file.

## Sound
Voice: TTS voice A (see `_engine/VOICES.md`), sped 1.199x (raw 44.4 s, aimed at 37 s), take 2 of 2 (the shorter one). `code/recipe.py` adds a clock tick every half second from "forty minutes" until the light is gone, getting louder; crickets as night falls and birds in the morning; a buzzer on the wrong password, falling notes as each code dialog lands, two clicks for the CAPTCHA ticks, two rising "?" blips for the pole, a long buzzer on "missed one", a low drone on "gone", a tap and a rising swell as the app opens. No music. Nobody has listened to the mix yet.

## Files
`code/demo.html` (runnable), `code/demo.src.html` + `code/_shared_ui.js` (the build sources: `/*SHARED_UI*/` in the src is replaced by the shared file), `code/recipe.py` (synthesised sound effects on the beat times; drop your own voice take next to it as `voiceover.wav`), `code/three.min.js` (three.js, MIT), `code/brand-assets.js` (generated by `engine/tools/apply_brand.py`), `media/poster.jpg`. Voice audio, the mixed sound and the rendered clip are not published.

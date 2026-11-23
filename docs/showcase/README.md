# Showcase film

The video at the top of the main README, made with the kit itself: one canvas page (`showcase.html`) where every frame is `render(t)`, every cut pinned to the voiceover's word times, library pieces playing inside it, and a soundtrack synthesised in `mix.py` (music bed ducked under the voice, effects on every cut and pop-in, a boom on the end card).

## Rebuild it

```bash
cd docs/showcase
./render_clips.sh 0 2 & ./render_clips.sh 1 2 & wait     # renders every clip in clips.txt at its own shape, in two parallel jobs
node ../../engine/tools/render_demo.cjs video showcase.html clips/silent.mp4 1920 1080
python3 mix.py clips/silent.mp4 ../media/showcase.mp4
./make_preview.sh                                          # the silent looping GIF at the top of the main README
```

## Change it

- **Voice:** replace `assets/voiceover.wav`, transcribe it (`skills/transcribe`), and move the word times in `T` at the top of `showcase.html` and in `mix.py`.
- **Script:** `script.txt`. Scenes `s1` to `s11` each carry the line they illustrate as a comment. The format wall (`s3`) is the hero: each format's clip pops in on its word at its own shape, the camera follows, then pulls back to the full wall.
- **Pieces shown:** `clips.txt` lists every clip (name, library path, render size, frame width). Tall reels render at 1080x1920 and play in 9:16 frames; wide films and interactions render at 1920x1080 and play in 16:9 frames. The lists `WIDE`, `TALL` and `PACK12` at the top of `showcase.html` choose where each appears.
- **Type:** all text is San Francisco (`FONT` at the top of `showcase.html`); on machines without it the system UI font is used.

The voiceover was made with ElevenLabs (Eleven v4, stability 50, similarity 75), pauses tightened and loudness normalised. The film's palette is `sunset-ink` (see `palettes/PALETTES.md`). Interaction ideas are common iOS patterns; their code here is original.

**Footage.** The `r_*`, `w_pp`, `w_launch2`, `w_gkfilm` and `w_dino` frame folders are the growthkit.net team's own reels and films, extracted locally with ffmpeg; they are not in the repository. Without them those tiles render as empty cards, so swap in your own videos (any mp4 → `ffmpeg -i in.mp4 -vf fps=30,scale=405:-2 frames/<name>/%04d.jpg`) and list them in `WALL`/`TALL` at the top of `showcase.html`.

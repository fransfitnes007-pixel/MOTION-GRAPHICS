# Showcase film

The video at the top of the main README, made with the kit itself: one canvas page (`showcase.html`) where every frame is `render(t)`, every cut pinned to the voiceover's word times, library pieces playing inside it, and a soundtrack synthesised in `mix.py` (music bed ducked under the voice, effects on every cut and pop-in, a boom on the end card).

## Rebuild it

```bash
cd docs/showcase
./render_clips.sh comma=comma-jump-number-input__digit-rise-comma-dip border=border-stroke-pulse-button__comet-around-capsule \
  burn=card-burn-particle-dissolve__noise-edge-ember-sparks flip=card-flip-overshoot__rotatey-spring-back-face
node ../../engine/tools/render_demo.cjs video showcase.html clips/silent.mp4 1920 1080
python3 mix.py clips/silent.mp4 ../media/showcase.mp4
```

## Change it

- **Voice:** replace `assets/voiceover.wav`, transcribe it (`skills/transcribe`), and move the word times in `T` at the top of `showcase.html` and in `mix.py`.
- **Script:** `script.txt`. Scene `s1` to `s12` each carry the line they illustrate as a comment.
- **Pieces shown:** the `pack` URL parameter picks which library interactions play in the micro-interaction scene.

The voiceover was made with ElevenLabs (Eleven v4, stability 50, similarity 75), sped up 6% and normalised. Interaction ideas in scene 5 are common iOS patterns; their code here is original.

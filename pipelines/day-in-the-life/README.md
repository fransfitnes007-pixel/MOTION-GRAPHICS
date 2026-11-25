# Day in the Life of a UGC Creator (low-poly 3D reel series)

A series format for a product that serves creators: about 40 seconds, 1080x1920, low-poly 3D, first person, dry humour,
hard cuts on the voice's word times, big word-timed captions with the current word in yellow, synthesised sound effects,
and a chrome end card with your monogram, wordmark and domain. Fifty parts were made with it; every one is in the
library as runnable code (`library/motion-graphics/day-in-the-life-*`), white-labelled to `YourBrand`.

Every part has the same spine:

1. **Pain (0 to about 20 s).** "Day in the life of a UGC creator. Part N." A new creator, a new place, one pain point
   from the job, told in their own voice, with one visual joke that gets worse each beat, ending on a new low point
   (face in the cake, sitting on the pool floor, tied in a knot).
2. **The product (around the midpoint).** "Then I found YourBrand." One real feature that answers that exact pain,
   shown on a floating phone or laptop sheet that copies the real screen.
3. **The closer.** "No X. No Y. No bullshit." (two swatted chips and crossed arms), then a callback that belongs to that
   episode (the habit that empties the pool, the skaters calling him unc), then the end card.

| File | What it is |
|---|---|
| [`PLAYBOOK.md`](PLAYBOOK.md) | The rules for the story and the claims, and the build steps from "go" to the finished file |
| [`SCENE-KIT.md`](SCENE-KIT.md) | How an episode's code is laid out: head, middle, shared UI; the person rig, poses, sheets, cameras, `state(t)`, and the traps |
| [`EPISODE-LOG.md`](EPISODE-LOG.md) | All 50 parts (creator, setting, pain, gags, payoff, closer, voice, length) and the "already used" lists. Read it before every part |
| `tools/` | `prep_voice.py` (speed rule), `words.py` (local word times), `tidy.py`, `fill.py` (assemble the episode), `sheet.py` (contact sheets), `mux.sh` (render, mix, mux, checks), `port_episode.py` (copy a private build into the public library, white-labelled) |

Start a part with the `/dayinlife` command or the `day-in-the-life-series` skill: "go" makes the next part end to end.

Nothing in the published pieces speaks: the voice takes, mixed sound and rendered clips are not in the repository.
`code/recipe.py` in each piece is the sound design (synthesised effects on the beat times) and picks up your own
`voiceover.wav` when you put one next to it.

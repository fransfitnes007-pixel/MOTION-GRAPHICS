# Day in the Life: the scene kit

Every part is one HTML file with two canvases: a three.js WebGL scene (`#gl`) and a 2D layer on top (`#ui`) for
captions, pills, stamps and the end card. Every frame is `window.render(t)`: `state(t)` poses the world, three.js draws
it, `overlay(t)` draws the 2D layer. No timers, no randomness without a seed, so any frame can be rendered alone.

## Layout of `code/demo.src.html`
| Part | Lines | What is in it |
|---|---|---|
| head | top to the first `// ---------- ` section | `CONFIG` (site, caption colours, card colours, `endLines`, outfit colours, `capY`, `safe` box), `WORDS` (`[word, start, end]`), `GROUPS` (`[first, last, break-after, size]` per caption), `T` (beat times), easing helpers (`seg`, `eo`, `eio`, `back`), renderer, lights, `M` (flat-shaded material), `box`, `cyl`, `grp`, `canvasTex`, the brand images |
| middle | your episode | the room, `makePerson()`, poses, props, sheets (`drawDoc`), `CAM`, `state(t)` |
| tail | from `/*SHARED_UI*/` | `notes`, `overlay`, `window.render`, the preview loop |

`/*SHARED_UI*/` is replaced by `code/_shared_ui.js` in `demo.html`: `pill(text, row, k, kind)`, `stamp(text, k, color,
rot, yShare)`, `coin(...)` (the spinning monogram), `captions(t)`, `endCard(t)`.

## The person
- `makePerson()` builds a box person with the origin at the hips: `root` > `torso` > `head` (eyes, mouth, brows, hair),
  arms `aL`/`aR` with `sh` (shoulder) and `el` (elbow) pivots, legs `lL`/`lR` with `hip` and `knee`, and a `phone` in
  the right hand. Outfit colours come from `CONFIG` (`skin`, `hoodie`, `sweats`, `hair`); add props (cap, whistle,
  apron, headset) as children of `head` or `torso`. Text on clothes is a small `canvasTex` plane.
- A pose is a flat object (`P0` lists every key: position, root and torso rotation, head, both arms, both legs, `eye`,
  `mw`/`mh` mouth size, `brow`). `pose({...})` fills the rest from `P0`, `mixP(a, b, k)` blends two poses, and
  `applyPose(q)` writes it to the rig. Keep a few named poses per part: `SIT`, `HOLD` (phone up), `SLUMP`, `FLOOR`,
  and a gesture overlay such as `BLOW` spread on top: `{ ...SIT, ...BLOW }`.
- Breathing: add `Math.sin(t * 2.2) * 0.012` to `tx` every frame so held poses are not frozen.

## Sheets (the floating phone or page)
- `doc` is a group at (0, 3.0, 2.6) holding a white slab and a 720x1040 canvas texture `dc`. `drawDoc(mode, t)` paints
  the sheet for the current beat; `docMode` chooses it. `showDoc(t0)` pops it in with `back()` and a slow sway.
- Keep text above y 540 or in the bottom band (930 to 1010): the middle of the sheet sits under the caption. Titles
  32 to 44 px, body 22 to 28 px at the least: smaller text does not survive a phone screen.
- Pain-half sheets copy the look of the app being mocked (white, coloured top bar); product-half sheets are dark
  (`#0b0c10`), monogram top left, the real screen's title and labels.

## Cameras and the timeline
- `CAM = { name: [position, target, fov] }`. `setCam(pos, target, fov, k, push, shake)` pushes in slowly over a beat
  (`k` from 0 to 1) and shakes on hits.
- `state(t)` is one `if / else if` chain on `T`: each branch picks a pose, a camera, a sheet, and pushes pills
  (`v.pills.push([label, row, k, 'good'|'bad'])`) or a stamp. `latest([[t0, 'LABEL'], [t1, 'NEXT']], kind)` shows only
  the newest pill of a list and shakes the camera when it lands.
- Light carries the story: dimmer and warmer in the pain half, brighter after "Then I found" (`good` eases 0 to 1).
- The swat finale: two chips fly in on "No X" and "No Y", an arm swings through them (`Math.sin(seg * PI)`), they spin
  away; on "No bullshit" the arms cross and the camera holds on `center`.

## Traps seen in 50 parts
- **Captions too long or too small.** More than about five words in a group shrinks the type; split groups and give
  punch words their own group with a larger size (1.4 to 1.6).
- **Pills over sheet titles.** Pills sit at the top of the safe box; move the sheet title down (y 74 or lower) or put
  the pill on row 1.
- **Small sheet text.** Under 22 px it turns to grey fuzz at phone size; cut words rather than shrink.
- **Props hidden behind furniture** (a swimmer behind the chair, a phone behind a laptop lid): check every gag beat on
  a still from the camera it is shot from.
- **Dim faces** in underwater, night or backlit shots: raise the hemisphere light for that beat or add a point light.
- **Something blocking the face** (tripod, raised arm, a mug) in desk shots: hide it for that camera.
- **Long takes.** A slow voice take capped at 1.3x leaves the part a few seconds long; shorten the next script.
- **Same low point twice.** Keep the Gags list in the log honest; "face-plant on the desk" was used early and often.

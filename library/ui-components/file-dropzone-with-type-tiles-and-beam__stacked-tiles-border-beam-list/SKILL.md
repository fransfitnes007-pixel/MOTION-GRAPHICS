---
name: file-dropzone-with-type-tiles-and-beam-stacked-tiles-border-beam-list
description: A white upload card with a dashed drop area, a fan of three small file tiles, 'Click to upload or drop files', the accepted types and a Browse files pill. A beam runs round the border on drag-over and dropped files appear as rows below. Use for any document or attachment upload.
---

# File dropzone with type tiles and beam

**Code name:** Stacked tiles, border beam, file list.

## What you see
A white card with a thin grey border and 22px corners (max width 448px in the real usage; the demo shows it at 1.55x). Inside it a dashed rounded drop area. Centred in the area, three small rounded-square tiles are stacked: the front one has a grey upload-file icon, the two behind lean out by about 7 degrees and carry file-type labels (PDF, DOC, XLSX, CSV, PNG, JPG) that swap every 0.9s. Under them 'Click to upload or drop files' in 17px black, the accepted types in 13.5px grey, and a pill button with an upload arrow and 'Browse files'. In the demo a cursor carries a PDF chip in at 1.3s; the tiles spread to about 16 degrees, the dashes turn violet-tinted, a short bright beam runs around the border and the title changes to 'Drop to upload'. At 2.6s it lands, and two rows (type badge, name, size, x) slide in under the zone and the card grows to hold them; at 6.4s they clear. The page had no video, so this motion is built from the description and the still.

## When to use it
Attaching documents to a form, a chat, a record or a data import. The list under the zone suits 1 to 5 files; for bulk uploads add a progress row design instead.

## How it works
The drop area is an SVG `rect` with `stroke-dasharray: 4 5`. The beam is a second `rect` with `pathLength=1000` and a dash of 140 followed by a gap of 860, so animating `stroke-dashoffset` makes the beam travel the perimeter at any size. In the demo the offset is `-(t * 520) % 1000`; in React it would be driven by the drag-over state. The tiles are absolutely positioned and rotate and spread with a drag-over value from 0 to 1. Rows animate in with a short fade and 10px rise, staggered 0.2s.

```js
beam.setAttribute('stroke-dasharray', `140 860`)
beam.setAttribute('stroke-dashoffset', -((t * 520) % 1000))
tile.style.transform = `rotate(${7 + 9 * hover}deg)`
```

The real component's motion was not available as video, so timings and the beam style are guesses. Check them against the original before copying numbers.

## Numbers that matter
| | |
|---|---|
| Card | 520 wide, border `#e6e6e9`, radius 22, padding 16 |
| Drop area | 300 tall, dashed `#d2d2d8`, radius 16 |
| Tiles | 56px, radius 15, spread 22px idle and 42px on drag, lean 7 to 16 degrees |
| Label swap | every 0.9s, 0.35s ease-out |
| Beam | 140 of 1000 of the perimeter, 2.5px, `#6f7bff` with glow |
| File row | 46px tall, 54px pitch, type badge 30px |
| Loop | 8s, drag-in 1.3s, drop 2.6s, clear 6.4s |

## Sound
Silent.

## Adapt it
- `types` and `hint`: the accepted formats.
- `beam` and `beamLen`: colour and length of the border beam.
- `files`: the sample rows, replaced by real state.
- `zoom`: only for the demo; drop it in your app.

## Files
- `code/demo.html` runs on its own and loops. Everything it draws is a function of time, with `CONFIG` at the top of the script.
- `media/poster.jpg` is one frame.

## Credit
Idea: "File Upload" by extend-hq on 21st.dev (https://21st.dev/@extend-hq/components/file-upload-2), MIT. This demo is an original recreation written from the public preview.

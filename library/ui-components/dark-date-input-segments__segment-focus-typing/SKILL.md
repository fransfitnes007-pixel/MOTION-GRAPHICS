---
name: dark-date-input-segments-segment-focus-typing
description: A dark labelled date field with three typed segments (mm / dd / yyyy). Reach for it on a checkout or sign-up form that asks for a birthday.
---

# Dark date input with mm/dd/yyyy segments

**Code name:** Segment focus typing.

## What you see
On a near-black page (#121212) a 256px-wide field sits in the middle: the label "Date" in white 14px, then a 40px-tall rounded box (#18181a, 1px grey border, 14px radius) holding the grey placeholder `mm / dd / yyyy`. The 21st.dev clip is a still of this resting state for 4 seconds.

The demo adds the states you would use it for. At 1.3s the pointer clicks the field: a blue ring (3px, soft) appears and the `mm` segment fills solid blue. Digits arrive every 0.32s from 1.5s: `0` `7` fills month and focus jumps to `dd`, `1` `4` fills day, `2` `0` `2` `6` fills year. At 5.6s a click elsewhere drops the ring and a line under the field reads the saved date.

## When to use it
Checkout, age-gate or sign-off forms where the person types a date rather than picking one from a calendar. It is a text-style input, so it is wrong for a trip or booking where a month grid helps the person choose.

## How it works
Each part of the date is its own tiny element, not one text box, so the caret can jump between them. Placeholders (`mm`, `dd`, `yyyy`) are grey; a typed segment turns white; the segment that will receive the next key gets the accent fill. The group border and ring are driven by one `focused` flag.

```js
const n = Math.floor((t - CONFIG.firstKey) / CONFIG.keyGap) + 1      // keys typed so far
// each segment takes its share of CONFIG.digits: 2, 2, 4 characters
segs[i].textContent = typed || placeholder
```

The 21st.dev clip only shows the empty state. The focus ring, segment highlight, typing and the saved line are rebuilt from how a standard date field behaves, not copied from the video.

## Numbers that matter
| | |
|---|---|
| Field | 256px wide, 40px tall, 14px radius, scaled 1.7x in the demo |
| Colours | page `#121212`, field `#18181a`, border `#38383b`, placeholder `#8b8b92` |
| Typing | first key at 1.5s, one key every 0.32s, 8 digits |
| Loop | 8.5s |

## Sound
Silent.

## Adapt it
- `CONFIG.digits` for the date that gets typed, `CONFIG.label` and `CONFIG.hint` for the words.
- `CONFIG.accent` for the ring and active segment colour.
- `CONFIG.width` and `CONFIG.scale` for size.
- Swap segment order or lengths in the `segs` list for a day-first or year-first date.

## Files
- `code/demo.html` runs on its own and loops; every frame is `render(t)`. Edit the `CONFIG` block at the top of its script.
- `media/poster.jpg` is the page's preview image.

## Credit
Idea: "DateField" by hero_ui on 21st.dev (https://21st.dev/@hero_ui/components/heroui-date-field), MIT. This demo is an original recreation written from the public preview.

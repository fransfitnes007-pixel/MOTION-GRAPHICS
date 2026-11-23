---
name: video-call-controls-bar-icon-swap-mute-toggles
description: A dark call-controls panel with a green live dot, mic, camera and share-screen toggle buttons and a red Leave button. Clicking a toggle swaps its icon to the slashed version and its label (Mute to Unmute). Reach for it on a meeting or live-session screen.
---

# Video call controls bar

**Code name:** Icon and label swap on toggle.

## What you see
A near-black screen with a dark grey rounded panel, 585 by 255 in the preview. A green dot with a soft ring and "In call · 12:34" sit centred at the top. Below are four columns, each a 72px rounded-square button with a label underneath: Mute (mic), Stop video (camera), Share screen (monitor) and Leave. Leave is filled coral `#ff5a62` with a white handset-off icon. The other three are dark grey with a thin outline.

In the clip, a cursor clicks Mute at about 0.9s. The mic icon becomes a mic with a slash, the label turns to "Unmute", and the button fills slightly lighter grey with a faint red-brown border. At about 2.6s it clicks the camera: "Stop video" becomes "Start video" with the slashed camera. The preview is 3.9s long. The demo stretches it to 6.2s and clicks both back on at the end so it loops.

## When to use it
Any live call, stream or voice-room screen where a handful of switches need instant, readable state. The label change matters as much as the icon: "Unmute" tells you what the next click does. It is wrong for settings screens with many switches; use a toggle list there.

## How it works
Each button holds two icons stacked in the same box and two labels stacked in the same line. The state flips which pair is visible; the demo crossfades them over 0.18s with a small scale from 0.8 to 1 on the incoming icon.

```js
const mix = 1 - fromA            // 0 on, 1 off
background: rgb(lerp(30,45,mix), lerp(30,43,mix), lerp(32,43,mix))
borderColor: rgb(lerp(51,74,mix), lerp(51,53,mix), lerp(54,53,mix))
```

Leave has no off state. The green dot has a breathing ring (box-shadow 3 to 6px, 2s period). The usage example on 21st.dev is just `<Pattern />` with no props, so the labels and states are fixed inside the component.

## Numbers that matter
| | |
|---|---|
| Panel | 585 x 255, 30px radius, fill `#171717`, 1.5px border `#2b2b2d`, page `#0a0a0a` |
| Button | 72 x 72, 17px radius, fill `#1e1e20`, border `#333336`, icon 28px stroke 1.7 |
| Off state | fill `#2d2b2b`, border `#4a3535` |
| Leave | fill `#ff5a62`, white icon |
| Labels | 21px, `#a8a8ad`, 14px under the button |
| Spacing | about 24px between columns; columns are as wide as their label |
| Swap | 0.18s crossfade, press scale 0.94 |
| Demo loop | 6.2s, clicks at 0.95 mic, 2.6 camera, 4.4 mic back, 5.0 camera back |

## Sound
Silent.

## Adapt it
- `CONFIG.clicks`: the times and which button gets clicked.
- `CONFIG.status` and `dotColor` for the line above.
- `leaveColor` and `offFill` for the brand palette.
- `defs` array to rename buttons, change labels or add a fifth button (raise the box width).

## Files
- `code/demo.html` runs on its own and loops. It is a recreation made from watching the video and reading the usage example.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Video Call Controls Bar" by cnippet-dev on 21st.dev (https://21st.dev/@cnippet-dev/components/v-toggle-9), MIT. This demo is an original recreation written from the public preview.

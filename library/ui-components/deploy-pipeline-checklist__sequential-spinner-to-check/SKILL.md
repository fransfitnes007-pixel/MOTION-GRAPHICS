---
name: deploy-pipeline-checklist-sequential-spinner-to-check
description: "A dark modal-style checklist of five pipeline stages that run in order: a grey dot becomes a spinning arc, then a white circle with a black check, with the stage icon lighting up. A footer bar spins until all stages finish. Reach for it for deploy, install, import or setup progress."
---

# Deploy pipeline checklist

**Code name:** Sequential spinner that resolves to a check.

## What you see
A near-black page with a rounded dark panel 697 by 782 (40px radius, `#1a1a1a`). The header has a four-point sparkle, "CI/CD Pipeline Protocol" in 28px bold, a small round close button at the right, and a grey line under it: "Execute build and deployment stages sequentially." Five rows follow, each 641 by 95 with 30px corners on a slightly darker `#131313`, 19px apart. Each row has a 62px rounded icon tile (git branch, download, chip, layers, copy), a 23px semibold title, a 17px grey description, and a 40px status circle on the right. At the bottom is a 62px pill bar `#262626` with a small spinner and "Deploying Pipeline..." in semibold.

Status states: pending is a dark circle with a tiny darker dot and a grey icon; running is a dark circle with a light spinning arc and a white icon; done is a solid white circle with a black check and a white icon.

In the 4.9s clip the first row has just finished, the second spins (done at about 3s), and the third starts around 3.9s. The stages take about 1.7 to 2.3s each. The demo extends this over 11s: all five complete, the footer reads "Pipeline Deployed" at 8.3s, and everything resets at 10.2s.

## When to use it
A multi-stage job where each step takes seconds: deployments, installs, data imports, account setup. The strict one-at-a-time order tells people exactly where it is. Not for jobs with a real percent; use a progress bar, or the percent-bar sibling.

## How it works
One timeline per row: `[start, end]` seconds for its running state. A row is pending before `start`, running between, done after `end`. The status circle holds four layers (dot, spinner, white fill, check) and shows only the layer for the state.

```js
spinner: rotate((t - start) / 0.85 * 360deg)     // 270 degree arc, 2.4px round stroke
done:    fill scale .6 to 1, opacity 0 to 1, check path dash 1 to 0 over 0.35s
```

The icon tile and title colour switch from grey `#858585` to white once a row starts running, and stay white. The footer shows a spinner and "Deploying Pipeline..." until the last row finishes. The usage on 21st.dev is `<DeploymentChecklist />` with no props, so the stage list is built in.

## Numbers that matter
| | |
|---|---|
| Panel | 697 x 782, 40px radius, `#1a1a1a`, 1px `#252525` |
| Row | 641 x 95, 30px radius, `#131313`, 114px pitch |
| Icon tile | 62px, 20px radius, `#222`, icon 28px stroke 2 |
| Title / text | 23px / 600 and 17px `#8e8e8e` |
| Status circle | 40px; done `#fff` with `#111` check; spinner stroke `#ddd` |
| Footer | 641 x 62, `#262626`, 22px / 600 |
| Spinner | 0.85s per turn |
| Stage times in demo | 0.7, 3.0, 5.0, 6.7, 8.3s (ends), reset 10.2s |

## Sound
Silent.

## Adapt it
- `CONFIG.stages`: titles, descriptions, icons and `[start, end]` times.
- `running` and `finished` footer text.
- `spinSec` and `checkSec` for pace.
- Change the white done circle to a brand colour by editing the `.fill` background.

## Files
- `code/demo.html` runs on its own and loops. It is a recreation made from watching the video and reading the usage example.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Great UI Deployment Checklist" by saurabh-2607 on 21st.dev (https://21st.dev/@saurabh-2607/components/great-ui-deployment-checklist), MIT. This demo is an original recreation written from the public preview.

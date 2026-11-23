---
name: brutalist-mono-bar-timeline-recharts-bar-toggle
description: "A strictly black and white, monospace analytics page with white label slabs, hard 2px rules, big plain numbers and a white bar chart with a segmented two-button toggle. Reach for it when a dashboard should look like a spec sheet, not an app."
---

# Brutalist mono bar timeline

**Code name:** Recharts bar toggle.

## What you see
Black page, white text, no colour at all. A giant uppercase title, a small status chip inverted to white on black, a tab bar with a 3px white underline on the active tab, section titles as solid white slabs with black text, and metric cells divided by 2px white rules. The chart is 30 plain white bars with a 2px white axis, faint 8% horizontal grid lines, 45-degree date labels every third day and a two-part toggle "VIDEOS POSTED / VIEWS".

- 0 to 1.5s: the bars grow from the baseline (Recharts default bar animation).
- 4.0s: the cursor clicks VIEWS. The active button inverts, the y-axis changes to 0 to 300K, and the bars grow again from zero, because swapping the chart re-mounts it.
- 6.0 to 8.2s: the cursor sweeps across the bars with the tooltip, a white box with black text.

## When to use it
Reports for a technical or editorial audience, "campaign brief" pages, anything meant to look like a printed data sheet. The contrast is the whole identity, so do not add accent colours. It is wrong where status colour matters (red and green).

## How it works
The look is made of three repeated rules rather than any one trick.

- Border grid: cells use `border-b-[2px] border-r-[2px] border-white`, and the outer container supplies the last edges. Nothing has a radius (`--radius: 0rem`).
- Slab title: `bg-white text-black px-4 py-3 inline-block`, tracking 0.2em, then a subtitle at 50% opacity and a 2px rule.
- Chart: Recharts `BarChart` with `CartesianGrid vertical={false} stroke="#fff" strokeOpacity={0.08}`, axes in 2px white, tick labels in IBM Plex Mono 9 to 10px, and a tooltip restyled to `background:#fff; color:#000; border:none`.

```tsx
<XAxis dataKey="label" interval={2} angle={-45} textAnchor="end" height={60}
  tick={{ fontSize: 9, fontFamily: "'IBM Plex Mono', monospace", fill: "#fff" }}
  axisLine={{ stroke: "#fff", strokeWidth: 2 }} />
<Bar dataKey="videos" fill="#fff" />
```

The demo grows each bar with Recharts' 1.5s default `ease` and re-runs it when the toggle flips. IBM Plex Mono was not on this machine, so the demo falls back to `ui-monospace, SF Mono, Menlo`. Add the font to `code/fonts/` if exact glyphs matter.

## Numbers that matter
| | |
|---|---|
| Colours | `#000` and `#fff`; grid `rgba(255,255,255,.08)`; secondary text 50 to 65% white |
| Rules | 2px everywhere, 3px tab underline, 6px footer rule |
| Type | monospace, 9 to 11px labels with 0.15 to 0.2em tracking, 40 to 60px black-weight titles |
| Bars | white, 1.5s ease grow, 30 categories, label every third |
| Toggle | 2px border, active = white fill with black text |

## Sound
Silent.

## Adapt it
- The title, tab names and the six numbers.
- The two series (`videos`, `views`) and their axis maxima.
- To get a variant, invert it: white page, black bars.

## Files
- `code/demo.html`: runs on its own with made-up data.

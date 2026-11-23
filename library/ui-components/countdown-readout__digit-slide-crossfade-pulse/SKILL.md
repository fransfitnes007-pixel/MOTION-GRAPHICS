---
name: countdown-readout-digit-slide-crossfade-pulse
description: "A big monospace timer where each digit that changes slides up out of its slot while the next slides in from below, with a pulsing clock icon, a green \"Running\" label and a thin bar draining underneath. Use for countdowns, session timers and deadlines."
---

# Countdown readout

**Code name:** Digit slide crossfade and pulse.

## What you see
A small grey label in tracked capitals, then a 72px semibold monospace time, `01:05`, in white with tabular figures and a lilac clock icon at its left. The icon breathes: it grows 8% and brightens from 70% to full opacity and back every two seconds while the timer runs. Each second, only the digits that change move: the old digit slides up 12px and fades while the new one slides up into place from 12px below, in .15 seconds. Each digit sits in its own clipped slot, one character wide, so nothing spills. Beneath is "Running" in green (or "Paused" in grey, with the clock dimmed to 40%) and a 160px bar that shrinks left to right in step with the clock.

## When to use it
A single number that changes every second and should be easy to watch: focus timers, auction or offer deadlines, test timers. The slide tells the eye which digit changed. Wrong for rapidly changing values (it will blur) and for non-monospace type, since each slot is `1ch` wide.

## How it works
The parent owns the clock and passes `seconds`. The text is split into characters, and each character renders in a `Digit` that keeps its slot width and animates changes of its own character:

```tsx
<span className="relative inline-grid overflow-hidden" style={{ width: ch === ':' ? '0.5ch' : '1ch' }}>
  <AnimatePresence mode="popLayout" initial={false}>
    <motion.span key={ch} initial={{ y: 12, opacity: 0 }} animate={{ y: 0, opacity: 1 }} exit={{ y: -12, opacity: 0 }}
      transition={{ duration: 0.15, ease: 'easeOut' }} className="col-start-1 row-start-1 text-center">{ch}</motion.span>
  </AnimatePresence>
</span>
```
`popLayout` keeps the exiting digit in the same grid cell (`col-start-1 row-start-1`) so the two overlap during the swap instead of pushing each other apart. The slot key is `${i}-${text.length}`, so a change from `1:00:00` to `59:59` re-keys the slots instead of sliding. The clock icon is `animate={{ scale: [1, 1.08, 1], opacity: [0.7, 1, 0.7] }}` with `duration: 2, repeat: Infinity, ease: 'easeInOut'`. The bar is a plain div whose width has a 1s linear CSS transition, so it drains smoothly between ticks. The wrapper has `role="timer"` with `aria-live="polite"` and a spoken label, while the digits are `aria-hidden`.

## Numbers that matter
| | |
|---|---|
| Digit swap | .15s easeOut, y 12 in, y -12 out |
| Slot width | `1ch` per digit, `0.5ch` for the colon |
| Size | `text-6xl sm:text-7xl` (72px) or `text-3xl` for the `md` size, `font-mono font-semibold tabular-nums tracking-tight` |
| Icon pulse | scale `1 > 1.08 > 1`, opacity `.7 > 1 > .7`, 2s easeInOut; paused: opacity .4 |
| Status | `text-xs`, `text-emerald-400` running, `text-rv-muted` paused |
| Bar | `h-1 w-40 bg-white/5`, fill `bg-rv-purple`, width transition 1s linear |

## Sound
Silent. A very soft tick per second, and a chime at zero, would fit.

## Adapt it
- Format function (`fmtClock`): add days, or tenths of a second.
- Swap distance (12px) and duration (.15s).
- Colours for running, paused and the last ten seconds (turn the bar and digits amber, then red).
- Drop the icon and bar for a bare readout.

## Files
- `code/demo.html` runs on its own and loops in 10s (counts 01:05 down to 00:55).

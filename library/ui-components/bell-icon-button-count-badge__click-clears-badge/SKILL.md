---
name: bell-icon-button-count-badge-click-clears-badge
description: A square outline icon button with a bell and a black round count badge hanging off the top-right corner. Click it and the badge vanishes. Reach for it as the notification bell in a dashboard header.
---

# Bell icon button with count badge

**Code name:** Click clears badge.

## What you see
A white 36px square button with a rounded 8px outline and a 16px bell icon. A black pill badge reading 3 sits on its top-right corner: 20px high, 12px white medium text, centred on the button's right edge and 8px above its top edge. In the clip the cursor drifts in, the button fills light grey on hover, you click, and the badge is gone on the next frame (no fade). The button stays as a plain bell. The demo puts the badge back with a small spring pop at the end so it loops.

## When to use it
The notifications bell in a dashboard top bar or sidebar, an unread-messages icon, a cart icon with item count. The badge clearing on click suits an inbox where opening it marks everything read. If counts need to stay, move the clearing into your own handler.

## How it works
Button is `relative`. The badge is absolutely placed with `-top-2 left-full -translate-x-1/2 min-w-5 px-1`, so its centre sits on the button's right edge. The count is local state and the badge is conditionally rendered, which is why it disappears in one frame.

```tsx
<Button variant="outline" size="icon" className="relative" onClick={() => setCount(0)}>
  <Bell size={16} />
  {count > 0 && <Badge className="absolute -top-2 left-full min-w-5 -translate-x-1/2 px-1">{count > 99 ? '99+' : count}</Badge>}
</Button>
```

The demo copies those offsets. Number shows `99+` above 99.

## Numbers that matter
| | |
|---|---|
| Button | 36px square, radius 8px, 1px `#e2e2e2` border, shown at 2x |
| Icon | bell, 16px, stroke 2 |
| Badge | min-width 20px, height 20px, 4px side padding, 12px medium text, `#171717` on white |
| Position | top -8px, left 100% minus half the badge width |
| Click | badge removed instantly; demo restores it at 5.2s with a 0.45s spring |

## Sound
Silent.

## Adapt it
- `CONFIG.count`: the number (0 hides the badge, over 99 shows 99+).
- `CONFIG.badgeColor`: swap black for red or your brand colour.
- `CONFIG.zoom`: size.
- `CONFIG.clickAt` and `CONFIG.resetAt`: when the click and the restore happen.

## Files
- `code/demo.html` runs on its own and loops. A scripted cursor does the click.
- `media/poster.jpg` is a still of the component.

## Credit
Idea: "Button" by originui on 21st.dev (https://21st.dev/@originui/components/button/button-with-badge), MIT. This demo is an original recreation written from the public preview.

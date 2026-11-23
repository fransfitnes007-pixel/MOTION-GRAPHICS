---
name: address-bar-domain-typewriter-substring-slice-chip
description: "The URL in a browser bar types out a new domain while a green tick chip pops up. Use it to show a site moving to a custom domain, or any rename-in-place moment."
---

# Address bar domain typewriter

**Code name:** Substring slice typing with pop-in chip.

## What you see
A browser window shows a page at a platform address. The address pill reads "alex.brand.link". On the spoken word "own" it is replaced by "y" and then types out "yourname.com" at a steady rate over 0.7s. A green tick chip, "Your domain, connected", springs in over the top-right corner of the window from 60% size. It stays for about a second, then fades out.

## When to use it
Any moment where an address changes: custom domain, rename, migration, a link shortening. Pair it with keystroke sounds. It is only the address; do not use it for long URLs because the typing rate is fixed by the duration.

## How it works
The address text is not animated by CSS. Every frame the code slices the final string by a progress value and writes the result to the pill.

```js
const dom = 'yourname.com', tp = seg(t, OWN - .05, DOMAIN + .35)
u.textContent = t < OWN - .05 ? 'alex.brand.link' : dom.slice(0, Math.max(1, Math.round(tp * dom.length)))
const dq = spring(seg(t, DOMAIN + .1, DOMAIN + .6), 8, 12)     // chip: scale .6 + .4 * dq
```

Because the string is a pure function of `t`, scrubbing backwards un-types it. The chip is a standard green tick pattern.

## Numbers that matter
- Typing: `seg` over 1.02s starting 0.05s before the word; 12 characters.
- Chip: `spring(k=8, f=12)` over 0.5s, scale .6 to 1, opacity `clamp(dq*1.5)`; fades with `ei` over 0.2s.
- Chip: 26px bold, white at .94, green tick circle `#16a34a`.
- Window: as in the browser window skill, zoom 1.12.

## Sound

## Adapt it
- The old and new address strings.
- The typing window (`OWN2` to `DOMAIN + .35`).
- The chip text and colour (green for success).
- Chip position; it hangs off the top-right corner of the window.

## Files
- `code/demo.html` runs on its own and loops. Domain strings are neutral placeholders.

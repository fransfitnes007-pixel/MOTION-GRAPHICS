---
name: sectioned-dropdown-search-list-filter-popover-section-headers
description: A dark search-as-you-type dropdown with grouped options under small headings. Reach for it for country, region or category pickers on checkout and settings forms.
---

# Searchable country dropdown with section headings

**Code name:** Filter popover with section headers.

## What you see
A 256px field labelled "Country" has a rounded input (placeholder `Search countries...`) with a chevron at the right. Below it, 6px away, a popover (#18181a, 20px radius, soft shadow) lists items in groups. Each group has a small grey heading (`North America`, `Europe`, `Asia`) and 36px rows in white 14px; a 1px line separates groups. The list is taller than the popover (max 319px) so it scrolls; the clip freezes it open with United States to Spain visible.

The demo plays a full use. The list opens with a short scroll to show Asia. At 2.2s the field takes focus (blue ring), `a` and `n` are typed and the list filters to Canada, France, Germany and Japan, with headings kept only for groups that still have a match. France is hovered at 3.5s and clicked at 4.05s: the popover scales away in 0.22s, the box shows France and the chevron flips down. A click on the chevron at 5.7s reopens it with a tick beside France; it closes again at 7.9s.

## When to use it
Long pick lists that read better in groups: countries by continent, timezones by region, products by category. Not for under about eight options, where a plain select is simpler.

## How it works
One flat list of rows (`hd` heading, `it` item, `sepr` line) is filtered by the typed text; a heading and the line above it are hidden when none of its items match. The popover is `max-height` clipped and its inner list moves with `translateY` for the scroll.

```js
r.ok = !q || r.name.toLowerCase().includes(q.toLowerCase())
heading visible  = some item of that section is ok
popover: opacity = open, scale = .96 + .04 * open       // 0.2 to 0.22s
chevron rotate   = open > .5 ? 0 : 180
```

The clip shows only the open list. Filtering, selecting, the tick and the close animation are rebuilt from how a standard combo box behaves.

## Numbers that matter
| | |
|---|---|
| Field | 256px wide, 40px input, 14px radius |
| Popover | 20px radius, 6px gap, 319px max height, rows 36px |
| Sections | North America (3), Europe (5), Asia (4) |
| Open / close | 0.2 to 0.22s scale and fade |
| Loop | 9.2s |

## Sound
Silent.

## Adapt it
- `CONFIG.sections` for your groups and items.
- `CONFIG.typed` and `CONFIG.pick` for what gets typed and chosen.
- `CONFIG.popoverMaxHeight` for how much shows before it scrolls.
- `CONFIG.accent` for the focus ring.

## Files
- `code/demo.html` runs on its own and loops; every frame is `render(t)`. Edit the `CONFIG` block at the top of its script.
- `media/poster.jpg` is the page's preview image.

## Credit
Idea: "ComboBox" by hero_ui on 21st.dev (https://21st.dev/@hero_ui/components/heroui-combo-box/with-sections), MIT. This demo is an original recreation written from the public preview.

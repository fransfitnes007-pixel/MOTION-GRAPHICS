---
name: dark-map-marker-hover-tooltip-scale-and-label-pop
description: A dark vector map with blue circle markers and white hover tooltips. Reach for it for store locators, delivery maps and any map where pins need a name on hover.
---

# Dark map marker hover tooltip

**Code name:** Scale and label pop.

## What you see
A rounded, thinly bordered map frame, 960px wide here, on a near-black page. The first two seconds in the preview the map tiles are still loading: only a corner of map and three blue dots (Central Park, Times Square, Empire State Building) over a dark void, with a small "CARTO, OpenStreetMap contributors" credit bottom right. Then the tiles arrive: a dark grey-blue street map of the New York area, with bright white place names (Hoboken, Jersey City, NEW YORK), water in lighter grey, thin roads and a round white info button replacing the credit. Hovering a marker scales it to about 110% and shows a small white rounded label with black text directly above, with a few pixels of gap, fading in over about 0.15s. Moving off removes it.

## When to use it
Store locators, delivery or pickup maps, property listings, event maps: any map where each pin should say its name on hover without a click. On touch screens hover does not exist, so pair it with tap-to-open.

## How it works
The map itself is MapLibre (via the mapcn wrapper); markers are DOM elements positioned on it. The marker is a `size-5` blue circle with a 2px white border and `hover:scale-110`. `MarkerTooltip` renders a white label anchored above the marker. In the usage code three `MapMarker`s with `MarkerContent` and `MarkerTooltip` children are placed at longitude and latitude pairs.

The demo does not use a map. It draws a placeholder dark map in SVG (fixed-seed road lines, water shapes, bold place names) so it runs with no network, fades it in at 2.1s like the tile load, and scripts a cursor that rests on three markers in turn.

```js
marker: scale(1 + .1*k)
tooltip: opacity k, top = marker.y - 12 - 6 - tooltipHeight + (1-k)*6
```

The real map style is CARTO dark; the placeholder only matches its tone and label weight, not its geometry. Panning and zooming are not recreated.

## Numbers that matter
| | |
|---|---|
| Frame | 960x450, 12px radius, 1px `#2a2c30` border |
| Marker | 24px circle, `#3b82f6`, 2.5px white border, hover scale 1.1 |
| Tooltip | white, 16px black text, 6px radius, 4px 10px padding, about 6px above the marker, fade .15s |
| Map colours | land `#0f1011`, water `#262b33`, roads `#34383d`, labels `#b4b7bd` |
| Timing | tiles in at 2.1s over .4s, hovers 2.5, 4.1, 5.4s, loop 7s |

## Sound
Silent.

## Adapt it
- `markers`: positions and names.
- `markerColor`, `water`, `land`, `road`, `label` for another map style.
- `hovers`: the cursor sequence.
- In a real project, keep the usage code and only restyle the marker and tooltip classes.

## Files
- `code/demo.html` runs on its own and loops. Everything is read from the `CONFIG` object at the top of the script.
- `media/poster.jpg` is one frame of it.

## Credit
Idea: "MarkerTooltip" by mapcn on 21st.dev (https://21st.dev/@mapcn/components/mapcn-marker-tooltip), MIT. This demo is an original recreation written from the public preview.

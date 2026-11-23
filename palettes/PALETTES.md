# Palettes

Every colour look used across the kit. `palettes.json` has the same data, plus the colours of all 221 library pieces. Open `index.html` to see the swatches.

## Arizona sunset (pixel dino reel) (`arizona-sunset`)

Dithered pixel sky behind a runner game; warm, scenic, reads well on phones. Type stays in the dark UI colours.

- **Sky:** `#1A0A38` `#35104F` `#641A63` `#A3285F` `#D9414A` `#F46A33` `#FF9A35` `#FFC65A`
- **Dusk:** `#0A0520` `#170838` `#33104F` `#641A66` `#A52A62` `#DD4D48` `#F47A36` `#FFAB45`
- **Floor:** `#3A1638` `#241028` `#150A1C` `#0A0510`
- **Sun:** `#FFF3B0` `#FFD670` `#FF9D4A`
- **Silhouette / rim:** `#170B20` / `#FFB057`; type on `#161619` cards
- **Example:** `motion-graphics/dino-runner-arizona-sunset__pixel-dithered-sky-mesa-parallax`

## Pictogram parable (black and white) (`pictogram-mono`)

Faceless explainer reels: white pictogram people on a dashed ground, black dot-grid background, white capsule tags, one soft glow behind the subject. Colour only on the end card.

- **Background:** `#000000`
- **Dot grid:** `rgba(255,255,255,0.075)`
- **Ink:** `#FFFFFF`
- **Grey people:** `#8F8F8F` `#A6A6A6` `#B0B0B0`
- **Labels:** `#BDBDBD`
- **Tag fill:** `#FFFFFF`
- **Tag text:** `#000000`
- **Example:** `pipelines/pictogram-reel`

## Dark ember title beats (`dark-ember`)

Black stage, white words, one hot orange-to-pink accent on the key word or card.

- **Colours:** `#000000` `#0B0B10` `#FFFFFF` `#FF6A3D` `#FF2E97` `#111111`
- **Example:** `motion-graphics/dark-ember-title-beat__word-reveal-inline-card`

## Gold and black book film (`gold-book`)

Long-form, premium: black, warm gold gradients on serif titles (Playfair, Rye), red accent for dates.

- **Colours:** `#000000` `#07080B` `#17120E` `#E8B43A` `#FFC766` `#E8C25A` `#FFB347` `#D8463A`
- **Example:** `motion-graphics/gold-timeline-rail__progress-fill-year-ticks`

## Violet AI dashboard (`violet-ai`)

Product films for AI tools: deep navy-black, violet glow, lavender text, one orange score accent.

- **Colours:** `#0B0B17` `#000000` `#8A5CFF` `#A7A6BD` `#E9E8F5` `#FF9A4D` `#FFFFFF`
- **Example:** `motion-graphics/violet-ai-dashboard-score-ring-push-in__counting-ring-glow-`

## Chrome wordmark and cobalt CTA (`chrome-cobalt`)

End cards and logo reveals: black, liquid-chrome logo, cobalt-to-sky blue button.

- **Colours:** `#000000` `#0B0B10` `#FFFFFF` `#2563EB` `#2F6BFF` `#38BDF8`
- **Example:** `motion-graphics/chrome-wordmark-end-card__blur-resolve-cta`

## LED dot rainbow word (`rainbow-led`)

One pivot word in a conic rainbow dot mask on black.

- **Colours:** `#000000` `#0B0B10` `#FF2E97` `#38BDF8` `#FFFFFF` `#2A2A2E`
- **Example:** `motion-graphics/led-dot-rainbow-word__conic-gradient-dot-mask`

## Light studio with drifting orbs (`light-studio`)

Bright, clean SaaS films: off-white stage, near-black ink, soft indigo and sky orbs.

- **Colours:** `#F4F4F6` `#F2F2F4` `#0B0B10` `#141028` `#5B5CE6` `#60A5FA`
- **Example:** `motion-graphics/light-orb-dot-background__blurred-orbs-drift`

## Cream and click yellow (`cursor-yellow`)

Screen-demo moments: dark stage, cream cards, a yellow cursor ripple.

- **Colours:** `#07080B` `#0B0C10` `#F3F1EA` `#FFD814` `#FFFFFF`
- **Example:** `motion-graphics/cursor-click-ripple__eased-keyframe-path`

## Using a palette

Tell Claude: *"Use the arizona-sunset palette for this reel"*. The `brand-setup` skill reads `palettes.json` and writes the colours into the piece's `CONFIG` block. Your own brand colours live in `brand.config.json`.

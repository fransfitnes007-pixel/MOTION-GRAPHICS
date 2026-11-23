---
description: "White-label the kit for a brand (name, domain, handle, colours, logo, app icon, App Store card)"
argument-hint: "[brand name and details, or \"from brand.config.json\"]"
---

Brand details: $ARGUMENTS

Use the `brand-setup` skill. Fill `brand.config.json` from what the user gave (ask only for what is missing and needed), run `engine/tools/apply_brand.py --dry-run`, then apply it, rebuild the index and render one branded still to show the result.

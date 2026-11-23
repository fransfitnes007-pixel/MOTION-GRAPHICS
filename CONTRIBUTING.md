# Contributing

New pieces, formats and fixes are welcome.

- **A new library piece:** follow `engine/SKILL-SPEC.md`. One folder per effect, a `demo.html` where every frame is `render(t)`, no network requests, placeholder copy only. Run `node engine/tools/verify_library.cjs <slug>` and `node engine/tools/make_posters.cjs <slug>` before opening a pull request.
- **A new format:** add it to `docs/FORMATS.md` with its beat sheet, look, sound, lessons, and a short and a detailed prompt; add the prompts to `prompts/PROMPTS.md`.
- **Never commit:** footage or audio you do not own, real people's faces or names, client names, API keys, `.env` files, or reference videos (they belong in the git-ignored `reference/` folder).
- Keep the brand placeholders (`YourBrand`, `yourbrand.com`, `@yourbrand`) in committed files so `engine/tools/apply_brand.py` keeps working for everyone.

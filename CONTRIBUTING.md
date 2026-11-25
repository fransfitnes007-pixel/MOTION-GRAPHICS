# Contributing

New pieces, formats and fixes are welcome.

- **A new library piece:** follow `engine/SKILL-SPEC.md`. One folder per effect, a `demo.html` where every frame is `render(t)`, no network requests, placeholder copy only. Run `node engine/tools/verify_library.cjs <slug>` and `node engine/tools/make_posters.cjs <slug>` before opening a pull request.
- **A new format:** add it to `docs/FORMATS.md` with its beat sheet, look, sound, lessons, and a short and a detailed prompt; add the prompts to `prompts/PROMPTS.md`.
- **Never commit:** footage or audio you do not own, real people's faces or names, client names, API keys, `.env` files, or reference videos (they belong in the git-ignored `reference/` folder).
- Keep the brand placeholders (`YourBrand`, `yourbrand.com`, `@yourbrand`) in committed files so `engine/tools/apply_brand.py` keeps working for everyone.
- **Licence gate:** MIT, ISC, Apache and your own builds go in, credited in `meta.json` (`credit`) and `THIRD_PARTY_NOTICES.md`. A component whose page shows no licence, or anything derived from a site whose terms forbid building a library from it, stays out (list it in `docs/LOCAL-LIBRARY-ONLY.md` instead). Recreations of public videos are original code with placeholder copy and credit the creator; never include their footage, frames, audio or prompt text.
- **Agents working at once:** see `AGENTS.md` (one build folder per agent, locks for shared resources, one index rebuild at the end, leak scan before a commit).

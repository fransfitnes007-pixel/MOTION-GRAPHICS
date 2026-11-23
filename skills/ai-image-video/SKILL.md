---
name: ai-image-video
description: "Generate images and short video clips with AI models for motion-graphics and short-form projects, with a style lock, batching, polling and a review-before-use step. Use when a project needs generated stills, backgrounds, b-roll, start frames or image-to-video clips."
---

# AI image and video generation

Prefer local or open tools first (for example ComfyUI or diffusers with open image models, and open video models if the machine has a GPU). Use paid cloud providers only when quality or speed needs them, and only with the user's own key.

## Keys and cost
- Bring your own key through an environment variable (`FAL_KEY`, `GEMINI_API_KEY`, `REPLICATE_API_TOKEN`, or the provider's own name). Never write a key into a file, a prompt, a commit or a log. If the variable is missing, tell the user which one to set and stop.
- Generation costs money per call. Say the approximate count of calls before a batch, test with one, then scale.

## Pick the tool by job
| Job | Options (examples, not endorsements) |
|---|---|
| Fast concept stills | Local diffusion model; hosted fast image models |
| High quality or text-in-image | Larger hosted image models |
| Edit an existing image (change, extend, remove background) | Image-edit models that take a source image |
| Image-to-video (animate a start frame) | Hosted image-to-video models; local open video models on a GPU |
| Text-to-video b-roll | Same; expect short clips (5 to 10 s) |
Provider lineups change quickly; check the provider's current model list before choosing.

## Workflow
1. **Style lock.** One or two reference images, palette as hex values, aspect ratio (9:16 for vertical, 16:9, 1:1), and constraints such as "no on-image text" or "no faces". Reuse the same block in every prompt.
2. **Prompt.** Subject, composition, lighting, lens or camera feel, mood, background, negative space for overlay text. For video prompts describe motion and camera only; the start frame carries appearance.
3. **Batch.** For ad or thumbnail variants, run 4 to 8 from one concept varying angle, subject or mood. For carousels keep one cover plus body slides in a locked style.
4. **Submit, poll, save.** Queue-style APIs return a job id: submit, poll status, download. `scripts/queue_job.sh <model-path> input.json result.json` does this for a fal-style queue; adapt the URLs for other providers. Save into a dated folder with the prompt next to each output.
5. **Review every asset** for artifacts (hands, text, faces, logos that look real), consistency with the style lock, and rights. Reject and regenerate rather than patching with edits.
6. **Prepare for video editing**: upscale or crop to the delivery size, then use media-processing.

## Image prompts that work
- Concrete over generic: "matte ceramic mug on oak desk, soft window light from left, shallow depth of field" beats "nice coffee photo".
- Say what to leave out. Add "candid phone photo" for a UGC feel, "studio, softbox" for product.
- Keep one idea per image; compose empty space where captions will sit.

## Realism and trust
- Real photos of the real product, team or work beat synthetic ones when the viewer is being asked to trust something. Use generated imagery for backgrounds, concepts and b-roll, not as fake proof.
- Do not generate real people's likenesses without permission, or content that implies endorsements, results or events that did not happen. Label synthetic media where required.
- Add alt text to any image used on a page, and compress for the web (WebP under about 300 KB for heroes).

## Output record
```
CONCEPT / PATTERN: carousel | variants | hero options | video
STYLE LOCK: references, palette, ratio, constraints
MODEL + SETTINGS: provider, model, seed if available
COUNT: n (approx cost: ask the user to check the provider's pricing)
SAVED TO: dated folder
REVIEW: pending approval before use
```

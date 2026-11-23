---
name: ugc-video-playbook
description: "Repeatable pipeline for making UGC-style vertical videos: scene brief, script and beats, start frame, image-to-video generation with a consistent character, edit and delivery. Use when planning or producing short-form talking, lifestyle or product videos, especially with AI-generated or AI-assisted footage."
---

# UGC-style vertical video playbook

Works with real footage, AI-generated footage, or a mix. Only use a real person's likeness with their written permission, and label synthetic content where the platform or the law requires it.

## Step 0: Character and reference bank (if a recurring on-screen person)
Keep a folder per character with at least 4, ideally 6 reference images: a clean frontal neutral close-up (required), a frontal expression, a profile or three-quarter, an alternate angle, optionally full body. Write a short character profile (age range, look, voice, wardrobe rules). Fork this playbook per character and log proven prompts at the bottom.

## Step 1: Idea and script (short-form writing)
- Write for one specific viewer, as if sending the video to them.
- Hook: a concrete object, number or claim that opens a question. Value lands by 5 to 10 s. Open a fresh loop about two thirds through. Cut every line that does not serve the hook's promise.
- Plain, short sentences that a newcomer can follow.
- Frame the request as Role, Context, Command, Format when delegating to a model.
- Draft only; a person approves before anything is posted.

## Step 2: Scene brief (per shot)
Camera angle, framing, what is visible, gaze direction, outfit, lighting, environment, action beats in order, camera behaviour (static, slow push, handheld drift), vibe (candid phone footage, cinematic, vlog).

## Step 3: Start frame
Generate a 9:16 still with an image model (see ai-image-video). Prompt covers composition, pose, wardrobe, lighting, environment, props. For a locked character, make the start-frame person look clearly different from the target so a later face step is not confused, then apply the character with a reference-based or face-swap tool you are licensed to use. Add "candid phone footage" to avoid an over-polished look.

## Step 4: Generate the clip
Use an image-to-video model with character references. Prompt rules:
- Motion, action beats and camera behaviour only; do not re-describe appearance or setting (the start frame holds them).
- Refer to the character by the model's reference tag, and sequence beats: "Character does X. Then Y. Then Z."
- State the camera explicitly: "Camera stays completely static."
- Two or three beats for a 5 s clip; 8 to 10 s for a single scene; use multi-shot for longer.
- Generation is queued: submit, poll, download. Costs money per clip, so iterate at 5 s first.

## Step 5: Edit and deliver
- Voiceover: record real, or use local TTS, or the optional cloud voice skill. Transcribe for captions (transcribe skill).
- Cuts every 1 to 3 s, cutaways instead of a long talking head, captions inside the safe area, music low under voice.
- Fit and export with the media-processing skill. Check the first and last 3 seconds.

## Troubleshooting
| Problem | Fix |
|---|---|
| Video ignores the action | Fewer beats, add timing words ("after a moment", "then") |
| Face does not hold | Cleaner, well-lit frontal reference; add more angles |
| Composition drifts | Make the start-frame prompt more specific |
| Looks too cinematic | "Candid phone footage" in the start frame, "camera stays static" in the video prompt |
| Hands or text look wrong | Crop them out, cover with real UI or overlays, or use a real clip |

## Log
Keep a "Proven concepts" list: prompt, settings, seed or reference set, result, what to change next time.

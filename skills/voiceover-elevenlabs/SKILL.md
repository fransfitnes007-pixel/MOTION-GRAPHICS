---
name: voiceover-elevenlabs
description: "Optional cloud voiceover with ElevenLabs text-to-speech, using the user's own API key. Use when a project needs a narration track and a local TTS voice is not good enough; covers voice choice, tuning, pacing and syncing. Prefer local TTS first."
---

# Voiceover with ElevenLabs (optional, bring your own key)

## Local first
Try a local text-to-speech engine before a cloud one (for example Piper, Kokoro or the OS voices). Use a cloud voice only if the user wants it, and say that the script text is sent to the provider.

## Key
Set `ELEVENLABS_API_KEY` in the environment. Never put a key in a file, prompt, commit or log. If it is not set, ask the user to set it and stop. Free tiers exist with limited characters; paid use is billed to the key's owner.

## Choosing a voice
Do not rely on remembered voice IDs. List what the account can use and let the user audition:
```bash
curl -s "https://api.elevenlabs.io/v2/voices?page_size=50" -H "xi-api-key: $ELEVENLABS_API_KEY" | python3 -c 'import sys,json;[print(v["voice_id"],v["name"],v.get("labels",{})) for v in json.load(sys.stdin)["voices"]]'
```
Each entry has a `preview_url` to listen to. Premade library voices include, by name, Rachel, Sarah, Charlotte, Alice, Matilda, Lily, Adam, Josh, Antoni, Daniel, George, Bill, Charlie and Liam. Look up the current ID in the listing rather than hard-coding one.
Match voice to content: energetic and warm for lifestyle and UGC, calm and low for explainers and brand films, crisp and neutral for tutorials. Only use a cloned voice of a person who gave permission.

## Generate
```bash
curl -s -X POST "https://api.elevenlabs.io/v1/text-to-speech/$VOICE_ID" \
  -H "xi-api-key: $ELEVENLABS_API_KEY" -H "Content-Type: application/json" \
  -d '{"text":"Your script here.","model_id":"eleven_multilingual_v2","voice_settings":{"stability":0.45,"similarity_boost":0.75,"style":0.2,"speed":1.0}}' \
  --output voice.mp3
```
Model names change; check the provider docs for the current flash (fast, cheaper) and multilingual (higher quality) models.

## Tuning
| Setting | Low | High |
|---|---|---|
| stability | more expressive, less predictable (good for casual UGC, 0.3 to 0.5) | steadier, flatter (narration, 0.6 to 0.8) |
| similarity_boost | looser | closer to the source voice (0.7 to 0.85 is typical) |
| style | neutral | more exaggerated; raise slowly, it can add artifacts |
| speed | 0.7 slower | 1.2 faster; short-form often sits near 1.05 to 1.15 |
Change one setting at a time and keep the same line to compare.

## Writing for the ear
- Short sentences. Write numbers the way they are spoken ("twenty-eight hundred dollars").
- Use commas and full stops for pacing; use "..." sparingly. Spell tricky names phonetically.
- Generate per paragraph or per scene, not one long block; it is easier to retake and sync.

## After generation
- Transcribe with the `transcribe` skill to get word timestamps, then line cuts and captions to the words.
- Normalise loudness to about -14 LUFS and duck music under the voice (media-processing).
- Listen through once for mispronunciations before using it.

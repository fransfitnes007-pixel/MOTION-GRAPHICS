"""Design new voices from a text description and save each as a reusable clone reference.
Usage: .venv/bin/python design.py name="description" [name2="description" ...]
Writes voices/<name>_ref.wav and adds <name> to voices/voices.json (clone mode). Re-run a name to re-roll it."""
import sys, os, json, subprocess, numpy as np, soundfile as sf
HERE = os.path.dirname(os.path.abspath(__file__)); MODELS = os.environ.get("VOICE_MODELS", os.path.join(HERE, "models")); VJ = os.path.join(HERE, "voices", "voices.json")
REF_TEXT = "Okay wait. You're telling me I can build the whole thing from my phone, with zero experience, in like ten minutes? Yeah. I typed one sentence, hit generate, and it gave me something that actually works, with a clean design and a dark mode toggle."
from mlx_audio.tts.utils import load_model
m = load_model(os.path.join(MODELS, "mlx-community__Qwen3-TTS-12Hz-1.7B-VoiceDesign-8bit"))
cfg = json.load(open(VJ))
for a in sys.argv[1:]:
    name, ins = a.split("=", 1)
    res = list(m.generate_voice_design(text=REF_TEXT, language="English", instruct=ins))
    audio = np.concatenate([np.array(r.audio) for r in res]); raw = os.path.join(HERE, "voices", name + "_raw.wav"); sf.write(raw, audio, res[0].sample_rate)
    ref = os.path.join(HERE, "voices", name + "_ref.wav")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-af", "silenceremove=start_periods=1:start_threshold=-40dB:start_silence=0.03", "-ar", "24000", "-ac", "1", ref], check=True); os.remove(raw)
    cfg[name] = {"mode": "clone", "model": "mlx-community__Qwen3-TTS-12Hz-1.7B-Base-8bit", "ref_audio": name + "_ref.wav", "ref_text": REF_TEXT, "design": ins}
    print(name, round(len(audio) / res[0].sample_rate, 1), "s", flush=True)
json.dump(cfg, open(VJ, "w"), indent=1)

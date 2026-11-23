"""Long voiceover, recorded line by line so pitch and pace stay locked.
Usage: .venv/bin/python reel_vo.py <voice> <script.txt (one paragraph per line)> <out.wav> [--pace 5.0] [--f0 130-165] [--gap 0.14] [--max-tempo 1.3]
Each line is generated up to 4 times until its median pitch is inside --f0, paced on its own, then joined."""
import sys, os, json, subprocess, wave, numpy as np, soundfile as sf
import voice as V
args = sys.argv[1:]
def opt(name, default):
    if name in args: i = args.index(name); v = args[i+1]; del args[i:i+2]; return v
    return default
V.PACE = float(opt("--pace", V.CFG["pace"]["syllables_per_second"])); lo, hi = map(float, opt("--f0", "0-1000").split("-")); gap = float(opt("--gap", 0.14)); V.MAX_TEMPO = float(opt("--max-tempo", 1.3))
who, script, out = args; v = V.CFG[who]
out = os.path.abspath(out)   # the concat list resolves paths relative to itself, so keep everything absolute
def f0med(path):
    tmp = path + ".16k.wav"; subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", path, "-ac", "1", "-ar", "16000", tmp])
    w = wave.open(tmp); x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768; os.remove(tmp); f = []
    for i in range(0, len(x) - 640, 320):
        s = x[i:i+640]
        if np.sqrt(np.mean(s ** 2)) < 0.02: continue
        s = s - s.mean(); ac = np.correlate(s, s, "full")[639:]; ac /= ac[0] + 1e-9; k = np.argmax(ac[40:228]) + 40
        if ac[k] > 0.5: f.append(16000 / k)
    f = np.array(f); return float(np.median(f)), float(12 * np.log2(np.percentile(f, 90) / np.percentile(f, 10)))
from mlx_audio.tts.utils import load_model
model = load_model(os.path.join(V.MODELS, v["model"]))
def gen(text):
    if v["mode"] == "clone": return list(model.generate(text=text, ref_audio=os.path.join(V.HERE, "voices", v["ref_audio"]), ref_text=v["ref_text"], language="English"))
    if v["mode"] == "kokoro": return list(model.generate(text=text, voice=v["voice"], speed=float(v.get("speed", 1.0)), lang_code="a"))
    kw = {k: v[k] for k in ("temperature", "top_p", "top_k") if k in v}
    return list(model.generate_custom_voice(text=text, speaker=v["speaker"], language="English", instruct=v.get("instruct", ""), **kw))
lines = [l.strip() for l in open(script) if l.strip()]; parts = []; report = []
for n, text in enumerate(lines):
    best = None
    for attempt in range(4):
        res = gen(text); audio = np.concatenate([np.array(r.audio) for r in res]); raw = f"{out}.{n}.raw.wav"; sf.write(raw, audio, res[0].sample_rate)
        # keep the tail: a little room tone after the last word so the pause trim cannot clip a final consonant
        padded = f"{out}.{n}.pad.wav"; subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-af", "apad=pad_dur=0.05", padded], check=True)
        piece = f"{out}.{n}.{attempt}.wav"; rate, tempo, d = V.pace(padded, piece, text, float(v.get("pitch", 0))); os.remove(raw); os.remove(padded)
        f, st = f0med(piece); miss = (0 if lo <= f <= hi else min(abs(f - lo), abs(f - hi))) + 60 * max(0, tempo - 1.22)
        if best is None or miss < best[0]: best = (miss, piece, f, st, tempo, d)
        if miss == 0: break
    parts.append(best[1]); report.append(dict(line=n + 1, f0=round(best[2]), semitones=round(best[3], 1), tempo=best[4], seconds=best[5], tries=attempt + 1)); print(json.dumps(report[-1]), flush=True)
sil = out + ".sil.wav"; subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono", "-t", str(gap), sil], check=True)
lst = out + ".txt"; open(lst, "w").write("".join(f"file '{p}'\nfile '{sil}'\n" for p in parts))
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-af", "loudnorm=I=-14:TP=-1.5:LRA=7,aresample=48000", "-ac", "1", out], check=True)
for p in os.listdir(os.path.dirname(out)):
    full = os.path.join(os.path.dirname(out), p)
    if full.startswith(out + ".") : os.remove(full)
json.dump(report, open(out.replace(".wav", ".report.json"), "w"), indent=1); print("wrote", out, round(V.dur(out), 1), "s")

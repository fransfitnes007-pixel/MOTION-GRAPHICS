"""Local voiceover for reels. Usage:  .venv/bin/python voice.py <voice> <script.txt> <out.wav> [--raw] [--pace 5.0]
<voice> is a key in voices/voices.json. --pace = syllables per second (a typical viral narration measures about 3.9;
4.5 is brisk, 5.0 fast, 5.5 very fast). Default is in voices/voices.json.
Cuts dead air, matches the pace, loudness -14 LUFS, 48 kHz mono.
Several jobs in one go (model loads once):  voice.py <voice> --batch a.txt:a.wav b.txt:b.wav ..."""
import sys, os, json, re, time, subprocess, numpy as np, soundfile as sf
HERE = os.path.dirname(os.path.abspath(__file__)); CFG = json.load(open(os.path.join(HERE, "voices", "voices.json")))
MODELS = os.environ.get("VOICE_MODELS", os.path.join(HERE, "models"))   # where setup.sh put the model folders
def syllables(text):
    def syl(w):
        w = re.sub(r"[^a-z]", "", w.lower())
        if not w: return 0
        n = len(re.findall(r"[aeiouy]+", w))
        if w.endswith("e") and not w.endswith(("le", "ee")) and n > 1: n -= 1
        if w.endswith("ed") and not w.endswith(("ted", "ded")) and n > 1: n -= 1
        return max(1, n)
    return sum(syl(w) for w in re.findall(r"[A-Za-z']+", text))
def dur(p):
    o = subprocess.run(["ffmpeg", "-hide_banner", "-i", p, "-f", "null", "-"], capture_output=True, text=True).stderr
    h, m, s = re.findall(r"time=(\d+):(\d+):([\d.]+)", o)[-1]; return int(h) * 3600 + int(m) * 60 + float(s)
TRIM = "silenceremove=start_periods=1:start_threshold=-40dB:start_silence=0.03,silenceremove=stop_periods=-1:stop_duration=0.16:stop_threshold=-40dB:stop_silence=0.08"
MAX_TEMPO = 1.5  # ceiling on the time-stretch
PACE = None  # --pace override, syllables per second
def pace(raw, out, text, semis=0.0):
    tmp = out + ".tight.wav"; f = TRIM
    if semis:
        r = 2 ** (semis / 12); f = f"asetrate=24000*{r:.5f},aresample=24000,atempo={1/r:.5f}," + TRIM
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-ar", "24000", "-af", f, tmp], check=True)
    target, tol = PACE or CFG["pace"]["syllables_per_second"], CFG["pace"]["tolerance"]
    rate = syllables(text) / dur(tmp); tempo = 1.0 if abs(rate - target) / target <= tol else max(0.8, min(MAX_TEMPO, target / rate))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp, "-af", f"atempo={tempo:.3f},loudnorm=I=-14:TP=-1.5:LRA=7,aresample=48000", "-ac", "1", out], check=True)
    os.remove(tmp); return round(rate, 2), round(tempo, 2), round(dur(out), 1)
def main():
    global PACE
    who = sys.argv[1]; v = CFG[who]; raw_only = "--raw" in sys.argv
    args = [a for a in sys.argv[2:] if a != "--raw"]
    if "--pace" in args: i = args.index("--pace"); PACE = float(args[i+1]); del args[i:i+2]
    jobs = [a.split(":", 1) for a in args[1:]] if args[0] == "--batch" else [[args[0], args[1]]]
    from mlx_audio.tts.utils import load_model
    t0 = time.time(); model = load_model(os.path.join(MODELS, v["model"])); load_s = time.time() - t0
    for script, out in jobs:
        text = " ".join(open(script).read().split()); t = time.time()
        if v["mode"] == "clone":
            res = list(model.generate(text=text, ref_audio=os.path.join(HERE, "voices", v["ref_audio"]), ref_text=v["ref_text"], language="English"))
        elif v["mode"] == "kokoro":
            res = list(model.generate(text=text, voice=v["voice"], speed=float(v.get("speed", 1.0)), lang_code="a"))
        else:
            kw = {k: v[k] for k in ("temperature", "top_p", "top_k") if k in v}
            res = list(model.generate_custom_voice(text=text, speaker=v["speaker"], language="English", instruct=v.get("instruct", ""), **kw))
        audio = np.concatenate([np.array(r.audio) for r in res]); sr = res[0].sample_rate
        raw = out + ".raw.wav"; sf.write(raw, audio, sr); gen_s = time.time() - t
        if raw_only: os.replace(raw, out); info = {}
        else:
            rate, tempo, d = pace(raw, out, text, float(v.get("pitch", 0))); os.remove(raw); info = dict(native_syl_per_s=rate, tempo=tempo, final_s=d)
        print(json.dumps(dict(voice=who, out=out, load_s=round(load_s, 1), gen_s=round(gen_s, 1), raw_s=round(len(audio) / sr, 1), **info)), flush=True)
if __name__ == "__main__": main()

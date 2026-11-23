#!/usr/bin/env python3
"""Measure a reference video you want to recreate: cuts, voice pace, pauses, and the sound design under the voice.
  python3 analyze_reference.py reference.mp4 [out_dir]          (needs ffmpeg, numpy, scipy; optional faster-whisper)
Writes to out_dir (default ./analysis):
  report.json     - scene cuts, words per minute, syllables per second, pauses, voice pitch, sfx onsets, music beat
  spectrum_*.png  - 12 s spectrogram strips: top = sound with the voice cancelled (side channel), bottom = full mix
  transcript.json - word timestamps, when faster-whisper is installed
How the sound part works: most reels keep the voice dead centre and music/sfx in stereo, so left minus right removes the
voice and leaves the bed and effects. Clicks are short bright transients (rise 10-25 ms), swishes are 150-400 ms swells of
1.5-7 kHz noise, thuds are low hits with a 100-300 ms tail. A mono file has no side channel; then only the pauses are measured."""
import json, os, re, subprocess, sys, math
import numpy as np, scipy.io.wavfile as wf, scipy.signal as sg
src = sys.argv[1]; out = sys.argv[2] if len(sys.argv) > 2 else "analysis"; os.makedirs(out, exist_ok=True)
FF = os.environ.get("FFMPEG", "ffmpeg"); wav = os.path.join(out, "audio.wav")
subprocess.run([FF, "-y", "-loglevel", "error", "-i", src, "-vn", "-ac", "2", "-ar", "48000", wav], check=True)
sr, x = wf.read(wav); x = x.astype(np.float64) / 32768; L, R = x[:, 0], x[:, 1]; M = (L + R) / 2; S = (L - R) / 2
db = lambda a: round(20 * math.log10(math.sqrt(float(np.mean(a ** 2))) + 1e-12), 1)
rep = {"duration_s": round(len(M) / sr, 2), "mix_db": db(M), "side_db": db(S), "stereo_correlation": round(float(np.corrcoef(L, R)[0, 1]), 3)}
stereo = rep["side_db"] > rep["mix_db"] - 42 and rep["stereo_correlation"] < 0.9995
# scene cuts
# scene scores for every frame, then peaks: dark motion-graphics reels change softly, so the threshold adapts to the video
o = subprocess.run([FF, "-hide_banner", "-i", src, "-vf", "scale=180:-2,select='gte(scene,0)',metadata=print", "-an", "-f", "null", "-"], capture_output=True, text=True).stderr
ts = np.array([float(v) for v in re.findall(r"pts_time:([0-9.]+)", o)]); sc = np.array([float(v) for v in re.findall(r"scene_score=([0-9.]+)", o)])
n = min(len(ts), len(sc)); ts, sc = ts[:n], sc[:n]
if n > 10:
    fps = n / max(ts[-1], 1e-6); pk, _ = sg.find_peaks(sc, height=max(0.015, float(np.percentile(sc, 96))), distance=max(1, int(fps * 0.4)))
    rep["cuts_s"] = [round(float(ts[i]), 2) for i in pk]
else: rep["cuts_s"] = []
c = rep["cuts_s"]; rep["mean_shot_s"] = round(rep["duration_s"] / (len(c) + 1), 2)
# words, pace, pauses
try:
    from faster_whisper import WhisperModel
    segs, _ = WhisperModel("small", compute_type="int8").transcribe(wav, word_timestamps=True)
    words = [(w.start, w.end, w.word.strip()) for s in segs for w in s.words]
    json.dump(words, open(os.path.join(out, "transcript.json"), "w"), indent=0)
    def syl(w):
        w = re.sub(r"[^a-z]", "", w.lower()); n = len(re.findall(r"[aeiouy]+", w))
        if w.endswith("e") and not w.endswith(("le", "ee")) and n > 1: n -= 1
        return max(1, n) if w else 0
    span = words[-1][1] - words[0][0]
    rep["words"] = len(words); rep["wpm"] = round(len(words) / span * 60); rep["syllables_per_s"] = round(sum(syl(w[2]) for w in words) / span, 2)
    gaps = [(round(words[i][1], 2), round(words[i + 1][0] - words[i][1], 2)) for i in range(len(words) - 1)]
    rep["pauses_over_0.15s"] = [g for g in gaps if g[1] > 0.15]; rep["mean_word_gap_s"] = round(float(np.mean([g[1] for g in gaps])), 3)
except ImportError:
    rep["words"] = "install faster-whisper for pace and pauses"
# voice pitch (autocorrelation on the mid channel)
y = sg.resample_poly(M, 1, 3); f0 = []
for i in range(0, len(y) - 640, 320):
    s = y[i:i + 640]
    if np.sqrt(np.mean(s ** 2)) < 0.02: continue
    s = s - s.mean(); ac = np.correlate(s, s, "full")[639:]; ac /= ac[0] + 1e-9; k = int(np.argmax(ac[40:228])) + 40
    if ac[k] > 0.5: f0.append(16000 / k)
if f0: rep["voice_f0_hz"] = round(float(np.median(f0))); rep["voice_range_semitones"] = round(12 * math.log2(np.percentile(f0, 90) / np.percentile(f0, 10)), 1)
# sound design in the side channel
if stereo:
    def env(a, lo, hi, ms):
        b = sg.butter(4, [lo, hi], btype="band", fs=sr, output="sos"); e = np.abs(sg.sosfiltfilt(b, a)); n = int(sr * ms / 1000)
        return e[:len(e) // n * n].reshape(-1, n).max(1), ms / 1000
    e, dt = env(S, 5000, min(16000, sr / 2 - 100), 2); pk, _ = sg.find_peaks(e, height=np.percentile(e, 97), distance=int(.05 / dt))
    rep["clicks_s"] = [round(i * dt, 2) for i in pk if 20 < i < len(e) - 40 and e[i] > 5 * np.median(e[i - 18:i - 4]) and e[i] > 3 * np.median(e[i + 12:i + 30])]
    e2, dt2 = env(S, 1500, 7000, 10); sm = np.convolve(e2, np.ones(15) / 15, "same"); r = sm / (sg.medfilt(sm, 201) + 1e-6)
    pk2, pr = sg.find_peaks(r, height=2.2, distance=int(.4 / dt2), width=(8, 80)); rep["swishes_s"] = [[round(i * dt2, 2), int(w * dt2 * 1000)] for i, w in zip(pk2, pr["widths"])]
    e3, dt3 = env(S, 30, 200, 10); pk3, _ = sg.find_peaks(e3, height=np.percentile(e3, 98), distance=int(.25 / dt3)); rep["low_hits_s"] = [round(i * dt3, 2) for i in pk3]
    f, t, Z = sg.stft(S, sr, nperseg=1024, noverlap=768); b = np.log1p(50 * np.abs(Z)); d = np.diff(b, axis=1); d[d < 0] = 0; fl = d.sum(0); fl -= fl.mean()
    ac = np.correlate(fl, fl, "full")[len(fl) - 1:]; tdt = t[1] - t[0]; lags = np.arange(int(.3 / tdt), int(1.5 / tdt)); best = lags[np.argmax(ac[lags])]
    rep["bed_beat_s"] = round(best * tdt, 3); rep["bed_bpm"] = round(60 / (best * tdt), 1)
    tail = M[int(max(0, len(M) / sr - 5) * sr):]; rep["loudest_moment_last_5s_db"] = round(20 * math.log10(np.abs(tail).max() + 1e-9), 1)
else:
    rep["sound_design"] = "mono file: no side channel to separate"
json.dump(rep, open(os.path.join(out, "report.json"), "w"), indent=1)
side = os.path.join(out, "side.wav"); subprocess.run([FF, "-y", "-loglevel", "error", "-i", wav, "-af", "pan=mono|c0=0.5*c0-0.5*c1,volume=12dB", side])
for i in range(int(rep["duration_s"] // 12) + 1):
    a, b2 = [os.path.join(out, f"_{n}.png") for n in "ab"]
    for s_, p_ in ((side, a), (wav, b2)):
        subprocess.run([FF, "-y", "-loglevel", "error", "-ss", str(i * 12), "-t", "12", "-i", s_, "-lavfi", "showspectrumpic=s=1600x360:legend=0:scale=log:fscale=log:color=fire:start=40:stop=16000", p_])
    subprocess.run([FF, "-y", "-loglevel", "error", "-i", a, "-i", b2, "-filter_complex", "vstack", os.path.join(out, f"spectrum_{i:02d}.png")])
for n in "ab":
    p_ = os.path.join(out, f"_{n}.png")
    if os.path.exists(p_): os.remove(p_)
print(json.dumps({k: v for k, v in rep.items() if not isinstance(v, list)}, indent=1)); print("wrote", out)

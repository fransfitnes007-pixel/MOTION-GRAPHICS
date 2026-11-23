"""Sound effects for a reel, made from scratch (no samples) and placed on the logged events.
Families copied from the example reel's measurements: bright clicks on pop-ins (10-25 ms rise, 15-60 ms fall),
soft swishes on scene changes (80-190 ms rise and fall), low thuds on stamps, typing/counter ticks,
and a deep boom on the end card.
Usage: python3 sfx.py events.json <voice.wav> <out_mix.wav> [--sfx-only sfx.wav] [--level 1.0]"""
import sys, json, numpy as np, scipy.io.wavfile as wf, scipy.signal as sg
SR = 48000
args = sys.argv[1:]
def opt(n, d=None):
    if n in args: i = args.index(n); v = args[i+1]; del args[i:i+2]; return v
    return d
sfx_only = opt("--sfx-only"); LEVEL = float(opt("--level", 1.0))
E = json.load(open(args[0])); B, C, DUR = E["B"], E["C"], E["DURATION"]
N = int((DUR + 0.3) * SR); out = np.zeros((N, 2)); rng = np.random.default_rng(7); log = []
t_ = lambda n: np.arange(n) / SR
def filt(x, kind, f): return sg.sosfilt(sg.butter(2, f, btype=kind, fs=SR, output="sos"), x)
def put(x, t, gain=1.0, pan=0.0, name=""):
    """pan -1..1; x mono or (n,2)"""
    i = int(round(t * SR))
    if i < 0: x = x[-i:]; i = 0
    x = x[: max(0, N - i)]
    if x.ndim == 1: a = (pan + 1) * np.pi / 4; x = np.stack([x * np.cos(a), x * np.sin(a)], 1) * 1.4142
    out[i:i+len(x)] += x * gain * LEVEL; log.append((round(t, 2), name))
def swish(dur=0.34, f0=2200, f1=8500, rise=0.45, direction=1, _second=None):
    n = int(dur * SR); x = rng.standard_normal(n + 1024)
    f, tt, Z = sg.stft(x, SR, nperseg=512, noverlap=384)
    fc = f0 * (f1 / f0) ** np.clip(tt / dur, 0, 1); lf = np.log2(np.maximum(f, 40))[:, None]
    Z = Z * np.exp(-0.5 * ((lf - np.log2(fc)[None, :]) / 0.55) ** 2); _, y = sg.istft(Z, SR, nperseg=512, noverlap=384); y = y[:n]
    u = np.arange(n) / n; env = np.where(u < rise, 0.5 - 0.5 * np.cos(np.pi * u / rise), (0.5 + 0.5 * np.cos(np.pi * (u - rise) / (1 - rise))) ** 1.5)
    y = y * env; y /= np.abs(y).max() + 1e-9
    if _second is None: y2 = swish(dur, f0, f1, rise, direction, _second=False)   # a second, unrelated noise take makes it wide, like the example's
    else: return y
    p = (u * 2 - 1) * 0.6 * direction; a = (p + 1) * np.pi / 4   # and it sweeps across the stereo field
    return np.stack([(0.75 * y + 0.25 * y2) * np.cos(a), (0.25 * y + 0.75 * y2) * np.sin(a)], 1) * 1.2
def click(body=1500, bright=5000, tail=0.011, body_gain=0.45):
    n = int(0.07 * SR); t = t_(n); x = filt(rng.standard_normal(n), "high", bright) * np.exp(-t / tail)
    fr = body * (0.62 + 0.38 * np.exp(-t / 0.012)); b = np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t / 0.014)
    y = x / (np.abs(x).max() + 1e-9) + b * body_gain; att = np.minimum(1, t / 0.0015); y *= att; return y / np.abs(y).max()
def blip(freq=2600):
    n = int(0.06 * SR); t = t_(n); y = np.sin(2 * np.pi * freq * t) * np.exp(-t / 0.012) + 0.35 * filt(rng.standard_normal(n), "high", 6500) * np.exp(-t / 0.004)
    return y * np.minimum(1, t / 0.001) / np.abs(y).max()
def tick():
    n = int(0.025 * SR); t = t_(n); lo = rng.uniform(2200, 3400); x = sg.sosfilt(sg.butter(2, [lo, lo * 2.4], btype="band", fs=SR, output="sos"), rng.standard_normal(n)) * np.exp(-t / 0.0028)
    return x / (np.abs(x).max() + 1e-9)
def tok(freq=520):
    n = int(0.09 * SR); t = t_(n); y = np.sin(2 * np.pi * freq * (0.8 + 0.2 * np.exp(-t / 0.01)) * t) * np.exp(-t / 0.02) + 0.25 * filt(rng.standard_normal(n), "low", 3000) * np.exp(-t / 0.006)
    return y * np.minimum(1, t / 0.002) / np.abs(y).max()
def thud(f0=170, f1=62, tail=0.075):
    n = int(0.36 * SR); t = t_(n); fr = f1 + (f0 - f1) * np.exp(-t / 0.03); b = np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t / tail)
    x = filt(rng.standard_normal(n), "low", 4200) * np.exp(-t / 0.03) * 0.5 + filt(rng.standard_normal(n), "high", 3500) * np.exp(-t / 0.006) * 0.3
    y = (b + x) * np.minimum(1, t / 0.002); return y / np.abs(y).max()
def boom():
    n = int(1.9 * SR); t = t_(n); fr = 44 + 30 * np.exp(-t / 0.12); sub = np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t / 0.5)
    mid = np.sin(2 * np.pi * 130 * t) * np.exp(-t / 0.38) * 0.5 + np.sin(2 * np.pi * 196 * t) * np.exp(-t / 0.22) * 0.18
    th = filt(rng.standard_normal(n), "low", 420) * np.exp(-t / 0.13) * 0.8 + filt(rng.standard_normal(n), "low", 5000) * np.exp(-t / 0.02) * 0.35
    y = np.tanh(1.6 * (sub + mid + th) * np.minimum(1, t / 0.006)); y *= np.minimum(1, (t[-1] - t) / 0.25); y /= np.abs(y).max()
    wide = filt(rng.standard_normal(n), "low", 900) * np.exp(-t / 0.3) * 0.12   # a little width, like the example's end hit
    return np.stack([y + wide, y - wide], 1)
def rocket(dur=1.25):
    n = int(dur * SR); x = rng.standard_normal(n + 1024); f, tt, Z = sg.stft(x, SR, nperseg=512, noverlap=384)
    fc = 260 * (2600 / 260) ** np.clip(tt / dur, 0, 1); Z = Z * (1 / (1 + (f[:, None] / fc[None, :]) ** 4)); _, y = sg.istft(Z, SR, nperseg=512, noverlap=384); y = y[:n]
    u = np.arange(n) / n; y = y * (u ** 1.6) * np.minimum(1, (1 - u) / 0.12); return y / np.abs(y).max()

L = lambda i, local: B[i] + local   # beat index (0-based) + seconds into the beat
at = lambda i, cue: C[cue] - B[i]
# 1. scene changes: a swish that peaks on the cut, sweeping the way the picture slides
put(swish(0.30, 1800, 6000), 0.02, 0.085, name="swish in")
for i in range(1, len(B) - 1):
    put(swish(0.34, 2200, 8500, direction=1 if i % 2 else -1), B[i] - 0.15, 0.115, name=f"swish b{i+1}")
# 2. logged pop-ins
near_cut = lambda t: any(0 <= t - b < 0.16 for b in B)
for e in E["list"]:
    t, k = e["t"], e["type"]; pan = float(rng.uniform(-0.7, 0.7))
    if k == "pill" and not near_cut(t): put(click(1500 + rng.uniform(-120, 120)), t + 0.02, 0.17, pan, "pop")
    elif k == "bubble": put(click(1050 + rng.uniform(-80, 80), 4200), t + 0.02, 0.15, pan, "bubble")
    elif k == "check": put(blip(2500 + rng.uniform(-150, 250)), t + 0.02, 0.10, pan, "check")
    elif k == "cross": put(thud(150, 70, 0.05), t + 0.02, 0.2, pan, "cross")
    elif k == "card" and not near_cut(t): put(swish(0.2, 2500, 6000)[:, 0], t - 0.03, 0.06, 0, "card")
# 3. typing: one key tick per character
for ty in E["typ"]:
    for j in range(ty["n"]):
        tt = ty["a"] + (ty["b"] - ty["a"]) * j / max(1, ty["n"] - 1) + rng.uniform(-0.008, 0.008); put(tick(), tt, rng.uniform(0.05, 0.085), rng.uniform(-0.2, 0.2), "key")
def ticks(t0, t1, n, g=0.05, curve=1.0):
    for j in range(n): put(tick(), t0 + (t1 - t0) * (j / max(1, n - 1)) ** curve, g * rng.uniform(0.75, 1.1), rng.uniform(-0.25, 0.25), "tick")
pop = lambda t, f=1500, g=0.16, pan=0.0: put(click(f), t, g, pan, "pop")
# 4. hand-placed moments, beat by beat
ticks(L(0, .5), L(0, 1.9), 20)                                    # ideas counter
pop(L(1, 1.02), 1300); pop(L(1, 2.32), 1700)                        # question mark, then the app icon
put(blip(3000), L(2, .57), 0.09, name="star")
pop(L(4, 1.52), 1650, pan=.3)                                       # app icon lights up
ticks(L(5, .05), L(5, .85), 7, .04); put(swish(0.24, 2000, 6000)[:, 0], L(5, .95), 0.07, name="note")
put(swish(0.26, 2500, 7500, direction=1), L(7, at(7, "opposite") - .04), 0.08, name="arrows")
d9 = B[9] - B[8]
for k in range(2, 13): put(tick(), L(8, .2 + (k - 1.5) / 11 * (d9 - .6)), 0.055, name="draft")
fp = at(9, "forty"); pop(L(9, .1), 1250); ticks(L(9, fp - .55), L(9, fp + .02), 13, .05); put(thud(), L(9, fp + .06), 0.26, .25, "price lands")
qp = at(10, "quit"); put(thud(190, 75, .05), L(10, qp + .02), 0.24, -.2, "X 1"); put(thud(165, 65, .06), L(10, qp + .15), 0.27, .2, "X 2")
put(swish(0.24, 2000, 6000, direction=-1), L(11, .12), 0.075, name="tag slides in")
put(swish(0.36, 1800, 7500), C["other"] - .1, 0.11, name="card flips")
ap, tp = at(13, "answer"), at(13, "taps"); pop(L(13, .47), 1500, .13, -.3)
for i in range(4): put(tok(420 + i * 55), L(13, ap + .3 + ((350 + i * 116 - 320) / 470) * (tp - ap - .45)), 0.13, -.3 + i * .2, "bridge tile")
pop(L(13, tp), 1900, .2, .35)                                       # the tap
ticks(L(14, .25), L(14, 1.1), 15, .045); put(thud(140, 55, .09), L(14, 1.78), 0.2, .2, "step flat")
wp, np_ = at(15, "watch"), at(15, "nocode")
for i in range(6): put(click(900 + i * 130, 4500), L(15, wp + i * .15 + .02), 0.14, -.15 + i * .06, "app builds")
put(thud(180, 70, .06), L(15, np_ + .03), 0.24, .3, "no code")
for i in range(8): put(tok(300 + rng.uniform(-30, 30)), L(16, .25 + i * .27 + .5), 0.07, .35, "paper ball")
sh, fx = at(17, "ships"), at(17, "fixes"); put(rocket(), L(17, sh + .3), 0.15, name="rocket")
pop(L(17, fx - .2 + .44), 1400, .15, -.3); pop(L(17, fx + .5 + .44), 1400, .15, .3)
for j in range(34): put(tick(), L(18, .3 + 2.2 * (j / 33) ** .55), 0.045 * rng.uniform(.8, 1.1), name="users")
put(thud(160, 55, .11), L(18, at(18, "luck") - .42), 0.32, 0, "title lands")
put(boom(), L(19, .08), 0.78, name="boom")
put(click(2100, 5500, .008, .3), L(19, E["TAP"]), 0.2, .15, "tap Get"); put(blip(1900), L(19, E["TAP"] + .12 + E["DL"]), 0.14, .15, "open")

sr, v = wf.read(args[1]); v = v.astype(np.float64) / 32768
if v.ndim > 1: v = v.mean(1)
if sr != SR: v = sg.resample_poly(v, SR, sr)
mix = out.copy(); n = min(len(v), N); mix[:n] += v[:n, None]
pk = np.abs(mix).max(); mix = mix * (0.97 / pk) if pk > 0.97 else mix
wf.write(args[2], SR, (mix * 32767).astype(np.int16))
if sfx_only: wf.write(sfx_only, SR, (np.clip(out, -1, 1) * 32767).astype(np.int16))
rms = lambda a: 20 * np.log10(np.sqrt((a ** 2).mean()) + 1e-9)
print(f"{len(log)} sounds placed; voice {rms(v):.1f} dB, effects {rms(out[:int(B[-1]*SR)]):.1f} dB before the end card, effects peak {20*np.log10(np.abs(out[:int(B[-1]*SR)]).max()):.1f} dB, boom peak {20*np.log10(np.abs(out[int(B[-1]*SR):]).max()):.1f} dB, mix peak {20*np.log10(min(pk,0.97)):.1f} dB")
json.dump(sorted(log), open(args[0].replace(".json", ".placed.json"), "w"))

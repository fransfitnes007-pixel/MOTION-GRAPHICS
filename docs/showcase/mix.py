#!/usr/bin/env python3
"""Soundtrack for the showcase film: a synthesised music bed (ducked under the voice), sound effects on the film's own
event times, the voiceover, then muxed onto the silent render.  Usage: python3 mix.py silent.mp4 out.mp4
Everything is generated here from sine waves and filtered noise: no samples, nothing to license."""
import json, os, subprocess, sys
import numpy as np, scipy.io.wavfile as wf, scipy.signal as sg
HERE = os.path.dirname(os.path.abspath(__file__)); SR = 48000; DUR = 62; N = int(DUR * SR)
rng = np.random.default_rng(11)
t_ = lambda n: np.arange(n) / SR
def filt(x, kind, f, o=2): return sg.sosfilt(sg.butter(o, f, btype=kind, fs=SR, output="sos"), x)
mix = np.zeros((N, 2))
def put(x, t, gain=1.0, pan=0.0, buf=None):
    buf = mix if buf is None else buf; i = int(t * SR); x = x[: max(0, N - i)]
    if x.ndim == 1: a = (pan + 1) * np.pi / 4; x = np.stack([x * np.cos(a), x * np.sin(a)], 1) * 1.414
    buf[i:i + len(x)] += x * gain

# ---------- sound effects
def click(f=1600):
    n = int(.07 * SR); t = t_(n); x = filt(rng.standard_normal(n), "high", 5200) * np.exp(-t / .01)
    b = np.sin(2 * np.pi * np.cumsum(f * (.62 + .38 * np.exp(-t / .012))) / SR) * np.exp(-t / .014)
    y = x / (np.abs(x).max() + 1e-9) + .45 * b; return y * np.minimum(1, t / .0015) / np.abs(y).max()
def tick():
    n = int(.025 * SR); t = t_(n); lo = rng.uniform(2300, 3300)
    x = sg.sosfilt(sg.butter(2, [lo, lo * 2.4], btype="band", fs=SR, output="sos"), rng.standard_normal(n)) * np.exp(-t / .003); return x / (np.abs(x).max() + 1e-9)
def swish(dur=.36, f0=1800, f1=8000, d=1):
    n = int(dur * SR); x = rng.standard_normal(n + 1024); f, tt, Z = sg.stft(x, SR, nperseg=512, noverlap=384)
    fc = f0 * (f1 / f0) ** np.clip(tt / dur, 0, 1); Z = Z * np.exp(-.5 * ((np.log2(np.maximum(f, 40))[:, None] - np.log2(fc)[None, :]) / .55) ** 2)
    _, y = sg.istft(Z, SR, nperseg=512, noverlap=384); y = y[:n]; u = np.arange(n) / n
    y = y * np.where(u < .45, .5 - .5 * np.cos(np.pi * u / .45), (.5 + .5 * np.cos(np.pi * (u - .45) / .55)) ** 1.5); y /= np.abs(y).max() + 1e-9
    p = (u * 2 - 1) * .6 * d; a = (p + 1) * np.pi / 4; return np.stack([y * np.cos(a), y * np.sin(a)], 1) * 1.3
def thud(f0=170, f1=55, tail=.09):
    n = int(.4 * SR); t = t_(n); fr = f1 + (f0 - f1) * np.exp(-t / .03); b = np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t / tail)
    y = b + .5 * filt(rng.standard_normal(n), "low", 4000) * np.exp(-t / .03); return y * np.minimum(1, t / .002) / np.abs(y).max()
def boom():
    n = int(2.2 * SR); t = t_(n); fr = 42 + 30 * np.exp(-t / .12); y = np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t / .55)
    y += .5 * np.sin(2 * np.pi * 130 * t) * np.exp(-t / .4) + .7 * filt(rng.standard_normal(n), "low", 420) * np.exp(-t / .13)
    y = np.tanh(1.6 * y * np.minimum(1, t / .006)); return y / np.abs(y).max()
def riser(dur=1.2):
    n = int(dur * SR); x = rng.standard_normal(n + 1024); f, tt, Z = sg.stft(x, SR, nperseg=512, noverlap=384)
    fc = 400 * (6000 / 400) ** np.clip(tt / dur, 0, 1); Z = Z * (1 / (1 + (f[:, None] / fc[None, :]) ** 4)); _, y = sg.istft(Z, SR, nperseg=512, noverlap=384)
    y = y[:n] * (np.arange(n) / n) ** 2; return y / np.abs(y).max()
def blip(f=2400):
    n = int(.08 * SR); t = t_(n); y = np.sin(2 * np.pi * f * t) * np.exp(-t / .02); return y * np.minimum(1, t / .001)

T = dict(prompt=.28, one2=1.16, finished=1.5, video=2.0, thisis=2.9, kit=3.58, open=4.9, claude=6.74, reels=8.04, tiktoks=8.76, shorts=9.58,
  ugc=10.24, demos=11.36, launch=12.44, dash=13.32, idents=14.24, everyf=15.26, everys=16.28, fromone=17.0, over=18.64, n300=18.82, pieces=19.9,
  builtin=20.48, kinetic=21.24, trans=22.24, dashb=23.18, endc=24.08, micro=25.24, bestapps=26.56, phone=27.46, every=27.72, code=29.04, exact=30.88,
  brand=31.96, file=33.0, logo=33.94, scene=34.72, endcard=35.2, follows=35.66, writes=36.66, records=37.66, pins=38.8, words=40.14, then=40.8,
  clicks=42.08, swishes=42.8, booms=43.34, exactf=44.14, show=45.4, viral=45.82, measures=46.9, cuts=47.4, pace=48.08, sound=48.92, rebuilds=49.62,
  format=50.76, clone=52.04, brandit=52.8, ship=53.5, mrk=54.44, created=55.32, gk=55.96, net=56.48, end=57.0)
SC = [T["thisis"], T["reels"], T["over"], T["every"], T["brand"], T["writes"], T["then"], T["show"], T["clone"], T["mrk"]]
sfx = np.zeros((N, 2))
for i, a in enumerate(SC): put(swish(d=1 if i % 2 else -1), a - .16, .16, buf=sfx)
for k in range(42): put(tick(), .05 + k * 1.25 / 42 + rng.uniform(-.004, .004), .09, rng.uniform(-.2, .2), sfx)   # the prompt typing, slower now
put(click(1300), T["finished"] - .1, .2, buf=sfx); put(swish(.5, 900, 6000), T["finished"] + .1, .14, buf=sfx)
put(thud(190, 60, .12), T["kit"] - .2, .32, buf=sfx); put(riser(.9), T["kit"] - 1.1, .06, buf=sfx)
for k in range(54): put(tick(), T["open"] - .2 + k * 2.3 / 54, .06, rng.uniform(-.2, .2), sfx)
for i in range(4): put(click(1500 + i * 120), T["claude"] + .1 + i * .14, .17, -.4 + i * .27, sfx)
# the format wall: a thud-click per format landing, a riser into the pull-back, a boom on "every format"
for a in ("reels", "tiktoks", "shorts", "ugc", "demos", "launch", "dash", "idents"): put(thud(200, 75, .06), T[a] - .04, .22, rng.uniform(-.4, .4), sfx); put(click(1700), T[a], .16, buf=sfx)
put(riser(1.2), T["everyf"] - 1.1, .09, buf=sfx); put(thud(120, 42, .2), T["everyf"], .45, buf=sfx); put(click(1900), T["fromone"], .18, buf=sfx)
for k in range(30): put(tick(), T["over"] - .1 + 1.4 * (k / 29) ** .6, .06, buf=sfx)
put(thud(150, 50, .1), T["pieces"] - .2, .22, buf=sfx)
for a in ("kinetic", "trans", "dashb", "endc"): put(click(1700), T[a], .18, rng.uniform(-.3, .3), sfx)
put(swish(.5, 1400, 7000), T["micro"] - .2, .14, buf=sfx)
for i in range(8): put(click(1300 + i * 90), T["micro"] - .1 + i * .07, .11, -.6 + i * .17, sfx)
put(click(1500), T["every"], .16, buf=sfx); put(blip(2600), T["exact"], .12, .3, sfx)
for k in range(9): put(tick(), T["brand"] + .3 + k * .06, .07, buf=sfx)
for k in range(4): put(tick(), T["file"] - .1 + k * .1, .08, buf=sfx)
for a, d in (("logo", 1), ("scene", -1), ("endcard", 1)): put(swish(.3, 2500, 7500, d), T[a] - .05, .1, buf=sfx)
put(click(1900), T["follows"] - .1, .16, buf=sfx)
for k in range(60): put(tick(), T["writes"] + k * .02, .05, buf=sfx)
for i in range(12): put(blip(1800 + i * 60), T["pins"] + i * .08 + .3, .07, -.5 + i * .09, sfx)
for a, kind in (("clicks", "c"), ("swishes", "s"), ("booms", "b"), ("booms+", "c"), ("exactf-", "s")):
    at = T[a.rstrip("+-")] + (.45 if a.endswith("+") else -.1 if a.endswith("-") else 0)
    if kind == "c": put(click(1700), at, .26, buf=sfx)
    elif kind == "s": put(swish(.3), at - .05, .2, buf=sfx)
    else: put(thud(120, 45, .16), at, .4, buf=sfx)
put(blip(2200), T["exactf"], .13, buf=sfx)
put(riser(1.4), T["viral"], .07, buf=sfx)
for a in ("cuts", "pace", "sound"): put(click(1500), T[a], .18, .3, sfx)
put(swish(.45, 1200, 7000), T["rebuilds"] - .1, .16, buf=sfx)
for a in ("clone", "brandit", "ship"): put(thud(170, 48, .14), T[a], .42, buf=sfx)
put(boom(), T["mrk"], .8, buf=sfx)
for k in range(31): put(tick(), T["mrk"] + .6 + k * .03, .06, buf=sfx)
put(thud(140, 50, .14), T["gk"] - .1, .3, buf=sfx); put(blip(2000), T["net"], .12, buf=sfx)

# ---------- music bed: 112 bpm, A minor (Am F C G), soft kick, pad, plucked arp; stops for the slams, returns on the end card
bpm = 112; beat = 60 / bpm; bed = np.zeros((N, 2))
chords = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]]; hz = lambda m: 440 * 2 ** ((m - 69) / 12)
bar = beat * 4
for b in range(int(DUR / bar) + 1):
    t0 = b * bar
    if t0 > DUR: break
    ch = chords[b % 4]; n = int(bar * SR); t = t_(n)
    pad = sum(np.sin(2 * np.pi * hz(m) * t + .3 * np.sin(2 * np.pi * .3 * t)) + .4 * np.sin(2 * np.pi * hz(m) * 2.003 * t) for m in ch)
    env = np.minimum(1, t / .4) * np.minimum(1, (bar - t) / .3); pad = filt(pad * env, "low", 1800) * .05
    put(np.stack([pad, np.roll(pad, 240)], 1), t0, 1, buf=bed)
    for k in range(8):   # arp in eighths
        m = ch[k % 3] + 12 * (k // 3 % 2); nn = int(.22 * SR); tt = t_(nn)
        pl = (np.sign(np.sin(2 * np.pi * hz(m) * tt)) * .25 + np.sin(2 * np.pi * hz(m) * tt)) * np.exp(-tt / .09)
        put(filt(pl, "low", 2600) * .045, t0 + k * beat / 2, 1, .35 if k % 2 else -.35, bed)
    for k in range(4): put(thud(150, 48, .12) * .22, t0 + k * beat, 1, buf=bed)
# duck under the voice, gap for the slams, swell on the end card
sr, v = wf.read(os.path.join(HERE, "assets", "voiceover.wav")); v = v.astype(float) / 32768
if v.ndim > 1: v = v.mean(1)
if sr != SR: v = sg.resample_poly(v, SR, sr)
env = np.convolve(np.abs(np.pad(v, (0, max(0, N - len(v))))[:N]), np.ones(int(.08 * SR)) / int(.08 * SR), "same")
duck = 1 - .55 * np.clip(env / (np.percentile(env[env > 1e-4], 70) + 1e-9), 0, 1)
tt = t_(N); gate = np.where((tt > T["clone"] - .05) & (tt < T["mrk"]), .15, 1.0); gate = np.convolve(gate, np.ones(2400) / 2400, "same")
fade_in = np.minimum(1, tt / 1.5); fade_out = np.clip((DUR - tt) / 1.2, 0, 1)
bed *= (duck * gate * fade_in * fade_out)[:, None]
out = bed * .9 + sfx * 1.0; out[:len(v)] += np.stack([v, v], 1)[:N] * 1.0
out = np.tanh(out * 1.1) / np.tanh(1.1)
pk = np.abs(out).max(); out *= .95 / pk
wav = os.path.join(HERE, "clips", "soundtrack.wav"); os.makedirs(os.path.dirname(wav), exist_ok=True); wf.write(wav, SR, (out * 32767).astype(np.int16))
src, dst = sys.argv[1], sys.argv[2]
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-i", wav, "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                "-af", "loudnorm=I=-14:TP=-1:LRA=9,aresample=48000", "-ar", "48000", "-shortest", "-movflags", "+faststart", dst], check=True)
rms = lambda a: 20 * np.log10(np.sqrt((a ** 2).mean()) + 1e-9)
print(f"wrote {dst}: voice {rms(v):.1f} dB, bed {rms(bed):.1f} dB, sfx {rms(sfx):.1f} dB")

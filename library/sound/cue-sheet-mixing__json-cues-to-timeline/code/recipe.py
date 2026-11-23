"""Cue-sheet driven mixing: a JSON list of {t, type} cues (the renderer dumps one while it plays the page) is turned into a sound
track by mapping each type to a sound and a volume, de-duplicating near-identical cues, and adding a drone bed. Volumes: click .55, key .5, tick .35, whoosh .5, thud .9, flip .8.
A production version would mix sampled files through ffmpeg amix; this recipe mixes synthesised stand-ins in numpy so it runs alone.
Usage: python3 recipe.py out.wav [cues.json]"""
import sys, numpy as np, soundfile as sf
from scipy.signal import lfilter
SR = 48000
rng = np.random.default_rng(11)

# ---- helpers shared by the recipes in this library (the only change: lp() uses scipy's lfilter when the cutoff is constant, which is the same one-pole filter, just faster)
def buf(dur): return np.zeros((int(SR * dur), 2), np.float32)
def put(buf, sig, t, gain=1.0, pan=0.0):
    i = int(t * SR)
    if i >= len(buf) or i < 0: return
    sig = sig[:len(buf) - i]
    if sig.ndim == 1:
        l, r = np.sqrt((1 - pan) / 2), np.sqrt((1 + pan) / 2)
        buf[i:i + len(sig), 0] += sig * gain * l * 1.41; buf[i:i + len(sig), 1] += sig * gain * r * 1.41
    else: buf[i:i + len(sig)] += sig * gain
def env(n, a, d):
    t = np.arange(n) / SR
    return np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / d)
def lp(x, fc):
    if np.ndim(fc) == 0:
        a = 1 - np.exp(-2 * np.pi * float(fc) / SR)
        return lfilter([a], [1, -(1 - a)], x)
    fc = np.broadcast_to(np.asarray(fc, float), x.shape)
    a = 1 - np.exp(-2 * np.pi * fc / SR); y = np.empty_like(x); s = 0.0
    for i in range(len(x)): s += a[i] * (x[i] - s); y[i] = s
    return y
def kick():
    n = int(.4 * SR); t = np.arange(n) / SR
    f = 48 + 120 * np.exp(-t / .03); ph = 2 * np.pi * np.cumsum(f) / SR
    return (np.sin(ph) * env(n, .001, .15) + .25 * np.sin(ph * 2) * env(n, .001, .02)).astype(np.float32)
def clap():
    n = int(.22 * SR); x = rng.standard_normal(n)
    e = sum(env(n, .0005, .012) * (np.arange(n) >= int(k * SR)) for k in (0, .009, .018)) + .6 * env(n, .001, .08)
    return (np.diff(np.concatenate([[0], x])) * e * .5).astype(np.float32)
def hat(open_=False):
    n = int((.2 if open_ else .045) * SR); x = rng.standard_normal(n); x = x - lp(x, 7500)
    return (x * env(n, .0005, .06 if open_ else .011)).astype(np.float32)
def saw(f, n):
    t = np.arange(n) / SR; return (2 * ((t * f) % 1) - 1)
def pluck(freqs, dur, bright):
    n = int(dur * SR); x = sum(saw(f, n) + saw(f * 1.004, n) for f in freqs) / len(freqs)
    return (lp(x, 350 + bright * env(n, .001, .12)) * env(n, .002, .26)).astype(np.float32)
def bass(f, dur):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) + .35 * lp(saw(f, n), 900)
    return (x * np.minimum(1, t / .004) * np.exp(-t / .32)).astype(np.float32)
def noise_swell(dur, peak_at, lo=500, hi=6000):
    n = int(dur * SR); t = np.arange(n) / SR; x = rng.standard_normal(n)
    e = np.where(t < peak_at, (t / peak_at) ** 2, np.exp(-(t - peak_at) / .12))
    fc = lo + (hi - lo) * np.clip(t / peak_at, 0, 1)
    return ((lp(x, fc) - lp(x, lo * .8)) * e).astype(np.float32)
def impact():
    n = int(1.4 * SR); t = np.arange(n) / SR
    body = np.sin(2 * np.pi * (38 + 60 * np.exp(-t / .05)) * t) * np.exp(-t / .5)
    air = (rng.standard_normal(n) * np.exp(-t / .18)); air = air - lp(air, 300)
    return (body * 1.2 + lp(air, 3500) * .5).astype(np.float32)
def whoosh(dur=.42, up=True):
    n = int(dur * SR); t = np.arange(n) / SR; x = rng.standard_normal(n)
    e = np.sin(np.pi * t / dur) ** 1.5
    fc = (800 + 5000 * (t / dur)) if up else (6000 - 5200 * (t / dur))
    return ((lp(x, fc) - lp(x, 300)) * e * .8).astype(np.float32)
def pop(f=880):
    n = int(.11 * SR); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * (f + 700 * np.exp(-t / .018)) * t) * np.exp(-t / .04)).astype(np.float32)
def click():
    n = int(.06 * SR); x = rng.standard_normal(n); x = x - lp(x, 2500)
    return (x * env(n, .0003, .006) * .9 + pop(1600)[:n] * .3).astype(np.float32)
def tick(f=2400):
    n = int(.03 * SR); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * f * t) * np.exp(-t / .006)).astype(np.float32)
def pad(freqs, dur):
    n = int(dur * SR); t = np.arange(n) / SR
    x = sum(np.sin(2 * np.pi * f * t + np.sin(2 * np.pi * .3 * t) * .3) for f in freqs) / len(freqs)
    return (x * np.minimum(1, t / 1.5) * np.minimum(1, (dur - t) / 1.5)).astype(np.float32)

# chords, one per bar: Am F C G
A2, F2, C3, G2 = 55.0, 43.65, 65.41, 49.0
AM = [220, 261.6, 329.6]; FM = [174.6, 220, 261.6]; CM = [261.6, 329.6, 392]; GM = [196, 246.9, 293.7]
CH = [(AM, A2), (FM, F2), (CM, C3), (GM, G2)]

def save(path, x, peak=.9):
    """Demo output only (not part of the mix chain): scale so the loudest sample sits at `peak`, write 16-bit WAV."""
    m = float(np.abs(x).max())
    if m > 0: x = x * (peak / m)
    sf.write(path, x.astype(np.float32), SR, subtype='PCM_16')
    print('wrote', path, f'{len(x) / SR:.2f}s', 'peak', round(float(np.abs(x).max()), 3))

import json
from scipy.signal import butter, lfilter as _lf
# ---- a cue sheet in the format the renderer writes: {"dur": seconds, "sounds": [{"t": s, "type": ...}], "vo": {key: start_s}}
DEMO = {'dur': 9.0, 'vo': {}, 'sounds':
    [{'t': 0.6 + i * .11, 'type': 'key'} for i in range(14)] + [{'t': 0.6 + 5 * .11, 'type': 'key'}] +   # one duplicate cue on purpose
    [{'t': 2.4, 'type': 'click'}, {'t': 3.0, 'type': 'whoosh'}, {'t': 3.5, 'type': 'thud'}, {'t': 3.5, 'type': 'thud'},
     {'t': 4.4, 'type': 'flip'}, {'t': 5.2, 'type': 'flip'}] +
    [{'t': 6.0 + i * .045, 'type': 'tick'} for i in range(18)] + [{'t': 7.3, 'type': 'click'}, {'t': 8.0, 'type': 'unknown-type'}]}
cues = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else DEMO
dur = float(cues['dur'])

# ---- stand-ins for sfx/*.wav (production versions use sampled files)
def key_(k):
    n = int(.045 * SR); t = np.arange(n) / SR
    x = rng.standard_normal(n); x = x - lp(x, 1800)
    return (x * env(n, .0003, .004) * .5 + np.sin(2 * np.pi * (150 + 12 * (k % 6)) * t) * np.exp(-t / .008) * .6).astype(np.float32)
def thud():
    n = int(.5 * SR); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * (45 + 80 * np.exp(-t / .04)) * t) * np.exp(-t / .16)).astype(np.float32)
def flip():
    n = int(.16 * SR); x = rng.standard_normal(n); x = lp(x, 5000) - lp(x, 900)
    return (x * np.sin(np.pi * np.arange(n) / n) ** 2 * .8).astype(np.float32)
SFX = {  # type -> (sound, volume)   volumes from audio_from_cues.py
    'click': (lambda k: click(), 0.55), 'key': (key_, 0.5), 'tick': (lambda k: tick(2400), 0.35),
    'whoosh': (lambda k: whoosh(), 0.5), 'thud': (lambda k: thud(), 0.9), 'flip': (lambda k: flip(), 0.8)}

mix = buf(dur); seen = set(); k = 0
for c in sorted(cues['sounds'], key=lambda c: c['t']):
    key = (c['type'], round(c['t'], 2))                  # dedupe near-identical cues
    if key in seen or c['type'] not in SFX: continue     # unknown types are skipped, as in a production mixer
    seen.add(key); fn, vol = SFX[c['type']]; put(mix, fn(k), c['t'], vol); k += 1
print(k, 'sounds from', len(cues['sounds']), 'cues')

# ---- drone bed, as in the dark-drone-bed recipe: 48 Hz sine + low-passed brown noise, tremolo, 2 s in / 2.5 s out
t = np.arange(len(mix)) / SR
trem = lambda f, d: (1 - d / 2) + (d / 2) * np.sin(2 * np.pi * f * t)
br = _lf([1], [1, -.995], rng.standard_normal(len(t))); br = br / np.abs(br).max() * .5
b, a = butter(2, 220 / (SR / 2))
drone = (np.sin(2 * np.pi * 48 * t) * .07 * trem(.13, .6) + _lf(b, a, br) * .16 * trem(.1, .5)) * np.minimum(1, t / 2) * np.minimum(1, (dur - t) / 2.5)
mix += np.stack([drone, drone], 1).astype(np.float32)
mix = np.clip(mix, -.95, .95)                            # stand-in for alimiter=limit=0.95 (loudnorm is in the final-master recipe)
save(sys.argv[1], mix)

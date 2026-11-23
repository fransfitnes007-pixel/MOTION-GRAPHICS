"""Fitting voice lines into beat slots: each line has a start and a latest end; render it at a base speed, and if it runs long,
re-render faster (speed multiplied by the overrun, plus 0.01, capped at 1.35x). Loop for a local TTS such as
Kokoro-82M. The TTS model is not bundled, so this recipe uses a stand-in 'say()' that makes speech-shaped syllable bursts whose
length is proportional to the text and inversely to the speed. The printed table shows which lines needed a retry and which hit the cap.
Usage: python3 recipe.py out.wav"""
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

LINES = [  # (start, latest end, text) on a 128 BPM grid
  (0.25, 3.55, 'Short lines that fit.'),
  (3.80, 5.50, 'In every single slot.'),
  (5.72, 7.40, 'This is the main title.'),
  (7.55, 11.10, 'Start the project, and watch the results roll in, live.'),
  (11.30, 14.90, 'Real people do the work for you. Every step checked before it goes live.'),
]
base = 1.1
def say(text, sp):
    """Stand-in for Kokoro: ~0.09 s per character at speed 1.0, as syllable bursts."""
    total = len(text) * .09 / sp; t0 = 0.0; out = np.zeros(int(total * SR) + 1, np.float32); r = np.random.default_rng(len(text))
    while t0 < total - .1:
        L = min(.17 / sp * float(r.uniform(.8, 1.2)), total - t0); n = int(L * SR); t = np.arange(n) / SR
        f0 = 130 + 20 * np.sin(2 * np.pi * .9 * (t0 + t)); ph = 2 * np.pi * np.cumsum(f0) / SR
        x = sum(np.sin(k * ph) * (np.exp(-((k * 130 - 650) / 300) ** 2) + .6 * np.exp(-((k * 130 - 1700) / 500) ** 2)) / k ** .3 for k in range(1, 25))
        i = int(t0 * SR); out[i:i + n] += (x * np.sin(np.pi * t / L) ** 1.5)[:len(out) - i]
        t0 += L * 1.12
    return out
DUR = 16.0
track = np.zeros(int(SR * DUR), np.float32)
for a0, a1, text in LINES:
    sp = base; y = say(text, sp)
    while len(y) / SR > (a1 - a0) and sp < 1.35:
        sp = min(1.35, sp * (len(y) / SR) / (a1 - a0) + 0.01); y = say(text, sp)
    y = y / (np.abs(y).max() + 1e-6) * 0.9
    i = int(a0 * SR); track[i:i + len(y)] += y[:len(track) - i]
    flag = 'OVERRUNS (cap hit)' if len(y) / SR > (a1 - a0) + .01 else 'fits'
    print(f'{a0:5.2f}-{a0 + len(y) / SR:5.2f} (slot {a1:5.2f}) x{sp:.2f} {flag}  {text}')
save(sys.argv[1], np.stack([track, track], 1))

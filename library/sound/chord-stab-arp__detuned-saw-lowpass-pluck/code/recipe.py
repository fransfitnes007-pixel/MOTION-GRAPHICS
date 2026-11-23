"""Chord stab and arp: detuned saw pairs through a low-pass whose cutoff starts at 350 Hz + `bright` and falls fast, over Am F C G.
Part 1 is an intro arp (8th-note arpeggio, filter opening across 12 beats at 128 BPM, heard before
the slam). Part 2 is the groove stabs (122 BPM). Usage: python3 recipe.py out.wav"""
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

# ---- voices for the 128 BPM and 104 BPM beds: same ideas, slightly longer tails
def kick2():
    n = int(.45 * SR); t = np.arange(n) / SR
    f = 45 + 110 * np.exp(-t / .035); ph = 2 * np.pi * np.cumsum(f) / SR
    return (np.sin(ph) * env(n, .001, .16) + .3 * np.sin(ph * 2) * env(n, .001, .02)).astype(np.float32)
def clap2():
    n = int(.25 * SR); x = rng.standard_normal(n)
    e = sum(env(n, .0005, .012) * (np.arange(n) >= int(k * SR)) for k in (0, .009, .018)) + .6 * env(n, .001, .09)
    return (np.diff(np.concatenate([[0], x])) * e * .5).astype(np.float32)
def hat2(open_=False):
    n = int((.22 if open_ else .05) * SR); x = rng.standard_normal(n)
    x = x - lp(x, 7000)
    return (x * env(n, .0005, .07 if open_ else .012)).astype(np.float32)
def pluck2(freqs, dur, bright):
    n = int(dur * SR); x = sum(saw(f, n) + saw(f * 1.004, n) for f in freqs) / len(freqs)
    return (lp(x, 300 + bright * env(n, .001, .12)) * env(n, .002, .28)).astype(np.float32)
def bass2(f, dur):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) + .35 * lp(saw(f, n), 900)
    return (x * np.minimum(1, t / .004) * np.exp(-t / .35)).astype(np.float32)
def impact2():
    n = int(1.6 * SR); t = np.arange(n) / SR
    boom = np.sin(2 * np.pi * (38 + 60 * np.exp(-t / .08)) * t) * np.exp(-t / .5)
    crash = rng.standard_normal(n); crash = (crash - lp(crash, 3000)) * np.exp(-t / .45) * .35
    return (boom * .9 + crash).astype(np.float32)
def pad2(freqs, dur, cutoff=900):
    n = int(dur * SR); t = np.arange(n) / SR
    x = sum(saw(f, n) + saw(f * 1.006, n) + saw(f * .994, n) for f in freqs) / (3 * len(freqs))
    e = np.minimum(1, t / .6) * np.minimum(1, (dur - t) / .8)
    return (lp(x, cutoff) * e).astype(np.float32)

# ---- Part 1: intro arp, 12 beats at 128 BPM with the filter opening (bright 900 -> 4900)
B2 = 60 / 128
CHS = [[220, 261.63, 329.63], [174.61, 220, 261.63], [196 * 1.0, 261.63, 329.63], [196, 246.94, 293.66]]
p1 = buf(12 * B2 + .8)
for beat in range(12):
    t = beat * B2; ch = CHS[(beat // 4) % 4]
    for e8 in range(2):
        notes = [ch[(beat * 2 + e8) % 3] * (2 if (beat + e8) % 4 == 3 else 1)]
        bright = 900 + 4000 * min(1, beat / 12)
        put(p1, pluck2(notes, B2, bright), t + e8 * B2 / 2, .16, pan=(-.35 if e8 else .35))
    if beat >= 4: put(p1, hat2(), t + B2 / 2, .06)

# ---- Part 2: groove stabs, 4 bars at 122 BPM, chord stabs on the off 8th of beats 1 and 3, octave stab on the last 16th of beat 4
B = 60 / 122
p2 = buf(16 * B + .8)
for b in range(16):
    t = b * B; beat = b % 4; chord, root = CH[(b // 4) % 4]
    if beat in (0, 2): put(p2, pluck(chord, .25, 2600), t + B / 2, .22, pan=(-.25 if beat else .25))
    if beat == 3: put(p2, pluck([f * 2 for f in chord], .18, 3000), t + 3 * B / 4, .12)
out = np.concatenate([p1, np.zeros((int(.3 * SR), 2), np.float32), p2])
save(sys.argv[1], out)

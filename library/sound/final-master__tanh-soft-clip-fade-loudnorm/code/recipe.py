"""Final master: sum the buses, soft-clip with tanh, fade the tail with a ^1.5 curve, then (optionally) ffmpeg limiter + loudnorm.
Soft-clip and fade; alimiter limit=0.95 and loudnorm I=-15 TP=-1.2 LRA=11 (alimiter limit=0.89 for a tighter ceiling). The recipe renders three versions of the same 4 s of music in a
row: a hot raw sum hard-clipped at full scale, the tanh + fade master, and the same followed by ffmpeg loudnorm (skipped if no
ffmpeg is found). Prints peak, RMS and, when ffmpeg is there, integrated LUFS. Usage: python3 recipe.py out.wav"""
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

def groove_hit(mus, t, beat, B, chord, root):
    """One beat of the full groove branch (kick, clap on 2 and 4, open + closed hats, offbeat bass, stabs)."""
    put(mus, kick(), t, .85)
    if beat in (1, 3): put(mus, clap(), t, .55)
    put(mus, hat(True), t + B / 2, .22); put(mus, hat(), t + B / 4, .1); put(mus, hat(), t + 3 * B / 4, .1)
    put(mus, bass(root, B * .45), t, .5); put(mus, bass(root, B * .3), t + B / 2, .35)
    if beat in (0, 2): put(mus, pluck(chord, .25, 2600), t + B / 2, .22, pan=(-.25 if beat else .25))
    if beat == 3: put(mus, pluck([f * 2 for f in chord], .18, 3000), t + 3 * B / 4, .12)

import os, re, shutil, subprocess, tempfile
BPM = 122; B = 60 / BPM
DUR = 4.0
mus = buf(DUR); fx = buf(DUR)
for b in range(int(DUR / B) + 1):
    chord, root = CH[(b // 4) % 4]
    groove_hit(mus, b * B, b % 4, B, chord, root)
put(mus, impact(), 0, .9); put(fx, whoosh(), 0, .45)
raw = (mus * 1.0 + fx) * 1.6                              # deliberately hot so the difference is audible

def master(mix, dur):
    N = len(mix)
    fade = np.ones(N); a = int((dur - 1.4) * SR); fade[a:] = np.linspace(1, 0, N - a) ** 1.5      # last 1.4 s
    mix = mix * fade[:, None]
    return np.tanh(mix * 1.1) / np.tanh(1.1)                                                       # soft clip

FF = shutil.which('ffmpeg') or 'ffmpeg'
def loudnorm(x):
    if not os.path.exists(FF): return None
    with tempfile.TemporaryDirectory() as d:
        i, o = os.path.join(d, 'in.wav'), os.path.join(d, 'out.wav')
        sf.write(i, x.astype(np.float32), SR)
        subprocess.run([FF, '-y', '-loglevel', 'error', '-i', i, '-af', 'alimiter=limit=0.95,loudnorm=I=-15:TP=-1.2:LRA=11', '-ar', str(SR), o], check=True)
        return sf.read(o, dtype='float32')[0]
def lufs(x):
    if not os.path.exists(FF): return None
    with tempfile.TemporaryDirectory() as d:
        i = os.path.join(d, 'in.wav'); sf.write(i, x.astype(np.float32), SR)
        r = subprocess.run([FF, '-i', i, '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True).stderr
        m = re.findall(r'I:\s+(-?[\d.]+) LUFS', r); return float(m[-1]) if m else None
def report(name, x):
    pk = float(np.abs(x).max()); rms = float(np.sqrt((x ** 2).mean()))
    print(f'{name:22s} peak {20 * np.log10(pk + 1e-9):6.1f} dBFS   rms {20 * np.log10(rms + 1e-9):6.1f} dBFS   LUFS {lufs(x)}')

A = np.clip(raw, -1, 1)                  # what a hot sum becomes when it hits full scale
Bm = master(raw / 1.6 * 1.0, DUR)        # master chain on the un-boosted sum: fade + tanh(x*1.1)/tanh(1.1)
Cm = loudnorm(Bm)
report('A raw, hard-clipped', A); report('B tanh + fade', Bm)
if Cm is not None: report('C B + loudnorm -15', Cm)
gap = np.zeros((int(.5 * SR), 2), np.float32)
parts = [A, gap, Bm] + ([gap, Cm] if Cm is not None else [])
out = np.concatenate(parts)
sf.write(sys.argv[1], out.astype(np.float32), SR, subtype='FLOAT')   # 32-bit float, no normalisation: levels are the point (B peaks above 0 dBFS, see SKILL.md)
print('wrote', sys.argv[1], f'{len(out) / SR:.2f}s peak', round(float(np.abs(out).max()), 3))

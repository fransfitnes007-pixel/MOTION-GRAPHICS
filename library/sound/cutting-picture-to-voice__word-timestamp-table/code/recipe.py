"""Cutting picture to voice words: a table of word start times from a speech-to-text pass (faster-whisper word_timestamps) is offset
by the time the voice starts in the final track, and every scene cut is written as 'word time minus a small lead'. Table and cut formulas (WT, VO = 0.4, C)
as used in a scripted page. This recipe lets you hear the grid: a soft tick on every word,
a whoosh on every cut. Usage: python3 recipe.py out.wav   (or: python3 recipe.py out.wav --transcribe voice.wav to regenerate the table; needs faster-whisper)"""
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

# ---- how the table is produced (not run by default)
def transcribe(path, model='small.en'):
    from faster_whisper import WhisperModel
    m = WhisperModel(model, device='cpu', compute_type='int8')
    segs, _ = m.transcribe(path, word_timestamps=True, beam_size=5, initial_prompt='YourBrand. yourbrand dot com.')
    return [{'w': w.word.strip(), 's': round(w.start, 3), 'e': round(w.end, 3), 'p': round(w.probability, 2)} for s in segs for w in s.words]

# ---- an example word table, seconds into the voice take
VO = 0.4
WT = { 'w01': 0, 'w02': .34, 'w03': .86, 'w04': 1.64, 'w05': 2.4, 'w06': 3.66, 'w07': 3.76, 'w08': 4.04, 'w09': 4.28, 'w10': 4.94, 'w11': 5.06, 'w12': 5.34, 'w13': 5.58, 'w14': 5.74, 'w15': 5.86, 'w16': 6.28,
  'w17': 7.42, 'w18': 7.44, 'w19': 7.64, 'w20': 7.78, 'w21': 7.94, 'w22': 8.24, 'w23': 8.5, 'w24': 8.64, 'w25': 9.26, 'w26': 10.52, 'w27': 10.84, 'w28': 11.52, 'w29': 11.88, 'w30': 12.42, 'w31': 12.6,
  'w32': 13.56, 'w33': 13.98, 'w34': 14.08, 'w35': 14.58, 'w36': 15.32, 'w37': 15.66, 'w38': 16.14, 'w39': 16.88, 'w40': 17.36, 'w41': 18.24, 'w42': 18.48, 'w43': 19.0, 'w44': 19.68, 'w45': 19.74, 'w46': 20.06, 'w47': 20.3, 'w48': 21.42, 'w49': 22.42 }
for k in WT: WT[k] += VO
# scene cuts: each lands a hair before the word that starts the scene, so the picture is already there when the word is heard
C = { 'cut01': WT['w06'] - .16, 'cut02': WT['w13'] - .02, 'cut03': WT['w15'], 'cut04': WT['w16'] + .02, 'cut05': WT['w17'] - .02, 'cut06': WT['w20'] - .02, 'cut07': WT['w26'] - .06, 'cut08': WT['w31'] - .02, 'cut09': WT['w32'] - .04, 'cut10': WT['w36'] - .04, 'cut11': WT['w39'] - .04, 'cut12': WT['w41'] - .04, 'cut13': WT['w45'] - .06, 'cut14': WT['w48'] - .5, 'cut15': 25.4 }
print('cut table (s):'); [print(f'  {k:7s} {v:6.2f}') for k, v in C.items()]

if len(sys.argv) > 3 and sys.argv[2] == '--transcribe':
    print(transcribe(sys.argv[3])); sys.exit()

# ---- hear the grid: tick on every word start, whoosh on every cut (placed 0.18 s early like the whooshes in the other recipes)
fx = buf(24.0)
for k, w in WT.items(): put(fx, tick(1800), w, .22)
for k, c in C.items():
    if k != 'end': put(fx, whoosh(), c - .18, .45)
save(sys.argv[1], fx)

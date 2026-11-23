"""Full video soundtrack: 122 BPM, A minor (Am F C G). Plucks + hats with a riser into a slam at 6.7 s, full groove from there, a drop-out
for the joke beat at 21.3 s, a soft pad under the end card, whooshes on every cut, pops on word reveals, cursor clicks, keypress-style
ticks under a counter, a confetti burst. The voice is optional.
Usage: python3 recipe.py out.wav [voice.wav]   (without a voice file the track is music and effects only; with one, the music ducks under it
and the voice starts at VO = 0.4 s, as in the demo mix)"""
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

BPM = 122; B = 60 / BPM; DUR = 29.0; VO = 0.4
N = int(SR * DUR)
mus = np.zeros((N, 2), np.float32); fx = np.zeros((N, 2), np.float32)

# ---- music: A minor, chords Am F C G, one chord per bar
SLAM, DONE, JOKE, END = 6.70, 13.00, 21.30, 25.40
beats = int(DUR / B) + 1
for b in range(beats):
    t = b * B; bar = b // 4; beat = b % 4; chord, root = CH[bar % 4]
    if t >= END - .2: break
    intro = t < SLAM; drop = JOKE <= t < END
    if intro:
        if beat in (0, 2): put(mus, pluck(chord, .3, 1800 + 2400 * t / SLAM), t, .22)
        if beat in (1, 3): put(mus, pluck([f * 2 for f in chord[:2]], .22, 2000 + 2400 * t / SLAM), t + B / 2, .12, pan=.3)
        put(mus, hat(), t + B / 2, .12 * (t / SLAM))
        if beat == 0 and bar > 0: put(mus, kick(), t, .5 * (t / SLAM))
    elif drop:
        if beat == 0: put(mus, pluck(chord, .6, 900), t, .12)
    else:
        groove_hit(mus, t, beat, B, chord, root)
put(mus, pad([110, 164.8, 220, 261.6], DUR - END), END, .18)
put(mus, noise_swell(2.2, 2.0), SLAM - 2.0, .5)                     # riser into the slam
put(mus, noise_swell(1.0, .9), DONE - .9, .3)
put(mus, impact(), SLAM, .9); put(mus, impact(), DONE, .55); put(mus, impact(), END, .4)

# ---- effects, timed to the picture (index.html cut times)
for c in (3.9, 5.96, 7.8, 8.16, 10.86, 13.92, 15.68, 17.24, 18.6, 20.08, 21.3): put(fx, whoosh(), c - .18, .45)
put(fx, whoosh(.9, True), 2.8, .6)                                   # the feed refresh scroll
for i, h in enumerate((0.4, 1.26, 2.04, 2.8)): put(fx, pop(640 + i * 90), h, .25)   # stamps
for h in (1.26,): put(fx, pop(1500), h + .05, .12)                   # heart
for i, h in enumerate((4.06, 4.16, 4.44, 4.68, 5.34, 5.46, 5.74)): put(fx, pop(900 + (i % 3) * 120), h, .11, pan=(-.3 if i % 2 else .3))
put(fx, whoosh(.35, False), 6.0, .5)                                 # IN THE sweep
put(fx, click(), 2.46, .9); put(fx, click(), 12.88, .9)              # button clicks
for i, h in enumerate((7.82, 7.84, 8.04)): put(fx, pop(1000 + i * 150), h, .13)
for i in range(48): put(fx, pop(1100 + (i % 5) * 90), 9.14 + (i % 12) * .035 + (i // 12) * .02, .06, pan=(i % 3 - 1) * .4)   # tiles
for h, f in ((13.0, 700), (13.12, 900), (13.26, 1100)): put(fx, pop(f), h, .18)     # And done + G bounce
for h in (14.5, 14.95, 16.06, 16.6): put(fx, pop(1250), h, .14)      # notes, review chips
for i in range(4): put(fx, pop(1300 + i * 80), 17.76 + i * .07, .12, pan=(i - 1.5) * .3)   # platform pills
for i in range(28): put(fx, tick(2200 + (i % 4) * 150), 18.64 + i * .028, .35)     # counter
put(fx, pop(1700), 20.7, .25)
for i in range(16): put(fx, pop(1500 + rng.integers(0, 900)), 20.72 + i * .03, .06, pan=rng.uniform(-.6, .6))   # confetti
put(fx, pop(500), 21.82, .18); put(fx, pop(420), 22.82, .22)         # two punchline pops
put(fx, click(), 27.0, .9); put(fx, whoosh(.5, True), 25.25, .5)   # end card click and wipe
for i in range(13): put(fx, pop(2000 + (i % 4) * 120), 27.15 + i * .06, .07)   # the address types itself

# ---- voice (optional) and the ducking maths, then the master
if len(sys.argv) > 2:
    vo, vsr = sf.read(sys.argv[2], dtype='float32')
    if vo.ndim > 1: vo = vo.mean(1)
    if vsr != SR: vo = np.interp(np.arange(int(len(vo) * SR / vsr)) / SR, np.arange(len(vo)) / vsr, vo).astype(np.float32)
    vo = np.concatenate([np.zeros(int(VO * SR), np.float32), vo])
else:
    vo = np.zeros(N, np.float32)
vo = np.pad(vo, (0, max(0, N - len(vo))))[:N]
lvl = np.convolve(np.abs(vo), np.ones(int(.05 * SR)) / int(.05 * SR), 'same')
duck = 1 - .5 * np.clip(lvl / .05, 0, 1)
duck = np.convolve(duck, np.ones(int(.08 * SR)) / int(.08 * SR), 'same')
mix = mus * duck[:, None] * .75 + fx * (0.6 + 0.4 * duck[:, None]) + np.stack([vo, vo], 1) * 1.05
fade = np.ones(N); a = int((DUR - 1.4) * SR); fade[a:] = np.linspace(1, 0, N - a) ** 1.5
mix *= fade[:, None]
mix = np.tanh(mix * 1.1) / np.tanh(1.1)
pk = float(np.abs(mix).max())
if pk > .95: mix *= .95 / pk     # demo only: tanh(x*1.1)/tanh(1.1) can reach 1.2, which a 16-bit file would clip
sf.write(sys.argv[1], mix.astype(np.float32), SR, subtype='PCM_16')
print('wrote', sys.argv[1], f'{DUR}s peak', round(float(np.abs(mix).max()), 3))

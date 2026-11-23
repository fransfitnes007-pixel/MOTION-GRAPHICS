#!/usr/bin/env python3
"""Any text as a liquid-chrome logo on a transparent background (numpy, scipy, Pillow).
Height field from the letter shapes, normals from it, reflection into a studio environment warped by low-frequency noise
so the dark reflections run like liquid metal, plus two sharp specular lights. The outline is the font's own; only the fill is chrome.
  python3 chrome_text.py <font.ttf> <out_dir> "yourbrand.com"      writes <slug>-chrome*.png and <slug>-chrome-glow*.png
  from chrome_text import chrome; plain, glow = chrome(font_path, "Y")   (PIL images)"""
import sys, os, numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage as nd

def chrome(font_path, text, SIZE=900):
    font = ImageFont.truetype(font_path, SIZE)
    x0, y0, x1, y1 = font.getbbox(text)
    pad = int(SIZE * 0.12)
    W, H = x1 - x0 + 2 * pad, y1 - y0 + 2 * pad
    mask_img = Image.new('L', (W, H), 0)
    ImageDraw.Draw(mask_img).text((pad - x0, pad - y0), text, font=font, fill=255)
    mask = np.asarray(mask_img, np.float32) / 255.0
    inside = mask > 0.5

    # Height: a soft blur of the letters, so the shading is smooth and adds no ridges; the outline stays the font's own.
    u = nd.gaussian_filter(mask, SIZE * 0.012)
    h = nd.gaussian_filter(mask, SIZE * float(os.environ.get("BEVEL", "0.022"))) * SIZE * 0.05
    gy, gx = np.gradient(h)
    k = 1.0
    nx, ny, nz = -gx * k, -gy * k, np.ones_like(h)
    n = np.sqrt(nx ** 2 + ny ** 2 + nz ** 2); nx /= n; ny /= n; nz /= n
    rx, ry, rz = 2 * nz * nx, 2 * nz * ny, 2 * nz * nz - 1

    # Liquid wobble: smooth noise from a few big blurred random fields, added to the reflection lookup.
    rng = np.random.default_rng(7)
    def smooth_noise(scale):
        sw, sh = max(4, int(W / scale)), max(4, int(H / scale))
        z = rng.standard_normal((sh, sw)).astype(np.float32)
        z = nd.zoom(z, (H / sh, W / sw), order=3)[:H, :W]
        z = np.pad(z, ((0, max(0, H - z.shape[0])), (0, max(0, W - z.shape[1]))), mode='edge')
        return z / (np.abs(z).max() + 1e-6)
    wob = 0.55 * smooth_noise(SIZE * 0.28) + 0.3 * smooth_noise(SIZE * 0.12)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)

    # Environment by reflected elevation e (-1 floor .. +1 sky), warped.
    rows = np.where(inside.any(1))[0]; xt, xb = rows[0] + (rows[-1] - rows[0]) * 0.18, rows[-1] - (rows[-1] - rows[0]) * 0.2  # x-height band
    yn = (yy - xt) / (xb - xt)
    e = (0.95 - 1.9 * yn) * 0.8 - ry * 0.55 + 0.20 * wob + 0.06 * rx
    def band(c, w): return np.exp(-((e - c) / w) ** 2)
    env = (0.58 + 0.40 * np.clip(e, 0, 1) ** 0.6          # sky: bright, whiter going up
           - 0.62 * band(0.02, 0.13)                       # the dark horizon band that makes chrome read as chrome
           - 0.35 * band(-0.42, 0.10)                      # a second dark reflection low down
           + 0.22 * band(-0.75, 0.16))                     # bright floor bounce
    env = np.where(e < -0.05, np.minimum(env, 0.62 + 0.25 * band(-0.75, 0.2)), env)
    # Two sharp lights, upper left and upper right, as hot white streaks.
    def spec(lx, ly, lz, p):
        l = np.sqrt(lx * lx + ly * ly + lz * lz)
        return np.clip((rx * lx + ry * ly + rz * lz) / l, 0, 1) ** p
    lum = env + 0.85 * spec(-0.45, -0.7, 0.55, 40) + 0.55 * spec(0.55, -0.55, 0.6, 70) + 0.25 * spec(0, 0.2, 1, 18)
    # Edges roll off into darker steel, like the rims on the logo.
    lum *= 0.80 + 0.20 * np.clip(u * 2, 0, 1)
    lum = np.clip(lum, 0, 1.25)
    lum = 1 - np.exp(-1.9 * lum)                           # soft shoulder, whites stay creamy, not clipped flat
    lum /= lum.max()

    # Neutral silver, a hair warm in the highlights and cool-grey in the shadows (never blue).
    r = np.clip(lum * 1.00 + 0.012, 0, 1); g = np.clip(lum * 0.995 + 0.010, 0, 1); b = np.clip(lum * 1.01 + 0.012, 0, 1)
    rgba = np.dstack([r, g, b, mask]) * 255
    img = Image.fromarray(rgba.astype(np.uint8))
    img = img.crop(img.getbbox())
    bw, bh = img.size; m = int(bh * 0.06)
    canvas = Image.new('RGBA', (bw + 2 * m, bh + 2 * m), (0, 0, 0, 0)); canvas.paste(img, (m, m)); img = canvas

    # A soft white glow version, the way a chrome mark is shown on dark backgrounds.
    a = np.asarray(img)[..., 3].astype(np.float32) / 255
    g1 = nd.gaussian_filter(a, img.size[1] * 0.06) * 0.55
    glow_a = np.clip(np.maximum(a, g1), 0, 1)
    base = np.asarray(img).astype(np.float32) / 255
    rgb = base[..., :3] * a[..., None] + 1.0 * (1 - a[..., None])           # glow is white
    glow = Image.fromarray((np.dstack([rgb, glow_a]) * 255).astype(np.uint8))


    return img, glow

if __name__ == "__main__":
    font_path, out = sys.argv[1], sys.argv[2]
    text = sys.argv[3] if len(sys.argv) > 3 else "yourbrand.com"
    img, glow = chrome(font_path, text)
    os.makedirs(out, exist_ok=True)
    slug = text.replace(".", "-").replace(" ", "-").lower()
    for wpx in (img.size[0], 2400, 1200, 600):
        sfx = "" if wpx == img.size[0] else f"-{wpx}"
        hpx = round(img.size[1] * wpx / img.size[0])
        img.resize((wpx, hpx), Image.LANCZOS).save(os.path.join(out, f"{slug}-chrome{sfx}.png"), optimize=True)
        glow.resize((wpx, hpx), Image.LANCZOS).save(os.path.join(out, f"{slug}-chrome-glow{sfx}.png"), optimize=True)
    print("master", img.size)

import sys, glob, os
from PIL import Image, ImageDraw
d, cols = sys.argv[1], int(sys.argv[2])
fs = sorted(glob.glob(d + '/t-*.png'), key=lambda f: float(os.path.basename(f)[2:-4]))
w, h = 270, 480; rows = (len(fs) + cols - 1) // cols
S = Image.new('RGB', (cols * w, rows * (h + 24)), 'black'); dr = ImageDraw.Draw(S)
for i, f in enumerate(fs):
    x, y = (i % cols) * w, (i // cols) * (h + 24); S.paste(Image.open(f).convert('RGB').resize((w, h)), (x, y + 24)); dr.text((x + 6, y + 4), os.path.basename(f), fill='yellow')
S.save(d + '/sheet.jpg', quality=85); print(d + '/sheet.jpg')

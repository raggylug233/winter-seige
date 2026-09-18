#!/usr/bin/env python3
"""Crop the squad list (with stronghold header) out of Winter Siege screenshots
and tile 4 per image for reading. Usage: tile.py <screenshot dir> <out dir>"""
import glob, os, sys
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
files = sorted(f for f in glob.glob(os.path.join(src, '*')) if f.lower().endswith(('.png', '.jpg', '.jpeg')))
crops = []
for f in files:
    im = Image.open(f)
    w, h = im.size
    # normalise to the 1206x2622 phone layout used so far
    if (w, h) != (1206, 2622):
        im = im.resize((1206, round(h * 1206 / w)))
    crops.append((os.path.basename(f), im.crop((60, 380, 1150, 1960)).resize((545, 790))))
for i in range(0, len(crops), 4):
    grp = crops[i:i + 4]
    m = Image.new('RGB', (545 * len(grp), 790), 'white')
    for j, (n, c) in enumerate(grp):
        m.paste(c, (545 * j, 0))
    m.save(f'{out}/t{i // 4:02d}.png')
print(len(crops), 'screens ->', (len(crops) + 3) // 4, 'tiles in', out)

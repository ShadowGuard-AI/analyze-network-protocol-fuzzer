#!/usr/bin/env python3
"""analyze-network-protocol-fuzzer wordmark banner: a collectors bench at dawn. The name enters
once only, handwritten in Averia Sans Libre on a bone white tag tied with string to the front
edge of the bench. No other readable writing anywhere."""
import random, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
random.seed(902)
V1 = "--v1" in sys.argv
W, H = 1200, 520
BLACK = (24, 20, 16); BONE = (240, 234, 220); AMBER = (206, 146, 52); RED = (176, 38, 32)
img = Image.new("RGB", (W, H), BLACK); d = ImageDraw.Draw(img, "RGBA")
for r in range(3):
    for c in range(5):
        x, y = 30 + c * 232, 16 + r * 80
        d.rectangle([x, y, x + 208, y + 62], outline=(58, 48, 38), width=3)
        d.ellipse([x + 96, y + 24, x + 112, y + 40], outline=(120, 96, 58), width=3)
for r in range(130, 10, -13):  # warm bench lamp glow at the left edge
    d.ellipse([36 - r, 44 - r * .6, 36 + r, 44 + r * .6], fill=(226, 164, 70, 10))
d.rectangle([1022, 24, 1156, 148], fill=(214, 224, 226))  # high window, pale dawn wash at the right
d.line([(1089, 24), (1089, 148)], fill=(90, 92, 90), width=4)
d.line([(1022, 86), (1156, 86)], fill=(90, 92, 90), width=4)
d.rectangle([0, 292, W, H], fill=(74, 58, 40))
d.rectangle([0, 292, W, 304], fill=(96, 76, 52))
for _ in range(500):
    x, y = random.uniform(0, W), random.uniform(306, H)
    d.point((x, y), fill=random.choice([(88, 68, 46), (64, 50, 34)]))
# second board leaning empty against the cabinet
d.polygon([(856, 158), (988, 186), (974, 306), (844, 280)], fill=(228, 220, 198))
d.line([(900, 168), (886, 290)], fill=(150, 140, 118), width=3)
# glass topped drawer half open, rows of set specimens as coloured wing shapes only
d.polygon([(620, 322), (884, 322), (920, 380), (596, 380)], fill=(30, 26, 22))
d.polygon([(632, 330), (876, 330), (902, 372), (610, 372)], fill=(232, 226, 208))
for r in range(2):
    for c in range(6):
        x, y = 662 + c * 38, 344 + r * 15
        col = random.choice([(206, 146, 52), (150, 90, 60), (110, 120, 140)])
        d.ellipse([x - 8, y - 3, x, y + 3], fill=col); d.ellipse([x, y - 3, x + 8, y + 3], fill=col)
if V1:  # v1 flaw: small printed labels inside the drawer resolve into readable marks
    for c in range(6):
        x = 640 + c * 38
        d.rectangle([x, 356, x + 26, 366], fill=(250, 248, 240))
        d.line([(x + 3, 361), (x + 22, 361)], fill=(40, 36, 32), width=2)
# the main setting board in the foreground, one amber winged specimen pinned and papered open
bx0, by0, bx1, by1 = 120, 318, 560, 478
d.rectangle([bx0, by0, bx1, by1], fill=BONE)
d.rectangle([bx0, by0, bx1, by1], outline=(198, 138, 44), width=4)
d.line([((bx0 + bx1) // 2, by0 + 8), ((bx0 + bx1) // 2, by1 - 8)], fill=(90, 78, 60), width=3)
cx, cy = (bx0 + bx1) // 2, (by0 + by1) // 2 + 4
d.ellipse([cx - 168, cy - 56, cx - 6, cy + 26], fill=(28, 23, 19)); d.ellipse([cx + 6, cy - 56, cx + 168, cy + 26], fill=(28, 23, 19))
d.ellipse([cx - 155, cy - 51, cx - 6, cy + 21], fill=AMBER); d.ellipse([cx + 6, cy - 51, cx + 155, cy + 21], fill=AMBER)
d.ellipse([cx - 128, cy + 14, cx - 10, cy + 64], fill=(28, 23, 19)); d.ellipse([cx + 10, cy + 14, cx + 128, cy + 64], fill=(28, 23, 19))
d.ellipse([cx - 116, cy + 19, cx - 10, cy + 59], fill=(188, 124, 44)); d.ellipse([cx + 10, cy + 19, cx + 116, cy + 59], fill=(188, 124, 44))
d.ellipse([cx - 34, cy + 22, cx - 22, cy + 34], fill=RED); d.ellipse([cx + 22, cy + 22, cx + 34, cy + 34], fill=RED)
for (x0, y0, x1, y1) in [(cx - 178, cy - 44, cx - 130, cy - 18), (cx + 130, cy - 44, cx + 178, cy - 18)]:
    d.rectangle([x0, y0, x1, y1], fill=(250, 247, 238, 210), outline=(200, 192, 170))
d.ellipse([cx - 8, cy - 34, cx + 8, cy + 42], fill=(24, 20, 17))
d.ellipse([cx - 6, cy - 58, cx + 6, cy - 46], fill=(8, 8, 8))
d.point((cx - 2, cy - 54), fill=(255, 255, 255))
# tools in the order they were used: pin row in cork, forceps on a folded cloth, blank tags with tangled string
d.rectangle([610, 420, 770, 456], fill=(186, 148, 96))
for i in range(6):
    x = 630 + i * 24
    d.line([(x, 426), (x, 450)], fill=(60, 58, 56), width=2); d.ellipse([x - 4, 422, x + 4, 430], fill=(12, 12, 12))
d.polygon([(806, 424), (966, 414), (978, 452), (818, 462)], fill=(148, 150, 144))
d.line([(830, 428), (950, 444)], fill=(168, 170, 172), width=4)
d.line([(836, 442), (950, 444)], fill=(140, 142, 144), width=4)
for i in range(3):
    x, y = 150 + i * 10, 250 - i * 4
    d.polygon([(x, y), (x + 66, y + 6), (x + 60, y + 34), (x - 4, y + 28)], fill=(238, 231, 214), outline=(190, 180, 158))
    d.arc([x + 52, y - 6, x + 78, y + 16], 200, 120, fill=(170, 150, 110), width=2)
# the one inscription: the collectors own cabinet label, a bone tag tied with string to the bench front edge
tx0, ty0, tx1, ty1 = (286, 428, 914, 492) if not V1 else (360, 434, 840, 486)
d.line([(330, 300), (tx0 + 26, ty0)], fill=(170, 150, 110), width=2)
d.line([(870, 300), (tx1 - 26, ty0)], fill=(170, 150, 110), width=2)
d.rounded_rectangle([tx0, ty0, tx1, ty1], 8, fill=(242, 236, 222), outline=(198, 138, 44), width=3)
d.ellipse([tx0 + 12, ty0 + 24, tx0 + 24, ty0 + 36], outline=(120, 100, 70), width=2)
d.ellipse([tx1 - 24, ty0 + 24, tx1 - 12, ty0 + 36], outline=(120, 100, 70), width=2)
try:
    f = ImageFont.truetype(__file__.rsplit("/", 1)[0] + "/fonts/AveriaSansLibre.ttf", 30 if V1 else 33)
except Exception:
    f = ImageFont.load_default()
# v1 flaw: the tag is too small, so the long name overflows both edges of the bone tag
d.text(((tx0 + tx1) // 2, (ty0 + ty1) // 2), "analyze-network-protocol-fuzzer", font=f, fill=(30, 25, 20), anchor="mm")
img = img.filter(ImageFilter.GaussianBlur(0.4))
out = "scratch/banner-v1.png" if V1 else "banner.png"
img.save(__file__.rsplit("/", 1)[0] + "/" + out); print("saved", out)

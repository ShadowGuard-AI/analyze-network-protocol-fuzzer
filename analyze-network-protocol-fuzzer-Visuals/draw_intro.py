#!/usr/bin/env python3
"""analyze-network-protocol-fuzzer intro: the collectors bench and its boards, nothing that can
be read. The setting board at close focus with one butterfly pinned flat under paper strips,
a pin row in cork, forceps on a cloth, blank tags from their unprinted sides, a half open glass
topped drawer, cabinet black behind, dawn at the high window and lamp glow at the left."""
import random, sys
from PIL import Image, ImageDraw, ImageFilter
random.seed(331)
V1 = "--v1" in sys.argv
W, H = 1200, 520
BLACK = (24, 20, 16); BONE = (240, 234, 220); AMBER = (206, 146, 52); RED = (176, 38, 32)
img = Image.new("RGB", (W, H), BLACK); d = ImageDraw.Draw(img, "RGBA")
# cabinet black drawers and shelving rising out of focus in the background
for r in range(3):
    for c in range(5):
        x, y = 30 + c * 232, 18 + r * 84
        d.rectangle([x, y, x + 208, y + 66], outline=(58, 48, 38), width=3)
        d.ellipse([x + 96, y + 26, x + 112, y + 42], outline=(120, 96, 58), width=3)
# warm lamp glow as a soft amber pool at the upper left, no fitting detailed
for r in range(120, 10, -12):
    d.ellipse([60 - r, 30 - r * .6, 60 + r, 30 + r * .6], fill=(226, 164, 70, 10))
# the high window as a pale rectangle at the upper right
d.rectangle([1010, 26, 1150, 150], fill=(214, 224, 226))
d.line([(1080, 26), (1080, 150)], fill=(90, 92, 90), width=4)
d.line([(1010, 88), (1150, 88)], fill=(90, 92, 90), width=4)
# bench surface
d.rectangle([0, 300, W, H], fill=(74, 58, 40))
d.rectangle([0, 300, W, 312], fill=(96, 76, 52))
for _ in range(500):
    x, y = random.uniform(0, W), random.uniform(314, H)
    d.point((x, y), fill=random.choice([(88, 68, 46), (64, 50, 34)]))
# the second empty board leaning against the cabinet, midground
d.polygon([(838, 168), (972, 196), (958, 322), (826, 296)], fill=(228, 220, 198))
d.line([(882, 178), (868, 306)], fill=(150, 140, 118), width=3)
# half open glass topped drawer with set specimens visible only as coloured wing shapes in rows
d.polygon([(64, 330), (330, 330), (366, 388), (40, 388)], fill=(30, 26, 22))
d.polygon([(76, 338), (322, 338), (348, 380), (56, 380)], fill=(232, 226, 208))
for r in range(2):
    for c in range(5):
        x, y = 96 + c * 48, 350 + r * 16
        col = random.choice([(206, 146, 52), (150, 90, 60), (110, 120, 140), (176, 60, 50)])
        d.ellipse([x - 9, y - 4, x, y + 4], fill=col); d.ellipse([x, y - 4, x + 9, y + 4], fill=col)
d.polygon([(64, 330), (330, 330), (366, 388), (40, 388)], outline=(140, 150, 150), width=2)
# pile of blank tags shown from their unprinted sides
for i in range(4):
    x, y = 996 + i * 9, 398 - i * 5
    d.polygon([(x, y), (x + 74, y + 8), (x + 68, y + 40), (x - 4, y + 32)], fill=(238, 231, 214), outline=(190, 180, 158))
# THE setting board at close focus, foreground centre
bx0, by0, bx1, by1 = 356, 330, 800, 496
d.rectangle([bx0, by0, bx1, by1], fill=BONE)
d.rectangle([bx0, by0, bx1, by1], outline=(168, 138, 70), width=4)
d.line([((bx0 + bx1) // 2, by0 + 8), ((bx0 + bx1) // 2, by1 - 8)], fill=(90, 78, 60), width=3)  # central groove
cx, cy = (bx0 + bx1) // 2, (by0 + by1) // 2 + 4
if V1:  # v1 flaw: the wings are drawn tall and raised, a specimen folding instead of set flat
    d.ellipse([cx - 118, cy - 74, cx - 8, cy + 6], fill=AMBER); d.ellipse([cx + 8, cy - 74, cx + 118, cy + 6], fill=AMBER)
    d.ellipse([cx - 92, cy - 2, cx - 8, cy + 52], fill=(52, 40, 30)); d.ellipse([cx + 8, cy - 2, cx + 92, cy + 52], fill=(52, 40, 30))
else:  # wings held perfectly flat: wide forewings in amber deepening to cabinet black margins
    d.ellipse([cx - 168, cy - 56, cx - 6, cy + 26], fill=(30, 25, 20)); d.ellipse([cx + 6, cy - 56, cx + 168, cy + 26], fill=(30, 25, 20))
    d.ellipse([cx - 155, cy - 51, cx - 6, cy + 21], fill=AMBER); d.ellipse([cx + 6, cy - 51, cx + 155, cy + 21], fill=AMBER)
    d.ellipse([cx - 128, cy + 14, cx - 10, cy + 66], fill=(30, 25, 20)); d.ellipse([cx + 10, cy + 14, cx + 128, cy + 66], fill=(30, 25, 20))
    d.ellipse([cx - 116, cy + 19, cx - 10, cy + 61], fill=(188, 124, 44)); d.ellipse([cx + 10, cy + 19, cx + 116, cy + 61], fill=(188, 124, 44))
    # one tag red spot near the base of each hindwing
    d.ellipse([cx - 34, cy + 22, cx - 22, cy + 34], fill=RED); d.ellipse([cx + 22, cy + 22, cx + 34, cy + 34], fill=RED)
    # paper strips pinned over the wing tips
    for (x0, y0, x1, y1) in [(cx - 176, cy - 44, cx - 128, cy - 18), (cx + 128, cy - 44, cx + 176, cy - 18), (cx - 140, cy + 40, cx - 96, cy + 64), (cx + 96, cy + 40, cx + 140, cy + 64)]:
        d.rectangle([x0, y0, x1, y1], fill=(250, 247, 238, 210), outline=(200, 192, 170))
# thorax and the single pin, its black head catching one point of light
d.ellipse([cx - 8, cy - 34, cx + 8, cy + 44], fill=(26, 22, 18))
d.line([(cx, cy - 52), (cx, cy + 6)], fill=(40, 38, 36), width=3)
d.ellipse([cx - 6, cy - 60, cx + 6, cy - 48], fill=(10, 10, 10))
d.point((cx - 2, cy - 56), fill=(255, 255, 255))
# pin row in a cork strip at the lower left
d.rectangle([66, 436, 250, 478], fill=(186, 148, 96))
for i in range(6):
    x = 88 + i * 27
    d.line([(x, 442), (x, 470)], fill=(60, 58, 56), width=2)
    d.ellipse([x - 4, y - 4 if False else 438, x + 4, 446], fill=(12, 12, 12))
# forceps lying across a folded cloth at the lower right
d.polygon([(880, 448), (1064, 436), (1076, 478), (892, 490)], fill=(148, 150, 144))
d.line([(910, 452), (1046, 470)], fill=(168, 170, 172), width=4)
d.line([(916, 466), (1046, 470)], fill=(140, 142, 144), width=4)
img = img.filter(ImageFilter.GaussianBlur(0.45))
out = "scratch/intro-v1.png" if V1 else "intro-banner.png"
img.save(__file__.rsplit("/", 1)[0] + "/" + out); print("saved", out)

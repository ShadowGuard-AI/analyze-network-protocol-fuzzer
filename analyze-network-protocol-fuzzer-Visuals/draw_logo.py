#!/usr/bin/env python3
"""analyze-network-protocol-fuzzer logo: a setting board seen from directly above, bone white
with a central groove, one butterfly held open by two fine paper strips pinned at the wing tips,
amber forewings deepening to cabinet black margins, one tag red spot at each hindwing base,
a single pin through the thorax, the name in Averia Sans Libre in bone white on cabinet black."""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
V1 = "--v1" in sys.argv
W, H = 900, 560
BLACK = (24, 20, 16); BONE = (240, 234, 220); AMBER = (206, 146, 52); RED = (176, 38, 32)
img = Image.new("RGB", (W, H), BLACK); d = ImageDraw.Draw(img, "RGBA")
bx0, by0, bx1, by1 = 190, 44, 710, 356
d.rectangle([bx0, by0, bx1, by1], fill=BONE)
d.rectangle([bx0, by0, bx1, by1], outline=(198, 138, 44), width=5)
d.line([((bx0 + bx1) // 2, by0 + 10), ((bx0 + bx1) // 2, by1 - 10)], fill=(90, 78, 60), width=3)
cx, cy = (bx0 + bx1) // 2, (by0 + by1) // 2 + 6
# wings held flat and open
# each wing is drawn black first, then amber inset toward the body, so the black survives only as a margin band at the outer edge
d.ellipse([cx - 208, cy - 74, cx - 8, cy + 34], fill=(28, 23, 19)); d.ellipse([cx + 8, cy - 74, cx + 208, cy + 34], fill=(28, 23, 19))
d.ellipse([cx - 194, cy - 69, cx - 8, cy + 29], fill=AMBER); d.ellipse([cx + 8, cy - 69, cx + 194, cy + 29], fill=AMBER)
d.ellipse([cx - 158, cy + 20, cx - 12, cy + 88], fill=(28, 23, 19)); d.ellipse([cx + 12, cy + 20, cx + 158, cy + 88], fill=(28, 23, 19))
d.ellipse([cx - 145, cy + 25, cx - 12, cy + 83], fill=(188, 124, 44)); d.ellipse([cx + 12, cy + 25, cx + 145, cy + 83], fill=(188, 124, 44))
d.ellipse([cx - 42, cy + 30, cx - 28, cy + 44], fill=RED); d.ellipse([cx + 28, cy + 30, cx + 42, cy + 44], fill=RED)
if not V1:  # two fine strips of paper pinned at the wing tips; v1 left the specimen unheld
    for (x0, y0, x1, y1) in [(cx - 224, cy - 58, cx - 158, cy - 26), (cx + 158, cy - 58, cx + 224, cy - 26)]:
        d.rectangle([x0, y0, x1, y1], fill=(250, 247, 238, 215), outline=(198, 190, 168))
        d.ellipse([x0 + 4, y0 + 8, x0 + 12, y0 + 16], fill=(12, 12, 12))
        d.ellipse([x1 - 12, y0 + 8, x1 - 4, y0 + 16], fill=(12, 12, 12))
# thorax and the single pin, black head catching one point of light
d.ellipse([cx - 10, cy - 46, cx + 10, cy + 58], fill=(24, 20, 17))
d.ellipse([cx - 7, cy - 66, cx + 7, cy - 52], fill=(8, 8, 8))
d.point((cx - 2, cy - 62), fill=(255, 255, 255))
try:
    f = ImageFont.truetype(__file__.rsplit("/", 1)[0] + "/fonts/AveriaSansLibre.ttf", 35)
except Exception:
    f = ImageFont.load_default()
d.text((450, 452), "analyze-network-protocol-fuzzer", font=f, fill=BONE, anchor="mm")
img = img.filter(ImageFilter.GaussianBlur(0.3))
out = "scratch/logo-v1.png" if V1 else "logo.png"
img.save(__file__.rsplit("/", 1)[0] + "/" + out)
if not V1:
    img.resize((64, 64)).save(__file__.rsplit("/", 1)[0] + "/scratch/logo64-ship.png")
print("saved", out)

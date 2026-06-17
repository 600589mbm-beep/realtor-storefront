#!/usr/bin/env python3
"""Generate raster meta images (OG image + favicons) for the AgentEdge storefront.
SVG product art is authored by hand; this only produces the rasters that social
scrapers and legacy browsers need (they don't render SVG OG images well).
Run from repo root:  python3 tools/gen_meta_images.py
"""
from PIL import Image, ImageDraw, ImageFont
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "img")
os.makedirs(IMG, exist_ok=True)

NAVY = (11, 36, 64)
NAVY2 = (22, 62, 120)
BLUE = (37, 99, 235)
GOLD = (230, 169, 59)
WHITE = (255, 255, 255)
LBLUE = (157, 179, 214)

FB = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

def house_mark(size):
    """Navy rounded tile with portal-blue solid roof, white body, gold door."""
    s = size
    im = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, s - 1, s - 1], radius=s * 0.234, fill=NAVY)
    # roof (solid triangle with eaves overhang)
    d.polygon([(s*0.172, s*0.547), (s*0.5, s*0.258), (s*0.828, s*0.547)], fill=BLUE)
    # house body
    d.rounded_rectangle([s*0.297, s*0.516, s*0.703, s*0.773], radius=max(1, s*0.039), fill=WHITE)
    # gold door
    d.rounded_rectangle([s*0.4375, s*0.609, s*0.5625, s*0.773], radius=max(1, s*0.022), fill=GOLD)
    return im

# ---------- favicons ----------
for px in (16, 32, 48, 180):
    house_mark(px).save(os.path.join(IMG, f"favicon-{px}.png"))
# apple touch icon = 180
os.replace(os.path.join(IMG, "favicon-180.png"), os.path.join(IMG, "apple-touch-icon.png"))
# multi-size .ico at repo root
house_mark(64).save(os.path.join(ROOT, "favicon.ico"),
                    sizes=[(16, 16), (32, 32), (48, 48)])
# canonical 32 png for <link>
import shutil
shutil.copy(os.path.join(IMG, "favicon-32.png"), os.path.join(IMG, "favicon-32x32.png"))

# ---------- OG image 1200x630 ----------
W, H = 1200, 630
og = Image.new("RGB", (W, H), NAVY)
d = ImageDraw.Draw(og)
for y in range(H):  # vertical gradient navy -> navy2
    t = y / H
    d.line([(0, y), (W, y)], fill=tuple(int(NAVY[i] + (NAVY2[i]-NAVY[i])*t) for i in range(3)))
# gold accent bar
d.rectangle([0, 0, W, 10], fill=GOLD)

# brand row
mark = house_mark(96)
og.paste(mark, (80, 64), mark)
d.text((196, 84), "Abc Ore Pro", font=font(FB, 60), fill=WHITE)

# headline
d.text((80, 220), "Agent tools, listed like", font=font(FB, 78), fill=WHITE)
d.text((80, 312), "the homes you sell.", font=font(FB, 78), fill=GOLD)
d.text((82, 420), "Re-engage past clients  ·  boost reviews  ·  90 days of content",
       font=font(FR, 30), fill=LBLUE)

# price chips
chips = [("Reactivation", "$37", False), ("Reviews", "$37", False),
         ("Calendar", "$19", False), ("Starter Kit", "$67", True)]
fcb = font(FB, 28)
x, y, h = 80, 506, 66
for name, price, gold in chips:
    label = f"{name}  {price}"
    tw = d.textlength(label, font=fcb)
    w = int(tw + 56)
    d.rounded_rectangle([x, y, x + w, y + h], radius=18,
                        fill=GOLD if gold else None,
                        outline=None if gold else WHITE, width=0 if gold else 3)
    d.text((x + 28, y + 18), label, font=fcb, fill=NAVY if gold else WHITE)
    x += w + 22

og.save(os.path.join(IMG, "og-image.png"), optimize=True)
print("OK wrote:", sorted(os.listdir(IMG)))
print("ico:", os.path.exists(os.path.join(ROOT, "favicon.ico")))

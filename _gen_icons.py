from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OUT = Path(__file__).parent
SIZES = [180, 192, 512]

CREAM = (243, 238, 226)
INK = (26, 22, 18)
RED = (184, 57, 46)
GREY = (138, 127, 110)

GEORGIA_ITALIC = "/System/Library/Fonts/Supplemental/Georgia Italic.ttf"
MENLO = "/System/Library/Fonts/Menlo.ttc"


def render(size: int) -> Image.Image:
    img = Image.new("RGB", (size, size), CREAM)
    d = ImageDraw.Draw(img)

    cx = cy = size / 2
    r = size * 0.31
    stroke = max(2, int(size * 0.0125))
    d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=INK, width=stroke)

    d_font_size = int(size * 0.37)
    d_font = ImageFont.truetype(GEORGIA_ITALIC, d_font_size)
    bbox = d_font.getbbox("D")
    d_w = bbox[2] - bbox[0]
    d_h = bbox[3] - bbox[1]
    d.text(
        (cx - d_w / 2 - bbox[0], cy - d_h / 2 - bbox[1] - size * 0.02),
        "D",
        font=d_font,
        fill=RED,
    )

    label_size = max(8, int(size * 0.045))
    label_font = ImageFont.truetype(MENLO, label_size)
    label = "DOOMSDAY"
    lbbox = label_font.getbbox(label)
    lw = lbbox[2] - lbbox[0]
    d.text(
        (cx - lw / 2 - lbbox[0], cy + size * 0.20),
        label,
        font=label_font,
        fill=GREY,
    )

    return img


for s in SIZES:
    img = render(s)
    img.save(OUT / f"icon-{s}.png", "PNG", optimize=True)
    print(f"wrote icon-{s}.png")

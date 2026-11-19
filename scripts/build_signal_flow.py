"""Build the illustrative signal-flow GIF used in the README."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "images" / "signal-flow.gif"
W, H = 960, 360
BG = "#0b1220"
CARD = "#142238"
BORDER = "#29415a"
WHITE = "#edf6ff"
MUTED = "#91a9c0"
CYAN = "#54d4e8"
AMBER = "#ffca64"
GREEN = "#75e3b0"


def font(size, bold=False):
    name = "segoeuib.ttf" if bold else "segoeui.ttf"
    path = Path("C:/Windows/Fonts") / name
    return ImageFont.truetype(str(path), size) if path.exists() else ImageFont.load_default()


F_TITLE = font(25, True)
F_LABEL = font(17, True)
F_SMALL = font(14)
F_VALUE = font(34, True)
F_DIGIT = font(66, True)


def centered(draw, box, label, face, color):
    x0, y0, x1, y1 = box
    bounds = draw.textbbox((0, 0), label, font=face)
    width, height = bounds[2] - bounds[0], bounds[3] - bounds[1]
    draw.text(((x0 + x1 - width) / 2, (y0 + y1 - height) / 2 - bounds[1]), label, font=face, fill=color)


def frame(temp, phase):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((15, 15, W - 15, H - 15), radius=23, outline=BORDER, width=2)
    d.text((38, 34), "FROM HEAT TO A DIGITAL READING", font=F_TITLE, fill=WHITE)
    d.text((39, 70), "Ideal signal relationship · conceptual animation", font=F_SMALL, fill=MUTED)

    cards = [(38, 125, 213, 274), (274, 125, 449, 274), (510, 125, 685, 274), (746, 125, 921, 274)]
    labels = ["TEMPERATURE", "LM35 SENSOR", "ICL7107 ADC", "2-DIGIT DISPLAY"]
    accents = [AMBER, CYAN, GREEN, AMBER]
    for box, label, accent in zip(cards, labels, accents):
        d.rounded_rectangle(box, radius=17, fill=CARD, outline=BORDER, width=2)
        d.rounded_rectangle((box[0] + 16, box[1] + 17, box[0] + 51, box[1] + 22), radius=2, fill=accent)
        d.text((box[0] + 16, box[1] + 36), label, font=F_LABEL, fill=WHITE)

    centered(d, (54, 188, 197, 252), f"{temp:02d} °C", F_VALUE, AMBER)
    centered(d, (290, 188, 433, 252), f"{temp * 10:03d} mV", F_VALUE, CYAN)
    centered(d, (526, 190, 669, 247), "A/D", F_VALUE, GREEN)
    centered(d, (760, 179, 907, 267), f"{temp:02d}", F_DIGIT, AMBER)

    for left, right, color in [(213, 274, CYAN), (449, 510, GREEN), (685, 746, AMBER)]:
        d.line((left + 8, 201, right - 10, 201), fill=BORDER, width=5)
        d.polygon([(right - 12, 193), (right - 2, 201), (right - 12, 209)], fill=color)
        x = left + 10 + int((phase / 7) * (right - left - 25))
        d.ellipse((x - 5, 196, x + 5, 206), fill=color)

    d.text((39, 300), "LM35: 10 mV / °C", font=F_SMALL, fill=MUTED)
    d.text((742, 300), "0–99 °C design range", font=F_SMALL, fill=MUTED)
    return im


frames = [frame(t, p) for t in (0, 10, 25, 50, 75, 99) for p in range(8)]
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
frames[0].save(
    OUTPUT,
    save_all=True,
    append_images=frames[1:],
    duration=115,
    loop=0,
    optimize=True,
)
print(OUTPUT)

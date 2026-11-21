
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def create_thumbnail():
    with open("output/story.json", encoding="utf-8") as file:
        story = json.load(file)

    image = Image.new("RGB", (1280, 720), (40, 90, 145))
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/noto/NotoSansDevanagari-Bold.ttf",
            65
        )
    except OSError:
        font = ImageFont.load_default()

    draw.rounded_rectangle(
        (50, 50, 1230, 670),
        radius=45,
        fill=(255, 220, 120)
    )

    draw.text(
        (640, 300),
        story["title"],
        fill=(60, 35, 90),
        font=font,
        anchor="mm"
    )

    draw.text(
        (640, 520),
        "Hindi Kids Story",
        fill=(40, 60, 100),
        font=font,
        anchor="mm"
    )

    Path("output").mkdir(exist_ok=True)
    image.save("output/thumbnail.jpg", quality=90)
    print("Thumbnail created!")

if __name__ == "__main__":
    create_thumbnail()

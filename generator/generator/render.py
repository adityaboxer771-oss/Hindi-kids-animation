
import json
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUTPUT = Path("output")
FRAMES = OUTPUT / "frames"

def create_frames(story):
    FRAMES.mkdir(parents=True, exist_ok=True)

    font_path = "/usr/share/fonts/truetype/noto/NotoSansDevanagari-Regular.ttf"

    try:
        font = ImageFont.truetype(font_path, 42)
    except OSError:
        font = ImageFont.load_default()

    for i, scene in enumerate(story["scenes"], 1):
        image = Image.new("RGB", (1280, 720), (35, 65, 105))
        draw = ImageDraw.Draw(image)

        draw.rounded_rectangle(
            (40, 40, 1240, 680),
            radius=35,
            fill=(250, 230, 175)
        )

        draw.text(
            (640, 180),
            story["title"],
            fill=(80, 40, 100),
            font=font,
            anchor="mm"
        )

        draw.text(
            (640, 390),
            scene,
            fill=(30, 30, 30),
            font=font,
            anchor="mm"
        )

        image.save(FRAMES / f"scene_{i:03}.png")


def render_video():
    with open(OUTPUT / "story.json", encoding="utf-8") as file:
        story = json.load(file)

    create_frames(story)

    frames = sorted(FRAMES.glob("scene_*.png"))
    concat = OUTPUT / "frames.txt"

    with open(concat, "w") as file:
        for frame in frames:
            file.write(f"file '{frame.resolve()}'\n")
            file.write("duration 8\n")
        file.write(f"file '{frames[-1].resolve()}'\n")

    silent = OUTPUT / "silent.mp4"

    subprocess.run([
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", str(concat),
        "-vf", "fps=24,format=yuv420p",
        "-c:v", "libx264",
        str(silent)
    ], check=True)

    voice = OUTPUT / "audio" / "voice.mp3"
    music = OUTPUT / "audio" / "background.wav"
    final = OUTPUT / "final_video.mp4"

    if voice.exists() and music.exists():
        subprocess.run([
            "ffmpeg", "-y",
            "-i", str(silent),
            "-stream_loop", "-1", "-i", str(music),
            "-i", str(voice),
            "-map", "0:v",
            "-map", "2:a",
            "-c:v", "copy",
            "-c:a", "aac",
            "-shortest",
            str(final)
        ], check=True)
    else:
        silent.replace(final)

    print("Video ready:", final)


if __name__ == "__main__":
    render_video()


import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json

ROOT = Path(".")
OUTPUT = ROOT / "output"
FRAMES = OUTPUT / "frames"

def make_frames(story):
    FRAMES.mkdir(parents=True, exist_ok=True)
    font_path = "/usr/share/fonts/truetype/noto/NotoSansDevanagari-Regular.ttf"

    try:
        font = ImageFont.truetype(font_path, 42)
        title_font = ImageFont.truetype(font_path, 58)
    except OSError:
        font = ImageFont.load_default()
        title_font = font

    for i, scene in enumerate(story["scenes"], start=1):
        image = Image.new("RGB", (1280, 720), (35, 65, 105))
        draw = ImageDraw.Draw(image)

        draw.rounded_rectangle(
            (45, 45, 1235, 675),
            radius=35,
            fill=(250, 230, 175)
        )

        draw.text(
            (640, 180),
            story["title"],
            fill=(80, 40, 100),
            font=title_font,
            anchor="mm"
        )

        draw.text(
            (640, 390),
            scene,
            fill=(30, 35, 45),
            font=font,
            anchor="mm",
            align="center"
        )

        draw.text(
            (640, 600),
            f"Scene {i}",
            fill=(100, 70, 50),
            font=font,
            anchor="mm"
        )

        image.save(FRAMES / f"scene_{i:03}.png")


def render_video():
    story_path = OUTPUT / "story.json"
    voice_path = OUTPUT / "audio" / "voice.mp3"
    music_path = OUTPUT / "audio" / "background.wav"

    if not story_path.exists():
        raise FileNotFoundError("Story not found")

    with open(story_path, encoding="utf-8") as file:
        story = json.load(file)

    make_frames(story)

    scenes = sorted(FRAMES.glob("scene_*.png"))
    if not scenes:
        raise RuntimeError("No scene images created")

    concat_file = OUTPUT / "frames.txt"
    with open(concat_file, "w") as file:
        for frame in scenes:
            file.write(f"file '{frame.resolve()}'\n")
            file.write("duration 8\n")
        file.write(f"file '{scenes[-1].resolve()}'\n")

    silent_video = OUTPUT / "silent.mp4"
    final_video = OUTPUT / "final_video.mp4"

    subprocess.run([
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", str(concat_file),
        "-vf", "fps=24,format=yuv420p",
        "-c:v", "libx264",
        str(silent_video)
    ], check=True)

    if voice_path.exists() and music_path.exists():
        subprocess.run([
            "ffmpeg", "-y",
            "-i", str(silent_video),
            "-stream_loop", "-1", "-i", str(music_path),
            "-i", str(voice_path),
            "-filter_complex",
            "[1:a]volume=0.08[m];"
            "[2:a]apad[v];"
            "[m][v]amix=inputs=2:duration=first[a]",
            "-map", "0:v", "-map", "[a]",
            "-c:v", "copy", "-c:a", "aac",
            "-shortest", str(final_video)
        ], check=True)
    else:
        silent_video.replace(final_video)

    print("Video created:", final_video)


if __name__ == "__main__":
    render_video()

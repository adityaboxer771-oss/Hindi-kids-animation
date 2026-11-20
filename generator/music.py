
import subprocess
from pathlib import Path

def create_background_music():
    output_folder = Path("output/audio")
    output_folder.mkdir(parents=True, exist_ok=True)

    music_file = output_folder / "background.wav"

    # Generate simple instrumental background music
    command = [
        "ffmpeg",
        "-y",
        "-f", "lavfi",
        "-i", "sine=frequency=440:duration=60",
        "-af", "volume=0.04",
        str(music_file)
    ]

    try:
        subprocess.run(command, check=True)
        print("Background music created:", music_file)
    except FileNotFoundError:
        print("FFmpeg is not installed!")
    except subprocess.CalledProcessError:
        print("Music generation failed!")


if __name__ == "__main__":
    create_background_music()

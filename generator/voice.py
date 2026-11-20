
import json
import subprocess
from pathlib import Path

def create_voiceover():
    story_file = Path("output/story.json")
    output_folder = Path("output/audio")
    output_folder.mkdir(parents=True, exist_ok=True)

    if not story_file.exists():
        print("Story file not found!")
        return

    with open(story_file, "r", encoding="utf-8") as file:
        story = json.load(file)

    text = story["title"] + ". "
    text += " ".join(story["scenes"])
    text += " " + story["moral"]

    audio_file = output_folder / "voice.mp3"

    subprocess.run([
        "espeak-ng",
        "-v", "hi",
        "-w", str(audio_file),
        text
    ], check=True)

    print("Voiceover created:", audio_file)


if __name__ == "__main__":
    create_voiceover()

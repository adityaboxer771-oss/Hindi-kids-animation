
import json
import subprocess
from pathlib import Path

def create_video():
    story_file = Path("output/story.json")
    audio_file = Path("output/audio/voice.mp3")
    video_folder = Path("output/video")

    video_folder.mkdir(parents=True, exist_ok=True)

    if not story_file.exists():
        print("Story file missing!")
        return

    with open(story_file, "r", encoding="utf-8") as file:
        story = json.load(file)

    scenes = story["scenes"]

    print("Creating video for:", story["title"])
    print("Total scenes:", len(scenes))

    for number, scene in enumerate(scenes, start=1):
        print(f"Scene {number}: {scene}")

    if not audio_file.exists():
        print("Voiceover missing! Generate voice first.")
        return

    print("Story and voiceover are ready.")
    print("Next step: connect cartoon visuals and FFmpeg rendering.")

if __name__ == "__main__":
    create_video()

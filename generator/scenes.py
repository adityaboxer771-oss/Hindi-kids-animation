
import json
from pathlib import Path

def create_scenes():
    story_file = Path("output/story.json")
    output_folder = Path("output/scenes")
    output_folder.mkdir(parents=True, exist_ok=True)

    if not story_file.exists():
        print("Story file not found!")
        return

    with open(story_file, "r", encoding="utf-8") as file:
        story = json.load(file)

    for number, description in enumerate(story["scenes"], start=1):
        scene_data = {
            "scene_number": number,
            "description": description,
            "characters": story["characters"],
            "title": story["title"]
        }

        scene_file = output_folder / f"scene_{number}.json"

        with open(scene_file, "w", encoding="utf-8") as file:
            json.dump(scene_data, file, ensure_ascii=False, indent=4)

    print("All scenes created:", len(story["scenes"]))


if __name__ == "__main__":
    create_scenes()

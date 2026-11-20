
import json
from pathlib import Path

def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02}:{minutes:02}:{secs:02},000"


def create_subtitles():
    story_file = Path("output/story.json")
    output_folder = Path("output")
    output_folder.mkdir(exist_ok=True)

    if not story_file.exists():
        print("Story file not found!")
        return

    with open(story_file, "r", encoding="utf-8") as file:
        story = json.load(file)

    subtitles = []
    scenes = story["scenes"]

    for index, scene in enumerate(scenes):
        start = index * 15
        end = start + 15

        subtitles.append(
            f"{index + 1}\n"
            f"{format_time(start)} --> {format_time(end)}\n"
            f"{scene}\n"
        )

    subtitles.append(
        f"{len(scenes) + 1}\n"
        f"{format_time(len(scenes) * 15)} --> "
        f"{format_time(len(scenes) * 15 + 15)}\n"
        f"Seekh: {story['moral']}\n"
    )

    subtitle_file = output_folder / "subtitles.srt"
    subtitle_file.write_text("\n".join(subtitles), encoding="utf-8")

    print("Hindi subtitles created:", subtitle_file)


if __name__ == "__main__":
    create_subtitles()

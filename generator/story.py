
import random
import json
from pathlib import Path

STORIES = [
    {
        "title": "Bandar Aur Sher Ki Dosti",
        "characters": ["Bandar", "Sher"],
        "scenes": [
            "Ek hare-bhare jungle mein Chiku naam ka bandar rehta tha.",
            "Chiku bahut shararti tha aur sabko hansata rehta tha.",
            "Ek din usne jungle mein ek sher ko akela baithe dekha.",
            "Sher ka naam Raja tha aur woh bahut udaas tha.",
            "Chiku ne Raja se poocha ki woh itna udaas kyun hai.",
            "Raja ne bataya ki jungle mein uska koi dost nahi hai.",
            "Chiku ne kaha ki woh uska dost ban sakta hai.",
            "Dono saath mein jungle ghoomne lage.",
            "Ek din Chiku raste mein kho gaya.",
            "Raja ne apni awaaz se Chiku ko dhoondh liya.",
            "Chiku bahut khush hua aur usne Raja ko dhanyavaad kaha.",
            "Dheere-dheere jungle ke sabhi jaanwar unke dost ban gaye.",
            "Ab dono milkar sabki madad karte the.",
            "Jungle mein khushi aur dosti ka mahaul ban gaya."
        ],
        "moral": "Sacchi dosti sabse badi taakat hai."
    },
    {
        "title": "Chhota Haathi Aur Chidiya",
        "characters": ["Haathi", "Chidiya"],
        "scenes": [
            "Ek sundar jungle mein Golu naam ka chhota haathi rehta tha.",
            "Golu sabki madad karna pasand karta tha.",
            "Ek subah usne ped ke neeche ek chidiya ko dekha.",
            "Chidiya bahut pareshan thi.",
            "Golu ne poocha ki kya hua hai.",
            "Chidiya ne bataya ki uska ghosla ped se gir gaya hai.",
            "Golu ne chidiya ki madad karne ka faisla kiya.",
            "Usne apni soond se ghosle ko sambhala.",
            "Phir usne ghosla surakshit jagah par rakh diya.",
            "Chidiya apna ghosla dekhkar bahut khush hui.",
            "Usne Golu ko dil se dhanyavaad kaha.",
            "Dono acche dost ban gaye.",
            "Ab Golu aur chidiya roz saath khelte the.",
            "Jungle ke sabhi jaanwar Golu ki tareef karne lage."
        ],
        "moral": "Dusron ki madad karna sabse achhi aadat hai."
    }
]


def create_story():
    story = random.choice(STORIES)

    output = {
        "title": story["title"],
        "characters": story["characters"],
        "scenes": story["scenes"],
        "moral": story["moral"],
        "language": "Hindi",
        "target_duration": "3-5 minutes"
    }

    output_folder = Path("output")
    output_folder.mkdir(exist_ok=True)

    output_file = output_folder / "story.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(
            output,
            file,
            ensure_ascii=False,
            indent=4
        )

    print("Story created successfully!")
    print("Title:", story["title"])
    print("Saved to:", output_file)


if __name__ == "__main__":
    create_story()


import os
import json
from pathlib import Path
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_video():
    token = os.environ.get("YOUTUBE_TOKEN_JSON")

    if not token:
        print("YouTube authorization is not configured.")
        return

    credentials_data = json.loads(token)

    credentials = Credentials.from_authorized_user_info(
        credentials_data,
        scopes=["https://www.googleapis.com/auth/youtube.upload"]
    )

    youtube = build("youtube", "v3", credentials=credentials)

    video_path = Path("output/final_video.mp4")

    if not video_path.exists():
        raise FileNotFoundError("Video not found")

    with open("output/story.json", encoding="utf-8") as file:
        story = json.load(file)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": story["title"],
                "description": (
                    "Hindi kids story for learning and entertainment."
                    "\n#HindiStories #KidsAnimation"
                ),
                "categoryId": "1"
            },
            "status": {
                "privacyStatus": "private",
                "selfDeclaredMadeForKids": True
            }
        },
        media_body=MediaFileUpload(
            str(video_path),
            mimetype="video/mp4",
            resumable=True
        )
    )

    response = request.execute()
    print("Uploaded video ID:", response["id"])


if __name__ == "__main__":
    upload_video()

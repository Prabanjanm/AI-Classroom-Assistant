import uuid

from pathlib import Path

import yt_dlp


class YouTubeVideoService:

    def __init__(self):

        self.output_dir = Path(
            "storage/youtube_audio"
        )

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    async def download_audio(
        self,
        url: str
    ):

        filename = str(
            uuid.uuid4()
        )

        output_template = str(
            self.output_dir / filename
        )

        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192"
                }
            ]
        }

        with yt_dlp.YoutubeDL(
            ydl_opts
        ) as ydl:

            info = ydl.extract_info(
                url,
                download=True
            )

            title = info.get(
                "title",
                "YouTube Video"
            )

        final_audio_path = (
            self.output_dir /
            f"{filename}.mp3"
        )

        return {
            "title": title,
            "audio_path": str(
                final_audio_path
            )
        }
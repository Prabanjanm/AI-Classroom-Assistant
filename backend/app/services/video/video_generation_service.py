import uuid

from pathlib import Path

from moviepy import (
    ImageClip,
    AudioFileClip,
    concatenate_videoclips
)

from app.db.supabase_client import (
    supabase
)

from app.repositories.video_repository import (
    VideoRepository
)


class VideoGenerationService:

    def __init__(self):

        self.output_dir = Path(
            "storage/generated_videos"
        )

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.repository = (
            VideoRepository()
        )

    async def generate_video(
        self,
        db,
        title: str,
        image_paths: list[str],
        audio_path: str,
        audio_url: str
    ):

        audio_clip = AudioFileClip(
            audio_path
        )

        total_duration = (
            audio_clip.duration
        )

        image_duration = (
            total_duration /
            len(image_paths)
        )

        clips = []

        for image_path in image_paths:

            clip = (
                ImageClip(image_path)
                .with_duration(
                    image_duration
                )
            )

            clips.append(clip)

        final_video = (
            concatenate_videoclips(
                clips,
                method="compose"
            )
        )

        final_video = (
            final_video.with_audio(
                audio_clip
            )
        )

        filename = (
            f"{uuid.uuid4()}.mp4"
        )

        output_path = (
            self.output_dir / filename
        )

        final_video.write_videofile(
            str(output_path),
            fps=24
        )

        with open(
            output_path,
            "rb"
        ) as f:

            supabase.storage.from_(
                "generated-videos"
            ).upload(
                filename,
                f,
                {
                    "content-type": "video/mp4"
                }
            )

        video_url = (
            supabase.storage
            .from_("generated-videos")
            .get_public_url(filename)
        )

        saved_video = await (
            self.repository.create_video(
                db=db,
                title=title,
                video_url=video_url,
                audio_url=audio_url
            )
        )

        return {
            "success": True,
            "video_id": str(saved_video.id),
            "video_url": video_url
        }
import uuid

from pathlib import Path

from moviepy import VideoFileClip

from app.db.supabase_client import (
    supabase
)

from app.repositories.video_summary_repository import (
    VideoSummaryRepository
)

from app.services.audio.whisper_service import (
    WhisperService
)

from app.services.video.youtube_video_service import (
    YouTubeVideoService
)
from app.services.lecture.lecture_summary_service import (
    SummaryService
)


class VideoSummaryService:

    def __init__(self):

        self.output_dir = Path(
            "storage/video_uploads"
        )

        self.audio_dir = Path(
            "storage/video_audio"
        )

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.audio_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.repository = (
            VideoSummaryRepository()
        )

        self.whisper_service = (
            WhisperService()
        )

        self.summary_service = (
            SummaryService()
        )
        self.youtube_service = (
    YouTubeVideoService()
)

    async def summarize_video(
        self,
        db,
        title: str,
        video_path: str
    ):

        video = VideoFileClip(
            video_path
        )

        audio_filename = (
            f"{uuid.uuid4()}.mp3"
        )

        audio_path = (
            self.audio_dir /
            audio_filename
        )

        video.audio.write_audiofile(
            str(audio_path)
        )

        transcript_result = await (
            self.whisper_service
            .transcribe_audio(
                str(audio_path)
            )
        )

        transcript = (
            transcript_result[
                "transcript"
            ]
        )

        saved_transcription = await (
    self.whisper_service
    .save_transcript(
        db=db,
        lecture_title=title,
        audio_url=str(audio_path),
        transcript=transcript
    )
)

        summary_result = await (
            self.summary_service
            .summarize_text(
                db=db,
                transcription_id=saved_transcription.id
            )
            )
        

        summary = (
            summary_result["summary"]
        )

        filename = (
            f"{uuid.uuid4()}.mp4"
        )

        with open(
            video_path,
            "rb"
        ) as f:

            supabase.storage.from_(
                "lecture-videos"
            ).upload(
                filename,
                f,
                {
                    "content-type": "video/mp4"
                }
            )

        video_url = (
            supabase.storage
            .from_("lecture-videos")
            .get_public_url(filename)
        )

        saved_summary = await (
            self.repository.create_summary(
                db=db,
                title=title,
                video_url=video_url,
                transcript=transcript,
                summary=summary
            )
        )

        return {
            "success": True,
            "video_id": str(
                saved_summary.id
            ),
            "video_url": video_url,
            "summary": summary
        }
    
    async def summarize_youtube_video(
    self,
    db,
    url: str
):

        download_result = await (
            self.youtube_service
            .download_audio(url)
        )

        title = (
            download_result["title"]
        )

        audio_path = (
            download_result["audio_path"]
        )

        transcript_result = await (
            self.whisper_service
            .transcribe_audio(
                audio_path
            )
        )

        transcript = (
            transcript_result[
                "transcript"
            ]
        )
        saved_transcription = await (
            self.whisper_service
            .save_transcript(
                db=db,
                lecture_title=title,
                audio_url=str(audio_path),
                transcript=transcript
            )
        )

        summary_result = await (
            self.summary_service
            .summarize_text(
                db=db,
                transcription_id=saved_transcription.id
            )
        )

        summary = (
            summary_result["summary"]
        )

        saved_summary = await (
            self.repository.create_summary(
                db=db,
                title=title,
                video_url=url,
                transcript=transcript,
                summary=summary
            )
        )

        return {
            "success": True,
            "video_id": str(
                saved_summary.id
            ),
            "title": title,
            "summary": summary
        }
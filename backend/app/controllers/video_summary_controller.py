import uuid

from pathlib import Path

from fastapi import UploadFile

from app.services.video.video_summary_service import (
    VideoSummaryService
)
from app.schemas.youtube_video_schema import (
    YouTubeVideoRequest
)


class VideoSummaryController:

    def __init__(self):

        self.video_service = (
            VideoSummaryService()
        )

        self.upload_dir = Path(
            "storage/video_uploads"
        )

        self.upload_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    async def summarize_video(
        self,
        db,
        file: UploadFile
    ):

        filename = (
            f"{uuid.uuid4()}_{file.filename}"
        )

        file_path = (
            self.upload_dir / filename
        )

        with open(
            file_path,
            "wb"
        ) as buffer:

            buffer.write(
                await file.read()
            )

        return await (
            self.video_service
            .summarize_video(
                db=db,
                title=file.filename,
                video_path=str(file_path)
            )
        )
    
    async def summarize_youtube_video(
    self,
    db,
    payload: YouTubeVideoRequest
):

        return await (
            self.video_service
            .summarize_youtube_video(
                db=db,
                url=payload.url
            )
        )
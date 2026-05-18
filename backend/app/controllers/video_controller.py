from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.video_schema import (
    VideoGenerationRequest
)

from app.services.video.video_generation_service import (
    VideoGenerationService
)


class VideoController:

    def __init__(self):

        self.video_service = (
            VideoGenerationService()
        )

    async def generate_video(
        self,
        payload: VideoGenerationRequest,
        db: AsyncSession
    ):

        return await (
            self.video_service.generate_video(
                db=db,
                title=payload.title,
                image_paths=payload.image_paths,
                audio_path=payload.audio_path,
                audio_url=payload.audio_url
            )
        )
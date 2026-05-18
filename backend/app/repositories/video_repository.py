from sqlalchemy.ext.asyncio import AsyncSession

from app.models.video_model import (
    GeneratedVideo
)


class VideoRepository:

    async def create_video(
        self,
        db: AsyncSession,
        title,
        video_url,
        audio_url
    ):

        obj = GeneratedVideo(
            title=title,
            video_url=video_url,
            audio_url=audio_url
        )

        db.add(obj)

        await db.commit()

        await db.refresh(obj)

        return obj
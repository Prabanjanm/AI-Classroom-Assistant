from sqlalchemy.ext.asyncio import AsyncSession

from app.models.video_summary_model import (
    VideoSummary
)


class VideoSummaryRepository:

    async def create_summary(
        self,
        db: AsyncSession,
        title,
        video_url,
        transcript,
        summary
    ):

        obj = VideoSummary(
            title=title,
            video_url=video_url,
            transcript=transcript,
            summary=summary
        )

        db.add(obj)

        await db.commit()

        await db.refresh(obj)

        return obj
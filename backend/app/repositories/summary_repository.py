from sqlalchemy.ext.asyncio import AsyncSession

from app.models.summary_model import Summary


class SummaryRepository:

    async def create_summary(
        self,
        db: AsyncSession,
        lecture_title: str,
        transcript: str,
        summary: str,
        transcription_id
    ):

        summary_obj = Summary(
            lecture_title=lecture_title,
            transcript=transcript,
            summary=summary,
            transcription_id=transcription_id
        )

        db.add(summary_obj)

        await db.commit()

        await db.refresh(summary_obj)

        return summary_obj
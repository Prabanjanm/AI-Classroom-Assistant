from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.summary_schema import (
    SummaryRequest
)

from app.services.lecture.lecture_summary_service import (
    SummaryService
)


class SummaryController:

    def __init__(self):

        self.summary_service = (
            SummaryService()
        )

    async def summarize(
        self,
        payload: SummaryRequest,
        db: AsyncSession
    ):

        return await (
            self.summary_service.summarize_text(
                db=db,
                transcription_id=payload.transcription_id
            )
        )
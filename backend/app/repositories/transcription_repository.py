from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select

from app.models.transcription_model import (
    Transcription
)


class TranscriptionRepository:

    async def create_transcription(
        self,
        db: AsyncSession,
        lecture_title: str,
        audio_url: str,
        transcript: str
    ):

        transcription = Transcription(
            lecture_title=lecture_title,
            audio_url=audio_url,
            transcript=transcript
        )

        db.add(transcription)

        await db.commit()

        await db.refresh(transcription)

        return transcription

    async def get_transcription_by_id(
        self,
        db: AsyncSession,
        transcription_id
    ):

        query = select(Transcription).where(
            Transcription.id == transcription_id
        )

        result = await db.execute(query)

        return result.scalar_one_or_none()
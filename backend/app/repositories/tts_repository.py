from sqlalchemy.ext.asyncio import AsyncSession

from app.models.tts_model import (
    GeneratedAudio
)


class TTSRepository:

    async def create_audio(
        self,
        db: AsyncSession,
        text,
        voice,
        audio_url
    ):

        obj = GeneratedAudio(
            text=text,
            voice=voice,
            audio_url=audio_url
        )

        db.add(obj)

        await db.commit()

        await db.refresh(obj)

        return obj
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.tts_schema import (
    TTSRequest
)

from app.services.tts.tts_service import (
    TTSService
)


class TTSController:

    def __init__(self):

        self.tts_service = (
            TTSService()
        )

    async def generate_audio(
        self,
        payload: TTSRequest,
        db: AsyncSession
    ):

        return await (
            self.tts_service.generate_audio(
                db=db,
                text=payload.text,
                voice=payload.voice
            )
        )
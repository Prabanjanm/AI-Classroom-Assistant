from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

from app.controllers.tts_controller import (
    TTSController
)

from app.schemas.tts_schema import (
    TTSRequest
)


router = APIRouter(
    prefix="/tts",
    tags=["TTS"]
)

tts_controller = (
    TTSController()
)


@router.post("/generate")
async def generate_audio(
    payload: TTSRequest,
    db: AsyncSession = Depends(get_db)
):

    return await (
        tts_controller.generate_audio(
            payload,
            db
        )
    )
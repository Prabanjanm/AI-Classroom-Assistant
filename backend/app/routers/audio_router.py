from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from fastapi import APIRouter, UploadFile, File
from app.controllers.audio_controller import AudioController
from app.core.database import get_db


router = APIRouter()
audio_controller = AudioController()


@router.post("/transcribe")
async def transcribe_audio(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db)
):

    return await audio_controller.transcribe_audio(
        file,
        db
    )
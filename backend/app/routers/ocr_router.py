from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends
)

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

from app.controllers.ocr_controller import (
    OCRController
)


router = APIRouter()

ocr_controller = OCRController()


@router.post("/extract")
async def extract_text(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db)
):
    """
    Extract text from image or PDF.
    """

    return await ocr_controller.process_file(
        file,
        db
    )
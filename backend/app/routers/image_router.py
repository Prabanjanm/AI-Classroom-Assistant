from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers.image_controller import (
    ImageController
)

from app.schemas.image_schema import (
    TextToImageRequest
)

from app.core.database import get_db


router = APIRouter()

image_controller = ImageController()


@router.post("/generate")
async def generate_image(
    payload: TextToImageRequest,
    db: AsyncSession = Depends(get_db)
):

    return await image_controller.generate_image(
        payload,
        db
    )
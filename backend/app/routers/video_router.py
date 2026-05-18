from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers.video_controller import (
    VideoController
)

from app.schemas.video_schema import (
    VideoGenerationRequest
)

from app.core.database import (
    get_db
)


router = APIRouter(
    prefix="/video",
    tags=["Video"]
)

video_controller = (
    VideoController()
)


@router.post("/generate")
async def generate_video(
    payload: VideoGenerationRequest,
    db: AsyncSession = Depends(get_db)
):

    return await (
        video_controller.generate_video(
            payload,
            db
        )
    )
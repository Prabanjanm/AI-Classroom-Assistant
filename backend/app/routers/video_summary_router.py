from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends
)

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import (
    get_db
)

from app.controllers.video_summary_controller import (
    VideoSummaryController
)

from app.schemas.youtube_video_schema import (
    YouTubeVideoRequest
)

router = APIRouter(
    prefix="/video-summary",
    tags=["Video Summary"]
)

video_controller = (
    VideoSummaryController()
)


@router.post("/upload")
async def summarize_video(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db)
):

    return await (
        video_controller
        .summarize_video(
            db=db,
            file=file
        )
    )

@router.post("/youtube")
async def summarize_youtube_video(
    payload: YouTubeVideoRequest,
    db: AsyncSession = Depends(get_db)
):

    return await (
        video_controller
        .summarize_youtube_video(
            db=db,
            payload=payload
        )
    )
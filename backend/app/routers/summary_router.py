from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers.summary_controller import (
    SummaryController
)

from app.schemas.summary_schema import (
    SummaryRequest
)

from app.core.database import get_db


router = APIRouter()

summary_controller = SummaryController()


@router.post("/generate")
async def generate_summary(
    payload: SummaryRequest,
    db: AsyncSession = Depends(get_db)
):

    return await (
        summary_controller.summarize(
            payload,
            db
        )
    )
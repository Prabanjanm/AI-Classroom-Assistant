from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers.rag_controller import (
    RAGController
)

from app.schemas.rag_schema import (
    RAGQuestionRequest
)

from app.core.database import get_db


router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)

rag_controller = (
    RAGController()
)


@router.post("/ask")
async def ask_question(
    payload: RAGQuestionRequest,
    db: AsyncSession = Depends(get_db)
):

    return await (
        rag_controller.ask_question(
            payload,
            db
        )
    )
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.rag_schema import (
    RAGQuestionRequest
)

from app.services.rag.rag_chat_service import (
    RAGChatService
)


class RAGController:

    def __init__(self):

        self.rag_service = (
            RAGChatService()
        )

    async def ask_question(
        self,
        payload: RAGQuestionRequest,
        db: AsyncSession
    ):

        return await (
            self.rag_service.ask_question(
                db=db,
                question=payload.question
            )
        )
import google.generativeai as genai

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import GEMINI_API_KEY

from app.services.rag.retrieval_service import (
    RetrievalService
)


class RAGChatService:
    """
    Conversational RAG service.
    """

    def __init__(self):

        genai.configure(
            api_key=GEMINI_API_KEY
        )

        self.model = genai.GenerativeModel(
            "models/gemini-3.1-flash-lite"
        )

        self.retrieval_service = (
            RetrievalService()
        )

    async def ask_question(
        self,
        db: AsyncSession,
        question: str
    ):

        retrieved_chunks = await (
            self.retrieval_service
            .retrieve_context(
                db=db,
                query=question
            )
        )

        context = ""

        for chunk in retrieved_chunks:

            context += f"""
            CONTENT:
            {chunk.content}

            DESCRIPTION:
            {chunk.description}
            """

        prompt = f"""
        You are an AI classroom assistant.

        Use the provided context to answer the question.

        If partial information exists,
        provide the closest relevant answer.

        Only say "Answer not found"
        if context is completely unrelated.

        If answer is not found,
        say:
        "Answer not found in lecture."

        CONTEXT:
        {context}

        QUESTION:
        {question}
        """

        response = self.model.generate_content(
            prompt
        )

        return {
            "success": True,
            "answer": response.text,
            "retrieved_chunks": len(
                retrieved_chunks
            )
        }
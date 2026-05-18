from sqlalchemy import text

from sqlalchemy.ext.asyncio import AsyncSession

from app.services.rag.text_embedding_service import (
    TextEmbeddingService
)


class RetrievalService:
    """
    Semantic retrieval service.
    """

    def __init__(self):

        self.embedding_service = (
            TextEmbeddingService()
        )

    async def retrieve_context(
        self,
        db: AsyncSession,
        query: str,
        limit: int = 5
    ):

        embedding = await (
            self.embedding_service
            .generate_embedding(
                query
            )
        )

        sql = text("""
                SELECT
                    content,
                    file_url,
                    description
                FROM multimodal_embeddings
                WHERE text_embedding IS NOT NULL
                ORDER BY text_embedding <=> CAST(:embedding AS vector)
                LIMIT :limit
                """)

        result = await db.execute(
            sql,
            {
                "embedding": str(embedding),
                "limit": limit
            }
        )

        rows = result.fetchall()
        print("\nRETRIEVED CHUNKS:\n")

        for row in rows:

            print(row.content)

            print("\n----------------\n")

        return rows
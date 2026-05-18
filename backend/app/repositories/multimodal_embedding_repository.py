from sqlalchemy.ext.asyncio import AsyncSession

from app.models.multimodal_embedding_model import (
    MultimodalEmbedding
)


class MultimodalEmbeddingRepository:

    async def create_embedding(
        self,
        db: AsyncSession,
        content_type,
        source_id,
        chunk_index,
        content,
        file_url,
        description,
        text_embedding=None,
        image_embedding=None
    ):

        obj = MultimodalEmbedding(
            content_type=content_type,
            source_id=source_id,
            chunk_index=chunk_index,
            content=content,
            file_url=file_url,
            description=description,
            text_embedding=text_embedding,
            image_embedding=image_embedding
        )

        db.add(obj)

        await db.commit()

        await db.refresh(obj)

        return obj
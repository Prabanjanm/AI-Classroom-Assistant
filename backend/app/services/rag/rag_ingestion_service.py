from sqlalchemy.ext.asyncio import AsyncSession

from app.services.rag.chunking_service import (
    ChunkingService
)

from app.services.rag.clip_embedding_service import (
    CLIPEmbeddingService
)

from app.services.rag.image_description_service import (
    ImageDescriptionService
)

from app.repositories.multimodal_embedding_repository import (
    MultimodalEmbeddingRepository
)

from app.services.rag.text_embedding_service import (
    TextEmbeddingService
)


class RAGIngestionService:
    """
    Multimodal RAG ingestion pipeline.
    """

    def __init__(self):

        self.chunking_service = (
            ChunkingService()
        )

        self.clip_embedding_service = (
    CLIPEmbeddingService()
)

        self.text_embedding_service = (
    TextEmbeddingService()
)

        self.image_description_service = (
            ImageDescriptionService()
        )

        self.repository = (
            MultimodalEmbeddingRepository()
        )

    async def ingest_text(
        self,
        db: AsyncSession,
        source_id: str,
        content_type: str,
        text: str,
        file_url: str | None = None
    ):
        """
        Ingest transcript/OCR/text content.
        """

        chunks = await (
            self.chunking_service.chunk_text(
                text
            )
        )

        for index, chunk in enumerate(chunks):

            embedding = await (
                self.text_embedding_service
                .generate_embedding(
                    chunk
                )
            )

            await (
                self.repository.create_embedding(
                    db=db,
                    content_type=content_type,
                    source_id=source_id,
                    chunk_index=index,
                    content=chunk,
                    file_url=file_url,
                    description=None,
                    text_embedding=embedding
                )
            )

        return {
            "success": True,
            "chunks_created": len(chunks)
        }

    async def ingest_image(
        self,
        db: AsyncSession,
        source_id: str,
        image_path: str,
        file_url: str,
        ocr_text: str | None = None
    ):
        """
        Ingest image into multimodal RAG.
        """

        description = await (
            self.image_description_service
            .describe_image(
                image_path
            )
        )

        embedding = await (
            self.clip_embedding_service
            .generate_image_embedding(
                image_path
            )
        )

        combined_content = f"""
        OCR TEXT:
        {ocr_text}

        IMAGE DESCRIPTION:
        {description}
        """

        await (
            self.repository.create_embedding(
                db=db,
                content_type="image",
                source_id=source_id,
                chunk_index=0,
                content=combined_content,
                file_url=file_url,
                description=description,
                image_embedding=embedding
            )
        )

        return {
            "success": True,
            "description": description
        }
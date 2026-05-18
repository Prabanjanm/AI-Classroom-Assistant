import pytesseract

from PIL import Image

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.ocr_repository import (
    OCRRepository
)

from app.services.rag.rag_ingestion_service import (
    RAGIngestionService
)

class ImageOCRService:

    def __init__(self):

        self.repository = OCRRepository()
        self.rag_ingestion_service = (
    RAGIngestionService()
)

    async def extract_text(
        self,
        db: AsyncSession,
        image_path: str,
        file_url: str
    ):

        image = Image.open(image_path)

        extracted_text = pytesseract.image_to_string(
            image
        )

        saved_result = await (
            self.repository.create_ocr_result(
                db=db,
                file_url=file_url,
                extracted_text=extracted_text
            )
        )
        await self.rag_ingestion_service.ingest_image(
    db=db,
    source_id=str(saved_result.id),
    image_path=image_path,
    file_url=file_url,
    ocr_text=extracted_text
)

        return {
            "success": True,
            "ocr_id": str(saved_result.id),
            "file_url": file_url,
            "extracted_text": extracted_text
        }
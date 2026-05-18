import fitz
import pytesseract

from PIL import Image

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.ocr_repository import (
    OCRRepository
)

from app.services.rag.rag_ingestion_service import (
    RAGIngestionService
)

class PDFOCRService:

    def __init__(self):

        self.repository = OCRRepository()
        self.rag_ingestion_service = (
    RAGIngestionService()
)

    async def extract_text(
        self,
        db: AsyncSession,
        pdf_path: str,
        file_url: str
    ):

        document = fitz.open(pdf_path)

        extracted_text = ""

        for page_number in range(len(document)):

            page = document.load_page(
                page_number
            )

            pix = page.get_pixmap(
    matrix=fitz.Matrix(1, 1)
)

            image = Image.frombytes(
        "RGB",
        [pix.width, pix.height],
           pix.samples
    )

            image = image.resize(
        (1200, 1200)
    )

            image = image.convert("L")

            page_text = pytesseract.image_to_string(
                image
            )

            extracted_text += (
                f"\n\n--- Page {page_number + 1} ---\n"
            )

            extracted_text += page_text

        saved_result = await (
            self.repository.create_ocr_result(
                db=db,
                file_url=file_url,
                extracted_text=extracted_text
            )
        )

        await self.rag_ingestion_service.ingest_text(
    db=db,
    source_id=str(saved_result.id),
    content_type="pdf",
    text=extracted_text,
    file_url=file_url
)

        return {
            "success": True,
            "ocr_id": str(saved_result.id),
            "file_url": file_url,
            "extracted_text": extracted_text
        }
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.ocr_model import OCRResult


class OCRRepository:

    async def create_ocr_result(
        self,
        db: AsyncSession,
        file_url: str,
        extracted_text: str
    ):

        result = OCRResult(
            file_url=file_url,
            extracted_text=extracted_text
        )

        db.add(result)

        await db.commit()

        await db.refresh(result)

        return result
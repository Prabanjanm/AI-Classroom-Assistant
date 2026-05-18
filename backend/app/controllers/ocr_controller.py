import uuid

from pathlib import Path

from fastapi import UploadFile

from sqlalchemy.ext.asyncio import AsyncSession

from app.services.ocr.image_ocr_service import (
    ImageOCRService
)

from app.services.ocr.pdf_ocr_service import (
    PDFOCRService
)

from app.utils.storage_utils import (
    upload_file
)


class OCRController:

    def __init__(self):

        self.image_ocr_service = (
            ImageOCRService()
        )

        self.pdf_ocr_service = (
            PDFOCRService()
        )

        self.upload_dir = Path(
            "storage/uploads"
        )

        self.upload_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    async def process_file(
        self,
        file: UploadFile,
        db: AsyncSession
    ):

        filename = (
            f"{uuid.uuid4()}_{file.filename}"
        )

        file_path = (
            self.upload_dir / filename
        )

        file_bytes = await file.read()

        with open(file_path, "wb") as buffer:

            buffer.write(file_bytes)

        extension = (
            file.filename
            .split(".")[-1]
            .lower()
        )

        if extension in [
            "png",
            "jpg",
            "jpeg"
        ]:

            file_url = await upload_file(
                bucket_name="lecture-images",
                file_name=filename,
                file_path=str(file_path)
            )

            return await (
                self.image_ocr_service.extract_text(
                    db=db,
                    image_path=str(file_path),
                    file_url=file_url
                )
            )

        elif extension == "pdf":

            file_url = await upload_file(
                bucket_name="lecture-pdfs",
                file_name=filename,
                file_path=str(file_path)
            )

            return await (
                self.pdf_ocr_service.extract_text(
                    db=db,
                    pdf_path=str(file_path),
                    file_url=file_url
                )
            )

        return {
            "success": False,
            "message": "Unsupported file type"
        }
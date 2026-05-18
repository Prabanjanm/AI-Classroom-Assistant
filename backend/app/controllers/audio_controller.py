import uuid

from pathlib import Path

from fastapi import UploadFile

from sqlalchemy.ext.asyncio import AsyncSession

from app.services.audio.whisper_service import (
    WhisperService
)

from app.utils.storage_utils import (
    upload_file
)

from app.services.rag.rag_ingestion_service import (
    RAGIngestionService
)

class AudioController:
    """
    Controller for audio transcription.
    """

    def __init__(self):

        self.whisper_service = (
            WhisperService()
        )

        self.upload_dir = Path(
            "storage/uploads"
        )

        self.upload_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.rag_ingestion_service = (
    RAGIngestionService()
)

    async def transcribe_audio(
        self,
        file: UploadFile,
        db: AsyncSession
    ):
        """
        Handle uploaded audio transcription.
        """

        filename = (
            f"{uuid.uuid4()}_{file.filename}"
        )

        file_path = (
            self.upload_dir / filename
        )

        file_bytes = await file.read()

        with open(file_path, "wb") as buffer:

            buffer.write(file_bytes)

        audio_url = await upload_file(
            bucket_name="lecture-audio",
            file_name=filename,
            file_path=str(file_path)
        )

        result = await (
            self.whisper_service.transcribe_audio(
                str(file_path)
            )
        )

        saved_transcription = await (
    self.whisper_service.save_transcript(
        db=db,
        lecture_title=file.filename,
        audio_url=audio_url,
        transcript=result["transcript"]
    )
)
        await self.rag_ingestion_service.ingest_text(
    db=db,
    source_id=str(saved_transcription.id),
    content_type="audio",
    text=result["transcript"],
    file_url=audio_url
)

        return result
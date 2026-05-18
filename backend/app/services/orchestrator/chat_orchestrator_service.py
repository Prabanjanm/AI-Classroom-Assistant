import google.generativeai as genai

from fastapi import UploadFile

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import GEMINI_API_KEY

from app.services.orchestrator.modality_detector_service import (
    ModalityDetectorService
)

from app.services.orchestrator.context_builder_service import (
    ContextBuilderService
)

from app.services.ocr.image_ocr_service import (
    ImageOCRService
)

from app.services.ocr.pdf_ocr_service import (
    PDFOCRService
)

from app.services.audio.whisper_service import (
    WhisperService
)

from app.services.video.video_summary_service import (
     VideoSummaryService
)

from app.services.rag.retrieval_service import (
    RetrievalService
)


class ChatOrchestratorService:

    def __init__(self):

        genai.configure(
            api_key=GEMINI_API_KEY
        )

        self.model = genai.GenerativeModel(
            "models/gemini-3.1-flash-lite"
        )

        self.detector = (
            ModalityDetectorService()
        )

        self.context_builder = (
            ContextBuilderService()
        )

        self.image_ocr_service = (
            ImageOCRService()
        )

        self.pdf_ocr_service = (
            PDFOCRService()
        )
        self.whisper_service = (
            WhisperService()
        )

        self.video_service = (
            VideoSummaryService()
        )

        self.retrieval_service = (
            RetrievalService()
        )

    async def process_chat(
        self,
        db: AsyncSession,
        message: str,
        file_path: str | None = None,
        filename: str | None = None
    ):

        extracted_text = ""

        if file_path and filename:

            modality = await (
                self.detector.detect(
                    filename
                )
            )

            if modality == "image":

                result = await (
                    self.image_ocr_service
                     .extract_text(
                        db=db,
                        image_path=file_path,
                        file_url=file_path
                    )
                )

                extracted_text = (
                    result[
                        "extracted_text"
                    ]
                )

            elif modality == "pdf":

                result = await (
                    self.pdf_ocr_service
                    .extract_text(
                        db=db,
                        pdf_path=file_path,
                        file_url=file_path
                    )
                )

                extracted_text = (
                    result[
                        "extracted_text"
                    ]
                )

            elif modality == "audio":

                result = await (
                    self.whisper_service
                    .transcribe_audio(
                        
                        file_path
                    )
                )
                extracted_text = (
                    result[
                        "transcript"
                    ]
                )

        rag_results = await (
            self.retrieval_service
            .retrieve_context(
                db=db,
                query=message
            )
        )

        rag_context = ""

        for row in rag_results:

            rag_context += (
                row.content + "\n"
            )

        final_context = await (
            self.context_builder
            .build_context(
                user_message=message,
                extracted_text=extracted_text,
                rag_context=rag_context
            )
        )
        prompt = f"""
        You are an AI classroom assistant.

        Use the provided context
        to answer the student.

        CONTEXT:
        {final_context}
        """

        response = self.model.generate_content(
            prompt
        )

        return {
            "success": True,
            "answer": response.text,
            "context_used": bool(
                extracted_text or rag_context
            )
        }
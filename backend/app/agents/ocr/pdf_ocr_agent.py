from app.agents.base.base_agent import (
    BaseAgent
)

from app.services.ocr.pdf_ocr_service import (
    PDFOCRService
)


class PDFOCRAgent(BaseAgent):

    def __init__(self):

        super().__init__()

        self.name = "pdf_ocr_agent"

        self.description = (
            "Extract text from PDFs"
        )

        self.capabilities = [
            "pdf_ocr",
            "pdf_text_extraction",
            "ocr"
        ]

        self.service = (
            PDFOCRService()
        )

    async def execute(
        self,
        task: dict
    ):

        return await (
            self.service.extract_text(
                db=task["db"],
                pdf_path=task["pdf_path"],
                file_url=task.get(
    "file_url",
    task["pdf_path"]
)
            )
        )
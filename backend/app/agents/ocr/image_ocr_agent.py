from app.agents.base.base_agent import (
    BaseAgent
)

from app.services.ocr.image_ocr_service import (
    ImageOCRService
)


class ImageOCRAgent(BaseAgent):

    def __init__(self):

        super().__init__()

        self.name = "image_ocr_agent"

        self.description = (
            "Extract text from images"
        )

        self.capabilities = [
            "image_ocr",
            "ocr",
            "image_text_extraction"
        ]

        self.service = (
            ImageOCRService()
        )

    async def execute(
        self,
        task: dict
    ):

        return await (
            self.service.extract_text(
                db=task["db"],
                image_path=task["image_path"],
                file_url=task.get(
    "file_url",
    task["image_path"]
)
            )
        )

    async def validate(
        self,
        task: dict
    ):

        required = [
            "db",
            "image_path",
            "file_url"
        ]

        for field in required:

            if field not in task:

                raise ValueError(
                    f"{field} required"
                )

        return True
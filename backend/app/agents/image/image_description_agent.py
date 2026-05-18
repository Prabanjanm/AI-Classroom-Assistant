from app.agents.base.base_agent import (
    BaseAgent
)

from app.services.rag.image_description_service import (
    ImageDescriptionService
)


class ImageDescriptionAgent(
    BaseAgent
):

    def __init__(self):

        super().__init__()

        self.name = (
            "image_description_agent"
        )

        self.description = (
            "Generate image captions"
        )

        self.capabilities = [
            "image_captioning",
            "image_understanding"
        ]

        self.service = (
            ImageDescriptionService()
        )

    async def execute(
        self,
        task: dict
    ):

        description = await (
            self.service.describe_image(
                task["image_path"]
            )
        )

        return {
            "success": True,
            "description": description
        }
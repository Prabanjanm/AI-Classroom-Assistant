from app.agents.base.base_agent import (
    BaseAgent
)

from app.services.image.image_generation_service import (
    ImageGenerationService
)


class ImageGenerationAgent(BaseAgent):

    def __init__(self):

        super().__init__()

        self.name = (
            "image_generation_agent"
        )

        self.description = (
            "AI image generation"
        )

        self.capabilities = [
            "image_generation",
            "text_to_image"
        ]

        self.service = (
            ImageGenerationService()
        )

    async def execute(
        self,
        task: dict
    ):

        return await self.service.generate_image(
            db=task["db"],
            prompt=task["prompt"],
            negative_prompt=task.get(
                "negative_prompt"
            )
        )
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.image_schema import (
    TextToImageRequest
)

from app.services.image.image_generation_service import (
    ImageGenerationService
)


class ImageController:

    def __init__(self):

        self.image_service = ImageGenerationService()

    async def generate_image(
        self,
        payload: TextToImageRequest,
        db: AsyncSession
    ):

        return await self.image_service.generate_image(
            db=db,
            prompt=payload.prompt,
            negative_prompt=payload.negative_prompt,
            height=payload.height,
            width=payload.width,
            steps=payload.steps
        )
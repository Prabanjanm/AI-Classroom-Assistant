from sqlalchemy.ext.asyncio import AsyncSession

from app.models.image_model import GeneratedImage


class ImageRepository:

    async def create_image(
        self,
        db: AsyncSession,
        prompt: str,
        image_url: str
    ):

        image = GeneratedImage(
            prompt=prompt,
            image_url=image_url
        )

        db.add(image)

        await db.commit()

        await db.refresh(image)

        return image
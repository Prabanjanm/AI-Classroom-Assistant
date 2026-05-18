import uuid
from pathlib import Path

import torch

from diffusers import AutoPipelineForText2Image

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.image_repository import (
    ImageRepository
)
from app.utils.storage_utils import (
    upload_file
)

class ImageGenerationService:
    """
    Lightweight CPU-friendly image generation service.
    """

    def __init__(self):

        self.output_dir = Path(
            "storage/generated_images"
        )

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.device = "cpu"

        self.repository = ImageRepository()

        self.pipe = AutoPipelineForText2Image.from_pretrained(
            "segmind/tiny-sd",
            torch_dtype=torch.float32
        ).to(self.device)

    async def generate_image(
        self,
        db: AsyncSession,
        prompt: str,
        negative_prompt: str | None = None,
        height: int = 512,
        width: int = 512,
        steps: int = 4
    ) -> dict:
        """
        Generate image from prompt.
        """

        image = self.pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            height=height,
            width=width,
            num_inference_steps=steps
        ).images[0]

        filename = f"{uuid.uuid4()}.png"

        image_path = self.output_dir / filename

        image.save(image_path)

        image_url = await upload_file(
    bucket_name="generated-images",
    file_name=filename,
    file_path=str(image_path)
)

        saved_image = await self.repository.create_image(
        db=db,
        prompt=prompt,
        image_url=image_url
    )

        return {
            "success": True,
            "image_id": str(saved_image.id),
            "prompt": prompt,
            "image_url": image_url,
                "image_path": str(
        image_path
    ),

    "image_paths": [
        str(image_path)
    ]
        }
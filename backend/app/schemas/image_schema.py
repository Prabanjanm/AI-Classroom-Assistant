from pydantic import BaseModel, Field


class TextToImageRequest(BaseModel):
    """
    Request schema for text-to-image generation.
    """

    prompt: str = Field(..., min_length=3, max_length=1000)
    negative_prompt: str | None = None
    height: int = 512
    width: int = 512
    steps: int = 30
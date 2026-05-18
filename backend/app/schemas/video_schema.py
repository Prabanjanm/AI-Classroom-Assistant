from pydantic import BaseModel


class VideoGenerationRequest(
    BaseModel
):

    title: str

    image_paths: list[str]

    audio_path: str

    audio_url: str
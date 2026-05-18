from pydantic import BaseModel


class YouTubeVideoRequest(
    BaseModel
):

    url: str
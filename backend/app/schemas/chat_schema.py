from pydantic import BaseModel


class ChatRequest(BaseModel):

    message: str

    youtube_url: str | None = None
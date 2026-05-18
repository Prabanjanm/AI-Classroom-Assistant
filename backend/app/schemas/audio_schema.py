from pydantic import BaseModel


class AudioTranscriptionResponse(BaseModel):
    """
    Response schema for audio transcription.
    """

    success: bool
    transcript: str
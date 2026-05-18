from pydantic import BaseModel


class SummaryRequest(BaseModel):

    transcription_id: str
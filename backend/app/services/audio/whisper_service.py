import whisper

from app.repositories.transcription_repository import (
    TranscriptionRepository
)


class WhisperService:
    """
    Service for audio transcription.
    """

    model = None

    def load_model(self):

        if self.model is None:

            self.model = whisper.load_model(
                "base"
            )

        self.repository = (
            TranscriptionRepository()
        )

    async def transcribe_audio(
        self,
        audio_path: str
    ) -> dict:
        """
        Convert audio to text.
        """
        self.load_model()
        result = self.model.transcribe(
            audio_path
        )

        return {
            "success": True,
            "transcript": result["text"],
             "transcription": result["text"]

        }

    async def save_transcript(
    self,
    db,
    lecture_title,
    audio_url,
    transcript
):
     self.load_model()
     return await (
        self.repository.create_transcription(
            db=db,
            lecture_title=lecture_title,
            audio_url=audio_url,
            transcript=transcript
        )
    )
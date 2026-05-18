from app.agents.base.base_agent import (
    BaseAgent
)

from app.services.audio.whisper_service import (
    WhisperService
)


class WhisperAgent(BaseAgent):

    def __init__(self):

        super().__init__()

        self.name = "whisper_agent"

        self.description = (
            "Speech-to-text transcription agent"
        )

        self.capabilities = [
            "transcription",
            "speech_to_text",
            "audio_transcription"
        ]

        self.service = (
            WhisperService()
        )

    async def execute(
        self,
        task: dict
    ):

        return await (
            self.service.transcribe_audio(
                task["audio_path"]
            )
        )

    async def validate(
        self,
        task: dict
    ):

        if "audio_path" not in task:

            raise ValueError(
                "audio_path required"
            )

        return True
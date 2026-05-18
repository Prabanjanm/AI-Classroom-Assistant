from app.agents.base.base_agent import (
    BaseAgent
)

from app.services.tts.tts_service import (
    TTSService
)


class TTSAgent(BaseAgent):

    def __init__(self):

        super().__init__()

        self.name = "tts_agent"

        self.description = (
            "Text to speech generation"
        )

        self.capabilities = [
            "tts",
            "audio_generation",
            "speech_synthesis"
        ]

        self.service = (
            TTSService()
        )

    async def execute(
        self,
        task: dict
    ):

        return await (
            self.service.generate_audio(
                db=task["db"],
                text = task.get(
    "text",

    task.get(
        "summary",

        task.get(
            "content",

            task.get(
                "user_request",
                "Hello from AI assistant"
            )
        )
    )
),
                voice=task.get(
    "voice",
    "en-US-GuyNeural"
)
            )
        )
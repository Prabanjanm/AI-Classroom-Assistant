from app.agents.base.base_agent import (
    BaseAgent
)

from app.services.video.youtube_video_service import (
    YouTubeVideoService
)


class YouTubeAgent(BaseAgent):

    def __init__(self):

        super().__init__()

        self.name = "youtube_agent"

        self.description = (
            "Download YouTube audio"
        )

        self.capabilities = [
            "youtube_download",
            "youtube_audio"
        ]

        self.service = (
            YouTubeVideoService()
        )

    async def execute(
        self,
        task: dict
    ):

        return await (
            self.service.download_audio(
                task["url"]
            )
        )
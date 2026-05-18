from app.agents.base.base_agent import (
    BaseAgent
)

from app.services.video.video_summary_service import (
    VideoSummaryService
)


class VideoSummaryAgent(
    BaseAgent
):

    def __init__(self):

        super().__init__()

        self.name = (
            "video_summary_agent"
        )

        self.description = (
            "Summarize uploaded videos"
        )

        self.capabilities = [
            "video_summary",
            "lecture_summary"
        ]

        self.service = (
            VideoSummaryService()
        )

    async def execute(
        self,
        task: dict
    ):

        return await (
            self.service.summarize_video(
                db=task["db"],
                title=task["title"],
                video_path=task[
                    "video_path"
                ]
            )
        )
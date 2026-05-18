from app.agents.base.base_agent import (
    BaseAgent
)

from app.services.video.video_generation_service import (
    VideoGenerationService
)


class VideoGenerationAgent(
    BaseAgent
):

    def __init__(self):

        super().__init__()

        self.name = (
            "video_generation_agent"
        )

        self.description = (
            "Generate videos from images and audio"
        )

        self.capabilities = [
            "video_generation"
        ]

        self.service = (
            VideoGenerationService()
        )

    async def validate(
        self,
        task: dict
    ):

        if not task.get(
            "audio_path"
        ):

            raise ValueError(
                "audio_path required "
                "for video generation"
            )

        if not task.get(
            "image_paths"
        ):

            raise ValueError(
                "image_paths required "
                "for video generation"
            )

    async def execute(
        self,
        task: dict
    ):

        await self.validate(task)

        return await (
            self.service.generate_video(
                db=task["db"],

                title=task.get(
                    "title",
                    "Generated Video"
                ),

                image_paths=task.get(
                    "image_paths",
                    []
                ),

                audio_path=task.get(
                    "audio_path",
                    ""
                ),

                audio_url=task.get(
                    "audio_url",
                    ""
                )
            )
        )
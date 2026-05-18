from app.agents.base.base_agent import (
    BaseAgent
)

from app.services.lecture.lecture_summary_service    import (
    SummaryService
)


class SummaryAgent(
    BaseAgent
):

    def __init__(self):

        super().__init__()

        self.name = (
            "summary_agent"
        )

        self.description = (
            "Summarize educational content"
        )

        self.capabilities = [
            "summarization"
        ]

        self.service = (
            SummaryService()
        )

    async def validate(
        self,
        task: dict
    ):

        if "db" not in task:

            raise ValueError(
                "db is required"
            )

        text = (
            task.get("text")
            or
            task.get("extracted_text")
        )

        if not text:

            raise ValueError(
                "text or extracted_text "
                "is required"
            )

        return True

    async def execute(
        self,
        task: dict
    ):

        text = (
            task.get("text")
            or
            task.get("extracted_text")
        )

        return await (
            self.service.summarize_text(
                text=text
            )
        )
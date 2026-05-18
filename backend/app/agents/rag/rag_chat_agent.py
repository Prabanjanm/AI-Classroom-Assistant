from app.agents.base.base_agent import (
    BaseAgent
)

from app.services.rag.rag_chat_service import (
    RAGChatService
)


class RAGChatAgent(BaseAgent):

    def __init__(self):

        super().__init__()

        self.name = "rag_chat_agent"

        self.description = (
            "Conversational RAG agent"
        )

        self.capabilities = [
            "rag_chat",
            "question_answering"
        ]

        self.service = (
            RAGChatService()
        )

    async def execute(
        self,
        task: dict
    ):

        return await (
            self.service.ask_question(
                db=task["db"],
                question = task.get(
                    "question",
                    task.get(
                        "query",
                        task.get(
                            "user_request",
                            ""
                        )
                    )
                )
            )
        )
from app.agents.base.base_agent import (
    BaseAgent
)

from app.services.rag.retrieval_service import (
    RetrievalService
)


class RetrievalAgent(BaseAgent):

    def __init__(self):

        super().__init__()

        self.name = "retrieval_agent"

        self.description = (
            "Semantic retrieval agent"
        )

        self.capabilities = [
            "semantic_search",
            "retrieval",
            "rag_retrieval"
        ]

        self.service = (
            RetrievalService()
        )

    async def execute(
        self,
        task: dict
    ):

        chunks = await (
            self.service.retrieve_context(
                db=task["db"],
                query=task["query"]
            )
        )

        return {
            "success": True,
            "chunks": chunks
        }
from app.agents.base.base_agent import (
    BaseAgent
)

from app.services.rag.clip_embedding_service import (
    CLIPEmbeddingService
)


class CLIPEmbeddingAgent(
    BaseAgent
):

    def __init__(self):

        super().__init__()

        self.name = (
            "clip_embedding_agent"
        )

        self.description = (
            "Generate image embeddings"
        )

        self.capabilities = [
            "image_embedding",
            "multimodal_embedding"
        ]

        self.service = (
            CLIPEmbeddingService()
        )

    async def execute(
        self,
        task: dict
    ):

        embedding = await (
            self.service
            .generate_image_embedding(
                task["image_path"]
            )
        )

        return {
            "success": True,
            "embedding": embedding
        }
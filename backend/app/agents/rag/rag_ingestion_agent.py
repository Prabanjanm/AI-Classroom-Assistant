from app.agents.base.base_agent import (
    BaseAgent
)

from app.services.rag.rag_ingestion_service import (
    RAGIngestionService
)


class RAGIngestionAgent(
    BaseAgent
):

    def __init__(self):

        super().__init__()

        self.name = (
            "rag_ingestion_agent"
        )

        self.description = (
            "Ingest content into RAG"
        )

        self.capabilities = [
            "rag_ingestion",
            "embedding_storage"
        ]

        self.service = (
            RAGIngestionService()
        )

    async def execute(
        self,
        task: dict
    ):

        content_type = task[
            "content_type"
        ]

        if content_type == "image":

            return await (
                self.service.ingest_image(
                    db=task["db"],
                    source_id=task[
                        "source_id"
                    ],
                    image_path=task[
                        "image_path"
                    ],
                    file_url=task[
                        "file_url"
                    ],
                    ocr_text=task.get(
                        "ocr_text"
                    )
                )
            )

        return await (
            self.service.ingest_text(
                db=task["db"],
                source_id=task[
                    "source_id"
                ],
                content_type=content_type,
                text=task["text"],
                file_url=task.get(
                    "file_url"
                )
            )
        )
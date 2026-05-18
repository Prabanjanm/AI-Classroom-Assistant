from sentence_transformers import (
    SentenceTransformer
)


class TextEmbeddingService:
    """
    Text embedding service for RAG.
    """
    model = None

    def load_model(self):

     if self.model is None:

        print(
                "Loading embedding model..."
            )

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    async def generate_embedding(
        self,
        text: str
    ):
        self.load_model()
        embedding = self.model.encode(
            text
        )
 
        return embedding.flatten().tolist()
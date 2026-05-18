from app.agents.registry.agent_registry import (
    AgentRegistry
)

from app.agents.summary.summary_agent import (
    SummaryAgent
)

from app.agents.whisper.whisper_agent import (
    WhisperAgent
)

from app.agents.ocr.image_ocr_agent import (
    ImageOCRAgent
)

from app.agents.ocr.pdf_ocr_agent import (
    PDFOCRAgent
)

from app.agents.tts.tts_agent import (
    TTSAgent
)

from app.agents.image.image_generation_agent import (
    ImageGenerationAgent
)

from app.agents.image.image_description_agent import (
    ImageDescriptionAgent
)

from app.agents.image.clip_embedding_agent import (
    CLIPEmbeddingAgent
)

from app.agents.rag.rag_ingestion_agent import (
    RAGIngestionAgent
)

from app.agents.rag.retrieval_agent import (
    RetrievalAgent
)

from app.agents.rag.rag_chat_agent import (
    RAGChatAgent
)

from app.agents.video.video_generation_agent import (
    VideoGenerationAgent
)

from app.agents.video.video_summary_agent import (
    VideoSummaryAgent
)

from app.agents.youtube.youtube_agent import (
    YouTubeAgent
)

registry = AgentRegistry()

registry.register(
    SummaryAgent()
)

registry.register(
    WhisperAgent()
)

registry.register(
    ImageOCRAgent()
)

registry.register(
    PDFOCRAgent()
)

registry.register(
    TTSAgent()
)

registry.register(
    ImageGenerationAgent()
)

registry.register(
    ImageDescriptionAgent()
)

registry.register(
    CLIPEmbeddingAgent()
)

registry.register(
    RAGIngestionAgent()
)

registry.register(
    RetrievalAgent()
)

registry.register(
    RAGChatAgent()
)

registry.register(
    VideoGenerationAgent()
)

registry.register(
    VideoSummaryAgent()
)

registry.register(
    YouTubeAgent()
)
import asyncio

from app.core.database import engine, Base

from app.models.user_model import User
from app.models.transcription_model import Transcription
from app.models.summary_model import Summary
from app.models.image_model import GeneratedImage
from app.models.ocr_model import OCRResult
from app.models.multimodal_embedding_model import (
    MultimodalEmbedding
)
from app.models.tts_model import GeneratedAudio
from app.models.video_model import (
    GeneratedVideo
)
from app.models.video_summary_model import (
    VideoSummary
)
async def init_db():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


asyncio.run(init_db())
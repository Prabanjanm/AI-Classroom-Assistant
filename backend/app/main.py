from fastapi import FastAPI

from app.routers.image_router import router as image_router
from app.routers.audio_router import router as audio_router
from app.routers.rag_router import (
    router as rag_router
)
from app.routers.tts_router import (
    router as tts_router
)
from app.routers.video_router import (
    router as video_router
)

from app.routers.video_summary_router import (
    router as video_summary_router
)


from app.routers.orchestrator_router import (
    router as orchestrator_router
)


app = FastAPI(
    title="AI Classroom Assistant"
)
# app.include_router(
#     chat_router
# )
app.include_router(
    orchestrator_router
)
app.include_router(
    rag_router,
    prefix="/api/rag",
    tags=["RAG"]
)
app.include_router( 
    video_summary_router
)
app.include_router(
    video_router
)
app.include_router(
    tts_router
)
app.include_router(
    image_router,
    prefix="/api/image",
    tags=["Image Generation"]
)
app.include_router(
    audio_router,
    prefix="/api/audio",
    tags=["Audio"]
)

from app.routers.summary_router import router as summary_router

app.include_router(
    summary_router,
    prefix="/api/summary",
    tags=["Summary"]
)

from app.routers.ocr_router import router as ocr_router

app.include_router(
    ocr_router,
    prefix="/api/ocr",
    tags=["OCR"]
)
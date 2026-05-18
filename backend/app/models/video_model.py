from sqlalchemy import (
    Column,
    String
)

from sqlalchemy.dialects.postgresql import UUID

import uuid

from app.core.database import Base


class GeneratedVideo(Base):

    __tablename__ = "generated_videos"

    __table_args__ = {
        "extend_existing": True
    }

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    title = Column(String)

    video_url = Column(String)

    audio_url = Column(String)
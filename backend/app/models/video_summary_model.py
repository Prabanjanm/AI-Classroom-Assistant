from sqlalchemy import (
    Column,
    String,
    Text
)

from sqlalchemy.dialects.postgresql import UUID

import uuid

from app.core.database import Base


class VideoSummary(Base):

    __tablename__ = "video_summaries"

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

    transcript = Column(Text)

    summary = Column(Text)
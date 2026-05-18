from sqlalchemy import (
    Column,
    String,
    Text
)

from sqlalchemy.dialects.postgresql import UUID

import uuid

from app.core.database import Base


class Transcription(Base):

    __tablename__ = "transcriptions"

    __table_args__ = {
        "extend_existing": True
    }

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    lecture_title = Column(String)

    audio_url = Column(String)

    transcript = Column(Text)
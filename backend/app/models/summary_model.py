from sqlalchemy import (
    Column,
    Text,
    String,
    ForeignKey
)

from sqlalchemy.dialects.postgresql import UUID

import uuid

from app.core.database import Base


class Summary(Base):
    """
    Lecture summary model.
    """

    __tablename__ = "summaries"

    __table_args__ = {
        "extend_existing": True
    }

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    lecture_title = Column(String)

    transcript = Column(Text)

    summary = Column(Text)

    transcription_id = Column(
        UUID(as_uuid=True),
        ForeignKey("transcriptions.id")
    )
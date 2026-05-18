from sqlalchemy import (
    Column,
    String,
    Text
)

from sqlalchemy.dialects.postgresql import UUID

import uuid

from app.core.database import Base


class GeneratedAudio(Base):

    __tablename__ = "generated_audio"

    __table_args__ = {
        "extend_existing": True
    }

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    text = Column(Text)

    voice = Column(String)

    audio_url = Column(String)
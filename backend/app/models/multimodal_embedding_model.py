from sqlalchemy import (
    Column,
    Text,
    String,
    Integer
)

from sqlalchemy.dialects.postgresql import UUID

from pgvector.sqlalchemy import Vector

import uuid

from app.core.database import Base


class MultimodalEmbedding(Base):

    __tablename__ = "multimodal_embeddings"

    __table_args__ = {
        "extend_existing": True
    }

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    content_type = Column(String)

    source_id = Column(String)

    chunk_index = Column(Integer)

    content = Column(Text)

    file_url = Column(String)

    description = Column(Text)

    text_embedding = Column(
        Vector(384),
        nullable=True
    )

    image_embedding = Column(
        Vector(512),
        nullable=True
    )
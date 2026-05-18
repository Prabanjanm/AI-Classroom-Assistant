from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

import uuid

from app.core.database import Base


class GeneratedImage(Base):

    __tablename__ = "generated_images"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    prompt = Column(String)

    image_url = Column(String)
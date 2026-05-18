from sqlalchemy import (
    Column,
    Text,
    String
)

from sqlalchemy.dialects.postgresql import UUID

import uuid

from app.core.database import Base


class OCRResult(Base):

    __tablename__ = "ocr_results"

    __table_args__ = {
        "extend_existing": True
    }

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    file_url = Column(String)

    extracted_text = Column(Text)
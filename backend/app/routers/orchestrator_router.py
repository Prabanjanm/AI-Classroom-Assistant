from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form,
    Depends
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from pathlib import Path

import uuid

from app.core.database import get_db

from app.controllers.orchestrator_controller import (
    OrchestratorController
)

router = APIRouter()

controller = (
    OrchestratorController()
)

UPLOAD_DIR = Path(
    "storage/uploads"
)

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)


@router.post("/execute")
async def execute_workflow(
    user_request: str = Form(...),

    file: UploadFile | None = File(None),

    db: AsyncSession = Depends(get_db)
):

    uploaded_file_path = None

    if file:

        filename = (
            f"{uuid.uuid4()}_"
            f"{file.filename}"
        )

        uploaded_file_path = (
            UPLOAD_DIR / filename
        )

        with open(
            uploaded_file_path,
            "wb"
        ) as f:

            content = await file.read()

            f.write(content)

    return await (
        controller.execute(
            db=db,
            user_request=user_request,
            uploaded_file_path=(
                str(uploaded_file_path)
                if uploaded_file_path
                else None
            )
        )
    )
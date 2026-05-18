from supabase import create_client

from app.core.config import (
    SUPABASE_URL,
    SUPABASE_SERVICE_KEY
)


supabase = create_client(
    SUPABASE_URL,
    SUPABASE_SERVICE_KEY
)


async def upload_file(
    bucket_name: str,
    file_name: str,
    file_path: str
):

    with open(file_path, "rb") as file:

        supabase.storage.from_(
            bucket_name
        ).upload(
            file_name,
            file
        )

    public_url = (
        supabase.storage
        .from_(bucket_name)
        .get_public_url(file_name)
    )

    return public_url
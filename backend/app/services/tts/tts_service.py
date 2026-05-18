import uuid

from pathlib import Path

import edge_tts

from app.db.supabase_client import (
    supabase
)

from app.repositories.tts_repository import (
    TTSRepository
)


class TTSService:

    def __init__(self):

        self.output_dir = Path(
            "storage/generated_audio"
        )

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.repository = (
            TTSRepository()
        )

    async def generate_audio(
        self,
        db,
        text: str,
        voice: str
    ):

        filename = (
            f"{uuid.uuid4()}.mp3"
        )

        output_path = (
            self.output_dir / filename
        )

        communicate = edge_tts.Communicate(
            text=text,
            voice=voice
        )

        await communicate.save(
            str(output_path)
        )

        with open(
            output_path,
            "rb"
        ) as f:

            supabase.storage.from_(
                "generated-audio"
            ).upload(
                filename,
                f,
                {
                    "content-type": "audio/mpeg"
                }
            )

        audio_url = (
            supabase.storage
            .from_("generated-audio")
            .get_public_url(filename)
        )

        saved_audio = await (
            self.repository.create_audio(
                db=db,
                text=text,
                voice=voice,
                audio_url=audio_url
            )
        )

        return {
            "success": True,
            "audio_id": str(saved_audio.id),
            "audio_url": audio_url,
            "audio_path": str(
        output_path
    ),
            "voice": voice
        }
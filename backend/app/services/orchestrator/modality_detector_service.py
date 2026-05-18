class ModalityDetectorService:

    async def detect(
        self,
        filename: str
    ):  


        extension = (
            filename
            .split(".")[-1]
            .lower()
        )

        if extension in [
            "png",
            "jpg",
            "jpeg"
        ]:
            return "image"

        elif extension == "pdf":
            return "pdf"

        elif extension in [
            "mp3",
            "wav",
            "m4a"
        ]:
            return "audio"

        elif extension in [
            "mp4",
            "mov"
        ]:
            return "video"

        return "unknown"
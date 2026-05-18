# import google.generativeai as genai

# from sqlalchemy.ext.asyncio import AsyncSession

# from app.core.config import GEMINI_API_KEY

# from app.repositories.summary_repository import (
#     SummaryRepository
# )

# from app.repositories.transcription_repository import (
#     TranscriptionRepository
# )


# class SummaryService:

#     def __init__(self):

#         genai.configure(
#             api_key=GEMINI_API_KEY
#         )

#         self.model = genai.GenerativeModel(
#             "models/gemini-3.1-flash-lite"
#         )

#         self.summary_repository = (
#             SummaryRepository()
#         )

#         self.transcription_repository = (
#             TranscriptionRepository()
#         )

#     async def summarize_text(
#         self,
#         db: AsyncSession,
#         transcription_id: str
#     ):
        
#         transcription = await (
#             self.transcription_repository
#             .get_transcription_by_id(
#                 db,
#                 transcription_id
#             )
#         )

#         if not transcription:

#             return {
#                 "success": False,
#                 "message": "Transcription not found"
#             }

#         transcript = transcription.transcript

#         prompt = f"""
#         You are an AI educational assistant.

#         Summarize the following lecture transcript.

#         Focus on:
#         - main topic
#         - important concepts
#         - key ideas

#         Transcript:
#         {transcript}
#         """

#         response = self.model.generate_content(
#             prompt
#         )

#         summary_text = response.text

#         saved_summary = await (
#             self.summary_repository.create_summary(
#                 db=db,
#                 lecture_title=transcription.lecture_title,
#                 transcript=transcript,
#                 summary=summary_text,
#                 transcription_id=transcription.id
#             )
#         )

#         return {
#             "success": True,
#             "summary_id": str(saved_summary.id),
#             "summary": summary_text
#         }
    
#     async def summarize_raw_text(
#     self,
#     text: str
# ):

#         prompt = f"""
#         You are an AI educational assistant.

#         Summarize the following content.

#         Focus on:
#         - main topic
#         - important concepts
#         - key ideas

#         CONTENT:
#         {text}
#         """

#         response = (
#             self.model.generate_content(
#                 prompt
#             )
#         )

#         return {
#             "success": True,
#             "summary": response.text
#         }


import google.generativeai as genai

from app.core.config import (
    GEMINI_API_KEY
)


class SummaryService:

    def __init__(self):

        genai.configure(
            api_key=GEMINI_API_KEY
        )

        self.model = (
            genai.GenerativeModel(
                "models/gemini-3.1-flash-lite"
            )
        )

    async def summarize_text(
        self,
        text: str
    ):

        prompt = f"""
        You are an AI educational assistant.

        Summarize the following content.

        Focus on:
        - main topic
        - important concepts
        - key ideas

        CONTENT:
        {text}
        """

        response = (
            self.model.generate_content(
                prompt
            )
        )

        return {
            "success": True,
            "summary": response.text
        }
class ContextBuilderService:

    async def build_context(
        self,
        user_message: str,
        extracted_text: str = "",
        rag_context: str = "",
        image_description: str = ""
    ):

        return f"""
        USER QUESTION:
        {user_message}

        OCR / TRANSCRIPT:
        {extracted_text}

        IMAGE DESCRIPTION:
        {image_description}

        RAG CONTEXT:
        {rag_context}
        """
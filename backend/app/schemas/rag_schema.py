from pydantic import BaseModel


class RAGQuestionRequest(
    BaseModel
):

    question: str
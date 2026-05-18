import json

import google.generativeai as genai

from app.core.config import (
    GEMINI_API_KEY
)


class ResponseSynthesisAgent:

    def __init__(self):

        genai.configure(
            api_key=GEMINI_API_KEY
        )

        self.model = (
            genai.GenerativeModel(
                "models/gemini-3.1-flash-lite"
            )
        )

    async def synthesize(
        self,
        workflow_goal: str,
        workflow_results: dict
    ):

        prompt = f"""
        You are an AI assistant.

        Convert workflow execution results
        into a conversational AI response.

        WORKFLOW GOAL:
        {workflow_goal}

        WORKFLOW RESULTS:
        {json.dumps(workflow_results, indent=2)}

        RULES:
        - Return ONLY JSON
        - Hide internal workflow details
        - Sound like ChatGPT/Gemini
        - Create a natural assistant message
        - Extract media into artifacts array

        FORMAT:
        {{
        "role": "assistant",

        "message": "Natural AI response",

        "artifacts": [
            {{
            "type": "video",
            "url": "..."
            }}
        ]
        }}
        """

        response = (
            self.model.generate_content(
                prompt
            )
        )

        raw_text = (
            response.text.strip()
        )

        # Remove markdown if exists
        raw_text = (
            raw_text
            .replace(
                "```json",
                ""
            )
            .replace(
                "```",
                ""
            )
            .strip()
        )

        try:

            return json.loads(
                raw_text
            )

        except:

            return {
                "workflow_status": (
                    "success"
                ),
                "raw_response": raw_text
            }
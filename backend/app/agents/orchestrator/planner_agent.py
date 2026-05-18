import json
import re

import google.generativeai as genai

from app.core.config import (
    GEMINI_API_KEY
)

from app.agents import registry


class PlannerAgent:

    def __init__(self):

        genai.configure(
            api_key=GEMINI_API_KEY
        )

        self.model = genai.GenerativeModel(
            "models/gemini-3.1-flash-lite"
        )

    def get_available_agents(self):

        agents = []

        for agent_name in (
            registry.list_agents()
        ):

            agent = registry.get(
                agent_name
            )

            agents.append({
                "name": agent.name,

                "description": (
                    agent.description
                ),

                "capabilities": (
                    agent.capabilities
                ),

                "input_schema": getattr(
                    agent,
                    "input_schema",
                    {}
                ),

                "output_schema": getattr(
                    agent,
                    "output_schema",
                    {}
                )
            })

        return agents

    async def create_plan(
        self,
        user_request: str,
        uploaded_file_path: str | None = None
    ):
        greetings = [
            "hi",
            "hello",
            "hey",
            "good morning",
            "good evening",
            "how are you"
        ]

        if (
            user_request
            .lower()
            .strip()
            in greetings
        ):

            return {
                "goal": "Greeting response",
                "tasks": [],
                "response": {
                    "role": "assistant",
                    "message": (
                        "Hello! How can I help you today?"
                    ),
                    "artifacts": []
                }
            }
        agents = (
            self.get_available_agents()
        )

        prompt = f"""
        You are an AI workflow planner.

        Create workflow plan.

        AVAILABLE AGENTS:
        {json.dumps(agents, indent=2)}

        USER REQUEST:
        {user_request}
        UPLOADED FILE PATH:
        {uploaded_file_path}

        IMPORTANT:
        return only json in the following format without any additional text or explanation.
        If uploaded file exists:
        - use it in input_data
        - determine whether it is:
        image
        pdf
        audio
        video

        - Use rag_chat_agent ONLY when:
        - user asks questions about uploaded documents
        - lecture content
        - stored knowledge
        - semantic retrieval

        - NEVER use rag_chat_agent for:
        - creative generation
        - image generation
        - storytelling
        - educational video creation
        - narration generation

        Examples:

        If uploaded file is image:
        {{
        "goal": "describe image",
        "tasks": [
            {{
            "task_id": "task1",
            "agent_name": "image_description_agent",
            "input_data": {{
                "image_path": "{uploaded_file_path}"
            }},
            "depends_on": []
            }}
        ]
        }}
        EXAMPLES:

        USER REQUEST:
        Extract text from PDF and summarize it

        RESPONSE:
        {{
        "goal": "Summarize PDF",
        "tasks": [
            {{
            "task_id": "task1",
            "agent_name": "pdf_ocr_agent",
            "input_data": {{
                "pdf_path": "uploaded_file.pdf"
            }},
            "depends_on": []
            }},
            {{
            "task_id": "task2",
            "agent_name": "summary_agent",
            "input_data": {{
                "text": "task1.extracted_text"
            }},
            "depends_on": ["task1"]
            }}
        ]
        }}

        FORMAT:
        {{
          "goal": "string",
          "tasks": [
            {{
              "task_id": "task1",
              "agent_name": "summary_agent",
              "input_data": {{}},
              "depends_on": []
            }}
          ] 
        }}
        """

        response = self.model.generate_content(
            prompt
        )

        raw_text = response.text.strip()

        print(
            "RAW LLM RESPONSE:",
            raw_text
        )

        # Extract JSON block safely
        match = re.search(
            r'\{.*\}',
            raw_text,
            re.DOTALL
        )

        if not match:

            raise Exception(
                "No valid JSON found "
                "in LLM response"
            )

        json_text = match.group(0)

        try:

            parsed = json.loads(
                json_text
            )

            return parsed

        except Exception as e:

            print(
                "JSON PARSE ERROR:",
                str(e)
            )

            print(
                "FAILED JSON:",
                json_text
            )

            raise Exception(
                "Invalid JSON returned "
                "from planner"
            )
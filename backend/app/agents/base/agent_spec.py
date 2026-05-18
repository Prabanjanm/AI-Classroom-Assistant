from pydantic import BaseModel
from typing import List, Dict, Any


class AgentSpec(BaseModel):

    name: str

    description: str

    capabilities: List[str]

    input_schema: Dict[str, Any]

    output_schema: Dict[str, Any]
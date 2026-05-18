from pydantic import BaseModel
from typing import List, Dict, Any, Optional


class WorkflowTask(BaseModel):

    task_id: str

    agent_name: str

    input_data: Dict[str, Any]

    depends_on: List[str] = []


class WorkflowPlan(BaseModel):

    goal: str

    tasks: List[WorkflowTask]
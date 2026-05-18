from streamlit import json

from app.agents.orchestrator.planner_agent import (
    PlannerAgent
)

from app.agents.orchestrator.workflow_engine import (
    WorkflowEngine
)

from app.agents.final.final_response_agent import (
    ResponseSynthesisAgent
)

class OrchestratorController:

    def __init__(self):

        self.planner = (
            PlannerAgent()
        )

        self.engine = (
            WorkflowEngine()
        )

        self.final_response_agent = (
    ResponseSynthesisAgent()
)

    async def execute(
        self,
        db,
        user_request: str,
        uploaded_file_path: str | None = None
    ):

        plan = await (
            self.planner.create_plan(
                user_request=user_request,
                uploaded_file_path=(
                    uploaded_file_path
                )
            )
        )
        if not plan["tasks"]:

            return {
                "success": True,
                "response": plan["response"]
            }

        results = await (
            self.engine.execute_plan(
                db=db,
                workflow_plan=plan
            )
        )

        final_response = await (
            self.final_response_agent
            .synthesize(
                workflow_goal=user_request,
                workflow_results=results
            )
        )
        print("\nFINAL RESPONSE TYPE:")
        print(type(final_response))

        print("\nFINAL RESPONSE:")
        print(final_response)

        for k, v in final_response.items():

            print(
                f"\nKEY: {k}"
            )

            print(
                f"TYPE: {type(v)}"
            )

            try:

                json.dumps(v)

                print("SERIALIZABLE")

            except Exception as e:

                print(
                    "NOT SERIALIZABLE:"
                )

                print(str(e))

        return {
    "success": True,
    "response": {
        k: (
            str(v)

            if not isinstance(
                v,
                (
                    str,
                    int,
                    float,
                    bool,
                    list,
                    dict,
                    type(None)
                )
            )

            else v
        )

        for k, v in final_response.items()
    }
}
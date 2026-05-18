from app.agents import registry

from app.agents.orchestrator.execution_context import (
    ExecutionContext
)


class WorkflowEngine:

    def __init__(self):

        pass

    async def execute_plan(
        self,
        db,
        workflow_plan
    ):
        self.context = (
        ExecutionContext()
    )
        tasks = workflow_plan["tasks"]

        for task in tasks:

            try:

                agent = registry.get(
                    task["agent_name"]
                )

                if not agent:

                    raise Exception(
                        f"Agent not found: "
                        f"{task['agent_name']}"
                    )

                # Initial workflow input
                workflow_input = dict(
                    task.get(
                        "input_data",
                        {}
                    )
                )

                # Inject dependency outputs
                for dep in task.get(
                    "depends_on",
                    []
                ):

                    dependency_result = (
                        self.context.get_result(
                            dep
                        )
                    )

                    if dependency_result:

                        safe_result = {

                            k: v

                            for k, v
                            in dependency_result.items()

                            if (
                                k != "db"
                                and
                                "sqlalchemy"
                                not in str(
                                    type(v)
                                ).lower()
                            )
                        }

                        workflow_input.update(
                            safe_result
                        )

                # Resolve references
                workflow_input = (
                    self.resolve_references(
                        workflow_input
                    )
                )

                # Runtime-only context
                runtime_input = dict(
                    workflow_input
                )

                runtime_input["db"] = db

                print(
                    "\nFINAL INPUT:"
                )

                print(
                    runtime_input
                )

                # Validate
                await agent.validate(
                    runtime_input
                )

                # Execute
                result = await (
                    agent.execute(
                        runtime_input
                    )
                )

                print(
                    f"\nRESULT OF "
                    f"{task['task_id']}:"
                )

                print(result)

            except Exception as e:

                print(
                    f"\nERROR IN "
                    f"{task['task_id']}:"
                )

                print(str(e))

                result = {
                    "success": False,
                    "error": str(e)
                }

            # Clean result
            if isinstance(
                result,
                dict
            ):

                cleaned_result = {}

                for k, v in result.items():

                    # Skip DB/session objects
                    if (
                        k == "db"
                        or
                        "sqlalchemy"
                        in str(
                            type(v)
                        ).lower()
                    ):

                        continue

                    cleaned_result[k] = v

            else:

                cleaned_result = result

            # Save task result
            self.context.set_result(
                task["task_id"],
                cleaned_result
            )

        return (
            self.context.all_results()
        )

    def resolve_references(
        self,
        input_data: dict
    ):

        resolved = {}

        for key, value in input_data.items():

            # Handle task references
            if (
                isinstance(value, str)
                and value.startswith("task")
                and "." in value
            ):

                try:

                    parts = value.split(
                        "."
                    )

                    task_id = parts[0]

                    field = parts[1]

                    task_result = (
                        self.context.get_result(
                            task_id
                        )
                    )

                    if (
                        task_result
                        and field in task_result
                    ):

                        resolved_value = (
                            task_result[field]
                        )

                        print(
                            f"\nRESOLVED "
                            f"{value}"
                        )

                        print(
                            f"→ "
                            f"{resolved_value}"
                        )

                        resolved[key] = (
                            resolved_value
                        )

                    else:

                        print(
                            f"\nFAILED TO "
                            f"RESOLVE: "
                            f"{value}"
                        )

                        resolved[key] = value

                except Exception as e:

                    print(
                        f"\nREFERENCE "
                        f"ERROR: "
                        f"{value}"
                    )

                    print(str(e))

                    resolved[key] = value

            else:

                resolved[key] = value

        return resolved
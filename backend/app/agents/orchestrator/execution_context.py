class ExecutionContext:

    def __init__(self):

        self.results = {}

    def set_result(
        self,
        task_id,
        result
    ):

        self.results[task_id] = result

    def get_result(
        self,
        task_id
    ):

        return self.results.get(task_id)

    def all_results(self):

        return self.results
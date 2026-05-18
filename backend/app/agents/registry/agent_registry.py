class AgentRegistry:
    """
    Central registry for all agents.
    """

    def __init__(self):

        self.agents = {}

    def register(
        self,
        agent
    ):

        self.agents[agent.name] = agent

    def get(
        self,
        agent_name: str
    ):

        return self.agents.get(agent_name)

    def list_agents(self):

        return list(
            self.agents.keys()
        )

    def find_by_capability(
        self,
        capability: str
    ):

        matching_agents = []

        for agent in self.agents.values():

            if capability in agent.capabilities:

                matching_agents.append(
                    agent
                )

        return matching_agents
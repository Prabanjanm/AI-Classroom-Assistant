from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """
    Base class for all agents.
    """

    def __init__(self):

        self.name = ""
        self.description = ""
        self.capabilities = []

    @abstractmethod
    async def execute(
        self,
        task: dict
    ):
        """
        Execute the agent task.
        """
        pass

    async def validate(
        self,
        task: dict
    ):
        """
        Optional validation.
        """
        return True

    def metadata(self):
        """
        Return agent metadata.
        """

        return {
            "name": self.name,
            "description": self.description,
            "capabilities": self.capabilities
        }
from abc import ABC, abstractmethod
from typing import Any


class BaseLLMProvider(ABC):

    @abstractmethod
    async def generate(
        self,
        messages: list[dict[str, Any]]
    ) -> str:
        pass
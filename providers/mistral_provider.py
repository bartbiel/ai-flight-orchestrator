import os
from typing import Any, List, Dict, Sequence
from mistralai.client import Mistral
from providers.base import BaseLLMProvider
from dotenv import load_dotenv

load_dotenv()

class MistralProvider(BaseLLMProvider):
    def __init__(self):
        api_key = os.getenv("MISTRAL_API_KEY")
        if not api_key:
            raise RuntimeError("MISTRAL_API_KEY not found")

        self.client = Mistral(api_key=api_key)
        print("MistralProvider initialized successfully")

    async def generate(
        self,
        messages: Sequence[Dict[str, Any]]
    ) -> str:
        # No conversion needed; just pass the list of dicts
        response = self.client.chat.complete(
            model="mistral-large-latest",
            messages=messages  # type: ignore[arg-type]
        )

        choice = response.choices[0]
        message = choice.message
        if message is None:
            raise RuntimeError("Mistral returned no assistant message")

        content = message.content
        if content is None:
            raise RuntimeError("Mistral returned an empty assistant message")

        return str(content)
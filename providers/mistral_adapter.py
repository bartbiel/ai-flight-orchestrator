import asyncio

from providers.mistral_provider import MistralProvider


class MistralAdapter:

    def __init__(self):
        self.provider = MistralProvider()

    def invoke(
        self,
        prompt: str
    ) -> str:

        return asyncio.run(
            self.provider.generate(
                [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
        )
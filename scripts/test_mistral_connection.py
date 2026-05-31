import os
import asyncio

from mistralai.client import Mistral


async def main():

    api_key = os.getenv("MISTRAL_API_KEY")

    if not api_key:
        print("Missing MISTRAL_API_KEY")
        return

    try:

        client = Mistral(api_key=api_key)

        response = client.chat.complete(
            model="mistral-small-latest",
            messages=[
                {
                    "role": "user",
                    "content": "Say hello in one sentence."
                }
            ]
        )

        choice = response.choices[0]
        message = choice.message
        if message is None:
            raise RuntimeError("Mistral returned no assistant message")

        content = message.content
        if content is None:
            raise RuntimeError("Mistral returned an empty assistant message")

        print("MODEL AVAILABLE")
        print(str(content))

    except Exception as e:
        print(f"ERROR: {e}")


asyncio.run(main())


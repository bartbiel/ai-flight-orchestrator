import asyncio

from providers.mistral_provider import MistralProvider


async def main():

    provider = MistralProvider()

    response = await provider.generate([
        {
            "role": "user",
            "content": "Say hello in one sentence."
        }
    ])

    print("MISTRAL TEST SUCCESS")
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
import asyncio

from atlas import AtlasAsync


async def main():
    api = AtlasAsync(grok_api_key="your_api_key")
    response = await api.analyze_text("Hello, Atlas!", web_access=True)
    print(response)


if __name__ == "__main__":
    asyncio.run(main())

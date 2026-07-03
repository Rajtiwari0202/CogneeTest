import cognee
import asyncio

async def main():
    await cognee.add("Cognee is working with Ollama locally.")
    await cognee.cognify()
    result = await cognee.search("What is working?")
    print(result)

asyncio.run(main())

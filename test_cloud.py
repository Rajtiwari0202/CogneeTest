import cognee
import asyncio

async def main():
    await cognee.serve(
        url="https://tenant-33d0c107-36e9-442c-956b-75bfcda821ad.aws.cognee.ai",
        api_key="dadd75c01b297687e73342f1a933c6fc7aae4971af64a136b70a457ece423e0e"
    )

    await cognee.remember("Cognee is working with Cognee Cloud.")
    result = await cognee.recall("What is working?")
    print(result)

    await cognee.disconnect()

asyncio.run(main())

import asyncio
import os

import cognee
from dotenv import load_dotenv

load_dotenv()

CLOUD_URL = "https://tenant-33d0c107-36e9-442c-956b-75bfcda821ad.aws.cognee.ai"
CLOUD_API_KEY = os.getenv("COGNEE_CLOUD_API_KEY")


async def main():
    if not CLOUD_API_KEY:
        raise ValueError(
            "COGNEE_CLOUD_API_KEY not found. Add it to your .env file."
        )

    await cognee.serve(
        url=CLOUD_URL,
        api_key=CLOUD_API_KEY
    )

    try:
        await cognee.remember("Cognee is working with Cognee Cloud.")

        result = await cognee.recall("What is working?")

        print("\n=== Recall Result ===")
        print(result)

    finally:
        await cognee.disconnect()


if __name__ == "__main__":
    asyncio.run(main())

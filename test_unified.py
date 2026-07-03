import asyncio
import os
from dotenv import load_dotenv
load_dotenv()
# ─── THE ONE SWITCH ────────────────────────────────────────────────
# Change this to flip between cloud and local. That's it.
USE_CLOUD = False   # True = Cognee Cloud (uses credits) | False = local Ollama ($0)
# ────────────────────────────────────────────────────────────────────

CLOUD_URL = "https://tenant-33d0c107-36e9-442c-956b-75bfcda821ad.aws.cognee.ai"
CLOUD_API_KEY = os.getenv("COGNEE_CLOUD_API_KEY")

async def main():
    import cognee

    if USE_CLOUD:
        print(">> Running in CLOUD mode (uses Cognee Cloud credits)")
        await cognee.serve(url=CLOUD_URL, api_key=CLOUD_API_KEY)

        await cognee.remember("Testing the unified script in cloud mode.")
        result = await cognee.recall("What is being tested?")
        print(result)

        await cognee.disconnect()

    else:
        print(">> Running in LOCAL mode (free, via Ollama — needs .env configured)")
        # Local mode reads config from .env automatically on import,
        # so make sure .env in this folder has LLM_PROVIDER=ollama etc.

        await cognee.add("Testing the unified script in local mode.")
        await cognee.cognify()
        result = await cognee.search("What is being tested?")
        print(result)


if __name__ == "__main__":
    asyncio.run(main())

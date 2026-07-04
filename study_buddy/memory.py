# study_buddy/memory.py
import cognee

async def remember(text: str):
    try:
        print("MEMORY: storing")

        await cognee.add(text)
        await cognee.cognify()

        print("MEMORY: stored")

    except Exception as e:
        print("MEMORY ERROR:", str(e))


async def recall(query: str) -> str:
    try:
        print("MEMORY: searching")

        result = await cognee.search(query)

        print("MEMORY: search complete")

        if result:
            return str(result)

        return ""

    except Exception as e:
        print("RECALL ERROR:", str(e))
        return ""
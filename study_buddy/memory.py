import cognee


async def remember(text: str):
    await cognee.add(text)
    await cognee.cognify()


async def recall(query: str):
    try:
        result = await cognee.search(query)
        return str(result)
    except Exception:
        return ""

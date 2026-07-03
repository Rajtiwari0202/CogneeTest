from fastapi import FastAPI, BackgroundTasks

from study_buddy.models import ChatRequest, ChatResponse
from study_buddy.tutor import generate_response
from study_buddy.memory import remember, recall

app = FastAPI(title="Study Buddy AI")


@app.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    background_tasks: BackgroundTasks
):
    print("STEP 1")

    memory_context = await recall(request.message)

    print("STEP 2")
    print("MEMORY LENGTH:", len(str(memory_context)))

    prompt = f"""
You are an expert tutor.

Previous memory:
{memory_context}

Student Question:
{request.message}

Give a clear educational answer.
"""

    response = generate_response(prompt)

    print("STEP 3")

    background_tasks.add_task(
        remember,
        f"""
Student asked:
{request.message}

Tutor answered:
{response}
"""
    )

    print("STEP 4")

    return ChatResponse(response=response)

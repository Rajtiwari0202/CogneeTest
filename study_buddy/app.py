# study_buddy/app.py

from fastapi import FastAPI
from fastapi import BackgroundTasks

from study_buddy.models import ChatRequest
from study_buddy.models import ChatResponse

from study_buddy.memory import remember
from study_buddy.memory import recall

from study_buddy.tutor import generate_response


app = FastAPI(
    title="Study Buddy AI"
)


@app.get("/")
async def root():
    return {
        "status": "running"
    }


@app.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    background_tasks: BackgroundTasks
):
    print("STEP 1")

    memory_context = await recall(
        request.message
    )

    print("STEP 2")

    prompt = f"""
You are an expert teacher.

Relevant memory:
{memory_context}

Student Question:
{request.message}

Provide a clear and educational answer.
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

    return ChatResponse(
        response=response
    )
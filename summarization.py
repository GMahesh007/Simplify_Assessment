import openai
from database import chats_collection
from fastapi import FastAPI

app = FastAPI()

openai.api_key = "your_openai_api_key"

async def summarize_chat(conversation_id: str):
    messages = await chats_collection.find({"conversation_id": conversation_id}).to_list(None)
    text = "\n".join([msg["message"] for msg in messages])

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Summarize this conversation:\n{text}"}]
    )
    
    return response["choices"][0]["message"]["content"]

@app.post("/chats/summarize")
async def summarize(conversation_id: str):
    summary = await summarize_chat(conversation_id)
    return {"conversation_id": conversation_id, "summary": summary}

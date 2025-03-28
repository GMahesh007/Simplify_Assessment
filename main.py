from fastapi import FastAPI, HTTPException, Depends
from fastapi import WebSocket
from pydantic import BaseModel
from typing import List
from datetime import datetime
import openai
from database import chats_collection

app = FastAPI()

# Define Pydantic models
class ChatMessage(BaseModel):
    user_id: str
    conversation_id: str
    message: str
    timestamp: datetime = datetime.utcnow()

# Store Chat Messages (Heavy INSERT)
@app.post("/chats")
async def store_chat(chat: ChatMessage):
    chat_dict = chat.dict()
    await chats_collection.insert_one(chat_dict)
    return {"message": "Chat stored successfully"}

# Retrieve Chats (Heavy SELECT)
@app.get("/chats/{conversation_id}", response_model=List[ChatMessage])
async def get_chats(conversation_id: str):
    chats = await chats_collection.find({"conversation_id": conversation_id}).to_list(None)
    return chats

# Delete Chat (Heavy DELETE)
@app.delete("/chats/{conversation_id}")
async def delete_chat(conversation_id: str):
    result = await chats_collection.delete_many({"conversation_id": conversation_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Chat not found")
    return {"message": "Chat deleted successfully"}

@app.get("/users/{user_id}/chats")
async def get_user_chats(user_id: str, page: int = 1, limit: int = 10):
    skips = (page - 1) * limit  # Calculate how many records to skip

    # Get the total count of chats for this user
    total_count = await chats_collection.count_documents({"user_id": user_id})
    total_pages = (total_count // limit) + (1 if total_count % limit != 0 else 0)

    # Fetch only the required number of chats
    chats = await chats_collection.find({"user_id": user_id}).skip(skips).limit(limit).to_list(length=limit)

    return {
        "user_id": user_id,
        "page": page,
        "limit": limit,
        "total_chats": total_count,
        "total_pages": total_pages,
        "chats": chats
    }


@app.get("/chats/insights/{conversation_id}")
async def get_insights(conversation_id: str):
    async def analyze_chat(conversation_id: str):
        # Placeholder logic for analyzing chat
        return {"conversation_id": conversation_id, "insights": "Analysis results"}
    
    insights = await analyze_chat(conversation_id)
    return insights


@app.websocket("/ws/summarize/{conversation_id}")
async def websocket_summary(websocket: WebSocket, conversation_id: str):
    await websocket.accept()
    summary = await summarize_chat(conversation_id)
    async def summarize_chat(conversation_id: str) -> str:
        return f"Summary for conversation {conversation_id}"
    await websocket.send_text(summary)
    await websocket.close()

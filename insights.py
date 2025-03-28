from textblob import TextBlob
from collections import Counter
from motor.motor_asyncio import AsyncIOMotorClient

# Initialize MongoDB client and collection
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["chat_database"]
chats_collection = db["chats"]

async def analyze_chat(conversation_id: str):
    messages = await chats_collection.find({"conversation_id": conversation_id}).to_list(None)
    text = "\n".join([msg["message"] for msg in messages])
    
    sentiment = TextBlob(text).sentiment.polarity
    words = [word for word in text.lower().split() if len(word) > 3]
    common_words = Counter(words).most_common(5)
    
    return {"sentiment_score": sentiment, "top_keywords": common_words}

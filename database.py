from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import IndexModel, ASCENDING

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "chatdb"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
chats_collection = db["chats"]

# Create indexes for optimized queries
async def create_indexes():
    await chats_collection.create_index([("conversation_id", ASCENDING)])

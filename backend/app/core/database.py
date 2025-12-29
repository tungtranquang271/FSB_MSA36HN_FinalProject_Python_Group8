from pymongo import MongoClient
from app.core.config import MONGO_URI, MONGO_DB_NAME

client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]

student_collection = db["students"]

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017") # Connection string for MongoDB Compass

db = client.todo_db

collection_name = db["todo_collection"]
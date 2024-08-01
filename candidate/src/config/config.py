from dotenv import load_dotenv
from pymongo import MongoClient
import os
load_dotenv()

MONGO_URI = os.environ["MONGO_URI"]
ENV = os.environ["ENV"]

print(f"MongoDB URI: {MONGO_URI}")
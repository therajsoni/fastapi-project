import os 
from dotenv import load_dotenv 

load_dotenv()
MONGO_URL = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

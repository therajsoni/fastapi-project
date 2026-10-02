import os 
from dotenv import load_dotenv 

load_dotenv()
MONGO_URL = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
SECRET_TOKEN = os.getenv("SECRET_TOKEN")
ALGORITHM = os.getenv("ALGORITHM")
POSTGRES_URL = os.getenv("POSTGRES_URL")

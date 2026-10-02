from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker , declartive_base 
from app.core.config import POSGRESQL_URL

engine = create_engine(POSGRESQL_URL)
SessionLocal = sessionmaker(
    autoFlush = False , autoCommit = False , bind = engine
)
Base = declartive_base()
def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()
            
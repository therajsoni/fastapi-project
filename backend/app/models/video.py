from sqlalchemy import Column , Integer , String , Text 
from app.core.postgres import Base 

class Video(Base):
    __tablename__ = "videos"
    id = Column(Integer , primary_key=True , index = True)
    title = Column(String(200) , nullable=False)
    description = Column(Text , nullable=True)
    video_url = Column(String , nullable=False)
    
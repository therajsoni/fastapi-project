from fastapi import FastAPI 
from app.routes.health import router as HealthRouter
from app.routes.users import router as UserRouter 
from app.core.postgres import Base , engine
from app.models.video import Video
from app.routes import videos

app = FastAPI()

@app.get("/")
def home():
    return {
        "message" : "DevOpsHUB API is running"
    }

Base.metadata.create_all(bind=engine)
app.include_router(HealthRouter)
app.include_router(UserRouter)
app.include_router(videos.router)
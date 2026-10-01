from fastapi import FastAPI 
from app.routes.health import router as HealthRouter


app = FastAPI()

@app.get("/")
def home():
    return {
        "message" : "DevOpsHUB API is running"
    }

app.include_router(HealthRouter)

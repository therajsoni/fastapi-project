from fastapi import FastAPI 
from app.routes.health import router as HealthRouter
from app.routes.users import router as UserRouter 

app = FastAPI()

@app.get("/")
def home():
    return {
        "message" : "DevOpsHUB API is running"
    }

app.include_router(HealthRouter)
app.include_router(UserRouter)
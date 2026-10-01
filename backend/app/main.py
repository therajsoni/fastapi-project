from fastapi import FastAPI 
app = FastAPI()

@app.get("/")
def home():
    return {
        "message" : "DevOpsHUB API is running"
    }
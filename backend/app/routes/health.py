from fastapi import APIRouter 

router = APIRouter(prefix="/health")

@router.get("/")
def healthCheck():
    return {
        "status" : "App is running"
    }
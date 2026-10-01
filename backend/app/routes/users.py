from fastapi import APIRouter
from app.schemas.users import UserCreate

router = APIRouter(prefix="/users" , tags=["users"])

@router.post("/")
def create_user(user:UserCreate):
    return {
        "username" : user.username , 
        "password" : user.password , 
        "email" : user.email
    }
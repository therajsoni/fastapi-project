from pydantic import BaseModel , EmailStr # EmailStr - need to install email-validator
class UserCreate(BaseModel):
    username: str 
    email: EmailStr
    password: str 

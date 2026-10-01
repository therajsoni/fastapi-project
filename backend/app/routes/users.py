from fastapi import APIRouter
from app.schemas.users import UserCreate , UserUpdate
from app.core.database import db
from bson import ObjectId
 
router = APIRouter(prefix="/users" , tags=["users"])

@router.post("/")
def create_user(user:UserCreate):
    user_data = {
        "username" : user.username , 
        "password" : user.password , 
        "email" : user.email
    }
    result = db.insert_one(user_data)
    return { 
        "message" : "User created" , 
         "success" : True , 
         "id" : str(result.inserted_id) , 
         "data" : result
    }

@router.patch("/{id}")
def update_user(id:ObjectId , user:UserUpdate):
    exist = db.find_one({
        "_id" : id  
    })
    if not exist:
        return {
         "message" : "User Not Found" , 
         "success" : False , 
         "id" : str(id) , 
        }
    data = user.model_dump(exclude_unset=True)    
    result = db.update_one({
        "_id" : id
    } , {
        "$set" : data
    })
    return { 
        "message" : "User updated" , 
         "success" : True , 
         "id" : str(result.inserted_id) , 
         "data" : result, 
         "result" : result.modified_count
    }

@router.delete("/{id}")
def delete_user(id:ObjectId):
    exist = db.find_one({
        "_id" : id  
    })
    if not exist:
        return {
         "message" : "User Not Found" , 
         "success" : False , 
         "id" : str(id) , 
    }
    db.delete_one({
        "_id" : id
    })
    return { 
        "message" : "User deleted" , 
         "success" : True , 
         "id" : str(id) , 
         "data" : exist
    }

@router.get("/{id}")
def get_user_by_id(id:ObjectId):
    exist = db.find_one({
        "_id" : id  
    })
    if not exist:
        return {
         "message" : "User Not Found" , 
         "success" : False , 
         "id" : str(id) , 
    }
    return { 
        "message" : "User Getted Successfully" , 
         "success" : True , 
         "id" : str(id) , 
         "data" : exist
    }

@router.get("/")
def get_users():
    users = db.find({ })
    if len(users) == 0:
        return { 
            "message" : "Users not , Empty List" , 
            "success" : True  , 
            "status" : 204
        }
    return { 
        "message" : "Users Getted Successfully" , 
         "success" : True , 
         "data" : users
    }

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from app.schemas.users import UserCreate , UserUpdate
from app.core.database import db
from bson import ObjectId , json_util
from fastapi.responses import JSONResponse
import json  
def serialize_doc(doc):
    if doc:
        doc["_id"] = str(doc["_id"])
    return doc
def serialize_docs(docs):
    return [serialize_doc(doc) for doc in docs]    

router = APIRouter(prefix="/users" , tags=["users"])

Users = db["users"]

@router.post("/")
def create_user(user:UserCreate):
    user_data = {
        "username" : user.username , 
        "password" : user.password , 
        "email" : user.email
    }
    result = Users.insert_one(user_data)
    return { 
        "message" : "User created" , 
         "success" : True , 
         "id" : str(result.inserted_id) 
    }

@router.patch("/{id}")
def update_user(id:str , user:UserUpdate):
    exist = Users.find_one({
        "_id" : ObjectId(id)  
    })
    if not exist:
        return {
         "message" : "User Not Found" , 
         "success" : False , 
         "id" : str(id) , 
        }
    data = user.model_dump(exclude_unset=True)    
    result = Users.update_one({
        "_id" :  ObjectId(id) 
    } , {
        "$set" : data
    })
    return { 
        "message" : "User updated" , 
         "success" : True , 
         "id" : id , 
         "modified_count" : result.modified_count ,
         "data" : serialize_doc(exist)
    }

@router.delete("/{id}")
def delete_user(id:str):
    exist = Users.find_one({
        "_id" :  ObjectId(id) 
    })
    if not exist:
        return {
         "message" : "User Not Found" , 
         "success" : False , 
         "id" : str(id) , 
    }
    Users.delete_one({
        "_id" :   ObjectId(id) 
    })
    exist["_id"] = str(exist["_id"])
    return { 
        "message" : "User deleted" , 
         "success" : True , 
         "id" : str(id) ,
         "data" : serialize_doc(exist)
    }

@router.get("/{id}")
def get_user_by_id(id:str):
    exist = Users.find_one({
        "_id" :   ObjectId(id) 
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
         "data" : serialize_doc(exist)
    }

@router.get("/")
def get_users():
    users = Users.find({ })
    if int(Users.count_documents({} , limit=1)) == 0:
        return { 
            "message" : "Users not , Empty List" , 
            "success" : True  , 
            "status" : 204
        }
        
    response = { 
        "message" : "Users Getted Successfully" , 
         "success" : True ,
        "data" : serialize_docs(list(users))
    }
    return JSONResponse(content=response)

from fastapi import APIRouter , Depends
from fastapi.encoders import jsonable_encoder
from app.schemas.users import UserCreate , UserUpdate , Login
from app.core.database import db
from app.helpers.serializa import serialize_doc , serialize_docs
from bson import ObjectId , json_util
from fastapi.responses import JSONResponse
from app.helpers.bcrypt import hashPassword , verifyPassword
from app.helpers.token import create_token , bearer_token_verify
import json  

router = APIRouter(prefix="/users" , tags=["users"])

Users = db["users"]

@router.post("/")
def create_user(user:UserCreate):
    user_data = {
        "username" : user.username , 
        "password" : hashPassword(user.password) , 
        "email" : user.email
    }
    result = Users.insert_one(user_data)
    return { 
        "message" : "User created" , 
         "success" : True , 
         "id" : str(result.inserted_id) 
    }

@router.patch("/{id}")
def update_user(id:str , user:UserUpdate,current_user=Depends(bearer_token_verify)):
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
    if user.password:
        data["password"] = hashPassword(user.password)
    result = Users.update_one({
        "_id" :  ObjectId(id) 
    } , {
        "$set" : data
    })
    return { 
        "message" : "User updated" , 
         "success" : True , 
         "id" : id , 
         "modified_count" : result.modified_count 
    }

@router.delete("/{id}")
def delete_user(id:str,current_user=Depends(bearer_token_verify)):
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
def get_user_by_id(id:str,current_user=Depends(bearer_token_verify)):
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
def get_users(current_user=Depends(bearer_token_verify)):
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

@router.post("/login")
def login_user(data: Login):
    exist = Users.find_one({
            "email" : data.email
    })
    if not exist:
      return {
         "message" : "User Not Found" , 
         "success" : False , 
         "id" : str(id) , 
      }
    if not verifyPassword(data.password , exist.password):
       return {
         "message" : "User Password Wrong" , 
         "success" : False , 
         "id" : str(id) , 
    }
    return { 
        "message" : "User Login successfully" , 
        "status" : 200,
        "success" : True ,
        "token" : create_token(exist)
    }



import jwt 
from app.core.config import SECRET_TOKEN , ALGORITHM
from fastapi import Request 
from app.core.serializa import serialize_doc

def create_token(payload):
    token = jwt.encode(serialize_doc(payload) , SECRET_TOKEN , algorithm=str(ALGORITHM))
    return token 

def verify_token(token):
    return jwt.decode(token ,  SECRET_TOKEN , algorithm=ALGORITHM)

def bearer_token_verify(request: Request):
    authorization = request.headers.get("Authorization")
    if not authorization:
        return {
            "status" : 401,
            "detail": "Authorization header required"
        }

    try:
        token = authorization.split(" ")[1]
        verify = verify_token(token)
        if not verify:
           return {
             "detail":"Invalid token" , 
              "success" : False , 
              "status" : 401  
           }
        else:
            return verify  
    except e: 
           return {
             "detail":"Invalid token" , 
              "success" : False , 
              "status" : 401 , 
              "error" : e
           }             
            
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

Phase 1

| Step | Topic                | Video                          |
| ---- | -------------------- | ------------------------------ |
| 1    | FastAPI setup        | Build FastAPI Project          |
| 2    | Project structure    | Professional FastAPI Structure |
| 3    | Routes               | FastAPI Routing                |
| 4    | Pydantic             | Request & Response Validation  |
| 5    | PostgreSQL           | Database Connection            |
| 6    | SQLAlchemy           | ORM                            |
| 7    | Models               | Database Tables                |
| 8    | CRUD                 | Create/Read/Update/Delete      |
| 9    | Dependency Injection | `Depends()`+ DB Session      |
| 10   | Swagger              | API Documentation              |

```
mkdir devopshub
cd devopshub

python3 -m venv venv
source venv/bin/activate

pip install fastapi uvicorn

++++++++++++++++++++++++++++++++++++++++++++++
main.py

from fastapi import FastAPI
app = FastAPI(title="DevOpsHub API")
@app.get("/")
def home():
    return {"message": "DevOpsHub API is running"}

++++++++++++++++++++++++++++++++++++++++++++++

Run 
uvicorn app.main:app --reload --port 8000

++++++++++++++++++++++++++++++++++++++++++++++

http://127.0.0.1:8000/docs
```

```
Pydatic for data validation
Pydantic: Request & Response Validation

pip install email-validator

from pydantic import BaseModel, EmailStr
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

```

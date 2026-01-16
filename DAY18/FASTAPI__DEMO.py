from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr
from typing import Dict

app = FastAPI(title="FastAPI API Demo")

# In-memory database (for demo)
fake_db: Dict[int, dict] = {}

# -------------------
# Pydantic Model
# -------------------
class UserCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    age: int = Field(..., ge=18, le=100)

class UserResponse(UserCreate):
    id: int

# -------------------
# POST Endpoint
# -------------------
@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    user_id = len(fake_db) + 1

    # Business validation
    if any(u["email"] == user.email for u in fake_db.values()):
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    fake_db[user_id] = user.dict()

    return {
        "id": user_id,
        **user.dict()
    }

# -------------------
# GET Endpoint
# -------------------
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    if user_id not in fake_db:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": user_id,
        **fake_db[user_id]
    }

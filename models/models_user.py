from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel, validator
from starlette import status


class AuthUser(BaseModel):
    username: str
    password: str


class RegisterUser(AuthUser):
    email:  Optional[str] = None

    @validator('password')
    def check_password(cls, v):
        if len(v) < 6:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Short password")
        return v


class User(BaseModel):
    id: int
    username: str
    email:  Optional[str] = None


class UserInDb(User):
    hashed_password: str

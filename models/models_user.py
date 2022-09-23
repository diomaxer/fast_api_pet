import datetime
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
    sum: float = 0


class UserFull(User):
    is_admin: bool
    is_stuff: bool
    is_active: bool


class UserInDb(User):
    hashed_password: str


class UserSum(BaseModel):
    value: float = 0

    @validator('value')
    def check_value(cls, v):
        if v < 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Sum can't be negative")
        return round(v, 2)


class Order(BaseModel):
    id: int
    title: str
    price: int
    amount: int
    date: datetime.date

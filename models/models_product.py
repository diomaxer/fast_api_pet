from fastapi import HTTPException
from pydantic import BaseModel, validator
from starlette import status


class ProductBase(BaseModel):
    name: str | None
    price: float | None

    @validator('price')
    def price_mast_be_number(cls, v):
        if len(str(v).split('.')[1]) > 2:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Price can have maximum two decimal places"
            )
        return v


class ProductRegister(BaseModel):
    name: str
    price: float
    user_id: int


class Product(ProductRegister):
    id: int

from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel, validator
from starlette import status


class ProductBase(BaseModel):
    title:  Optional[str]
    price:  Optional[float]
    amount: Optional[int]

    @validator('price')
    def price_mast_be_number(cls, v):
        if len(str(v).split('.')[1]) > 2:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Price can have maximum two decimal places"
            )
        return v

    @validator('amount')
    def amount_check(cls, v):
        if v < 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="amount can't be negative")
        return v


class ProductInfo(BaseModel):
    id: int


class Product(ProductBase, ProductInfo):
    pass


class BuyProduct(BaseModel):
    amount: int

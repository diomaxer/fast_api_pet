from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel, validator
from starlette import status


class ProductBase(BaseModel):
    name:  Optional[str]
    price:  Optional[float]

    @validator('price')
    def price_mast_be_number(cls, v):
        if len(str(v).split('.')[1]) > 2:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Price can have maximum two decimal places"
            )
        return v


class ProductInfo(BaseModel):
    id: int
    user_id: int


class Product(ProductBase, ProductInfo):
    pass

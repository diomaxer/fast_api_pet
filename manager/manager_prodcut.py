from typing import List, Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from models.models_user import User
from service.service_prod import ServiceProduct
from models.models_product import Product, ProductBase


class ProductManager:
    @staticmethod
    async def get_all(skip: int, limit: int, session: Session) -> Optional[List[Product]]:
        products = await ServiceProduct.get_all(skip=skip, limit=limit, session=session)
        if products:
            return [Product(**elem) for elem in products]

    @staticmethod
    async def get_one(product_id: int, session: Session) -> Optional[Product]:
        product = await ServiceProduct.get_one(product_id=product_id, session=session)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product doesn't exist")
        return Product(**product)

    @staticmethod
    async def update(product_id: int, new_product: ProductBase, session: Session):
        product = await ServiceProduct.get_one(product_id=product_id, session=session)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product doesn't exist")
        valid_product = new_product.dict(exclude_defaults=True, exclude_none=True)
        if not valid_product:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="wrong field name")

    @staticmethod
    async def delete(product_id: int, session: Session):
        product = await ServiceProduct.get_one(product_id=product_id, session=session)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product doesn't exist")
        await ServiceProduct.delete(product_id=product_id, session=session)

    @staticmethod
    async def create(product: ProductBase, session: Session):
        new_product = product.dict(exclude_defaults=True, exclude_none=True)
        if set(new_product.keys()) != set(ProductBase.__fields__):
            raise HTTPException(
                status_code=400,
                detail=f'fields: {", " .join(ProductBase.__fields__).upper()} are required'
            )

        error = await ServiceProduct.create(product=product, session=session)
        if error:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product title already exist")

    @staticmethod
    async def buy(product_id: int, amount: int, user: User, session: Session):
        product = await ProductManager.get_one(product_id=product_id, session=session)
        if product.amount < amount:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="so many out of stock")
        if amount * product.price > user.sum:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="not enough money")
        await ServiceProduct.buy(product=product, amount=amount, user_id=user.id, session=session)

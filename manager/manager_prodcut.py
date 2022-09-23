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
    async def update(product_id: int, new_product: ProductBase, user_id: int, session: Session):
        if not await ServiceProduct.is_user_have_product(product_id=product_id, user_id=user_id, session=session):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="Yoy don't have permission to modify this product")
        await ServiceProduct.update(product_id=product_id, new_product=new_product.dict(exclude_defaults=True, exclude_none=True), session=session)

    @staticmethod
    async def delete(product_id: int, user_id: int, session: Session):
        if not await ServiceProduct.is_user_have_product(product_id=product_id, user_id=user_id, session=session):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Yoy don't have permission to modify this product")
        await ServiceProduct.delete(product_id=product_id, session=session)

    @staticmethod
    async def create(product: ProductBase, user_id: int, session: Session):
        new_product = product.dict(exclude_defaults=True, exclude_none=True)
        if set(new_product.keys()) != set(ProductBase.__fields__):
            raise HTTPException(
                status_code=400,
                detail=f'fields: {", " .join(ProductBase.__fields__).upper()} are required'
            )

        await ServiceProduct.create(product=product, user_id=user_id, session=session)

    @staticmethod
    async def buy(product_id: int, amount: int, user_id: int, session: Session):
        await ServiceProduct.buy(product_id=product_id, amount=amount, user_id=user_id, session=session)

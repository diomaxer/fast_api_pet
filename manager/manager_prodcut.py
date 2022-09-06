from typing import List
from fastapi import HTTPException
from starlette import status

from models.models_user import User
from service.service_prod import ServiceProduct
from models.models_product import Product, ProductBase, ProductRegister


class ProductManager:
    @staticmethod
    async def get_all(skip: int, limit: int) -> List[Product] | None:
        products = await ServiceProduct.get_all(skip=skip, limit=limit)
        if products:
            return [Product(**elem) for elem in products]

    @staticmethod
    async def get_one(product_id: int) -> Product | None:
        product = await ServiceProduct.get_one(product_id=product_id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product doesn't exist")
        return Product(**product)

    @staticmethod
    async def update(product_id: int, new_product: ProductBase, user_id: int):
        if not await ServiceProduct.is_user_have_product(product_id=product_id, user_id=user_id):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="Yoy don't have permission to modify this product")
        await ServiceProduct.update(product_id=product_id, new_product=new_product.dict(exclude_defaults=True, exclude_none=True))

    @staticmethod
    async def delete(product_id: int, user_id: int):
        if not await ServiceProduct.is_user_have_product(product_id=product_id, user_id=user_id):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Yoy don't have permission to modify this product")
        await ServiceProduct.delete(product_id=product_id)

    @staticmethod
    async def create(product: ProductBase, user: User):
        new_product = product.dict(exclude_defaults=True, exclude_none=True)
        if set(new_product.keys()) != set(ProductBase.__fields__):
            raise HTTPException(
                status_code=400,
                detail=f'fields: {", " .join(ProductBase.__fields__).upper()} are required'
            )

        await ServiceProduct.create(product=ProductRegister(**product.__dict__, user_id=user.id))

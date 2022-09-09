from typing import List, Optional

from fastapi import APIRouter, Depends

from manager.manager_token import get_current_user
from models.models_product import Product, ProductBase
from models.models_user import User
from manager.manager_prodcut import ProductManager

router = APIRouter()


@router.get('/', response_model=Optional[List[Product]])
async def get_products(skip: int = 0, limit: int = 100):
    return await ProductManager.get_all(skip=skip, limit=limit)


@router.get('/{product_id}', response_model=Optional[Product])
async def get_one_product(product_id: int = 0):
    return await ProductManager.get_one(product_id=product_id)


@router.post('/create/', response_model=None)
async def create_product(product: ProductBase, user: User = Depends(get_current_user)):
    return await ProductManager.create(product=product, user_id=user.id)


@router.put('/{product_id}', response_model=Optional[Product])
async def update_product(product_id: int, new_product: ProductBase, user: User = Depends(get_current_user)):
    return await ProductManager.update(product_id=product_id, new_product=new_product, user_id=user.id)


@router.delete('/{product_id}', response_model = None)
async def delete_product(product_id: int,  user: User = Depends(get_current_user)):
    return await ProductManager.delete(product_id=product_id, user_id=user.id)

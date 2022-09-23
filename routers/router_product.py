from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from manager.manager_token import get_current_user
from models.models_product import Product, ProductBase, BuyProduct
from models.models_user import User
from manager.manager_prodcut import ProductManager

router = APIRouter()


@router.get('/', response_model=Optional[List[Product]])
async def get_products(skip: int = 0, limit: int = 100, session: Session = Depends(get_db)):
    return await ProductManager.get_all(skip=skip, limit=limit, session=session)


@router.get('/{product_id}', response_model=Optional[Product])
async def get_one_product(product_id: int = 0, session: Session = Depends(get_db)):
    return await ProductManager.get_one(product_id=product_id, session=session)


@router.post('/create/', response_model=None)
async def create_product(product: ProductBase, user: User = Depends(get_current_user), session: Session = Depends(get_db)):
    return await ProductManager.create(product=product, user_id=user.id, session=session)


@router.put('/{product_id}', response_model=Optional[Product])
async def update_product(product_id: int, new_product: ProductBase, user: User = Depends(get_current_user), session: Session = Depends(get_db)):
    return await ProductManager.update(product_id=product_id, new_product=new_product, user_id=user.id, session=session)


@router.delete('/{product_id}', response_model=None)
async def delete_product(product_id: int,  user: User = Depends(get_current_user), session: Session = Depends(get_db)):
    return await ProductManager.delete(product_id=product_id, user_id=user.id, session=session)


@router.post('/{product_id}', response_model=None)
async def buy(product_id: int, buy: BuyProduct, user: User = Depends(get_current_user), session: Session = Depends(get_db)):
    return await ProductManager.buy(product_id=product_id, amount=buy.amount, user_id=user.id, session=session)
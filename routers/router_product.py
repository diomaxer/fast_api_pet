from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from manager.manager_token import get_admin_user
from models.models_product import Product, BuyProduct
from models.models_user import User
from manager.manager_prodcut import ProductManager

router = APIRouter()


@router.get('/', response_model=Optional[List[Product]])
async def get_products(skip: int = 0, limit: int = 100, session: Session = Depends(get_db)):
    return await ProductManager.get_all(skip=skip, limit=limit, session=session)


@router.get('/{product_id}', response_model=Optional[Product])
async def get_one_product(product_id: int = 0, session: Session = Depends(get_db)):
    return await ProductManager.get_one(product_id=product_id, session=session)


@router.post('/{product_id}', response_model=None)
async def buy(product_id: int, buy: BuyProduct, user: User = Depends(get_admin_user), session: Session = Depends(get_db)):
    return await ProductManager.buy(product_id=product_id, amount=buy.amount, user_id=user.id, session=session)


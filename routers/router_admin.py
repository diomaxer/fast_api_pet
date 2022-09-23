from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from manager.manager_prodcut import ProductManager
from manager.manager_token import get_admin_user
from models.models_product import ProductBase, Product
from models.models_user import User

router = APIRouter()


@router.post('/create/', response_model=None)
async def create_product(product: ProductBase, user: User = Depends(get_admin_user), session: Session = Depends(get_db)):
    return await ProductManager.create(product=product, user_id=user.id, session=session)


@router.put('/{product_id}', response_model=Optional[Product])
async def update_product(product_id: int, new_product: ProductBase, user: User = Depends(get_admin_user), session: Session = Depends(get_db)):
    return await ProductManager.update(product_id=product_id, new_product=new_product, user_id=user.id, session=session)


@router.delete('/{product_id}', response_model=None)
async def delete_product(product_id: int,  user: User = Depends(get_admin_user), session: Session = Depends(get_db)):
    return await ProductManager.delete(product_id=product_id, user_id=user.id, session=session)

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database.db import get_db
from manager.manager_token import get_current_user
from manager.manager_user import UserManager
from models.models_user import User, RegisterUser, UserSum

router = APIRouter()


@router.post(
    path='/register',
    description='Register new user',
    status_code=status.HTTP_200_OK,
)
async def register(new_user: RegisterUser, session: Session = Depends(get_db)):
    return await UserManager.create_user(new_user=new_user, session=session)


@router.post(
    path='/token',
    description='Authenticate',
    status_code=status.HTTP_200_OK
)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_db)):
    return await UserManager.auth_user(form_data=form_data, session=session)


@router.get(
    path='/info',
    description='Users information',
    response_model=User,
    status_code=status.HTTP_200_OK
)
async def user_info(user: User = Depends(get_current_user), session: Session = Depends(get_db)):
    return await UserManager.get_user(username=user.username, session=session)


@router.delete(
    path='/info',
    description='Delete account',
    status_code=status.HTTP_200_OK
)
async def delete_user(user: User = Depends(get_current_user), session: Session = Depends(get_db)):
    return await UserManager.delete_user(user=user, session=session)


@router.post(
    path='/top_up',
    description='Top up your account',
    status_code=status.HTTP_200_OK,
)
async def top_up_money(user_sum: UserSum, user: User = Depends(get_current_user), session: Session = Depends(get_db)):
    return await UserManager.top_up(user_id=user.id, value=user_sum.value, session=session)


@router.get(
    path='/orders',
    description='User orders',
    status_code=status.HTTP_200_OK
)
async def user_orders(user: User = Depends(get_current_user), session: Session = Depends(get_db)):
    return await UserManager.user_orders(user_id=user.id, session=session)

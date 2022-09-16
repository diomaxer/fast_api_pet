from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from manager.manager_token import get_current_user
from manager.manager_user import UserManager
from models.models_user import User, RegisterUser, UserSum

router = APIRouter()


@router.post(
    path='/register',
    description='Register new user',
    status_code=status.HTTP_200_OK,
)
async def register(new_user: RegisterUser):
    return await UserManager.create_user(new_user=new_user)


@router.post(
    path='/token',
    description='Authenticate',
    status_code=status.HTTP_200_OK
)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return await UserManager.auth_user(form_data=form_data)


@router.get(
    path='/info',
    description='Users information',
    status_code=status.HTTP_200_OK
)
async def user_info(user: User = Depends(get_current_user)):
    return await UserManager.get_user(username=user.username)


@router.post(
    path='/top_up',
    description='Top up your account',
    status_code=status.HTTP_200_OK,
)
async def top_up(user_sum: UserSum, user: User = Depends(get_current_user)):
    return await UserManager.top_up(user_id=user.id, value=user_sum.value)

# @router.get(
#     path='/orders',
#     description='Users orders',
#     status_code=status.HTTP_200_OK
# )
# async def user_orders(user: User = Depends(get_current_user)):
#     return await UserManager.user_orders(user_id=user.id)

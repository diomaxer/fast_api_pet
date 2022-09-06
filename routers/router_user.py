from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from manager.manager_user import UserManager
from models.models_user import User, RegisterUser, AuthUser

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
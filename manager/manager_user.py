from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from hash_data import get_password_hash, verify_password
from manager.manager_token import *
from models.models_user import RegisterUser, User, Order
from service.service_user import UserService


class UserManager:
    @staticmethod
    async def auth_user(session: Session, form_data: OAuth2PasswordRequestForm = Depends()):
        user = await UserService.get_user(username=form_data.username, session=session)
        if not user or not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=AuthConfig.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = await create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}

    @staticmethod
    async def create_user(new_user: RegisterUser, session: Session):
        new_user.password = get_password_hash(new_user.password)
        user = await UserService.get_user(username=new_user.username, email=new_user.email, session=session)
        if not user:
            await UserService.create_user(new_user=new_user, session=session)
        elif len(user) == 2:
            raise HTTPException(status_code=400, detail="Username and email already registered")
        elif len(user) == 1:
            if user[0].username == new_user.username:
                raise HTTPException(status_code=400, detail="Username already registered")
            else:
                raise HTTPException(status_code=400, detail="Email already registered")

    @staticmethod
    async def get_user(username: str, session: Session):
        user = await UserService.get_user(username=username, session=session)
        return User(**user)

    @staticmethod
    async def delete_user(user: User, session: Session):
        await UserService.delete_user(user_id=user.id, session=session)

    @staticmethod
    async def top_up(user_id: int, value: float, session: Session):
        await UserService.top_up(user_id=user_id, value=value, session=session)

    # @staticmethod
    # async def user_orders(user_id: int):
    #     orders = await UserService.get_user_orders(user_id=user_id)
    #     return [Order(**elem) for elem in orders]
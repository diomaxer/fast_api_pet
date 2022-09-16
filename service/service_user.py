from typing import Optional

from sqlalchemy import select, insert, or_, update

from database.db import engine
from database.tables import user_table, order_table
from models.models_user import RegisterUser


class UserService:
    @staticmethod
    async def get_user(username: str, email:  Optional[str] = None):
        with engine.connect() as conn:
            query = select(user_table).where(
                user_table.c.username == username
            )
            if email:
                query = select(user_table).where(
                    or_(
                        user_table.c.username == username,
                        user_table.c.email == email
                    )
                )
            result = conn.execute(query).first()
            return result

    @staticmethod
    async def create_user(new_user: RegisterUser):
        with engine.connect() as conn:
            query = insert(user_table).values(
                username=new_user.username,
                hashed_password=new_user.password,
                email=new_user.email,
                is_active=False,
                sum=2000
            )
            conn.execute(query)

    @staticmethod
    async def top_up(user_id: int, value: float):
        with engine.connect() as conn:
            query = update(user_table).values(sum=user_table.sum + value).where(user_table.c.id == user_id)
            conn.execute(query)

    # @staticmethod
    # async def get_user_orders(user_id: int):
    #     with engine.connect() as conn:
    #         query = select(order_table).where(order_table.c.user_id == user_id)
    #         result = conn.execute(query)
    #         return result

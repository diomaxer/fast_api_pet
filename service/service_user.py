from typing import Optional

from sqlalchemy import select, insert, or_

from database.db import engine
from database.tables import users_tables
from models.models_user import RegisterUser


class UserService:
    @staticmethod
    async def get_user(username: str, email:  Optional[str] = None):
        with engine.connect() as conn:
            query = select(users_tables).where(
                users_tables.c.username == username
            )
            if email:
                query = select(users_tables).where(
                    or_(
                        users_tables.c.username == username,
                        users_tables.c.email == email
                    )
                )
            result = conn.execute(query).first()
            return result

    @staticmethod
    async def create_user(new_user: RegisterUser):
        with engine.connect() as conn:
            query = insert(users_tables).values(
                username=new_user.username,
                hashed_password=new_user.password,
                email=new_user.email,
                is_active=False
            )
            conn.execute(query)

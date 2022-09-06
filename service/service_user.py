from sqlalchemy import select, insert, or_
from database.db import database as db
from database.tables import users_tables
from models.models_user import RegisterUser


class UserService:
    @staticmethod
    async def get_user(username: str, email: str | None = None):
        query = select(users_tables).where(
            users_tables.c.username == username
        )
        result = await db.fetch_one(query)
        if email:
            query = select(users_tables).where(
                or_(
                    users_tables.c.username==username,
                    users_tables.c.email==email
                )
            )
            result = await db.fetch_all(query)
        return result

    @staticmethod
    async def create_user(new_user: RegisterUser):
        query = insert(users_tables).values(
            username=new_user.username,
            hashed_password=new_user.password,
            email=new_user.email,
            is_active=False
        )
        await db.execute(query)



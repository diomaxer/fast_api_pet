from typing import Optional
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, insert, or_, delete
from sqlalchemy.orm import Session

from database.tables import user_table
from models.models_user import RegisterUser


class UserService:
    @staticmethod
    async def get_user(username: str, session: Session, email:  Optional[str] = None):
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
        return session.execute(query).first()

    @staticmethod
    async def create_user(new_user: RegisterUser, session: Session):
            query = insert(user_table).values(
                username=new_user.username,
                hashed_password=new_user.password,
                email=new_user.email,
                sum=2000
            )
            try:
                session.execute(query)
                session.commit()
            except IntegrityError as e:
                session.rollback()
                error = str(e.__dict__['orig'])
                if 'users_username_key' in error:
                    return 'username'
                elif 'users_email_key' in error:
                    return 'email'





    @staticmethod
    async def top_up(user_id: int, value: float, session: Session):
        session.query(user_table).where(user_table.c.id == user_id).update(
            {user_table.c.sum: user_table.c.sum + value}
        )
        session.commit()


    @staticmethod
    async def delete_user(user_id: int, session: Session):
        query = delete(user_table).where(user_table.c.id == user_id)
        session.execute(query)
        session.commit()

    # @staticmethod
    # async def get_user_orders(user_id: int):
    #     with engine.connect() as conn:
    #         query = select(order_table).where(order_table.c.user_id == user_id)
    #         result = conn.execute(query)
    #         return result

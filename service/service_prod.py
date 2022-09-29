import datetime

from sqlalchemy import insert, delete, update
from sqlalchemy.exc import IntegrityError
from database.db import engine
from database.tables import product_table, user_table, order_table
from models.models_product import ProductBase
from sqlalchemy.orm import Session

# from database.tables import Product


class ServiceProduct:
    @staticmethod
    async def get_all(skip: int, limit: int, session: Session):
        return session.query(product_table).offset(skip).limit(limit).all()

    @staticmethod
    async def get_one(product_id: int, session: Session):
        return session.query(product_table).where(product_table.c.id == product_id).first()

    @staticmethod
    async def create(product: ProductBase, session: Session):
        query = insert(product_table).values(**product.__dict__)
        try:
            session.execute(query)
            session.commit()
        except IntegrityError as e:
            return 'title'


    @staticmethod
    async def delete(product_id: int, session: Session):
        query = delete(product_table).where(product_table.c.id == product_id)
        session.execute(query)
        session.commit()

    @staticmethod
    async def update(product_id: int, new_product: dict, session: Session):
        session.query(
            product_table
        ).where(
            product_table.c.id == product_id
        ).update(new_product)
        session.commit()

    @staticmethod
    async def buy(product_id: int, amount: int, user_id: int, session: Session):
        with engine.connect() as conn:
            # Вычесть из product
            session.query(product_table).where(
                product_table.c.id==product_id
            ).update(
                {product_table.c.amount: product_table.c.amount - amount}
            )
            # Вычесть из user.sum

            # user_query = update(user_table).values(sum=user_table.sum - )
            # Добавить order
            order_query = insert(order_table).values(
                product_id=product_id,
                amount=amount,
                date=datetime.date.today()
            )
            # conn.execute(product_query)
            # conn.execute(order_query)


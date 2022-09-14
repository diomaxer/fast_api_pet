from sqlalchemy import select, insert, delete, update

from database.db import engine
from database.tables import product_table
from models.models_product import ProductBase


class ServiceProduct:
    @staticmethod
    async def get_all(skip: int, limit: int):
        with engine.connect() as conn:
            query = select(product_table).offset(skip).limit(limit)
            return conn.execute(query)

    @staticmethod
    async def get_one(product_id: int):
        with engine.connect() as conn:
            query = select(product_table).where(product_table.c.id == product_id)
            return conn.execute(query).first()

    @staticmethod
    async def create(product: ProductBase, user_id: int):
        with engine.connect() as conn:
            product_dict = product.__dict__
            product_dict['user_id'] = user_id
            query = insert(product_table).values(**product_dict)
            conn.execute(query)

    @staticmethod
    async def is_user_have_product(product_id: int, user_id: int):
        with engine.connect() as conn:
            query = select(product_table).where(
                product_table.c.id == product_id,
                product_table.c.user_id == user_id
            )
            return conn.execute(query).first()

    @staticmethod
    async def delete(product_id: int):
        with engine.connect() as conn:
            query = delete(product_table).where(
                product_table.c.id == product_id
            )
            conn.execute(query)

    @staticmethod
    async def update(product_id: int, new_product: dict):
        with engine.connect() as conn:
            query = update(product_table).where(
                product_table.c.id == product_id
            ).values(
                new_product
            )
            conn.execute(query)

from typing import List

from sqlalchemy import select, insert, delete, update

from database.tables import product_table
from database.db import database as db
from models.models_product import ProductBase


class ServiceProduct:
    @staticmethod
    async def get_all(skip: int, limit: int):
        query = select(product_table).offset(skip).limit(limit)
        return await db.fetch_all(query)

    @staticmethod
    async def get_one(product_id: int):
        query = select(product_table).where(product_table.c.id == product_id)
        return await db.fetch_one(query)

    @staticmethod
    async def create(product: ProductBase, user_id: int):
        product_dict = product.__dict__
        product_dict['user_id'] = user_id
        query = insert(product_table).values(**product_dict)
        await db.execute(query)

    @staticmethod
    async def is_user_have_product(product_id: int, user_id: int):
        query = select(product_table).where(
            product_table.c.id == product_id,
            product_table.c.user_id == user_id
        )
        return await db.fetch_one(query)

    @staticmethod
    async def delete(product_id: int):
        query = delete(product_table).where(
            product_table.c.id == product_id
        )
        await db.execute(query)

    @staticmethod
    async def update(product_id: int, new_product: dict):
        query = update(product_table).where(
            product_table.c.id == product_id
        ).values(
            new_product
        )
        await db.execute(query)
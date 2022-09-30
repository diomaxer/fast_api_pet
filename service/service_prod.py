from sqlalchemy import insert, delete
from sqlalchemy.exc import IntegrityError
from database.tables import product_table, user_table, order_table
from models.models_product import ProductBase, Product
from sqlalchemy.orm import Session


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
    async def buy(product: Product, amount: int, user_id: int, session: Session):
        try:
            # subtract the amount product
            session.query(product_table).where(
                product_table.c.id == product.id
            ).update(
                {
                    product_table.c.amount: product_table.c.amount - amount
                }
            )
            # subtract the sum from user
            session.query(user_table).where(
                user_table.c.id == user_id
            ).update(
                {
                    user_table.c.sum: user_table.c.sum - amount * product.price,

                }
            )
            # create order
            create_order_stmt = insert(order_table).values(
                {
                    'product_id': product.id,
                    'user_id': user_id,
                    'amount': amount,
                    'price': amount * product.price
                }
            )
            session.execute(create_order_stmt)
            session.commit()

        except Exception as e:
            print(e)
            session.rollback()

from sqlalchemy import Table, Column, Integer, String, Float, Boolean, ForeignKey, Date

from database.db import new_metadata


user_table = Table(
    'users',
    new_metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('username', String(30), unique=True, nullable=False),
    Column('email', String(80), unique=True),
    Column('hashed_password', String(100), nullable=False),
    Column('sum', Float, default=0, nullable=False),
    Column('is_stuff', Boolean, default=False, nullable=False),
    Column('is_admin', Boolean, default=False, nullable=False),
    Column('is_active', Boolean, default=False, nullable=False)
)

product_table = Table(
    'product',
    new_metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', Integer, ForeignKey('users.id'), nullable=False),
    Column('name', String(50), unique=True),
    Column('price', Float),
    Column('amount', Integer, default=0)
)

order_table = Table(
    'orders',
    new_metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('product_id', Integer, ForeignKey('product.id'), nullable=False),
    Column('amount', Integer, default=1),
    Column('date', Date)
)

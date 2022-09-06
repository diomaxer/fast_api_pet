from sqlalchemy import Table, Column, Integer, String, Float, Boolean, ForeignKey

from database.db import metadata


users_tables = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('username', String(30), unique=True, nullable=False),
    Column('email', String(80), unique=True),
    Column('hashed_password', String(100), nullable=False),
    Column('is_active', Boolean, default=False, nullable=False)
)

product_table = Table(
    'product',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', Integer, ForeignKey('users.id'), nullable=False),
    Column('name', String(50)),
    Column('price', Float)
)

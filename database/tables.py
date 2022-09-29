from sqlalchemy import Table, Column, Integer, String, Float, Boolean, ForeignKey, \
    DateTime, Date, func
from sqlalchemy.orm import relationship

from database.db import new_metadata, Base


user_table = Table(
    'users',
    new_metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('username', String(30), unique=True, nullable=False),
    Column('email', String(80), unique=True),
    Column('hashed_password', String(100), nullable=False),
    Column('sum', Float, nullable=False),
    Column('is_stuff', Boolean, default=False, nullable=False),
    Column('is_admin', Boolean, default=False, nullable=False),
    Column('is_active', Boolean, default=False, nullable=False)
)


product_table = Table(
    'product',
    new_metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(50), unique=True),
    Column('price', Float),
    Column('amount', Integer)
)


order_table = Table(
    'orders',
    new_metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('product_id', Integer, ForeignKey('product.id'), nullable=True),
    Column('user_id', Integer, ForeignKey('users.id'), nullable=False),
    Column('amount', Integer),
    Column('date', DateTime, server_default=func.now())
)


# class Users(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     username = Column(String(30), unique=True, nullable=False)
#     email = Column(String(80), unique=True)
#     hashed_password = Column(String(100), nullable=False)
#     sum = Column(Float, nullable=False)
#     is_stuff = Column(Boolean, nullable=False)
#     is_admin = Column(Boolean, nullable=False)
#     is_active = Column(Boolean, nullable=False)
#
#     orders = relationship('Orders', back_populates='users')
#
#
# class Product(Base):
#     __tablename__ = 'product'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), unique=True)
#     price = Column(Float)
#     amount = Column(Integer)
#
#     orders = relationship('Orders', back_populates='product')
#
#
# class Orders(Base):
#     __tablename__ ='orders'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     product_id = Column(Integer, ForeignKey('product.id'))
#     amount = Column(Integer)
#     created_at = Column(DateTime, nullable=False, server_default=func.now())
#
#     users = relationship('Users', back_populates='orders')
#     product = relationship('Product', back_populates='orders')

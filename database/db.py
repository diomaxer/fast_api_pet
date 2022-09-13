import databases

from config import DatabaseConfig
from sqlalchemy import create_engine, MetaData

engine = create_engine(DatabaseConfig.DB_URL)
metadata = MetaData()

database = databases.Database(DatabaseConfig.DB_URL)

import databases

from config import HerokuConfig
from sqlalchemy import create_engine, MetaData

engine = create_engine(HerokuConfig.DATABASE_URL)
metadata = MetaData()

database = databases.Database(HerokuConfig.DATABASE_URL)

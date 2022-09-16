from config import HerokuConfig
from sqlalchemy import create_engine, MetaData

engine = create_engine(HerokuConfig.DATABASE_URL)

new_metadata = MetaData()

from config import HerokuConfig
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(HerokuConfig.DATABASE_URL)
Session = sessionmaker(engine)

Base = declarative_base()
new_metadata = MetaData()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


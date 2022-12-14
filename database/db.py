from config import HerokuConfig
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine(HerokuConfig.DATABASE_URL)
Session = sessionmaker(engine)

new_metadata = MetaData()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


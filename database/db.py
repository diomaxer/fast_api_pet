import os

import dotenv
import databases
from sqlalchemy import create_engine, MetaData

dotenv.load_dotenv()

SQL_URL = os.getenv('SQL_URL')

engine = create_engine(SQL_URL)
metadata = MetaData()

database = databases.Database(SQL_URL)

import os
import dotenv


dotenv.load_dotenv()


class DatabaseConfig(object):
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT") if os.getenv("DB_PORT") is not None else "5432"
    DB_NAME = os.getenv("DB_NAME")

    DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

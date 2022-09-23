import os
# import dotenv


# dotenv.load_dotenv()

class HerokuConfig:
    DATABASE_URL = os.getenv("DATABASE_URL")
    # DATABASE_URL = os.getenv("DATABASE_URL2")


class AuthConfig:
    ACCESS_TOKEN_EXPIRE_MINUTES = 600
    ALGORITHM = "HS256"
    SECRET_KEY = os.getenv("JWT_SECRET_KEY")

# class DatabaseConfig:
#     DB_USER = os.getenv("DB_USER")
#     DB_PASSWORD = os.getenv("DB_PASSWORD")
#     DB_HOST = os.getenv("DB_HOST")
#     DB_PORT = os.getenv("DB_PORT") if os.getenv("DB_PORT") is not None else "5432"
#     DB_NAME = os.getenv("DB_NAME")
#
#     DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

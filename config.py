import os


class HerokuConfig:
    DATABASE_URL = os.getenv("DATABASE_URL").replace('postgres', 'postgresql')


class AuthConfig:
    ACCESS_TOKEN_EXPIRE_MINUTES = 600
    ALGORITHM = "HS256"
    SECRET_KEY = os.getenv("JWT_SECRET_KEY")

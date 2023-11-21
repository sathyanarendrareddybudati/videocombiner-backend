import os
from dotenv import load_dotenv
from datetime import timedelta
from pydantic_settings import BaseSettings
from typing import ClassVar


load_dotenv('.env')

class Settings(BaseSettings):

    DEBUG: str = os.getenv('DEBUG', False)
    WEB_API_KEY: str = os.getenv('WEB_API_KEY')
    MASTER_DB_NAME: str = os.getenv('MASTER_DB_NAME')
    MASTER_DB_USER: str = os.getenv('MASTER_DB_USER')
    MASTER_DB_PASSWORD: str = os.getenv('MASTER_DB_PASSWORD')
    MASTER_DB_HOST: str = os.getenv('MASTER_DB_HOST')
    DB_URL: str = f"mysql://{MASTER_DB_USER}:{MASTER_DB_PASSWORD}@{MASTER_DB_HOST}/{MASTER_DB_NAME}"
    CORS_ORIGINS: ClassVar[list] = ['http://localhost:3000']

settings = Settings()
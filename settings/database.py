from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings.base import settings
from typing import Any


db_url = settings.DB_URL

engine = create_engine(
    db_url
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_database_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

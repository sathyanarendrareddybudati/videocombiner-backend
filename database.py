from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings.base import MASTER_DB_HOST, MASTER_DB_NAME, MASTER_DB_PASSWORD, MASTER_DB_USER


db_url = f"mysql://{MASTER_DB_USER}:{MASTER_DB_PASSWORD}@{MASTER_DB_HOST}/{MASTER_DB_NAME}"

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
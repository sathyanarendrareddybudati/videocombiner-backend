# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base, as_declarative, declared_attr
# from sqlalchemy.orm import sessionmaker
# from settings.base import settings
# from typing import Any


# db_url = settings.DB_URL

# engine = create_engine(
#     db_url
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# def get_database_session():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @as_declarative()
# class Base:
#     id: Any
#     __name__: str

#     # Generate __tablename__ automatically
#     @declared_attr
#     def __tablename__(cls) -> str:
#         return cls.__name__.lower()
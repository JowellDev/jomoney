from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import Config


SQLALCHEMY_DB_URL = Config.DB_CONNECTION
engine = create_engine(SQLALCHEMY_DB_URL)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    try:
        db = sessionLocal()
        yield db
    finally:
        db.close()
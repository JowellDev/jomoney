from fastapi import FastAPI
from db.base import Base
from db.session import engine
from core.config import Config

def create_tables():
    Base.metadata.create_all(bind=engine)


def run_app():
    app = FastAPI(title=Config.APP_TITLE, version=Config.APP_VERSION)
    create_tables()
    return app

app = run_app()
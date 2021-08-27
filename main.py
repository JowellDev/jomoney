from fastapi import FastAPI
from db.base import Base
from db.session import engine
from core.config import Config
from api.base import api_router

def create_tables():
    Base.metadata.create_all(bind=engine)

def include_router(app):
    app.include_router(api_router)



def run_app():
    app = FastAPI(title=Config.APP_TITLE, version=Config.APP_VERSION)
    create_tables()
    include_router(app)
    return app

app = run_app()
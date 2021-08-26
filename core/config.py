import os
from pathlib import Path
from dotenv import load_dotenv


env_path: str = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Config:
    APP_TITLE: str = os.getenv("APP_NAME")
    APP_VERSION: str = os.getenv("APP_VERSION")
    HOST: str = os.getenv("HOST")
    PORT: int = os.getenv("PORT")

    #db
    DB_NAME: str = os.getenv("DB_NAME")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_CONNECTION: str = os.getenv("DB_CONNECTION")
    DB_URL: str = f"{DB_CONNECTION}//:{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
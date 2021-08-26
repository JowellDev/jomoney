from fastapi import FastAPI


from core.config import Config


app = FastAPI(title=Config.APP_TITLE, version=Config.APP_VERSION)

@app.get('/')
def home():
    return {"message": "Hello world !"}
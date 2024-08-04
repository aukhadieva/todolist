from fastapi import FastAPI

from starlette.templating import Jinja2Templates

import models
from database import SessionLocal, engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory='templates')


def get_db():
    """
    Создает и возвращает экземпляр сессии базы данных.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

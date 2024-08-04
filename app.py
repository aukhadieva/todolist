from fastapi import FastAPI, Request, Depends

from sqlalchemy.orm import Session
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


@app.get('/')
def home(request: Request, db: Session = Depends(get_db)):
    """
    Отображение главной страницы с списком всех TODO-задач.

    :param request: экземпляр запроса (типа Request)
    :param db: экземпляр сессии базы данных (типа Session)
    :return: страница с HTML-шаблоном и данными TODO-задач
    """
    todos = db.query(models.Todo).all()
    return templates.TemplateResponse('base.html',
                                      {'request': request, 'todo_list': todos})

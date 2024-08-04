from fastapi import FastAPI, Request, Depends, Form, status, HTTPException

from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
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
    tasks = db.query(models.Todo).all()
    return templates.TemplateResponse('base.html',
                                      {'request': request, 'todo_list': tasks})


@app.post('/add')
def add_task(request: Request, title: str = Form(...), db: Session = Depends(get_db)):
    """
    Добавление новой TODO-задачи.

    :param request: экземпляр запроса (типа Request)
    :param title: заголовок новой TODO-задачи (типа str)
    :param db: экземпляр сессии базы данных (типа Session)
    :return: перенаправление на главную страницу
    """
    task = models.Todo(title=title)
    db.add(task)
    db.commit()

    url = app.url_path_for('home')
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)

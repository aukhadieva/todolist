from fastapi import FastAPI
from starlette.templating import Jinja2Templates

import models
from database import engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory='templates')

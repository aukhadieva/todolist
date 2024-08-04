from database import Base
from sqlalchemy import Column, Integer, String, Boolean


class Todo(Base):
    """
    Модель для описания TODO-задачи.
    """
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    complete = Column(Boolean, default=False)

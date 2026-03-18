from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from core.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(14), unique=True, nullable=False)
    priority = Column(String(10), nullable=False)
    description = Column(String(100), unique=True, nullable=False)
    deadline = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

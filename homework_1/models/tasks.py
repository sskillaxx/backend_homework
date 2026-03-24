from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from core.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(14), unique=True, nullable=False)
    priority = Column(String(10), nullable=False)
    description = Column(String(100), unique=True, nullable=False)
    deadline = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    comments = relationship("Comment", back_populates="task", cascade="all, delete-orphan")
    
class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False, index=True)
    text = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    task = relationship("Task", back_populates="comments")
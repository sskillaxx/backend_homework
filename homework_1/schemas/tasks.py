from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class BaseTask(BaseModel):
    name: str = Field(min_length=2, max_length=14)
    priority: Literal["low", "middle", "high"]
    description: str = Field(min_length=1, max_length=100)

class CreateTask(BaseTask):
    deadline: datetime

class EditTask(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=14)
    priority: Literal["low", "middle", "high"] | None = None
    description: str | None = Field(default=None, min_length=1, max_length=100)
    deadline: datetime | None = None

class TaskResponse(BaseTask):
    id: int
    deadline: datetime
    model_config = ConfigDict(from_attributes=True)

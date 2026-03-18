from sqlalchemy.orm import Session

from models.tasks import Task
from schemas.tasks import CreateTask, EditTask

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_tasks(self) -> list[Task]:
        return self.db.query(Task).all()

    def get_task_by_id(self, task_id: int) -> Task | None:
        return self.db.query(Task).filter(Task.id == task_id).first()

    def create_task(self, new_task: CreateTask) -> Task:
        task = Task(**new_task.model_dump())
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def update_task(self, task_id: int, edited_task: EditTask) -> Task | None:
        task = self.get_task_by_id(task_id)
        if task is None:
            return None

        for field, value in edited_task.model_dump(exclude_unset=True).items():
            setattr(task, field, value)

        self.db.commit()
        self.db.refresh(task)
        return task

    def delete_task(self, task_id: int) -> bool:
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        self.db.delete(task)
        self.db.commit()
        return True
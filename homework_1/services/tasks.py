from repositories import TaskRepository
from schemas import CreateTask, EditTask


class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def get_all_tasks(self):
        return self.repository.get_all_tasks()

    def add_task(self, new_task: CreateTask):
        return self.repository.create_task(new_task)

    def edit_task(self, task_id: int, edited_task: EditTask):
        return self.repository.update_task(task_id, edited_task)

    def delete_task(self, task_id: int):
        return self.repository.delete_task(task_id)

from repositories import TaskRepository
from schemas import CreateTask, EditTask, CreateComment

from exceptions import TaskNotFound

class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def get_all_tasks(self):
        return self.repository.get_all_tasks()

    def create_task(self, new_task: CreateTask):
        return self.repository.create_task(new_task)

    def edit_task(self, task_id: int, edited_task: EditTask):
        task = self.repository.update_task(task_id, edited_task)
        if task is None:
            raise TaskNotFound(task_id)
        return task

    def delete_task(self, task_id: int):
        deleted = self.repository.delete_task(task_id)
        if not deleted:
            raise TaskNotFound(task_id)
        return True
    
    def create_comment(self, task_id: int, new_comment: CreateComment):
        task = self.repository.get_task_by_id(task_id)
        if task is None:
            raise TaskNotFound(task_id)
        return self.repository.create_comment(task_id, new_comment)

    def get_task_comments(self, task_id: int):
        task = self.repository.get_task_by_id(task_id)
        if task is None:
            raise TaskNotFound(task_id)
        return self.repository.get_comments_by_task_id(task_id)
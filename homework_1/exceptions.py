class AppError(Exception):
    code: str = "app_error"
    message: str = "application error"

    def __init__(self, message: str | None = None):
        if message is not None:
            self.message = message
        super().__init__(self.message)

class TaskNotFound(AppError):
    code = "task_not_found"

    def __init__(self, task_id: int):
        super().__init__(f"Task with id={task_id} not found")

class CommentNotFound(AppError):
    code = "comment_not_found"

    def __init__(self, comment_id: int):
        super().__init__(f"Comment with id={comment_id} not found")
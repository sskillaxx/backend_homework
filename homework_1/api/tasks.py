from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from core.auth import get_current_user
from core.database import get_db
from repositories import TaskRepository
from schemas import CreateTask, EditTask, TaskResponse, CreateComment, CommentResponse
from services import TaskService

router = APIRouter(
    prefix="/v1/tasks",
    tags=["Tasks"],
    dependencies=[Depends(get_current_user)],
)

def get_task_service(db: Session = Depends(get_db)) -> TaskService:
    repository = TaskRepository(db)
    return TaskService(repository)

@router.get(
    "/",
    response_model=list[TaskResponse],
    status_code=status.HTTP_200_OK,
)
def get_task(service: TaskService = Depends(get_task_service)):
    return service.get_all_tasks()

@router.post(
    "/",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(new_task: CreateTask, service: TaskService = Depends(get_task_service)):
    return service.create_task(new_task)

@router.put(
    "/{task_id}",
    response_model=TaskResponse,
    status_code=status.HTTP_200_OK,
)
def edit_task(task_id: int, edited_task: EditTask, service: TaskService = Depends(get_task_service)):
    return service.edit_task(task_id, edited_task)

@router.delete(
    "/{task_id}",
    status_code=status.HTTP_200_OK,
)
def delete_task(task_id: int, service: TaskService = Depends(get_task_service)):
    service.delete_task(task_id)
    return {"status": "task deleted"}

@router.post(
    "/{task_id}/comments",
    response_model=CommentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_comment(task_id: int, new_comment: CreateComment, service: TaskService = Depends(get_task_service)):
    return service.create_comment(task_id, new_comment)

@router.get(
    "/{task_id}/comments",
    response_model=list[CommentResponse],
    status_code=status.HTTP_200_OK,
)
def get_comments(task_id: int, service: TaskService = Depends(get_task_service)):
    return service.get_task_comments(task_id)
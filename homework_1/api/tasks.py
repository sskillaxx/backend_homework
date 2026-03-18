from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from core.auth import get_current_user
from core.database import get_db
from repositories import TaskRepository
from schemas import CreateTask, EditTask, TaskResponse
from services import TaskService

router = APIRouter(
    prefix="/tasks",
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
    return service.add_task(new_task)

@router.put(
    "/{task_id}",
    response_model=TaskResponse,
    status_code=status.HTTP_200_OK,
)
def edit_task(task_id: int, edited_task: EditTask, service: TaskService = Depends(get_task_service)):
    edit_result = service.edit_task(task_id, edited_task)
    if edit_result is None:
        return JSONResponse(
            {
                "status": "error",
                "message": "task cannot be edited",
            },
            status.HTTP_404_NOT_FOUND,
        )

    return edit_result

@router.delete(
    "/{task_id}",
    status_code=status.HTTP_200_OK,
)
def delete_task(task_id: int, service: TaskService = Depends(get_task_service)):
    delete_result = service.delete_task(task_id)
    if not delete_result:
        return JSONResponse(
            {
                "status": "error",
                "message": "task cannot be deleted",
            },
            status.HTTP_404_NOT_FOUND,
        )

    return {"status": "task deleted"}

from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from schemas import CreateTask, EditTask
from services import TaskService

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/", status_code=status.HTTP_200_OK)
def get_task(service: TaskService = Depends()):
    get_result = service.get_all_tasks()
    if not get_result:
        return JSONResponse({
            "status": "error",
            "message": "no tasks found"
        }, status.HTTP_404_NOT_FOUND)

    return get_result

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_task(new_task: CreateTask, service: TaskService = Depends()):
    create_result = service.add_task(new_task)
    if not create_result:
        return JSONResponse({
            "status": "error",
            "message": "task cannot be created"
        }, status.HTTP_404_NOT_FOUND)

    return create_result

@router.put("/{task_name}", status_code=status.HTTP_200_OK)
def edit_task(task_name: str, edited_task: EditTask, service: TaskService = Depends()):
    edit_result = service.edit_task(task_name, edited_task)
    if not edit_result:
        return JSONResponse({
            "status": "error",
            "message": "task cannot be edited"
        }, status.HTTP_404_NOT_FOUND)

    return edit_result

@router.delete("/{task_name}", status_code=status.HTTP_200_OK)
def delete_task(task_name: str, service: TaskService = Depends()):
    delete_result = service.delete_task(task_name)
    if not delete_result:
        return JSONResponse({
            "status": "error",
            "message": "task cannot be deleted"
        }, status.HTTP_404_NOT_FOUND)

    return delete_result
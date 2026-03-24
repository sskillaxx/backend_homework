from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from exceptions import TaskNotFound, CommentNotFound

from api.router import common_router
from core.database import Base, engine

import models

app = FastAPI()

@app.exception_handler(TaskNotFound)
def task_not_found_handler(request: Request, exc: TaskNotFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message,
            }
        },
    )

@app.exception_handler(CommentNotFound)
def comment_not_found_handler(request: Request, exc: CommentNotFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message,
            }
        },
    )

Base.metadata.create_all(bind=engine)
app.include_router(common_router)
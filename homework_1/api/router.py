from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from api import auth_router, tasks_router

common_router = APIRouter()

@common_router.get("/")
def root():
    return JSONResponse({"swagger": "imeetsa"}, status_code=status.HTTP_200_OK)

common_router.include_router(tasks_router)
common_router.include_router(auth_router)

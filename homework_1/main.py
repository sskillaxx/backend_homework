from fastapi import FastAPI

from api.router import common_router

app = FastAPI()
app.include_router(common_router)
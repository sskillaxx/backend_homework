from fastapi import FastAPI

from api.router import common_router
from core.database import Base, engine
import models

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(common_router)

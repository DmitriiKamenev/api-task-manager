from fastapi import FastAPI

from app.router.health import health_router
from app.router.task import task_router

app = FastAPI()

app.include_router(health_router)
app.include_router(task_router)

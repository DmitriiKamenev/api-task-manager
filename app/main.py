from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.health import health_router
from app.routers.task import task_router
from app.routers.users import user_router

from app.database.session import init_db, get_db, del_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(task_router)
app.include_router(user_router)

init_db()



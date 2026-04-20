from fastapi import APIRouter

task_router = APIRouter(prefix='/tasks', tags=['Работа с тасками'])

@task_router.get('/')
def get_task():
    return 'Задачи'
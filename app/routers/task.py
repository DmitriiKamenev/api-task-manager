from fastapi import APIRouter, HTTPException
from app.schemas.task import Task

task_router = APIRouter(prefix='/tasks', tags=['Работа с тасками'])

fake_list_task = []

@task_router.get('/')
def get_task():
    return fake_list_task

@task_router.post('/')
def create_task(task: Task):
    new_task = task.model_dump()
    new_task["id"] = len(fake_list_task)

    fake_list_task.append(new_task)
    return new_task

@task_router.put('/{task_id}')
def update_task(task_id: int, task: Task):
    for idx, t in enumerate(fake_list_task):
        if t["id"] == task_id:
            updated_task = task.model_dump()
            updated_task["id"] = task_id
            fake_list_task[idx] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Задача не найдена")

@task_router.delete('/{task_id}')
def delete_task(task_id: int):
    for idx, t in enumerate(fake_list_task):
        if t["id"] == task_id:
            del fake_list_task[idx]
            return {"message": "Задача успешно удалена"}
    raise HTTPException(status_code=404, detail="Задача не найдена")
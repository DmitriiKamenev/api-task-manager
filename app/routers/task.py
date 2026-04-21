from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.task import TaskCreate, TaskUpdate
import app.crud.task as crud_task
from app.database.session import get_db


task_router = APIRouter(prefix='/tasks', tags=['Работа с тасками'])

@task_router.get(path='/', name='Получить все задачи')
def get_task(db: Session = Depends(get_db)):
    return crud_task.get_all_tasks(db)

@task_router.get(path='/{user_id}', name='Получить задачи пользователя')
def get_task_user(user_id: int, db: Session = Depends(get_db)):
    return crud_task.get_task_current_user(user_id, db)

@task_router.post(path='/', name='Создать задачу')
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    crud_task.create_task(task, db)
    return task


@task_router.patch(path='/{task_id}', name='Изменить задачу')
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    crud_task.update_task(task_id, task, db)
    return task


@task_router.delete(path='/{task_id}', name='Удалить задачу')
def delete_task(task_id: int, db: Session = Depends(get_db)):
    crud_task.delete_task(task_id, db)
    return {f"Задача \"{task_id}\" удалена": True}
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.task import TaskCreate, TaskUpdate
import app.crud.task as crud_task
from app.database.session import get_db
from app.core.security import get_current_user


task_router = APIRouter(prefix='/tasks', tags=['Работа с тасками'])

@task_router.get(path='/', name='Получить все задачи')
def get_task(db: Session = Depends(get_db),
             current_user=Depends(get_current_user)):
    return crud_task.get_task_current_user(current_user.id, db)

@task_router.post(path='/', name='Создать задачу')
def create_task(task: TaskCreate, current_user=Depends(get_current_user),  db: Session = Depends(get_db)):
    new_task = crud_task.create_task(task, current_user, db)
    return new_task


@task_router.patch(path='/{task_id}', name='Изменить задачу')
def update_task(task_id: int, task: TaskUpdate, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    crud_task.update_task(task_id, task,current_user, db)
    return task


@task_router.delete(path='/{task_id}', name='Удалить задачу')
def delete_task(task_id: int, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    crud_task.delete_task(task_id, current_user, db)
    return {f"Задача \"{task_id}\" удалена": True}
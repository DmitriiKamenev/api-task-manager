from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.task import Task as TaskModel
from app.models.user import User as UserModel
from app.schemas.task import TaskCreate, TaskUpdate
from datetime import datetime

def get_all_tasks(db: Session):
    return db.query(TaskModel).all()

def get_task_current_user(user_id: int, db: Session):
    if not db.query(UserModel).filter(UserModel.id == user_id).first():
        raise HTTPException(status_code=404, detail="User not found")

    return db.query(TaskModel).filter(TaskModel.user_id == user_id).all()

def create_task(task: TaskCreate, db: Session):
    db_task = TaskModel(
        title=task.title,
        description=task.description,
        status=task.status,
        priority=task.priority,
        user_id=task.user_id,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(id: int, task: TaskUpdate, db: Session):
    db_task = db.query(TaskModel).filter(TaskModel.id == id).first()

    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    update_data = task.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_task, key, value)

    db_task.updated_at = datetime.now()
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(id: int, db: Session):
    db_task = db.query(TaskModel).filter(TaskModel.id == id).first()

    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(db_task)
    db.commit()
    return {"ok": True}

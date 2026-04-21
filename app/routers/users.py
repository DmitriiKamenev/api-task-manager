from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import User, UserCreate
import app.crud.user as crud_user
from app.database.session import get_db


user_router = APIRouter(prefix="/users", tags=["Пользователи"])

@user_router.get(path="/", name="Все пользователи")
def get_all_users(db: Session = Depends(get_db)):
    return crud_user.get_all_users(db)

@user_router.post(path="/", name="Создать пользователя")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    crud_user.create_user(user, db)
    return user


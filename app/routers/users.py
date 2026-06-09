from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import User, UserCreate
import app.crud.user as crud_user
from app.database.session import get_db
from app.schemas.user import UserLogin
from app.core.security import (
    verify_password,
    create_access_token
)
from app.models.user import User as UserModel
from fastapi.security import OAuth2PasswordRequestForm


user_router = APIRouter(prefix="/users", tags=["Пользователи"])

@user_router.get(path="/", name="Все пользователи")
def get_all_users(db: Session = Depends(get_db)):
    return crud_user.get_all_users(db)

@user_router.post(path="/", name="Создать пользователя")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    crud_user.create_user(user, db)
    return user

@user_router.post("/login")
def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
):

    db_user = (
        db.query(UserModel)
        .filter(
            UserModel.email == form_data.username
        )
        .first()
    )

    if not db_user:
        return {"error": "User not found"}

    if not verify_password(
            form_data.password,
            db_user.hashed_password):

        return {"error": "Wrong password"}

    token = create_access_token(
        {"sub": db_user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
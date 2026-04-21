from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.schemas.user import UserCreate
from datetime import datetime

def get_all_users(db: Session):
    return db.query(UserModel).all()

def create_user(user: UserCreate, db: Session):
    db_user = UserModel(email=user.email, hashed_password=user.hashed_password, created_at=datetime.now())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

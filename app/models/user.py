from datetime import datetime

from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int
    email: EmailStr
    hashed_password: str
    created_at: datetime

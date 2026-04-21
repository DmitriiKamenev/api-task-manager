from datetime import datetime

from pydantic import BaseModel, EmailStr, ConfigDict, Field

class User(BaseModel):
    id: int
    email: EmailStr
    hashed_password: str = Field(min_length=8)
    created_at: datetime

    model_config = ConfigDict(
        extra='forbid'
    )

class UserCreate(BaseModel):
    email: EmailStr
    hashed_password: str = Field(min_length=8)

    model_config = ConfigDict(
        extra='forbid'
    )

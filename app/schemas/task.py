from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

from app.enum.enums import PriorityEnum, StatusEnum

class Task(BaseModel):
    id: int
    title: str = Field(min_length=3, max_length=50)
    description: str = Field(max_length=255)
    status: StatusEnum
    priority: PriorityEnum
    created_at: datetime
    updated_at: datetime
    user_id: int

    model_config = ConfigDict(
        extra='forbid'
    )

class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=50)
    description: str = Field(max_length=255)
    status: StatusEnum
    priority: PriorityEnum
    user_id: int

    model_config = ConfigDict(
        extra='forbid'
    )

class TaskUpdate(BaseModel):
    title: str = Field(default=None, min_length=3, max_length=50)
    description: str = Field(default=None, max_length=255)
    status: StatusEnum = None
    priority: PriorityEnum = None


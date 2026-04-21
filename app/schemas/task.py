from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from enum import Enum

class StatusEnum(str, Enum):
    TODO = "текущая"
    IN_PROGRESS = "в процессе"
    DONE = "выполнена"

class PriorityEnum(str, Enum):
    LOW = "не важное"
    MEDIUM = "средний"
    HIGH = "важное"

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


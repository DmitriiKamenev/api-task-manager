from datetime import datetime
from pydantic import BaseModel
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
    title: str
    description: str
    status: StatusEnum
    priority: PriorityEnum
    created_at: datetime
    updated_at: datetime
    user_id: int


from enum import Enum

class StatusEnum(str, Enum):
    TODO = "текущая"
    IN_PROGRESS = "в процессе"
    DONE = "выполнена"

class PriorityEnum(str, Enum):
    LOW = "не важное"
    MEDIUM = "средний"
    HIGH = "важное"
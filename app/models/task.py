from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, ForeignKey, Integer
from datetime import datetime

from app.models.base import Base
from app.enum.enums import PriorityEnum, StatusEnum


class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(
        primary_key=True
    )
    title: Mapped[str] = mapped_column(
        unique=True,
        min_length=3
    )
    description: Mapped[str] = mapped_column(
        max_length=255
    )
    status: Mapped[StatusEnum] = mapped_column(
        nullable=False,
        default=StatusEnum.TODO
    )
    priority: Mapped[PriorityEnum] = mapped_column(
        nullable=False,
        default=PriorityEnum.MEDIUM
    )
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now()
    )
    updated_at: Mapped[datetime] = mapped_column(

    )

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))



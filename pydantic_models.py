from datetime import datetime
from pydantic import BaseModel, Field, field_validator, computed_field
from enums import Priority, Status
from exceptions import TaskStateError


class PydanticTask(BaseModel):
    task_id: str = Field(..., min_length=3, description="Идентификатор задачи")
    description: str = Field(..., min_length=10, description="Описание задачи")
    priority: Priority
    status: Status = Field(default=Status.PENDING)
    created_at: datetime = Field(default_factory=datetime.now)

    @field_validator('status')
    @classmethod
    def validate_status_transitions(cls, new_status: Status, info) -> Status:
        return new_status

    @computed_field
    @property
    def is_ready_for_execution(self) -> bool:
        return self.status == Status.PENDING and len(self.description) > 0

    def update_status(self, new_status: Status) -> None:
        if self.status in (Status.COMPLETED, Status.CANCELLED):
            raise TaskStateError(f"Задача уже {self.status.value}.")
        if self.status == Status.PENDING and new_status == Status.COMPLETED:
            raise TaskStateError("Нельзя завершить задачу, не взяв её в работу.")
        self.status = new_status

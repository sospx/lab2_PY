from enums import Priority, Status
from exceptions import TaskValidationError, TaskStateError
from descriptors import StringValidator, LazyCreationTime


class Task:
    """
    Доменная модель задачи.
    """

    task_id = StringValidator(min_length=3)
    description = StringValidator(min_length=10)
    created_at = LazyCreationTime()

    def __init__(self, task_id: str, description: str, priority: Priority):
        self.task_id = task_id
        self.description = description
        self.priority = priority
        self._status = Status.PENDING

    @property
    def priority(self) -> Priority:
        return self._priority

    @priority.setter
    def priority(self, value: Priority) -> None:
        if not isinstance(value, Priority):
            raise TaskValidationError("Приоритет должен быть экземпляром Enum Priority.")
        self._priority = value

    @property
    def status(self) -> Status:
        return self._status

    @status.setter
    def status(self, new_status: Status) -> None:
        if not isinstance(new_status, Status):
            raise TaskValidationError("Статус должен быть экземпляром Enum Status.")
        if self._status in (Status.COMPLETED, Status.CANCELLED):
            raise TaskStateError(f"Невозможно изменить статус: задача уже со статусом: {self._status.value}.")
        if self._status == Status.PENDING and new_status == Status.COMPLETED:
            raise TaskStateError("Нельзя завершить задачу, не взяв её в работу.")
        self._status = new_status

    @property
    def is_ready_for_execution(self) -> bool:
        return self.status == Status.PENDING and len(self.description) > 0

    def __repr__(self) -> str:
        return f"<Task {self.task_id} | Priority: {self.priority.name} | Status: {self.status.name}>"

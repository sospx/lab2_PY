from models import Task
from pydantic_models import PydanticTask
from enums import Priority, Status
from exceptions import TaskValidationError, TaskStateError


def main():
    print("Тестирование дескрипторов:")
    task1 = Task("TSK-001", "Реализовать API для базы данных", Priority.HIGH)
    print(task1)
    print(f"Готова к выполнению? {task1.is_ready_for_execution}")
    print(f"Время создания: {task1.created_at}")

    try:
        task2 = Task("T1", "Коротко", Priority.LOW)
    except TaskValidationError as e:
        print(f"Ожидаемая ошибка валидации: {e}")
    try:
        task1.status = Status.COMPLETED
    except TaskStateError as e:
        print(f"Ожидаемая ошибка состояния: {e}")
    task1.status = Status.IN_PROGRESS
    task1.status = Status.COMPLETED
    print(f"Финальный статус: {task1.status}")

    print("\nТестирование Pydantic Модели")
    p_task = PydanticTask(
        task_id="PYD-001",
        description="Переписать модель на Pydantic",
        priority=Priority.MEDIUM
    )
    print(p_task.model_dump_json(indent=2))
    print(f"Pydantic task готова? {p_task.is_ready_for_execution}")


if __name__ == "__main__":
    main()

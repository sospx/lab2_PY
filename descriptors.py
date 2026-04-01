from typing import Any, Type
from datetime import datetime
from exceptions import TaskValidationError


class StringValidator:
    """
    Data Descriptor для строк.
    """

    def __init__(self, min_length: int = 1):
        self.min_length = min_length
        self._name: str = ""

    def __set_name__(self, owner: Type[Any], name: str) -> None:
        self._name = f"_{name}"

    def __get__(self, instance: Any, owner: Type[Any]) -> Any:
        if instance is None:
            return self
        return getattr(instance, self._name, None)

    def __set__(self, instance: Any, value: Any) -> None:
        if not isinstance(value, str):
            raise TaskValidationError(f"Атрибут '{self._name.lstrip('_')}' должен быть строкой.")
        if len(value.strip()) < self.min_length:
            raise TaskValidationError(
                f"Атрибут '{self._name.lstrip('_')}' должен содержать минимум {self.min_length} символов.")
        setattr(instance, self._name, value.strip())


class LazyCreationTime:
    """
    Non-Data Descriptor для ленивого вычисления времени создания.
    """

    def __set_name__(self, owner: Type[Any], name: str) -> None:
        self.name = name

    def __get__(self, instance: Any, owner: Type[Any]) -> Any:
        if instance is None:
            return self
        current_time = datetime.now()
        instance.__dict__[self.name] = current_time
        return current_time

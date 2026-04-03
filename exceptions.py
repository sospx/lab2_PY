class TaskDomainError(Exception):
    """
    Базовое исключение для ошибок доменной модели задачи.
    """
    pass


class TaskValidationError(TaskDomainError, ValueError):
    """
    Исключение при попытке присвоить невалидные данные.
    """
    pass


class TaskStateError(TaskDomainError):
    """
    Исключение при нарушении инвариантов состояния.
    """
    pass

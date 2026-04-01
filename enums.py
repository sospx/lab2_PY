from enum import Enum


class Priority(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class Status(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

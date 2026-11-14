from enum import Enum


class BookStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    ISSUED = "ISSUED"

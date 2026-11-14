
from dataclasses import dataclass

from enums.book_status import BookStatus


# Stores information about a library book
@dataclass
class Book:

    book_id: str
    title: str
    author: str
    status: BookStatus = BookStatus.AVAILABLE

    # Change book status to ISSUED
    def mark_issued(self) -> None:

        if self.status == BookStatus.ISSUED:
            raise ValueError(f"Book '{self.title}' is already issued.")

        self.status = BookStatus.ISSUED

    # Change book status to AVAILABLE
    def mark_available(self) -> None:

        if self.status == BookStatus.AVAILABLE:
            raise ValueError(f"Book '{self.title}' is already available.")

        self.status = BookStatus.AVAILABLE

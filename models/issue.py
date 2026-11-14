
from dataclasses import dataclass
from datetime import date
from typing import Optional


# Stores information about a book issued to a member
@dataclass
class Issue:

    issue_id: str
    book_id: str
    member_id: str
    issue_date: date
    due_date: date
    return_date: Optional[date] = None

    # Check whether the book is still issued
    @property
    def is_active(self) -> bool:

        if self.return_date is None:
            return True

        return False

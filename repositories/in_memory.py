
from typing import Optional, List

from models.book import Book
from models.member import Member
from models.issue import Issue


# Repository for storing books
class InMemoryBookRepository:

    def __init__(self):
        # Store books using their IDs
        self.books = {}

    # Add a new book
    def add(self, book: Book) -> None:

        if book.book_id in self.books:
            raise ValueError(f"Book ID '{book.book_id}' already exists.")

        self.books[book.book_id] = book

    # Find a book using its ID
    def get(self, book_id: str) -> Optional[Book]:
        return self.books.get(book_id)

    # Get all books
    def list_all(self) -> List[Book]:
        return list(self.books.values())


# Repository for storing library members
class InMemoryMemberRepository:

    def __init__(self):
        self.members = {}

    # Register a new member
    def add(self, member: Member) -> None:

        if member.member_id in self.members:
            raise ValueError(f"Member ID '{member.member_id}' already exists.")

        self.members[member.member_id] = member

    # Find a member using their ID
    def get(self, member_id: str) -> Optional[Member]:
        return self.members.get(member_id)

    # Get all registered members
    def list_all(self) -> List[Member]:
        return list(self.members.values())


# Repository for storing issue records
class InMemoryIssueRepository:

    def __init__(self):
        self.issues = {}

    # Add a new issue record
    def add(self, issue: Issue) -> None:

        if issue.issue_id in self.issues:
            raise ValueError(f"Issue ID '{issue.issue_id}' already exists.")

        self.issues[issue.issue_id] = issue

    # Find an issue using its ID
    def get(self, issue_id: str) -> Optional[Issue]:
        return self.issues.get(issue_id)

    # Find an active issue for a particular book
    def get_active_for_book(self, book_id: str) -> Optional[Issue]:

        for issue in self.issues.values():

            if issue.book_id == book_id and issue.is_active:
                return issue

        return None

    # Get all issue records
    def list_all(self) -> List[Issue]:
        return list(self.issues.values())

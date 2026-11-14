
from datetime import date, timedelta
from uuid import uuid4

from models.issue import Issue


class LibraryService:

    def __init__(self, book_repository, member_repository, issue_repository,
                 loan_period_days=14):

        # Loan period should be greater than zero
        if loan_period_days <= 0:
            raise ValueError("Loan period must be greater than zero.")

        self.book_repo = book_repository
        self.member_repo = member_repository
        self.issue_repo = issue_repository
        self.loan_period_days = loan_period_days

    # Issue a book to a library member
    def issue_book(self, book_id: str, member_id: str) -> Issue:

        # Find the book
        book = self.book_repo.get(book_id)

        if book is None:
            raise ValueError(f"Book '{book_id}' was not found.")

        # Find the member
        member = self.member_repo.get(member_id)

        if member is None:
            raise ValueError(f"Member '{member_id}' was not found.")

        # Check whether the book is already issued
        active_issue = self.issue_repo.get_active_for_book(book_id)

        if active_issue is not None:
            raise ValueError(f"Book '{book.title}' is already issued.")

        # Update book status
        book.mark_issued()

        # Calculate issue date and due date
        today = date.today()
        due_date = today + timedelta(days=self.loan_period_days)

        # Create an issue record
        issue = Issue(
            issue_id=f"I-{uuid4().hex[:8].upper()}",
            book_id=book_id,
            member_id=member_id,
            issue_date=today,
            due_date=due_date
        )

        # Save the issue record
        self.issue_repo.add(issue)

        return issue

    # Return a book to the library
    def return_book(self, book_id: str, member_id: str) -> Issue:

        # Find the book
        book = self.book_repo.get(book_id)

        if book is None:
            raise ValueError(f"Book '{book_id}' was not found.")

        # Find the member
        member = self.member_repo.get(member_id)

        if member is None:
            raise ValueError(f"Member '{member_id}' was not found.")

        # Find the active issue record
        issue = self.issue_repo.get_active_for_book(book_id)

        if issue is None:
            raise ValueError(f"Book '{book.title}' is not currently issued.")

        # Check whether this member borrowed the book
        if issue.member_id != member_id:
            raise ValueError("This book was issued to a different member.")

        # Update return date and book status
        issue.return_date = date.today()
        book.mark_available()

        return issue

    # Display all issue and return records
    def list_issues(self):
        return self.issue_repo.list_all()


import unittest

from repositories.in_memory import (
    InMemoryBookRepository,
    InMemoryMemberRepository,
    InMemoryIssueRepository
)

from services.book_service import BookService
from services.member_service import MemberService
from services.library_service import LibraryService

from enums.book_status import BookStatus


class LibrarySystemTests(unittest.TestCase):

    # This method runs before every test
    def setUp(self):

        # Creating repositories
        self.book_repo = InMemoryBookRepository()
        self.member_repo = InMemoryMemberRepository()
        self.issue_repo = InMemoryIssueRepository()

        # Creating service objects
        self.book_service = BookService(self.book_repo)
        self.member_service = MemberService(self.member_repo)

        self.library_service = LibraryService(
            self.book_repo,
            self.member_repo,
            self.issue_repo
        )

        # Adding a sample book
        self.book_service.add_book(
            "B1", "Clean Code", "Robert C. Martin"
        )

        # Registering two members
        self.member_service.register_member(
            "M1", "Ajaz", "ajaz@example.com"
        )

        self.member_service.register_member(
            "M2", "Sam", "sam@example.com"
        )

    # Check whether book status changes after issuing
    def test_issue_book_changes_status(self):

        self.library_service.issue_book("B1", "M1")

        book = self.book_repo.get("B1")

        self.assertEqual(book.status, BookStatus.ISSUED)

    # Check that the same book cannot be issued twice
    def test_cannot_issue_same_book_twice(self):

        self.library_service.issue_book("B1", "M1")

        with self.assertRaises(ValueError):
            self.library_service.issue_book("B1", "M2")

    # Check whether book becomes available after returning
    def test_return_book_changes_status(self):

        self.library_service.issue_book("B1", "M1")
        self.library_service.return_book("B1", "M1")

        book = self.book_repo.get("B1")

        self.assertEqual(book.status, BookStatus.AVAILABLE)

    # Check that only the member who borrowed the book can return it
    def test_only_borrowing_member_can_return(self):

        self.library_service.issue_book("B1", "M1")

        with self.assertRaises(ValueError):
            self.library_service.return_book("B1", "M2")

    # Check that an available book cannot be returned
    def test_cannot_return_book_that_is_not_issued(self):

        with self.assertRaises(ValueError):
            self.library_service.return_book("B1", "M1")


if __name__ == "__main__":
    unittest.main()

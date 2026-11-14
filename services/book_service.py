
from models.book import Book


class BookService:

    def __init__(self, book_repository):
        # Repository is used to store and manage books
        self.book_repo = book_repository

    # Add a new book to the library
    def add_book(self, book_id: str, title: str, author: str) -> Book:

        # Check that book details are not empty
        self.validate_text(book_id, "Book ID")
        self.validate_text(title, "Title")
        self.validate_text(author, "Author")

        # Create a new book
        book = Book(book_id, title, author)

        # Save the book in the repository
        self.book_repo.add(book)

        return book

    # Find a book using its ID
    def get_book(self, book_id: str) -> Book:

        book = self.book_repo.get(book_id)

        if book is None:
            raise ValueError(f"Book '{book_id}' was not found.")

        return book

    # Get all books from the library
    def list_books(self):
        return self.book_repo.list_all()

    # Check whether a text field is empty
    @staticmethod
    def validate_text(value: str, field: str) -> None:

        if not value or not value.strip():
            raise ValueError(f"{field} cannot be empty.")

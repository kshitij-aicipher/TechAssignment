#from models import Book
from storage import FileStorage


class BookManager:
    """
    A class to manage books including adding, listing, searching, updating, and deleting.

    Attributes:
        storage (FileStorage): The file-based storage for books.
        items (list): The list of Book objects.
    """

    def __init__(self):
        """
        Initialize BookManager with a file-based storage and load existing books.
        """
        self.storage = FileStorage('books.json')
        self.items = [Book(**data) for data in self.storage.load_data()]

    def add_item(self, item):
        """
        Add a book to the list and save it to storage.

        Args:
            item (Book): The Book object to add.
        """
        self.items.append(item)
        self.storage.save_data([i.__dict__ for i in self.items])

    def list_items(self):
        """
        List all books in the library.

        Returns:
            list: The list of Book objects.
        """
        return self.items

    def search_by_title(self, title):
        """
        Search books by title.

        Args:
            title (str): The title to search for.

        Returns:
            list: The list of matching Book objects.
        """
        return [item for item in self.items if item.title.lower() == title.lower()]

    def search_by_author(self, author):
        """
        Search books by author.

        Args:
            author (str): The author to search for.

        Returns:
            list: The list of matching Book objects.
        """
        return [item for item in self.items if item.author.lower() == author.lower()]

    def search_by_isbn(self, isbn):
        """
        Search books by ISBN.

        Args:
            isbn (str): The ISBN to search for.

        Returns:
            list: The list of matching Book objects.
        """
        return [item for item in self.items if item.isbn == isbn]

    def update_item(self, isbn, new_data):
        """
        Update book details by ISBN.

        Args:
            isbn (str): The ISBN of the book to update.
            new_data (dict): The new data to update.

        Returns:
            bool: True if update successful, False otherwise.
        """
        for item in self.items:
            if item.isbn == isbn:
                for key, value in new_data.items():
                    setattr(item, key, value)
                self.storage.save_data([i.__dict__ for i in self.items])
                return True
        return False

    def delete_item(self, isbn):
        """
        Delete a book by ISBN.

        Args:
            isbn (str): The ISBN of the book to delete.

        Returns:
            bool: True if deletion successful, False otherwise.
        """
        self.items = [item for item in self.items if item.isbn != isbn]
        self.storage.save_data([i.__dict__ for i in self.items])
        return True  # Assuming deletion is successful

class Book:
    """Represents a book in the library."""

    def __init__(self, title, author, isbn, copies_available):
        """
        Initialize a Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (int): The ISBN of the book.
            copies_available (int): The number of copies available in the library.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies_available = copies_available

    def __repr__(self):
        """
        Return a string representation of the Book object.

        Returns:
            str: A formatted string representing the Book object.
        """
        return f"Book(title={self.title}, author={self.author}, isbn={self.isbn}, copies_available={self.copies_available})"

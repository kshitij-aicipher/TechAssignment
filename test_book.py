import unittest
from book import BookManager, Book
from storage import FileStorage


class TestBookManager(unittest.TestCase):
    def setUp(self):
        # Initialize BookManager with a temporary storage file for testing
        self.storage = FileStorage('test_books.json')
        self.book_manager = BookManager(storage=self.storage)

    def tearDown(self):
        # Clean up after each test by deleting the temporary storage file
        self.storage.delete_file()

    # def test_add_item(self):
    #     # Create a new Book object and add it to the BookManager
    #     book = Book("Python Programming", "John Smith", "978-0134853987", 5)
    #     self.book_manager.add_item(book)

    #     # Check if the added book exists in the BookManager's items
    #     self.assertIn(book, self.book_manager.items)

    def test_list_items(self):
        # Add multiple books to the BookManager
        books = [
            Book("Book 1", "Author 1", "1111111111", 3),
        ]
        # for book in books:
        #     self.book_manager.add_item(book)

        # Get the list of books from the BookManager and check if they match
        listed_books = self.book_manager.list_items()
        self.assertEqual(len(listed_books), len(books))
        self.assertEqual(listed_books, books)

    def test_search_by_title(self):
        # Add books with different titles to the BookManager
        books = [
            Book("Game Theory", "John", "2332", 16),
        ]
        # for book in books:
        #     self.book_manager.add_item(book)

        # Search for a book by title and check if the correct book is returned
        found_books = self.book_manager.search_by_title("Game Theory")
        self.assertEqual(len(found_books), 1)
        self.assertEqual(found_books[0].isbn, "2332")


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch
from io import StringIO
from main import *

class TestMain(unittest.TestCase):
    def setUp(self):
        self.book_manager = LibraryBookManager()
        self.user_manager = LibraryUserManager()

    @patch('builtins.input', side_effect=["Game Theory", "John", "2332", "2"])
    def test_add_book(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            add_book()
            self.assertIn("Book added successfully.", fake_out.getvalue().strip())

    def test_list_books(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            list_books()
            self.assertIn("Books in the library:", fake_out.getvalue().strip())

    @patch('builtins.input', side_effect=["Game Theory", "1", "2332"])
    def test_search_books(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            search_books()
            self.assertIn("Search results:", fake_out.getvalue().strip())

    @patch('builtins.input', side_effect=["2112", "New Title", "New Author", "5"])
    def test_update_book(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            update_book()
            self.assertIn("Book updated successfully.", fake_out.getvalue().strip())

    @patch('builtins.input', side_effect=["2112"])
    def test_delete_book(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            delete_book()
            self.assertIn("Book deleted successfully.", fake_out.getvalue().strip())

    @patch('builtins.input', side_effect=["Shyam", "456"])
    def test_add_user(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            add_user()
            self.assertIn("User added successfully.", fake_out.getvalue().strip())

    def test_list_users(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            list_users()
            self.assertIn("Users in the system:", fake_out.getvalue().strip())

    @patch('builtins.input', side_effect=["Shyam", "456"])
    def test_search_users(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            search_users()
            self.assertIn("Search results:", fake_out.getvalue().strip())

    @patch('builtins.input', side_effect=["456", "Ram"])
    def test_update_user(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            update_user()
            self.assertIn("User updated successfully.", fake_out.getvalue().strip())

    @patch('builtins.input', side_effect=["456"])
    def test_delete_user(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            delete_user()
            self.assertIn("User deleted successfully.", fake_out.getvalue().strip())

    @patch('builtins.input', side_effect=["2112"])
    def test_check_out_book(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            check_out_book()
            self.assertIn("Book checked out successfully.", fake_out.getvalue().strip())

    @patch('builtins.input', side_effect=["2112"])
    def test_check_in_book(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            check_in_book()
            self.assertIn("Book checked in successfully.", fake_out.getvalue().strip())

if __name__ == '__main__':
    unittest.main()

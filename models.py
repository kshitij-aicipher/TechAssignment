from book import BookManager
from user import UserManager
from check import CheckInOutMixin

# class Book:
#     """Represents a book in the library."""

#     def __init__(self, title, author, isbn, copies_available):
#         """
#         Initialize a Book object.

#         Args:
#             title (str): The title of the book.
#             author (str): The author of the book.
#             isbn (int): The ISBN of the book.
#             copies_available (int): The number of copies available in the library.
#         """
#         self.title = title
#         self.author = author
#         self.isbn = isbn
#         self.copies_available = copies_available

#     def __repr__(self):
#         """
#         Return a string representation of the Book object.

#         Returns:
#             str: A formatted string representing the Book object.
#         """
#         return f"Book(title={self.title}, author={self.author}, isbn={self.isbn}, copies_available={self.copies_available})"


# class User:
#     """Represents a user in the library system."""

#     def __init__(self, name, user_id):
#         """
#         Initialize a User object.

#         Args:
#             name (str): The name of the user.
#             user_id (str): The unique ID of the user.
#         """
#         self.name = name
#         self.user_id = user_id

#     def __repr__(self):
#         """
#         Return a string representation of the User object.

#         Returns:
#             str: A formatted string representing the User object.
#         """
#         return f"User({self.name}, {self.user_id})"

    

class LibraryBookManager(BookManager, CheckInOutMixin):
    """
    A class representing the library's book manager, inheriting from BookManager and CheckInOutMixin.

    This class is responsible for managing books in the library and implements check-in and check-out functionalities.

    Attributes:
        Inherits attributes from BookManager and CheckInOutMixin.
    """
    pass

class LibraryUserManager(UserManager):
    """
    A class representing the library's user manager, inheriting from UserManager.

    This class is responsible for managing users in the library.

    Attributes:
        Inherits attributes from UserManager.
    """
    pass

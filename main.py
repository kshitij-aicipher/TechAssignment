from models import LibraryBookManager, LibraryUserManager
from book import Book
from user import User

user_manager = LibraryUserManager()
book_manager = LibraryBookManager()

def add_book():
    """Add a new book to the library."""
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    isbn = input("Enter ISBN: ")
    copies_available = int(input("Enter copies available: "))
    book = Book(title, author, isbn, copies_available)
    book_manager.add_item(book)
    print("Book added successfully.")

def list_books():
    """List all books in the library."""
    books = book_manager.list_items()
    print("Books in the library:")
    for book in books:
        print(book)

def search_books():
    """Search for books by title, author, or ISBN."""
    search_key = input("Enter search keyword: ")
    books = book_manager.search_by_title(search_key) + \
            book_manager.search_by_author(search_key) + \
            book_manager.search_by_isbn(search_key)
    if books:
        print("Search results:")
        for book in books:
            print(book)
    else:
        print("No matching books found.")

def update_book():
    """Update information of an existing book."""
    isbn = input("Enter book ISBN to update: ")
    new_title = input("Enter new title (leave blank to keep current): ")
    new_author = input("Enter new author (leave blank to keep current): ")
    new_copies_available = input("Enter new copies available (leave blank to keep current): ")
    new_data = {}
    if new_title:
        new_data['title'] = new_title
    if new_author:
        new_data['author'] = new_author
    if new_copies_available:
        new_data['copies_available'] = int(new_copies_available)
    if book_manager.update_item(isbn, new_data):
        print("Book updated successfully.")
    else:
        print("Book not found or invalid ISBN.")

def delete_book():
    """Delete a book from the library."""
    isbn = input("Enter book ISBN to delete: ")
    if book_manager.delete_item(isbn):
        print("Book deleted successfully.")
    else:
        print("Book not found or invalid ISBN.")

def add_user():
    """Add a new user to the library system."""
    name = input("Enter user name: ")
    user_id = input("Enter user ID: ")
    user = User(name, user_id)
    user_manager.add_item(user)
    print("User added successfully.")

def list_users():
    """List all users in the library system."""
    users = user_manager.list_items()
    print("Users in the system:")
    for user in users:
        print(user)

def search_users():
    """Search for users by name or user ID."""
    search_key = input("Enter search keyword: ")
    users = user_manager.search_by_name(search_key) + \
            user_manager.search_by_id(search_key)
    if users:
        print("Search results:")
        for user in users:
            print(user)
    else:
        print("No matching users found.")

def update_user():
    """Update information of an existing user."""
    user_id = input("Enter user ID to update: ")
    new_name = input("Enter new name (leave blank to keep current): ")
    new_data = {}
    if new_name:
        new_data['name'] = new_name
    if user_manager.update_user(user_id, new_data):
        print("User updated successfully.")
    else:
        print("User not found or invalid ID.")

def delete_user():
    """Delete a user from the library system."""
    user_id = input("Enter user ID to delete: ")
    if user_manager.delete_user(user_id):
        print("User deleted successfully.")
    else:
        print("User not found or invalid ID.")

def check_out_book():
    """Check out a book from the library."""
    item_id = input("Enter book ISBN to check out: ")
    if book_manager.check_out(item_id):
        print("Book checked out successfully.")
    else:
        print("Book not available or invalid ISBN.")

def check_in_book():
    """Check in a book to the library."""
    item_id = input("Enter book ISBN to check in: ")
    if book_manager.check_in(item_id):
        print("Book checked in successfully.")
    else:
        print("Invalid ISBN.")

# Defined dictionary mapping for menu options and corresponding functions
menu_options = {
    '1': add_book,
    '2': list_books,
    '3': search_books,
    '4': update_book,
    '5': delete_book,
    '6': add_user,
    '7': list_users,
    '8': search_users,
    '9': update_user,
    '10': delete_user,
    '11': check_out_book,
    '12': check_in_book,
}

if __name__ == "__main__":
    book_manager = LibraryBookManager()
    user_manager = LibraryUserManager()

    while True:
        print("\n\n1. Add Book")
        print("2. List Books")
        print("3. Search Books")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Add User")
        print("7. List Users")
        print("8. Search Users")
        print("9. Update User")
        print("10. Delete User")
        print("11. Check Out Book")
        print("12. Check In Book")
        print("13. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice in menu_options:
            menu_options[choice]()
        elif choice == '13':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

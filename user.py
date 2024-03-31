from storage import FileStorage

class UserManager:
    """
    A class to manage users including adding, listing, searching, updating, and deleting.

    Attributes:
        storage (FileStorage): The file-based storage for users.
        items (list): The list of user dictionaries.
    """

    def __init__(self):
        """
        Initialize UserManager with a file-based storage and load existing users.
        """
        self.storage = FileStorage('users.json')
        self.items = self.storage.load_data()

    def add_item(self, user):
        """
        Add a user to the list and save it to storage.

        Args:
            user (User): The User object to add.
        """
        user_dict = user.__dict__
        self.items.append(user_dict)
        self.storage.save_data(self.items)

    def list_items(self):
        """
        List all users in the system.

        Returns:
            list: The list of user dictionaries.
        """
        return self.items

    def search_by_name(self, name):
        """
        Search users by name.

        Args:
            name (str): The name to search for.

        Returns:
            list: The list of matching user dictionaries.
        """
        return [item for item in self.items if item['name'].lower() == name.lower()]

    def search_by_id(self, user_id):
        """
        Search users by user ID.

        Args:
            user_id (str): The user ID to search for.

        Returns:
            list: The list of matching user dictionaries.
        """
        return [item for item in self.items if item['user_id'] == user_id]

    def update_user(self, user_id, new_data):
        """
        Update user details by user ID.

        Args:
            user_id (str): The user ID of the user to update.
            new_data (dict): The new data to update.

        Returns:
            bool: True if update successful, False otherwise.
        """
        for user in self.items:
            if user['user_id'] == user_id:
                user.update(new_data)
                self.storage.save_data(self.items)
                return True
        return False

    def delete_user(self, user_id):
        """
        Delete a user by user ID.

        Args:
            user_id (str): The user ID of the user to delete.

        Returns:
            bool: True if deletion successful, False otherwise.
        """
        self.items = [user for user in self.items if user['user_id'] != user_id]
        self.storage.save_data(self.items)
        return True


class User:
    """
    Represents a user in the library system.
    """

    def __init__(self, name, user_id):
        """
        Initialize a User object.

        Args:
            name (str): The name of the user.
            user_id (str): The unique ID of the user.
        """
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        """
        Return a string representation of the User object.

        Returns:
            str: A formatted string representing the User object.
        """
        return f"User({self.name}, {self.user_id})"


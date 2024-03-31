
class CheckInOutMixin:
    """
    A mixin class providing check-out, check-in, and item retrieval functionalities.

    This mixin class is designed to be used with classes managing items that can be checked in and checked out.

    Attributes:
        None
    """

    def check_out(self, item_id):
        """
        Checks out an item with the given item ID.

        Parameters:
            item_id (str): The unique identifier of the item to check out.

        Returns:
            bool: True if the item was successfully checked out, False otherwise.
        """
        item = self.get_item_by_id(item_id)
        if item and item.copies_available > 0:
            item.copies_available -= 1
            self.storage.save_data([i.__dict__ for i in self.items])
            return True
        return False

    def check_in(self, item_id):
        """
        Checks in an item with the given item ID.

        Parameters:
            item_id (str): The unique identifier of the item to check in.

        Returns:
            bool: True if the item was successfully checked in, False otherwise.
        """
        item = self.get_item_by_id(item_id)
        if item:
            item.copies_available += 1
            self.storage.save_data([i.__dict__ for i in self.items])
            return True
        return False

    def get_item_by_id(self, item_id):
        """
        Retrieves an item with the given item ID.

        Parameters:
            item_id (str): The unique identifier of the item to retrieve.

        Returns:
            object: The item object if found, None otherwise.
        """
        for item in self.items:
            if item.isbn == item_id:
                return item
        return None

    
    

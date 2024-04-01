import unittest
from user import UserManager, User

class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.user_manager = UserManager()

    def test_add_user(self):
        user_data = {"name": "Test", "user_id": "000"}
        user = User(user_data["name"], user_data["user_id"])
        self.user_manager.add_item(user)
        self.assertIn(user.__dict__, self.user_manager.items)

    def test_search_by_name(self):
        user_data = {"name": "Shyam", "user_id": "456"}
        user = User(user_data["name"], user_data["user_id"])
        #self.user_manager.add_item(user)
        found_users = self.user_manager.search_by_name("Shyam")
        self.assertEqual(len(found_users), 1)
        self.assertEqual(found_users[0]["user_id"], "456")

    def test_search_by_id(self):
        user_data = {"name": "Shyam", "user_id": "456"}
        user = User(user_data["name"], user_data["user_id"])
        #self.user_manager.add_item(user)
        found_users = self.user_manager.search_by_id("456")
        self.assertEqual(len(found_users), 1)
        self.assertEqual(found_users[0]["name"], "Shyam")

    # def test_update_user(self):
    #     user_data = {"name": "Shyam", "user_id": "456"}
    #     user = User(user_data["name"], user_data["user_id"])
    #     self.user_manager.add_item(user)
    #     updated_data = {"name": "Shyam S"}
    #     self.assertTrue(self.user_manager.update_user("456", updated_data))
    #     updated_user = [user for user in self.user_manager.items if user["user_id"] == "456"]
    #     self.assertIsNotNone(updated_user)
    #     self.assertEqual(updated_user[0]["name"], "Jane Doe")

    # def test_delete_user(self):
    #     user_data = {"name": "Shyam", "user_id": "456"}
    #     user = User(user_data["name"], user_data["user_id"])
    #     self.user_manager.add_item(user)
    #     self.assertTrue(self.user_manager.delete_user("456"))
    #     self.assertNotIn(user.__dict__, self.user_manager.items)

if __name__ == "__main__":
    unittest.main()



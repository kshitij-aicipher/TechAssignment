import unittest
from unittest.mock import MagicMock
from check import CheckInOutMixin

class MockStorage:
    def __init__(self):
        self.saved_data = None

    def save_data(self, data):
        self.saved_data = data

class TestCheckInOutMixin(unittest.TestCase):
    def setUp(self):
        self.mixin = CheckInOutMixin()
        self.mixin.storage = MockStorage()
        self.mixin.items = [
            MagicMock(isbn='123', copies_available=2),
            MagicMock(isbn='456', copies_available=0)
        ]

    def test_check_out_available(self):
        self.assertTrue(self.mixin.check_out('123'))
        self.assertEqual(self.mixin.storage.saved_data[0]['copies_available'], 1)

    def test_check_out_unavailable(self):
        self.assertFalse(self.mixin.check_out('456'))
        self.assertIsNone(self.mixin.storage.saved_data)

    def test_check_in_existing(self):
        self.assertTrue(self.mixin.check_in('123'))
        self.assertEqual(self.mixin.storage.saved_data[0]['copies_available'], 3)

    def test_check_in_non_existing(self):
        self.assertFalse(self.mixin.check_in('789'))
        self.assertIsNone(self.mixin.storage.saved_data)

    def test_get_item_by_id_existing(self):
        item = self.mixin.get_item_by_id('123')
        self.assertEqual(item.isbn, '123')

    def test_get_item_by_id_non_existing(self):
        item = self.mixin.get_item_by_id('789')
        self.assertIsNone(item)

if __name__ == '__main__':
    unittest.main()

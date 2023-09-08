import os
import sys
import pickle
import unittest
from datetime import datetime, timedelta
from modules.history_manager import HistoryManager

#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestHistoryManager(unittest.TestCase):

    def setUp(self):
        self.history_manager = HistoryManager("test_history.bin")
        self.password = "TestPass123"
    
    def tearDown(self):
        if os.path.exists("test_history.bin"):
            os.remove("test_history.bin")

    def test_default_expiry(self):
        current_time = datetime(2023, 1, 1)
        self.history_manager.save_to_history(self.password, current_time=current_time)

        with open("test_history.bin", 'rb') as file:
            passwords = pickle.load(file)

        self.assertEqual(len(passwords), 1)
        password, expiry_date = passwords[0]
        self.assertEqual(expiry_date, current_time + timedelta(days=60))

    def test_custom_expiry(self):
        current_time = datetime(2023, 1, 1)
        self.history_manager.save_to_history(self.password, validity_days=30, current_time=current_time)

        with open("test_history.bin", 'rb') as file:
            passwords = pickle.load(file)

        self.assertEqual(len(passwords), 1)
        password, expiry_date = passwords[0]
        self.assertEqual(expiry_date, current_time + timedelta(days=30))

if __name__ == '__main__':
    unittest.main()

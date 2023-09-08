import os
import pickle
from datetime import datetime, timedelta
from termcolor import colored

class HistoryManager:
    def __init__(self, history_file="history.bin"):
        self.history_file = history_file

    def view_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, 'rb') as file:
                history_data = pickle.load(file)
            for password, expiry_date in history_data:
                days_left = (expiry_date - datetime.now()).days
                if days_left > 30:
                    color = "green"
                elif 0 <= days_left <= 30:
                    color = "blue"
                else:
                    color = "red"
                formatted_date = expiry_date.strftime("%Y-%m-%d")
                print(colored(f"{password} (Expiry: {formatted_date})", color))
        else:
            print("No password history found.")

    def clear_history(self):
        if os.path.exists(self.history_file):
            os.remove(self.history_file)
            print("Password history cleared.")
        else:
            print("No password history found.")

    def save_to_history(self, password, validity_days=60, current_time=None):
        passwords = []

        if not current_time:  
            current_time = datetime.now()

        expiry_date = current_time + timedelta(days=validity_days)

        if os.path.exists(self.history_file):
            with open(self.history_file, 'rb') as file:
                passwords = pickle.load(file)

        with open(self.history_file, 'wb') as file:
            passwords.append((password, expiry_date))
            pickle.dump(passwords, file)

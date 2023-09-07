import os
import pickle

class HistoryManager:
    def __init__(self, history_file="history.bin"):
        self.history_file = history_file

    def view_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, 'rb') as file:
                history_data = pickle.load(file)
            for password in history_data:
                print(password)
        else:
            print("No password history found.")

    def clear_history(self):
        if os.path.exists(self.history_file):
            os.remove(self.history_file)
            print("Password history cleared.")
        else:
            print("No password history found.")

    def save_to_history(self, password):
        passwords = []
        if os.path.exists(self.history_file):
            with open(self.history_file, 'rb') as file:
                passwords = pickle.load(file)
        with open(self.history_file, 'wb') as file:
            passwords.append(password)
            pickle.dump(passwords, file)

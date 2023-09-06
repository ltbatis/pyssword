import random
import string

class PasswordGenerator:
    def __init__(self, length=8, use_digits=True, use_special_chars=True):
        self.length = length
        self.use_digits = use_digits
        self.use_special_chars = use_special_chars

    def generate(self):
        characters = string.ascii_letters
        if self.use_digits:
            characters += string.digits
        if self.use_special_chars:
            characters += string.punctuation
        return ''.join(random.choice(characters) for i in range(self.length))

import random
import string

class PasswordGenerator:
    def __init__(self, length=8, use_digits=True, use_special_chars=True, level='medium'):
        self.length = length
        self.use_digits = use_digits
        self.use_special_chars = use_special_chars
        self.level = level

    def set_complexity(self):
        if self.level == 'low':
            return string.ascii_lowercase
        elif self.level == 'medium':
            return string.ascii_letters
        elif self.level == 'high':
            characters = string.ascii_letters
            if self.use_digits:
                characters += string.digits
            if self.use_special_chars:
                characters += string.punctuation
            return characters
        else:
            return string.ascii_letters

    def generate(self):
        characters = self.set_complexity()
        return ''.join(random.choice(characters) for _ in range(self.length))

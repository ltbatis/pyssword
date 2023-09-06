import random
import string
import nltk
if not nltk.data.find('corpora/words'):
    nltk.download('words', quiet=True)
from nltk.corpus import words

class PasswordGenerator:
    def __init__(self, length=8, use_digits=True, use_special_chars=True, level='medium', avoid_similar=False):
        self.length = length
        self.use_digits = use_digits
        self.use_special_chars = use_special_chars
        self.level = level
        self.avoid_similar = avoid_similar

    def set_complexity(self):
        characters = string.ascii_letters
        if self.use_digits:
            characters += string.digits
        if self.use_special_chars:
            characters += string.punctuation
        return characters

    def filter_similar_chars(self, characters):
        similar_chars = 'I1l0O'
        return ''.join(char for char in characters if char not in similar_chars)

    def generate(self):
        characters = self.set_complexity()
        if self.avoid_similar:
            characters = self.filter_similar_chars(characters)
        return ''.join(random.choice(characters) for _ in range(self.length))
    
    def generate_pronounceable(self):
        word_list = words.words()
        password = ''
        while len(password) < self.length:
            password += random.choice(word_list)

            if len(password) < self.length and self.use_digits:
                password += random.choice(string.digits)

            if len(password) < self.length and self.use_special_chars:
                password += random.choice(string.punctuation)

        return password[:self.length]

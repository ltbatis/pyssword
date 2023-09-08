import os
import pickle
import random
import string
import nltk
if not nltk.data.find('corpora/words'):
    nltk.download('words', quiet=True)
from nltk.corpus import words
from termcolor import colored

class PasswordGenerator:
    def __init__(self, length=8, use_digits=True, use_special_chars=True, level='medium', avoid_similar=False, include_chars='', exclude_chars=''):
        self.length = length
        self.use_digits = use_digits
        self.use_special_chars = use_special_chars
        self.level = level
        self.avoid_similar = avoid_similar
        self.include_chars = include_chars
        self.exclude_chars = exclude_chars

    def set_complexity(self):
        characters = string.ascii_letters
        if self.use_digits:
            characters += string.digits
        if self.use_special_chars:
            characters += string.punctuation
        if self.include_chars:
            characters += self.include_chars
        for char in self.exclude_chars:
            characters = characters.replace(char, '')
        return characters


    def filter_similar_chars(self, characters):
        similar_chars = 'I1l0O'
        return ''.join(char for char in characters if char not in similar_chars)

    def generate(self):
        characters = self.set_complexity()
        if self.avoid_similar:
            characters = self.filter_similar_chars(characters)

        password = ''.join(random.choice(self.include_chars) for _ in range(len(self.include_chars)))
        
        password += ''.join(random.choice(characters) for _ in range(self.length - len(password)))
        
        password = ''.join(random.sample(password, len(password)))
        
        return password

    
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

    def assess_strength(self, password):
        score = 0

        if any(char.isdigit() for char in password):  
            score += 1
        if any(char in string.punctuation for char in password):  
            score += 1
        if any(char.isupper() for char in password) and any(char.islower() for char in password):  
            score += 1
        if len(password) >= 8:  
            score += 1

        if score == 4:
            return colored('Strong', 'green')
        elif score == 3:
            return colored('Medium', 'yellow')
        else:
            return colored('Weak', 'red')
        
    def keyword_based(self, keyword):
        modified_keyword = keyword

        if self.use_digits and not any(char.isdigit() for char in modified_keyword):
            modified_keyword += random.choice(string.digits)

        if self.use_special_chars and not any(char in string.punctuation for char in modified_keyword):
            modified_keyword += random.choice(string.punctuation)

        while len(modified_keyword) < self.length:
            modified_keyword += random.choice(string.ascii_letters)
        
        return modified_keyword[:self.length]
    
    def save_to_history(self, password):
        history_file = "password_history.bin"
        history_data = []
        
        if os.path.exists(history_file):
            with open(history_file, 'rb') as file:
                history_data = pickle.load(file)
        
        history_data.append(password)
        if len(history_data) > 10:  
            history_data.pop(0)

        
        with open(history_file, 'wb') as file:
            pickle.dump(history_data, file)
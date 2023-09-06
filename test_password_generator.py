import string
import unittest
from modules.password_generator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):

    def test_default_length(self):
        generator = PasswordGenerator()
        password = generator.generate()
        self.assertEqual(len(password), 8)
    
    def test_custom_length(self):
        generator = PasswordGenerator(length=12)
        password = generator.generate()
        self.assertEqual(len(password), 12)
    
    def test_avoid_similar(self):
        generator = PasswordGenerator(avoid_similar=True)
        password = generator.generate()
        for char in 'I1l0O':
            self.assertNotIn(char, password)
    
    def test_pronounceable_length(self):
        generator = PasswordGenerator(length=12)
        password = generator.generate_pronounceable()
        self.assertEqual(len(password), 12)
    
    def test_no_digits(self):
        generator = PasswordGenerator(use_digits=False)
        password = generator.generate()
        for char in string.digits:
            self.assertNotIn(char, password)
    
    def test_no_special(self):
        generator = PasswordGenerator(use_special_chars=False)
        password = generator.generate()
        for char in string.punctuation:
            self.assertNotIn(char, password)


if __name__ == '__main__':
    unittest.main()
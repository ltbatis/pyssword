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

    def test_assess_strength(self):
        generator = PasswordGenerator()

        strong_password = "Aa1@abcd"
        self.assertEqual(generator.assess_strength(strong_password), "\x1b[32mStrong\x1b[0m")

        medium_password = "Aa1abcde"
        self.assertEqual(generator.assess_strength(medium_password), "\x1b[33mMedium\x1b[0m")

        weak_password = "Aa"
        self.assertEqual(generator.assess_strength(weak_password), "\x1b[31mWeak\x1b[0m")

    def test_keyword_based(self):
        generator = PasswordGenerator()

        keyword = "openAI"

        password = generator.keyword_based(keyword)
        self.assertTrue(keyword in password)

        generator.use_digits = True
        password = generator.keyword_based(keyword)
        self.assertTrue(any(char.isdigit() for char in password))

        generator.use_special_chars = True
        password = generator.keyword_based(keyword)
        self.assertTrue(any(char in string.punctuation for char in password))

        generator.length = 10
        password = generator.keyword_based(keyword)
        self.assertEqual(len(password), 10)
    
    def test_include_chars(self):
        generator = PasswordGenerator(include_chars="@#")
        password = generator.generate()
        self.assertTrue(any(char in "@#" for char in password))
    
    def test_exclude_chars(self):
        generator = PasswordGenerator(exclude_chars="ABCD")
        password = generator.generate()
        for char in "ABCD":
            self.assertNotIn(char, password)
    
    def test_include_and_exclude_chars(self):
        generator = PasswordGenerator(include_chars="@#", exclude_chars="ABCD")
        password = generator.generate()
        self.assertTrue(any(char in "@#" for char in password))
        for char in "ABCD":
            self.assertNotIn(char, password)



if __name__ == '__main__':
    unittest.main()
import argparse
import pyperclip
from modules.password_generator import PasswordGenerator

def main():
    parser = argparse.ArgumentParser(description='Password Generator CLI')
    parser.add_argument('-l', '--length', type=int, default=8, help='Length of the password')
    parser.add_argument('--no-digits', action='store_false', help='Do not include digits in the password')
    parser.add_argument('--no-special', action='store_false', help='Do not include special characters in the password')
    parser.add_argument('-c', '--complexity', choices=['low', 'medium', 'high'], default='medium', help='Complexity level of the password')
    parser.add_argument('--avoid-similar', action='store_true', help='Avoid similar looking characters')
    parser.add_argument('--pronounceable', action='store_true', help='Generate a pronounceable password')
    parser.add_argument('-k', '--keyword', type=str, help='Provide a keyword to generate a modified version of the password')

    args = parser.parse_args()

    generator = PasswordGenerator(length=args.length, 
                                  use_digits=args.no_digits, 
                                  use_special_chars=args.no_special, 
                                  level=args.complexity, 
                                  avoid_similar=args.avoid_similar)
    
    if args.keyword:
        password = generator.keyword_based(args.keyword)
    elif args.pronounceable:
        password = generator.generate_pronounceable()
    else:
        password = generator.generate()

    strength = generator.assess_strength(password)
    
    print(f'Generated Password: {password}')
    pyperclip.copy(password)
    print(f'Strength: {strength}')
    print('Password copied to clipboard!')

if __name__ == '__main__':
    main()

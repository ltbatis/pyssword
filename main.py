import argparse
import pickle
import os
from modules.password_generator import PasswordGenerator

def view_history():
    history_file = "password_history.bin"
    
    if os.path.exists(history_file):
        with open(history_file, 'rb') as file:
            history_data = pickle.load(file)
        for password in history_data:
            print(password)
    else:
        print("No password history found.")

def clear_history():
    history_file = "password_history.bin"
    
    if os.path.exists(history_file):
        os.remove(history_file)
        print("Password history cleared.")
    else:
        print("No password history found.")

def main():
    parser = argparse.ArgumentParser(description='Password Generator CLI')
    parser.add_argument('-l', '--length', type=int, default=8, help='Length of the password')
    parser.add_argument('--no-digits', action='store_false', help='Do not include digits in the password')
    parser.add_argument('--no-special', action='store_false', help='Do not include special characters in the password')
    parser.add_argument('-c', '--complexity', choices=['low', 'medium', 'high'], default='medium', help='Complexity level of the password')
    parser.add_argument('--avoid-similar', action='store_true', help='Avoid similar looking characters')
    parser.add_argument('--pronounceable', action='store_true', help='Generate a pronounceable password')
    parser.add_argument('-k', '--keyword', type=str, help='Provide a keyword to generate a modified version of the password')
    parser.add_argument('--view-history', action='store_true', help='View the password generation history')
    parser.add_argument('--clear-history', action='store_true', help='Clear the password generation history')

    args = parser.parse_args()

    if args.view_history:
        view_history()
        return
    elif args.clear_history:
        clear_history()
        return

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

    generator.save_to_history(password)

    strength = generator.assess_strength(password)
    
    print(f'Generated Password: {password}')
    print(f'Strength: {strength}')

if __name__ == '__main__':
    main()

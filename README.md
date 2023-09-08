![Python Version](https://img.shields.io/badge/python-3.11.4-blue)


`pyssword` is a simple yet efficient command-line password generator. It allows users to specify password complexity, length, and even avoid similar-looking characters.

---
## Installation
```
git clone https://github.com/ltbatis/pyssword.git
cd pyssword
pip install requirements.txt
```

---
## Testing
```
python -m unittest tests.password_generator
python -m unittest tests.history_manager
```

---
## Usage
Here are some demonstrations of how you can generate passwords using `pyssword`:
1. Default Password (Medium Complexity, 8 Characters):
```
python main.py
```
2. Setting Password Length:
```
python main.py -l 12
```
3. Avoid Digits:
```
python main.py --no-digits
```
4. Avoid Special Characters:
```
python main.py --no-special
```
5. Complexity Levels:
- Low:
    ```
    python main.py -c low
    ```
- Medium:
    ```
    python main.py -c medium
    ```
- High:
    ```
    python main.py -c high
    ```
6. Avoid Similar-Looking Characters:
```
python main.py --avoid-similar
```
7. Pronounceable:
```
python main.py --pronounceable
```
8. Keyword usage:
```
python main.py --keyword Beauty
```
9. Expiring date:
```
python main.py --validity 15
```
10. Combination of Options:
```
python main.py -l 16 -c high --no-special --avoid-similar --validity 30
```
11. Specific chars:
```
python main.py --include-chars "@#" --exclude-chars "ABCD"
```
12. History:
```
python main.py --view-history
python main.py --clear-history
```

---
## Future Improvements

- [x] **Pronounceable Words**: We're planning to add a feature to generate passwords that are sequences of pronounceable words, making them easier to memorize.
  - **English**: ✅ Completed
  - **Portuguese**: 🔄 In progress... (10% done)
- [x] **Password Generation History**: Save the most recently generated passwords in a history (possibly stored locally) so users can revisit previously generated passwords if they lose them.
- [x] **Password Strength Assessment**: Evaluate and report how strong the generated password is, using criteria such as length, character variety, and common patterns.
  - **Basic Evaluation**: ✅ Completed
  - **Advanced Evaluation with Patterns**: 🚫 Not started yet
- [x] **Clipboard Integration**: Automatically copy the generated password to the clipboard.
- [x] **Password Expiry**: Set a date or time period after which the generated password will be considered invalid.
- [x] **Specific Character Inclusion/Exclusion**: Allow users to specifically include or exclude certain characters or sets of characters.
- [ ] **Safe Digraphs or Trigraphs**: Instead of picking characters entirely at random, choose pairs or trios of characters that are easier to type together.
- [ ] **Password Variations**: Create variations of a generated password for sites or apps that have specific requirements.
- [ ] **Password Masking**: Allow users to set a "mask" for the password, like "aA#aA#".
- [ ] **Save in Password Managers**: Integration with popular password managers to directly save the generated password.
- [x] **Keyword-based Password**: Generate a password based on a keyword provided by the user, but modify it to meet certain security criteria.
- [ ] **API/Web Service**: Turn your tool into an online service where other applications can generate passwords via API calls.
- [ ] **Graphical UI**: Create a simple graphical interface for the generator for those who don't want to use the command line.
- [ ] **Multi-language**: As mentioned earlier, support for generating pronounceable passwords in different languages.

---
## Contributing
Feel free to open an issue or make a pull request if you have any suggestions or corrections to contribute.

---
## License
MIT

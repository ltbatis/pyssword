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
python test_password_generator.py
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
8. Combination of Options:
```
python main.py -l 16 -c high --no-special --avoid-similar
```

---
## Future Improvements

- [x] **Pronounceable Words**: We're planning to add a feature to generate passwords that are sequences of pronounceable words, making them easier to memorize.
  - **English**: ✅ Completed
  - **Portuguese**: 🔄 In progress... (10% done)
  - **Spanish**: 🚫 Not started yet
  - **French**: 🚫 Not started yet
  - **Italian**: 🚫 Not started yet

---
## Contributing
Feel free to open an issue or make a pull request if you have any suggestions or corrections to contribute.

---
## License
MIT

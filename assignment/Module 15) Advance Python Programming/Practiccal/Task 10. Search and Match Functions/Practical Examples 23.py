# 23) Write a Python program to search for a word in a string using re.search().

import re

text = "Hello, welcome to Python programming."
word = "welcome"


if re.search(word, text):
    print(f"'{word}' found in the string!")
else:
    print(f"'{word}' not found.")
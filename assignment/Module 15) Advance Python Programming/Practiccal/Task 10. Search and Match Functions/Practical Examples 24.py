# 24) Write a Python program to match a word in a string using re.match().


import re

text = "Hello, welcome to Python programming."
word = "Hello"


if re.match(word, text):
    print(f"'{word}' matches the start of the string!")
else:
    print(f"'{word}' does NOT match the start.")

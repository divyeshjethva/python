import re

text = "Python is a powerful programming language."

word = "powerful"
result = re.search(word, text)

if result:
    print(f"'{word}' found in the string at position {result.start()}.")
else:
    print(f"'{word}' not found in the string.")

# =====================================================

import re

text = "Python is awesome!"
word = "Python"

result = re.match(word, text)

if result:
    print(f"String starts with '{word}'.")
else:
    print(f"String does not start with '{word}'.")

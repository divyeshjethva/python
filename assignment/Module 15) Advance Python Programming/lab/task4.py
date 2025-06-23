# file = open("demo.txt", "r")

# content = file.read()
# print(content)

# file.close()

# =========================================

file = open("demo", "w")

lines = [
    "This is the first line.\n",
    "This is the second line.\n",
    "Python makes file handling easy!\n"
]

file.writelines(lines)

file.close()

print("Multiple strings written to 'demo.txt' successfully.")



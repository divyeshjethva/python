# 9) Write a Python program to handle file exceptions and use the finally block for closing the file.

try:
    file = open("example.txt", "r")
    content = file.read()
    print("File content:")
    print(content)

except FileNotFoundError:
    print("Error: The file does not exist.")

except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    try:
        file.close()
        print("File closed.")
    except NameError:
        print("No file to close.")
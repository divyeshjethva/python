# 8) Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).

try:
    file = open("data.txt", "r")
    content = file.read()
    print("File content:", content)
    file.close()

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result of division:", result)

except FileNotFoundError:
    print("Error: File not found!")

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Please enter valid numbers.")

except Exception as e:
    print("An unexpected error occurred:", e)
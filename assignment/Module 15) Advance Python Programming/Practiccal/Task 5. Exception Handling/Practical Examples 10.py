# 10) Write a Python program to print custom exceptions.

class MyCustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise MyCustomError("Age cannot be negative!")
    else:
        print("Your age is:", age)

except MyCustomError as e:
    print("Custom Error:", e)

except ValueError:
    print("Please enter a valid number.")
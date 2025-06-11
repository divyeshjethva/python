# 8. Functions

# def fun1(message):
#     print("You entered:", message)

# fun1("python!")

# ===================================

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = sub(num1, num2)
elif operation == '*':
    result = mul(num1, num2)
elif operation == '/':
    result = div(num1, num2)
else:
    result = "Invalid operation"

print("Result:", result)

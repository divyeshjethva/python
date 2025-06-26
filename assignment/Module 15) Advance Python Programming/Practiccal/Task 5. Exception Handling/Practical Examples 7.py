# 7) Write a Python program to handle exceptions in a calculator

try:
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    op = input("Enter operator (+, -, *, /): ")

  
    if op == '+':
        print("Result:", num1 + num2)
    elif op == '-':
        print("Result:", num1 - num2)
    elif op == '*':
        print("Result:", num1 * num2)
    elif op == '/':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        print("Result:", num1 / num2)
    else:
        print("Invalid operator!")


except ValueError:
    print("Please enter valid numbers.")


except ZeroDivisionError as e:
    print("Error:", e)


except Exception as e:
    print("Something went wrong:", e)

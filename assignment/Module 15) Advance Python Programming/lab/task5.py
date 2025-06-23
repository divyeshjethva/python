# try:
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
    
#     result = num1 / num2
#     print(result)

# except:
#     print("Error: Division by zero is not allowed.")


# ============================================

try:
    num = int(input("Enter an integer: "))
    lst = [10, 20, 30]
    index = int(input("Enter index to access list element: "))
    
    result = lst[index] / num
    print(f"Result is: {result}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except IndexError:
    print("Error: Index out of range.")

except ValueError:
    print("Error: Invalid input. Please enter numbers only.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

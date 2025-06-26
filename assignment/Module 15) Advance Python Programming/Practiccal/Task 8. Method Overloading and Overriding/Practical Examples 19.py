# 19) Write a Python program to show method overloading.

class MathOperations:
    def add(self, a, b, c=0):  
        return a + b + c


obj = MathOperations()
print(obj.add(2, 3))        
print(obj.add(2, 3, 4))     
# 16) Write a Python program to show hierarchical inheritance

class Shape:
    def area(self):
        print("Calculating area.")

class Circle(Shape):
    def area(self):
        print("Calculating area of Circle.")

class Square(Shape):
    def area(self):
        print("Calculating area of Square.")


obj = Circle()
obj.area()  

obj = Square()
obj.area()  

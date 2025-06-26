#  11) Write a Python program to create a class and access the properties of the class using an object.


class Student:
    def __init__(self, name, age):
        self.name = name  
        self.age = age   


obj = Student("ug", 20)


print("Student Name:", obj.name)
print("Student Age:", obj.age)
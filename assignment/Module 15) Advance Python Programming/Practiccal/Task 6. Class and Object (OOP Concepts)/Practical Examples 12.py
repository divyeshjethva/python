# 12) Write a Python program to demonstrate the use of local and global variables in a class.


school = "Sunshine School"

class Student:
    def __init__(self, name):
        self.name = name  
    
    def show(self):
        print(f"{self.name} studies at {school}")

obj = Student("Rahul")
obj.show() 

school = "Bright School"
obj.show()  
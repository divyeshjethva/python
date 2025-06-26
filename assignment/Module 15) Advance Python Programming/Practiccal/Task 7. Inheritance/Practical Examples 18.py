# 18) Write a Python program to demonstrate the use of super() in inheritance.

class BaseClass:
    def __init__(self):
        print("Base class constructor called.")

class DerivedClass(BaseClass):
    def __init__(self):
        super().__init__()  
        print("Derived class constructor called.")


obj = DerivedClass()
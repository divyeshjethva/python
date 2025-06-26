# 17) Write a Python program to show hybrid inheritance.

class Person:
    def info(self):
        print("This is a person.")

class Employee(Person):
    def work(self):
        print("Employee is working.")

class Manager(Employee):
    def manage(self):
        print("Manager is managing.")

obj = Manager()
obj.info()   
obj.work()   
obj.manage() 

# 13) Write a Python program to show single inheritance.

class Vehicle:
    def start(self):
        print("Vehicle is starting.")

class Car(Vehicle):
    def drive(self):
        print("Car is driving.")


obj = Car()
obj.start()  
obj.drive()  
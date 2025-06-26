# 14) Write a Python program to show multilevel inheritance.

class Animal:
    def speak(self):
        print("Animal speaks.")

class Mammal(Animal):
    def walk(self):
        print("Mammal walks.")

class Dog(Mammal):
    def bark(self):
        print("Dog barks.")


obj = Dog()
obj.speak()  
obj.walk()   
obj.bark()   
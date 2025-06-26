# 20) Write a Python program to show method overriding.

class Animal:
    def sound(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def sound(self):  
        print("Dog barks.")

class Cat(Animal):
    def sound(self):  
        print("Cat meows.")


animal = Animal()
animal.sound()  

dog = Dog()
dog.sound()    

cat = Cat()
cat.sound()    
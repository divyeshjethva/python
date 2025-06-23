# Method Overloading

class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

# Method Overriding

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")


calc = Calculator()
print("Sum of 2 and 3:", calc.add(2, 3))
print("Sum of 2, 3, and 4:", calc.add(2, 3, 4))
print("Sum with no arguments:", calc.add())

a = Animal()
d = Dog()

a.sound()
d.sound()

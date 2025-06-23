# Single Inheritance

class Animal:
    def speak(self):
        print("Animals speak in different ways.")

class Dog(Animal):
    def bark(self):
        print("Dog barks.")

d = Dog()
d.speak()
d.bark()

# Multiple Inheritance

class Father:
    def father_info(self):
        print("Father's traits.")

class Mother:
    def mother_info(self):
        print("Mother's traits.")

class Child(Father, Mother):
    def child_info(self):
        print("Child has traits of both parents.")

c = Child()
c.father_info()
c.mother_info()
c.child_info()

# Multilevel Inheritance
class Grandparent:
    def show_gp(self):
        print("I am the grandparent.")

class Parent(Grandparent):
    def show_p(self):
        print("I am the parent.")

class Child(Parent):
    def show_c(self):
        print("I am the child.")

obj = Child()
obj.show_gp()
obj.show_p()
obj.show_c()

# Hybrid Inheritance

class A:
    def show_a(self):
        print("Class A")

class B(A):
    def show_b(self):
        print("Class B")

class C:
    def show_c(self):
        print("Class C")

class D(B, C):
    def show_d(self):
        print("Class D")

obj = D()
obj.show_a()
obj.show_b()
obj.show_c()
obj.show_d()

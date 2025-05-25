# --> Demonstrating variable creation and data types

age = 20

height = 4.8

name = "Divyesh"

student_atten = True

colors = ["red", "green", "blue"]

value = (10, 20)

student = {
    "name": "Divyesh",
    "age": age,
    "student_atten": student_atten
}


print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", student_atten)
print("Colors List:", colors)
print("Coordinates Tuple:", value)
print("Student Dictionary:", student)

# ================================================================


# How does the Python code structure work?


firstname = "Divyesh"
lastname = "jethava"
age = 20

print("my name is :", firstname+ " " + lastname, "and my age is : ",age)

#======================================================================


# How to create variables in Python?

name = "Divyesh"        # string
age = 20               # integer
height = 5.6           # float
is_student = True      # boolean

#======================================================================

# How to take user input using the input() function.

first = input("Enter your firstname :") 
last = input("Enter your lastname :") 

print(first+ " " + last)

#===================================================================


# How to check the type of a variable dynamically using type().

name = "Alice" 
age = 25        
height = 5.5 

print(type(name))     
print(type(age))      
print(type(height))   

#========================================================================

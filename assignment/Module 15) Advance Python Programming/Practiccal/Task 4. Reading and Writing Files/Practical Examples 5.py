#  5) Write a Python program to read a file and print the data on the console.


file = open("output.txt", "r")
data = file.read()
print(data)
file.close()
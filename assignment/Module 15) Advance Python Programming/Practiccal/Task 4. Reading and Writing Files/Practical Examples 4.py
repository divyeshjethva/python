# 4) Write a Python program to create a file and print the string into the file.


file = open("output.txt", "w")
print("This text is written using the print() function.", file=file)
file.close()
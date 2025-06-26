# 6) Write a Python program to check the current position of the file cursor using tell().


file = open("output.txt", "r")

data = file.read(10)
position = file.tell()
print("Current cursor position:", position)
file.close()
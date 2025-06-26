# 15) Write a Python program to show multiple inheritance.


class Writer:
    def write(self):
        print("Writing a story.")

class Artist:
    def draw(self):
        print("Drawing a picture.")

class CreativePerson(Writer, Artist):
    def create(self):
        print("Creating a masterpiece.")


obj = CreativePerson()
obj.write()  
obj.draw()   
obj.create() 
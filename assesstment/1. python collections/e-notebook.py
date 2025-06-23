class Notebook:
    def generate_note(self):
        name = input("Enter E-note generator name: ")
        if name.isdigit():
            print("INVALID NAME")

        title = input("Enter E-note title: ")
        content = input("Enter E-note content: ")
        
        f = open("main.txt", "a")
        f.write("============================ \n")
        f.write(f"Generator Name :{name} \n")
        f.write(f"E-Note Title :{title} \n")
        f.write(f"E-Note Description :{content} \n")

        

    def view_note(self):
        f = open("main.txt", "r")
        print(f.read())

            
obj = Notebook()

while True:
    menu = """
        ===== Welcome to E - Notebook =====

        Press 1 to Generate Note
        Press 2 to View Notes
        Press 3 to Exit
    """
    print(menu)
    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Please enter a valid number.")

    if choice == 1:
        obj.generate_note()

    elif choice == 2:
        obj.view_note()

    elif choice == 3:
        print("Thank you!!")
        break

    else:
        print("Please press a valid number.")

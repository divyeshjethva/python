
my_list = []

def grade_fun(average):
    
    if average>=90:
        return "A+"
    elif average>=80:
        return "A"
    elif average>=70:
        return "B"
    elif average>=60:
        return "C"
    elif average>=50:
        return "D"
    else:
        return "F"

def student_manage():
    student_dic = {}
    subject = {}
    total_marks = 0
    
    student = input("\nEnter Student Name :")
    sub = int(input("\nEnter How Many Subject ? :"))
    
    for i in range(sub):
        sub1 = input("Enter Name of Subject : ")
        marks = int(input(f"Enter Marks for {sub1} :"))

        subject[sub1] = marks
        total_marks += marks

    average = total_marks/sub
    grade = grade_fun(average)

    

    student_dic["Name"] = student
    student_dic["Average"] = average
    student_dic["Grade"] = grade

    my_list.append(student_dic)

    # print("list is ", my_list)

    print("\nStudent Added Successfully ")

def All_student():
    for i, entry in enumerate(my_list,1):
        print(f"{i}.  Name : {entry["Name"]}")
        print(f"   Average : {entry["Average"]}")
        print(f"   Grade : {entry["Grade"]}")

        print("------------------------")



while True:

    menu = """
        1. Add Student
        2. Show All Student
        3. Exit
    """

    print(menu)

    choice = int(input("\nEnter Your  Option :"))

    if choice == 1:
        student_manage()
    elif choice == 2:
        All_student()
    elif choice == 3:
        print("Thnak You !!")
        break
    else:
        print("Invalid Choice !!")
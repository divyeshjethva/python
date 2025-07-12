from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.geometry("1300x650")
root.title("Billing Software")
root.configure(bg="#074463")

customer_name = StringVar()
customer_phone = StringVar()
bill_no = StringVar()
bill_no.set(str(random.randint(1000, 9999)))

bath_soap = IntVar()
face_cream = IntVar()
face_wash = IntVar()
hair_spray = IntVar()
body_lotion = IntVar()

rice = IntVar()
food_oil = IntVar()
daal = IntVar()
wheat = IntVar()
sugar = IntVar()

maza = IntVar()
coke = IntVar()
frooti = IntVar()
nimkos = IntVar()
biscuits = IntVar()

total_cosmetics = StringVar()
total_grocery = StringVar()
total_others = StringVar()
cosmetics_tax = StringVar()
grocery_tax = StringVar()
others_tax = StringVar()

def total():
    tc = bath_soap.get()*40 + face_cream.get()*120 + face_wash.get()*120 + hair_spray.get()*180 + body_lotion.get()*140
    tg = rice.get()*80 + food_oil.get()*120 + daal.get()*90 + wheat.get()*60 + sugar.get()*70
    to = maza.get()*60 + coke.get()*60 + frooti.get()*50 + nimkos.get()*40 + biscuits.get()*20

    total_cosmetics.set("Rs. " + str(tc))
    total_grocery.set("Rs. " + str(tg))
    total_others.set("Rs. " + str(to))

    cosmetics_tax.set("Rs. " + str(round(tc * 0.05)))
    grocery_tax.set("Rs. " + str(round(tg * 0.05)))
    others_tax.set("Rs. " + str(round(to * 0.05)))

def clear():
    customer_name.set("")
    customer_phone.set("")
    bill_no.set(str(random.randint(1000, 9999)))
    for var in [bath_soap, face_cream, face_wash, hair_spray, body_lotion,
                rice, food_oil, daal, wheat, sugar,
                maza, coke, frooti, nimkos, biscuits]:
        var.set(0)
    total_cosmetics.set("")
    total_grocery.set("")
    total_others.set("")
    cosmetics_tax.set("")
    grocery_tax.set("")
    others_tax.set("")
    text_area.delete('1.0', END)

def generate_bill():
    if customer_name.get() == "" or customer_phone.get() == "":
        messagebox.showerror("Error", "Customer details are required")
        return
    text_area.delete('1.0', END)
    text_area.insert(END, f"\tWelcome To Hanan's Retail\n")
    text_area.insert(END, f"Bill No. : {bill_no.get()}\n")
    text_area.insert(END, f"Customer Name : {customer_name.get()}\n")
    text_area.insert(END, f"Phone No. : {customer_phone.get()}\n")
    text_area.insert(END, f"====================================\n")
    text_area.insert(END, f"Product\tQty\tPrice\n")
    text_area.insert(END, f"====================================\n")

    if bath_soap.get() != 0: text_area.insert(END, f"Bath Soap\t{bath_soap.get()}\t{bath_soap.get()*40}\n")
    if face_cream.get() != 0: text_area.insert(END, f"Face Cream\t{face_cream.get()}\t{face_cream.get()*120}\n")
    if face_wash.get() != 0: text_area.insert(END, f"Face Wash\t{face_wash.get()}\t{face_wash.get()*120}\n")
    if hair_spray.get() != 0: text_area.insert(END, f"Hair Spray\t{hair_spray.get()}\t{hair_spray.get()*180}\n")
    if body_lotion.get() != 0: text_area.insert(END, f"Body Lotion\t{body_lotion.get()}\t{body_lotion.get()*140}\n")

    if rice.get() != 0: text_area.insert(END, f"Rice\t{rice.get()}\t{rice.get()*80}\n")
    if food_oil.get() != 0: text_area.insert(END, f"Food Oil\t{food_oil.get()}\t{food_oil.get()*120}\n")
    if daal.get() != 0: text_area.insert(END, f"Daal\t{daal.get()}\t{daal.get()*90}\n")
    if wheat.get() != 0: text_area.insert(END, f"Wheat\t{wheat.get()}\t{wheat.get()*60}\n")
    if sugar.get() != 0: text_area.insert(END, f"Sugar\t{sugar.get()}\t{sugar.get()*70}\n")

    if maza.get() != 0: text_area.insert(END, f"Maza\t{maza.get()}\t{maza.get()*60}\n")
    if coke.get() != 0: text_area.insert(END, f"Coke\t{coke.get()}\t{coke.get()*60}\n")
    if frooti.get() != 0: text_area.insert(END, f"Frooti\t{frooti.get()}\t{frooti.get()*50}\n")
    if nimkos.get() != 0: text_area.insert(END, f"Nimkos\t{nimkos.get()}\t{nimkos.get()*40}\n")
    if biscuits.get() != 0: text_area.insert(END, f"Biscuits\t{biscuits.get()}\t{biscuits.get()*20}\n")

    text_area.insert(END, f"====================================\n")
    text_area.insert(END, f"Total Cosmetics : {total_cosmetics.get()}\n")
    text_area.insert(END, f"Total Grocery : {total_grocery.get()}\n")
    text_area.insert(END, f"Total Others : {total_others.get()}\n")
    text_area.insert(END, f"Cosmetics Tax : {cosmetics_tax.get()}\n")
    text_area.insert(END, f"Grocery Tax : {grocery_tax.get()}\n")
    text_area.insert(END, f"Others Tax : {others_tax.get()}\n")

header = Label(root, text="Billing Software", font=("Arial", 24, "bold"), fg="white", bg="#074463")
header.pack(fill=X)

customer_frame = LabelFrame(root, text="Customer Details", font=("Arial", 12, "bold"), fg="yellow", bg="#074463")
customer_frame.place(x=0, y=50)

Label(customer_frame, text="Customer Name", font=("Arial", 12), bg="#074463", fg="white").grid(row=0, column=0, padx=20, pady=5)
Entry(customer_frame, width=20, font="arial 12", textvariable=customer_name).grid(row=0, column=1, pady=5, padx=10)

Label(customer_frame, text="Phone No", font=("Arial", 12), bg="#074463", fg="white").grid(row=0, column=2, padx=20, pady=5)
Entry(customer_frame, width=20, font="arial 12", textvariable=customer_phone).grid(row=0, column=3, pady=5, padx=10)

Label(customer_frame, text="Bill No.", font=("Arial", 12), bg="#074463", fg="white").grid(row=0, column=4, padx=20, pady=5)
Entry(customer_frame, width=20, font="arial 12", textvariable=bill_no).grid(row=0, column=5, pady=5, padx=10)

Button(customer_frame, text="Enter", font="arial 12 bold", bg="white", fg="black", width=10).grid(row=0, column=6, padx=20)

cosmetics_frame = LabelFrame(root, text="Cosmetics", font=("Arial", 12, "bold"), fg="yellow", bg="#074463")
cosmetics_frame.place(x=0, y=140, width=300, height=300)

items1 = [("Bath Soap", bath_soap), ("Face Cream", face_cream), ("Face Wash", face_wash),
          ("Hair Spray", hair_spray), ("Body Lotion", body_lotion)]
for i, (item, var) in enumerate(items1):
    Label(cosmetics_frame, text=item, font=("Arial", 12), bg="#074463", fg="white").grid(row=i, column=0, padx=10, pady=5, sticky="w")
    Entry(cosmetics_frame, width=10, font="arial 12", textvariable=var).grid(row=i, column=1, padx=10, pady=5)

grocery_frame = LabelFrame(root, text="Grocery", font=("Arial", 12, "bold"), fg="yellow", bg="#074463")
grocery_frame.place(x=300, y=140, width=300, height=300)

items2 = [("Rice", rice), ("Food Oil", food_oil), ("Daal", daal), ("Wheat", wheat), ("Sugar", sugar)]
for i, (item, var) in enumerate(items2):
    Label(grocery_frame, text=item, font=("Arial", 12), bg="#074463", fg="white").grid(row=i, column=0, padx=10, pady=5, sticky="w")
    Entry(grocery_frame, width=10, font="arial 12", textvariable=var).grid(row=i, column=1, padx=10, pady=5)

others_frame = LabelFrame(root, text="Others", font=("Arial", 12, "bold"), fg="yellow", bg="#074463")
others_frame.place(x=600, y=140, width=300, height=300)

items3 = [("Maza", maza), ("Coke", coke), ("Frooti", frooti), ("Nimkos", nimkos), ("Biscuits", biscuits)]
for i, (item, var) in enumerate(items3):
    Label(others_frame, text=item, font=("Arial", 12), bg="#074463", fg="white").grid(row=i, column=0, padx=10, pady=5, sticky="w")
    Entry(others_frame, width=10, font="arial 12", textvariable=var).grid(row=i, column=1, padx=10, pady=5)

bill_frame = Frame(root)
bill_frame.place(x=900, y=140, width=380, height=300)

bill_title = Label(bill_frame, text="Bill Area", font="arial 12 bold", bd=7, relief=GROOVE)
bill_title.pack(fill=X)

scroll_y = Scrollbar(bill_frame, orient=VERTICAL)
text_area = Text(bill_frame, yscrollcommand=scroll_y.set)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=text_area.yview)
text_area.pack(fill=BOTH, expand=1)

menu_frame = LabelFrame(root, text="Bill Menu", font=("Arial", 12, "bold"), fg="yellow", bg="#074463")
menu_frame.place(x=0, y=440, relwidth=1, height=150)

Label(menu_frame, text="Total Cosmetics", font=("Arial", 12), bg="#074463", fg="white").grid(row=0, column=0, padx=20, pady=5)
Entry(menu_frame, width=15, font="arial 12", textvariable=total_cosmetics).grid(row=0, column=1, padx=10, pady=5)

Label(menu_frame, text="Total Grocery", font=("Arial", 12), bg="#074463", fg="white").grid(row=1, column=0, padx=20, pady=5)
Entry(menu_frame, width=15, font="arial 12", textvariable=total_grocery).grid(row=1, column=1, padx=10, pady=5)

Label(menu_frame, text="Others Total", font=("Arial", 12), bg="#074463", fg="white").grid(row=2, column=0, padx=20, pady=5)
Entry(menu_frame, width=15, font="arial 12", textvariable=total_others).grid(row=2, column=1, padx=10, pady=5)

Label(menu_frame, text="Cosmetics Tax", font=("Arial", 12), bg="#074463", fg="white").grid(row=0, column=2, padx=20, pady=5)
Entry(menu_frame, width=15, font="arial 12", textvariable=cosmetics_tax).grid(row=0, column=3, padx=10, pady=5)

Label(menu_frame, text="Grocery Tax", font=("Arial", 12), bg="#074463", fg="white").grid(row=1, column=2, padx=20, pady=5)
Entry(menu_frame, width=15, font="arial 12", textvariable=grocery_tax).grid(row=1, column=3, padx=10, pady=5)

Label(menu_frame, text="Others Tax", font=("Arial", 12), bg="#074463", fg="white").grid(row=2, column=2, padx=20, pady=5)
Entry(menu_frame, width=15, font="arial 12", textvariable=others_tax).grid(row=2, column=3, padx=10, pady=5)

Button(menu_frame, text="Total", bg="white", fg="black", font="arial 12 bold", width=12, command=total).grid(row=0, column=4, padx=30, pady=5)
Button(menu_frame, text="Generate Bill", bg="white", fg="black", font="arial 12 bold", width=12, command=generate_bill).grid(row=1, column=4, padx=30, pady=5)
Button(menu_frame, text="Clear", bg="white", fg="black", font="arial 12 bold", width=12, command=clear).grid(row=2, column=4, padx=30, pady=5)
Button(menu_frame, text="Exit", bg="white", fg="black", font="arial 12 bold", width=12, command=root.destroy).grid(row=2, column=5, padx=10, pady=5)

root.mainloop()
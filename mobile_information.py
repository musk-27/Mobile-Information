from tkinter import *
from tkinter import messagebox

window=Tk()
window.geometry("700x700")
window.title("Mobile Information")
first_name = StringVar()
first_number = StringVar()


def insert():
    file = open("numbers.txt")
    my_name = first_name.get()
    my_number = first_number.get()
    if my_number not in file.read():
        file = open("numbers.txt",'a')
        file.write("\n"+my_name + ":"+ my_number)
        messagebox.showinfo("Successfully done", "Data added successfully")
    else:
        messagebox.showerror("Invalid", "Data already exist")


def clear():
    name.delete(first=0,last=100)
    number.delete(first=0,last=100)


def exit1():
    window.destroy()


def check1():
    file = open("numbers.txt", 'r')
    summary.delete(0.0, END)
    for line in reversed(file.readlines()):
        summary.insert(0.0, line)

label1 = Label(master = window,text="ENTER YOUR INFORMATION",fg="blue",bg="yellow",relief="solid",width=30,font=("arial",19,"bold"))
label1.place(x=100,y=53)

first_name = StringVar()
first_number = StringVar()

label2 = Label(master = window,text="Enter Name",width=20,font=("arial",10,"bold"))
label2.place(x=90,y=130)

name = Entry(window,textvar=first_name)
name.place(x=240,y=130)


label3 = Label(master = window,text="Enter Number",width=20,font=("arial",10,"bold"))
label3.place(x=90,y=180)

number = Entry(window,textvar=first_number)
number.place(x=240,y=180)

b = Button(master = window,text="Insert",width=15,bg="brown",fg="white",command=insert)
b.place(x=180,y=250)

b1 = Button(master = window,text="Check",width=15,bg="brown",fg="white",command=check1)
b1.place(x=120,y=500)

b2 = Button(master = window,text="Clear",width=15,bg="brown",fg="white",command=clear)
b2.place(x=270,y=500)

b3 = Button(master = window,text="Exit",width=15,bg="brown",fg="white",command=exit1)
b3.place(x=200,y=550)

label4 = Label(master = window,text="VIEW YOUR INFORMATION",relief="solid",fg="blue",bg="yellow",width=40,font=("arial",10,"bold"))
label4.place(x=110,y=310)

summary = Text(window,width=25)
summary.place(x=150, y=350, height=120, width=200)
window.mainloop()




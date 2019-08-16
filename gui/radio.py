from tkinter import *

def m():
    gender = v.get()
    if int(gender) == 0:
        print("Male")
    else:
        print("Female")

master = Tk()
l = Label(master, text="Gender")
l.grid(row=0, column=0)
v = IntVar()
r1 = Radiobutton(master, text="Male", variable=v, value=0)
r1.grid(row=0, column=1)
r2 = Radiobutton(master, text="Female", variable=v, value=1)
r2.grid(row=0, column=2)
b = Button(master, text="Submit", command=m)
b.grid(row=1)
master.mainloop()

from tkinter import *

master = Tk()

master.title("MyApp")
master.config(bg="red")

# a = Label(master, text="Welcome to my app")
# a.pack()

b = Label(master, text="Welcome to my app")
b.config(font=24, bg="yellow", fg="blue")
b.grid(row=0, column=0, sticky=W)

d = Label(master, text="Welcome to my app")
d.grid(row=1, column=0, sticky=W)

c = Label(master, text="Welcome to my app")
c.place(x=100, y=100)

# master.mainloop()
mainloop()
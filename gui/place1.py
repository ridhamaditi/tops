from tkinter import *

master = Tk()

master.title("MyApp")
# a = Label(master, text="Welcome to my app")
# a.pack()

# b = Label(master, text="Welcome to my app")
# b.grid(row=0, column=0)

b = Label(master, text="Welcome to my app")
b.place(x=150, y=100)

c = Label(master, text="Welcome to my app")
c.place(x=100, y=100)

master.mainloop()
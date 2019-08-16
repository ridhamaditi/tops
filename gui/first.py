from tkinter import *

master = Tk()

master.title("MyApp")
a = Label(master, text="Welcome to my app")
a.pack()

# b = Label(master, text="Welcome to my app")
# b.grid(row=0, column=0)

# c = Label(master, text="Welcome to my app")
# c.place(x=0, y=0)

master.mainloop()